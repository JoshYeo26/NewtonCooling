"""
This script will use Euler's method to solve Newton's experimental law of cooling
for a cube with heat being transferred from 6 different sides. The model will tell us how
the cube will cool over a period of 900 seconds with an assumed initial temperature of 21 degrees C, and environmental temperature of 21 degrees C
The third function will then plot a graph of the data with appropriately labelled axes.
Finally the fourth function will write and label the data to a .txt file.

Euler's method rearranges the standard derivative formula as follows:
    dT/dt = f(t)
    dT/dt = (T(t+h) - T(t))/h
    f(t) = (T(t+h) - T(t))/h
    T(t+h) = h*T(t) + T(t)
    
This will allow us to calculate the stepwise temperature of the cube for increasing time (t).
"""
import numpy as np
import matplotlib.pyplot  as plt


T_0 =21 #initial temperature
T_env = 10 #environmental temperature
Coeff_room_edge = [0.001,0.002,0.002,0.002,0.002,0.0015] #cooling coefficients of each side of the cube

def newton_cool(T):
    """
    Right hand side of ODE (f(t)), the model we are using to calculate the change in temperature.

    Parameters
    ----------
    T : float
        Temperature with respect to given time

    Returns
    -------
    sum : float
        Rate of change of temperature over time.

    """
    sum = 0
    for i in Coeff_room_edge:
        sum += -i*(T - T_env)
    return sum #differential equation

def eulers_method(h = 0.1, t_start = 0, t_end = 900, T_0 = 21):
    """
    Solving the differential equation using Euler's method.

    Parameters
    ----------
    h : float
        Time step size
    t_start : float
        Starting time
    t_end : float
        Ending time 
    T_0 : float
        Initial temperature of the cube

    Returns
    -------
    t_values : float
        Values of time for which we calculate respective temperature
    T_values : float
        Temperature at the specified time

    """
    
    t_steps = int(((t_end - t_start)/h)) #Number of time steps for which we calculate temperature
    t_values = np.linspace(t_start, t_start + t_steps*h, t_steps + 1) #list of all times for which we calculate temperture
    T_values = np.zeros(t_steps + 1) #Temperature at specified times
    
    T_values[0] = T_0 #Store for initial temperature
    
    for i in range(t_steps): #Euler's method 
        T_values[i+1] = T_values[i] + (h * newton_cool(T_values[i]))
        
    return t_values, T_values

print(eulers_method()) #calls the function

t_values, T_values = eulers_method() #Global definition for these variables

def newton_plot(t_values, T_values):
    """
    Function to plot the time and temperature on a line graph.

    Parameters
    ----------
    t_values : float
        Time
    T_values : float
        Temperature

    Returns
    -------
    Plotted graph 

    """

    plt.plot(t_values, T_values) #plots values
    plt.xlabel("Time (seconds)") #labels x-axis
    plt.ylabel("Temperature (degrees C)") #labels y-axis
    plt.title("Newton Cooling graph") #titles the graph

    

print(newton_plot(t_values, T_values)) #calls the function


def newton_write(t_values, T_values, filename = "Cooling_Outputs.txt"):
    """
    

    Parameters
    ----------
    t_values : float
        Time
    T_values : float
        Temperature
    filename : file
        File in which we can store the values of temperature and their respective times

    Returns
    -------
    Written file

    """
    file = open(filename, "w") #opens file for writing
    file.write("Time(s)\tTemperature(C)\n") #writes the defined value headings into the file with appropriate spacing and specified units
    for i in range(len(t_values)):
        t = t_values[i]
        T = T_values[i]
        file.write(f"{t:.1f}\t\t{T}\n") #writes the defined value into the file with appropriate spacing and decimal places
    file.close() #closes the file
        
newton_write(t_values, T_values) #calls the function


    
    

    