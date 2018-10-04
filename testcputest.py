import os
import sys 
import random
import csv
import commands
#import psutil

uptime = commands.getoutput("uptime")


Load_avg=uptime.split(":")
LoadAvg=Load_avg[-1].split(",")
print("LoadAvg_within1min", float(LoadAvg[0]))
print("LoadAvg_within5min", float(LoadAvg[1]))
print("LoadAvg_within15min", float(LoadAvg[2]))

# Using CSV output and input
"""
os.system("uptime > uptime.csv")
csv_file = open("./uptime.csv", "r")
f = csv.reader(csv_file, delimiter=",", doublequote=True, 
	lineterminator="\r\n", quotechar='"', skipinitialspace=True)

Arrays=[]
for row in f:
	Arrays.append(row)

print("Load_avg(5 mins)")
print(float(Arrays[0][4]))

"""


cpu_temp = commands.getoutput("sudo ipmitool -c sdr list | grep CPU")
CPU_temp=cpu_temp.split(",")
SumOfCPUtemp=int(CPU_temp[1])+int(CPU_temp[4])
print("CPU temp avg", SumOfCPUtemp/2)


fan_rotation = commands.getoutput("sudo ipmitool -c sdr list | grep Fan")
Fan_rotation=fan_rotation.split(",")
SumOfFan=float(Fan_rotation[1])+float(Fan_rotation[6])
print("Fan rotation avg", SumOfFan/2)

# Using CSV output and input
"""


#os.system("while true; do ipmitool -c sdr list | grep CPU >> file1.csv; sleep 1s;done")
os.system("sudo ipmitool -c sdr list | grep CPU > cpuTemp.csv")

csv_file = open("./cpuTemp.csv", "r")
f = csv.reader(csv_file, delimiter=",", doublequote=True, 
	lineterminator="\r\n", quotechar='"', skipinitialspace=True)

Arrays_cpu=[]
for row in f:
	Arrays_cpu.append(row)
print("CPU_Temp")
for i in range(len(Arrays_cpu)):
	print(int(Arrays_cpu[i][1]))


os.system("sudo ipmitool -c sdr list | grep Fan > FanRotation.csv")

csv_file = open("./FanRotation.csv", "r")
f = csv.reader(csv_file, delimiter=",", doublequote=True, 
	lineterminator="\r\n", quotechar='"', skipinitialspace=True)

Arrays_fan=[]
for row in f:
	Arrays_fan.append(row)
print("Fan_Rotation_speed")
for i in range(len(Arrays_fan)):
	print(float(Arrays_fan[i][1]))

"""
