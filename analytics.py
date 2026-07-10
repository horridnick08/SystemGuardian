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

print("\n===== SYSTEM REPORT =====")

print(f"Average CPU : {np.mean(cpu):.2f}%")
print(f"Average RAM : {np.mean(ram):.2f}%")
print(f"Average Disk: {np.mean(disk):.2f}%")

print()

print(f"Peak CPU : {np.max(cpu):.2f}%")
print(f"Peak RAM : {np.max(ram):.2f}%")
print(f"Peak Disk: {np.max(disk):.2f}%")

print()

latest_ram = ram[-1]

if latest_ram > 85:
    print("⚠ WARNING: RAM usage is very high!")

if latest_ram > 90:
    print("🚨 CRITICAL: RAM usage above 90%")

print("\n===== RAM TREND ANALYSIS =====")

x = np.arange(len(ram))

trend = np.polyfit(x, ram, 1)

slope = trend[0]

print(f"Trend Slope: {slope:.4f}")

if slope > 0.1:
    print("⚠ RAM usage is trending upward")

elif slope < -0.1:
    print("✅ RAM usage is decreasing")

else:
    print("➖ RAM usage is stable")

if np.mean(ram[-5:]) > 90 and slope > 0:
    print("🚨 Possible memory leak detected")