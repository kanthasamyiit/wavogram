# wavogram
Plot spectrogram of a wav file using python

The function wavogram(wavFile) provides spectrogram for any wav file (mono).
Simple usage: wavogram(wavFile)
Optional arguments:
str:  pltTitle => send any string to be used as the plot title.
bool: masked   => set to false if full data needs to be plotted. Leave it default if masking lower amplitudes is okay.
bool: cbar     => set to true if colorbar needs to be plotted.

Dependencies:
matplotlib
numpy
scipy
