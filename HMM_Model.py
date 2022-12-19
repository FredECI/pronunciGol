import os
# import soundfile as sf
# from pydub import AudioSegment
import numpy as np
# from scipy.io import wavfile 
from hmmlearn import hmm
import librosa, json
from librosa.feature import mfcc
import settings
import warnings
warnings.filterwarnings("ignore")

class HMMTrainer(object):
    def __init__(self, model_name='GaussianHMM', n_components=4, cov_type='diag', n_iter=1000):
        self.model_name = model_name
        self.n_components = n_components
        self.cov_type = cov_type
        self.n_iter = n_iter
        self.models = []

        if self.model_name == 'GaussianHMM':
            self.model = hmm.GaussianHMM(n_components=self.n_components, 
                    covariance_type=self.cov_type, n_iter=self.n_iter)
        else:
            raise TypeError('Invalid model type')

    def get_score(self, reference_folder, input_audio):
        label = reference_folder[reference_folder.rfind('/') + 1:]
        X = np.array([])
        y_words = []
        for filename in [x for x in os.listdir(reference_folder) if x.endswith('.wav')][:-1]:
            filepath = os.path.join(reference_folder, filename)
            sampling_freq, audio = librosa.load(filepath)            
            mfcc_features = mfcc(sampling_freq, audio)
            if len(X) == 0:
                X = mfcc_features[:,:15]
            else:
                X = np.append(X, mfcc_features[:,:15], axis=0)            
            y_words.append(label)
        self.models = []
        self._train(X)
        score = self._compare_audios(input_audio)

        return score

    # X is a 2D numpy array where each row is 13D
    def _train(self, X):
        np.seterr(all='ignore')
        self.model = self.model.fit(X)

    def _compare_audios(self, input_file):
        sampling_freq, audio = librosa.load(input_file)

        # Extract MFCC features
        mfcc_features = mfcc(sampling_freq, audio)
        mfcc_features=mfcc_features[:,:15]

        score = self.model.score(mfcc_features)
        return score

    def test(self):
        final_dict = {}
        for word in settings.words_list:
            test_folder = r"palavras_teste\{}".format(word.capitalize())
            reference_folder = r"palavras\{}".format(word.capitalize())
            test_scores = []
            for filename in os.listdir(test_folder):
                f = os.path.join(test_folder, filename)
                # checking if it is a file
                test_scores.append(self.get_score(reference_folder, f))
            test_scores = np.array(test_scores)
            final_dict[word] = [np.quantile(test_scores, 0.33), np.quantile(test_scores, 0.66)]
        with open(r'words_limits/result.json', 'w') as fp:
            json.dump(final_dict, fp)

# hmm_class = HMMTrainer()
# score = hmm_class.test(r"palavras\Brincadeiras", r"palavras_teste\Brincadeiras")
# print(score)