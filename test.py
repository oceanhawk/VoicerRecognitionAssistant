# Recording sound to sound file
# import required libraries

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100 # sampling frequency
duration = 5 # recording duration

# Start recorder with the given values of duration and sample frequency
recording = sd.rec(int(duration * freq)
samplerate = freq
channels = 2)

# Record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio file with the given sampling frequency

write ("output.wav", freq, recording) # Save as WAV file

# Convert the NumPy arraw to audio file
wv.write("output.wav", recording, freq, sampwidth=2)
