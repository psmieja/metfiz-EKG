'''*****************************************************************************
* EXPERIMENTATION. Based on 0_3.py
* Reads EKG signal from ./data3 (Motion Artifact Contaminated ECG Database)
* https://physionet.org/content/macecgdb/1.0.0/





********************************************************************************
'''
#reading command line args
import sys

#importing file
import csv

#everything
import numpy as np

#all plotting
import matplotlib.pyplot as plt

from scipy.signal import find_peaks

# checking if proper number of system arguments was provided
if len(sys.argv) != 2:
    sys.exit('ERROR: Wrong number of arguments, single argument (file path) required')

filename = sys.argv[1]

with open(filename) as file:
    csv_data = csv.reader(file, delimiter=',')
    # data format [time [s], MLII [mV], V5 [mV]
    data = np.array( [[float(line[0]), float(line[2])] for line in csv_data] )

# finding ALL peaks, later we will filter the peaks based on prominence to find the R peaks of ECG
peaks_idx, peak_parameters = find_peaks(data[:,1], prominence=0.)
p_prominence = peak_parameters['prominences']
# histogram of peak prominences
p_hist_vals, p_hist_edges = np.histogram(p_prominence, density=True)
# all the bars in the histogram, the value of which is 0
# normally there are two non-zero hills in histogram divided by area of 0s
# first hill consists of peaks caused mostly by noise
# second hill consists exclusively of R peaks
# our goal is to find threshold prominence value, so that all R peaks are above it and none of the noise is
zerobars = np.where(p_hist_vals == 0)[0]
if zerobars.size == 0:
    print('ERROR: Zerobars empty')
    input()
# medium of the zerobar range is the right prominence threshold value
prominence_threshold = (p_hist_edges[zerobars[-1] + 1] + p_hist_edges[zerobars[0]]) / 2
prominent_peaks_idx, _ = find_peaks(data[:,1], prominence = prominence_threshold)

# entries of data corresponding to peaks
# like peaks = [data[i] for i in peaks]
peaks = data[prominent_peaks_idx]
pulse = np.zeros(len(peaks))
for i in range(1,len(peaks)):
    # 1 / time between the neighbour peaks in minutes
    pulse[i] = 1 / ((peaks[i, 0] - peaks[i - 1, 0]) / 60)

# PLOTTING FINAL DATA
# ECG data
fig, ax = plt.subplots()
ax.plot(data[:,0], data[:,1], color='dodgerblue')
ax.plot(peaks[:,0], peaks[:,1], 'x')
ax.set_ylabel("EKG", color='dodgerblue', fontsize=14)
# PULSE
ax2 = ax.twinx()
ax2.plot(peaks[1:,0], pulse[1:], color='r')
ax2.set_ylabel("pulse", color='r', fontsize=14)

plt.show()