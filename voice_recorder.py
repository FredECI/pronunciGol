import sounddevice as sd, os
from scipy.io.wavfile import write
import settings
import librosa
import soundfile as sf

class SoundRecord:

    def __init__(self, fs=44100, seconds=2) -> None:
        self.fs = fs
        self.seconds = seconds

    def record_sound(self):
        myrecording = sd.rec(int(self.seconds * self.fs), samplerate=self.fs, channels=2)
        sd.wait()  # Wait until recording is finished
        path = os.path.join(settings.BASE_PATH, 'input_audios', 'output.wav')
        write(path, self.fs, myrecording)  # Save as WAV file 
        audio, sr = librosa.load(path, sr= 8000, mono=True)
        path = self.adjust_audio_limits(audio, sr, path)
        return path

    def adjust_audio_limits(self, audio, sr, path):
        clips = librosa.effects.split(audio, top_db=15)
        wav_data = []
        for c in clips:
            data = audio[c[0]: c[1]]
            wav_data.extend(data)
        sf.write(path, wav_data, sr)
        return path