# JANUS-inductions- Niva Barde - 2025AARM2209H
JANUS avionics task submission - Niva 

Task1 - Avionics 
1) Converted the Pressure reading into Altitude using the barometric formula
2) Converted the excel into csv, to plot the values
3) Used the Scipy-savgol filter to reduce the noise and make the real data plotable
4) Created animated plots, Altitude vs time, Velocity vs time using matplotlib's animation function
5) Dependancies installed - pandas, numpy, scipy, matplotlib
6) Also used functions like intrapolate and errors to ignore the non numeric values and convert them into NaNs.

TAsk2-Avionics 
1) Used a moving average to smooth noisy force sensor data.
2) Calculated pressure by dividing force by surface area (0.01 m²).
3) Determined state by tracking if pressure is rising (descending), falling (ascending), or stable (at apogee).
4) Indicated state with colored LEDs: green for ascending, yellow for apogee, and red for descending.
5) Activated buzzer only at apogee to signal peak.
This approach filters sensor noise and provides clear visual and audio feedback of the device’s flight state.


   
