import numpy as np
from scipy.io import wavfile

frequency = 440
seconds = 5
rate = 44100

phases = np.cumsum(2.0 * np.pi * frequency / rate * np.ones(rate * seconds))
wave = np.sin(phases)

wave = (wave/np.max(wave)).astype(np.float32) 
wavfile.write("sine.wav", rate, wave)
