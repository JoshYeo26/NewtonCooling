import numpy as np
import matplotlib.pyplot  as plt
import os

T_0 =21
T_env = 10
list = [0.001,0.002,0.002,0.002,0.002,0.0015]

def newton_cool(T):
    sum = 0
    for i in list:
        sum += -i*(T - T_env)
    return sum

def eulers_method(h = 0.1, t_start = 0, t_end = 900, T_0 = 21):
    
    t_steps = int(((t_end - t_start)/h))
    t_values = np.linspace(t_start, t_start + t_steps*h, t_steps + 1)
    T_values = np.zeros(t_steps + 1)
    
    T_values[0] = T_0
    
    for i in range(t_steps):
        T_values[i+1] = T_values[i] + (h * newton_cool(T_values[i]))
        
    return t_values, T_values

print(eulers_method())

t_values, T_values = eulers_method()

def newtonplot(t_values, T_values):

    plt.plot(t_values, T_values)
    plt.xlabel("Time s")
    plt.ylabel("Temperature in degrees C")
    plt.title("Newton Cooling graph")
    plt.grid()

    return plt.show()

print(newtonplot(t_values, T_values))
filename = "Cooling_Outputs.txt"
file = open(filename, "w")
file.write("Time(s)\tTemperature (C)\n") 
for i in range(len(t_values)):
    t = t_values[i]
    T = T_values[i]
    file.write(f"{t:.1f}\t\t{T:.1f}\n")
file.close()

    
