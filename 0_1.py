'''*****************************************************************************
* INITIAL TESTS ON ECG-ID 10s SAMPLE
* Reads EKG signal from ./data1/data3.csv (ECG-ID 10s sample)
* detects maxima above given threshold => R peaks
* plots EKG and pulse data on a same plot




********************************************************************************
'''
#importing file
import csv

#everything
import numpy as np

#all plotting
import matplotlib.pyplot as plt

from scipy.signal import find_peaks
'''
#maximum filter
import scipy.ndimage.filters as filters
'''

def time_seconds(input: str):
    # input format: 'mm:ss.mmm'
    # with strip we get rid of ' characters, than split minutes from seconds & miliseconds
    s = input.strip('\'').split(':')
    # we cast strings to float, multiply minutes * 60 & add seconds
    return float(s[0])*60 + float(s[1])

with open('./data1/data.csv') as file:
    csv_data = csv.reader(file, delimiter=',')
    next(csv_data)
    next(csv_data)
    data_table = [[time_seconds(line[0]), float(line[2])] for line in csv_data]
    #print(data_table)
    data = np.array(data_table)

#-------------------------------------------------------------------------------
''' for the sake of find_peaks we use only y colum which gets rid of
    time values. To find pulse i have to define interval between points
'''  
dt = 0.002 # 2 miliseconds
dtm = dt / 60 # in minutes

# finds indexes of peak values above 0.6
peaks_idx, _ = find_peaks(data[:,1], height=0.6)
# entries of data corresponding to peaks
# like peaks = [data[i] for i in peaks]
peaks = data[peaks_idx]

pulse = np.zeros(len(peaks))
print(len(peaks))
for i in range(1,len(peaks)):
    # 1 / time between the neighbour peaks in minutes
    #print(i, peaks[i,0], peaks[i-1,0])
    pulse[i] = 1 / ((peaks[i, 0] - peaks[i -1, 0]) / 60)


fig, ax = plt.subplots()
ax.plot(data[:,0], data[:,1], color='dodgerblue')
ax.plot(peaks[:,0], peaks[:,1], 'x')
ax.set_ylabel("EKG", color='dodgerblue', fontsize=14)


ax2 = ax.twinx()
ax2.plot(peaks[1:,0], pulse[1:], color='r')
ax2.set_ylabel("pulse", color='r', fontsize=14)

ax2.legend()

plt.show()
