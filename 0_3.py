'''*****************************************************************************
* FILE WITH MOTION ARTIFACTS
* Reads EKG signal from ./data3 (Motion Artifact Contaminated ECG Database)
* https://physionet.org/content/macecgdb/1.0.0/





********************************************************************************
'''
#importing file
import csv

#everything
import numpy as np

#all plotting
import matplotlib.pyplot as plt

from scipy.signal import find_peaks

with open('./data3/test21_90j_rdsamp_output_no_head.csv') as file:
    csv_data = csv.reader(file, delimiter=',')
    # data format [time [s], MLII [mV], V5 [mV]
    data_table = [[float(line[0]), float(line[2])] for line in csv_data]
    #print(data_table)
    data0 = np.array(data_table)

data = data0

dt = 0.002 # 2 miliseconds
dtm = dt / 60 # in minutes

# finds indexes of peak values above 0.6
peaks_idx, _ = find_peaks(data[:,1], height=2.)
# entries of data corresponding to peaks
# like peaks = [data[i] for i in peaks]
peaks = data[peaks_idx]

pulse = np.zeros(len(peaks))
print(len(peaks))
for i in range(1,len(peaks)):
    # 1 / time between the neighbour peaks in minutes
    pulse[i] = 1 / ((peaks[i, 0] - peaks[i -1, 0]) / 60)

fig, ax = plt.subplots()
ax.plot(data[:,0], data[:,1], color='dodgerblue')
ax.plot(peaks[:,0], peaks[:,1], 'x')
ax.set_ylabel("EKG", color='dodgerblue', fontsize=14)

ax2 = ax.twinx()
ax2.plot(peaks[1:,0], pulse[1:], color='r')
ax2.set_ylabel("pulse", color='r', fontsize=14)

plt.show()