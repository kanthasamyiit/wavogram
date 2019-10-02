"""
Created on Wed Sep 18 16:47:06 2019

@author: Kanthasamy Chelliah

The function wavogram(wavFile) provides spectrogram for any wav file (mono).

Simple usage: wavogram(wavFile)

Optional arguments:

str:  pltTitle => send any string to be used as the plot title.
bool: masked   => set to false if full data needs to be plotted. Leave it default if masking lower amplitudes is okay.
bool: cbar     => set to true if colorbar needs to be plotted.

Output .jpg file is saved with the same basename as the .wav file

"""

import os
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
from scipy import signal

def wavogram(wavFile,pltTitle='',masked=True,cbar=False):
    f = plt.figure()
    plt.set_cmap('hot')
    ax1 = plt.subplot(3,1,1)
    sig, fs = sf.read(wavFile)
    if sig.ndim > 1:
        print("Error! Can process only mono files!!")
        return
    x,y,S = signal.spectrogram(sig,fs)
    S = 20.*np.log10(S/0.00002)
    if masked:
        cutOff = np.max(S) - 0.4* (np.max(S)-np.min(S))
        S[S<cutOff] = np.nan
        
    plt.pcolormesh(y,x,S)
    if pltTitle != '':
        ax1.set_title(pltTitle)
    plt.ylabel('Frequency (Hz)') 
    plt.xlabel('Time (s)') 
    if cbar:
        plt.colorbar()
    plt.tight_layout()
    plt.savefig(os.path.splitext(wavFile)[0]+'.jpg', bbox_inches = "tight",dpi=300)
 
if __name__ == '__main__':
    
    # To test a single wav file:
    wav_file = 'file.wav'
    wavogram(wav_file)
    
    # To test all wav files in one directory
    import glob
    wavLoc = '/Path/to/files/*.wav';
    for wav_file in glob.glob(wavLoc):
        wavogram(wav_file)
        
