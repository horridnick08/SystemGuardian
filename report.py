import numpy as np

data = np.genfromtxt(
    "system_logs.csv",
    delimiter=",",
    skip_header=1,
    usecols=(1, 2, 3)
)

cpu = data[:, 0]
ram = data[:, 1]
disk = data[:, 2]

avg_cpu = np.mean(cpu)
avg_ram = np.mean(ram)
avg_disk = np.mean(disk)

peak_cpu = np.max(cpu)
peak_ram = np.max(ram)
peak_disk = np.max(disk)

health = 100 - (
    avg_cpu * 0.3 +
    avg_ram * 0.5 +
    avg_disk * 0.2
)

report = f"""
=================================
      SYSTEM GUARDIAN REPORT
=================================

Average CPU Usage  : {avg_cpu:.2f}%
Peak CPU Usage     : {peak_cpu:.2f}%

Average RAM Usage  : {avg_ram:.2f}%
Peak RAM Usage     : {peak_ram:.2f}%

Average Disk Usage : {avg_disk:.2f}%
Peak Disk Usage    : {peak_disk:.2f}%

Health Score       : {health:.2f}/100

"""

if avg_ram > 80:
    report += "\nWARNING: RAM usage is consistently high"

if peak_ram > 90:
    report += "\nCRITICAL: RAM crossed 90%"

print(report)

with open("daily_report.txt", "w") as file:
    file.write(report)

print("\nReport saved as daily_report.txt")