# fftwav.py3
import numpy as np
from numpy.fft import fft
from numpy.fft import ifft
import wave
import sys
import struct
import math

print("fftwav.py3 reading ", sys.argv[1])
spf = wave.open(sys.argv[1],'rb')
n = spf.getnframes()
print('nframes=',n)

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
# print(signal) # junk
print("signal is ")
print('signal[0]=',signal[0])
print('signal[1]=',signal[1])

# idata = np.fromstring(signal, 'Int16') # old
idata = np.frombuffer(signal, 'Int16')
print("idata is")
print(idata)
print('idata[0]=',idata[0])
print('idata[1]=',idata[1])

ni = len(idata)
print("num int data=",ni)
fdata = [0.0 for i in range(ni)]
print("fdata is ")
for j in range(0, ni-1):
  fdata[j] = idata[j]/32768.0
  if j<5 :
    print(fdata[j])


junk1 = fft(fdata)

# mess up spectrum here

junk2 = ifft(junk1)


ndata = [0 for i in range(ni)]
print("ndata is ")
for j in range(0, ni-1):
  ndata[j] = int(junk2[j]*32768.0)
  if j<5 :
    print(ndata[j])

  
print("write-ran_wave.py3 writing fft1t.wav")
sampleRate = 10000.0 # hertz
obj = wave.open('fft1t.wav','w')
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sampleRate)
for i in range(ni):
  data = struct.pack('<h', ndata[i])
  obj.writeframesraw( data )
  
obj.close()

print("fftwav finished")

