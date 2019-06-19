import matplotlib.pyplot as plt
import csv
import os
import re

file = input("file: ")

alt = []
target = []
actual = []

with open(os.path.join('lander', file + ".txt"),'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        alt.append(float(row[0]))
        target.append(abs(float(row[1])))
        actual.append(float(re.findall("[-+]?\d*\.\d+|\d+",row[2])[1]))


plt.plot(alt, target, label='target')
plt.plot(alt, actual, label='actual')
plt.xlabel('Altitude (m)')
plt.ylabel('descent rate (m/s)')
plt.title(file)
plt.legend()
plt.show()
