import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.signal import savgol_filter #to smooth the noisy data inorder to create a readable graph)

P0, T0, g, L, R = 101325, 288.15, 9.80665, 0.0065, 287.05

def altitude_from_pressure(P):
    return (T0 / L) * (1 - (P / P0)**(R * L / g))#formula



df = pd.read_csv(r"C:\Users\NIVA\Downloads\Raw_Test_Flight_Data_25 - Sheet1 (1).csv")
pressure = pd.to_numeric(df['Pressure (Pa)'], errors='coerce').interpolate().fillna(method='bfill')#converts empty values to NaNs and allots them approximate values.

altitude = altitude_from_pressure(pressure)
alt_smooth = savgol_filter(altitude, 21, 2)#averages 21 points 
velocity = np.gradient(alt_smooth)#slope of the altitude time graph to form velocity time graph
vel_smooth = savgol_filter(velocity, 21, 2)
time = np.arange(len(pressure))#takes a sample time

fig, (ax1, ax2) = plt.subplots(2, 1)#plots two graphs one above the other, hence two rows, one column.

line1, = ax1.plot([], [], 'b')
ax1.set_xlim(0, len(time) - 1)  
ax1.set_ylim(min(alt_smooth), max(alt_smooth)) 

line2, = ax2.plot([], [], 'r')
ax2.set_xlim(0, len(time) - 1)
ax2.set_ylim(min(vel_smooth), max(vel_smooth))
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Velocity (m/s)')

def update(i):
    line1.set_data(time[:i], alt_smooth[:i])#this means in frame 0, no data, in frame1, the first data, so on and so forth. 
    line2.set_data(time[:i], vel_smooth[:i])

    return line1, line2

ani = FuncAnimation(fig, update, frames=len(time), interval=50, blit=True)
plt.show()