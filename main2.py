import sys
import zipfile
import os
import argparse 
import soundfile as sf
from pydub import AudioSegment
import numpy as np
from scipy.io import wavfile 
from hmmlearn import hmm
import librosa
from librosa.feature import mfcc

input_folder= "audios"
label_list = []
directory_list = os.listdir(input_folder)


for dirname in directory_list:
  # Get the name of the subfolder 
  subfolder = os.path.join(input_folder, dirname)
  label = subfolder[subfolder.rfind('/') + 1:]
  label_list.append(label)
print(label_list)