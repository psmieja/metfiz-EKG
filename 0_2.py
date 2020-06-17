'''*****************************************************************************
* READING LARGER FILE (sel100 from QT Database)
* Reads EKG signal from ./data2 (QT DB full file)






********************************************************************************
'''
#importing file
import csv

#everything
import numpy as np

#all plotting
import matplotlib.pyplot as plt

from scipy.signal import find_peaks

with open('./data2/sel100_rdsamp_output_no_head.csv') as file:
    csv_data = csv.reader(file, delimiter=',')
    # data format [time [s], MLII [mV], V5 [mV]
    data_table = [[float(line[0]), float(line[2])] for line in csv_data]
    #print(data_table)
    data0 = np.array(data_table)

data = data0[:30000]

dt = 0.002 # 2 miliseconds
dtm = dt / 60 # in minutes

# minimal height differs from 0_1.py bc of amplification difference
peaks_idx, _ = find_peaks(data[:,1], height=5.2)
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