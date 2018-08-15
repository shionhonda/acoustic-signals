import numpy as np
import argparse
from scipy.io import wavfile

spl = 44100
secs = 10
tmax = spl*secs
Lmin = 22
Lmax = 56
cmax = 12
fmin = 10

def shift(t, c):
    return c + t/(tmax)

def theta(t, c):
    return 2*np.pi/cmax*shift(t, c)

def L(t,c):
    return Lmin + (Lmax-Lmin)*(1-np.cos(theta(t, c)))/2

def fr(t, c):
    return fmin*2**shift(t, c)

def amp(t, c):
    return 10**(L(t, c)/20)

def main():
    parser = argparse.ArgumentParser(description='Shepard tone')
    parser.add_argument('--down', '-d', type=bool, default=False, help='Set True for going down')
    args = parser.parse_args()

    t = np.linspace(0, tmax-1, tmax)
    wave = np.zeros(tmax)
    for c in range(cmax):
        # Integrate frequency into phase
        wave += amp(t, c)*np.sin(2*np.pi*np.cumsum(fr(t, c))/spl)
    wave = np.hstack((wave, wave))
    if args.down:
        wave = wave[::-1]

    wave = (wave/np.max(wave)).astype(np.float32)
    if args.down:
        wavfile.write("shepard_down.wav", spl, wave)
    else:
        wavfile.write("shepard_up.wav", spl, wave)

if __name__ == '__main__':
    main()
