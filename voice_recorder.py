import sounddevice as sd, os
from scipy.io.wavfile import write
import settings

class SoundRecord:

    def __init__(self, fs=44100, seconds=3) -> None:
        self.fs = fs
        self.seconds = seconds

    def record_sound(self):
        myrecording = sd.rec(int(self.seconds * self.fs), samplerate=self.fs, channels=2)
        sd.wait()  # Wait until recording is finished
        write(os.path.join(settings.BASE_PATH, 'input_audios', 'output.wav'), self.fs, myrecording)  # Save as WAV file 
        return os.path.join(settings.BASE_PATH, 'input_audios', 'output.wav')