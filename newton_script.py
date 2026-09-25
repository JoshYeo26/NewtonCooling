"""
This script will read the data given in the specified file appropriately,
making it ready to be used or called at a later date.
"""
def newton_read(filename = "Cooling_Outputs.txt" ):
    """
    Reads the data in the file: "Cooling_Outputs.txt"

    Parameters
    ----------
    filename : file
        Calls the file to be read

    Returns
    -------
    Read file 

    """

    filename = "Cooling_Outputs" #name of file to be read
    file = open(filename, "r") #opens file for reading
    line = file.readline(1) #reads the first line of the file (headers for the data)

    Newton_Cooling_Time = [] #list space to store data with suitable variables assigned
    Newton_Cooling_Temperature = [] #list space to store data with suitable variables assigned
    for line in file:
        values = line.split(',') #splits the data into two seperate parts (time and temperature)
        Newton_Cooling_Time.append(float(values[1])) #reads the time values
        Newton_Cooling_Temperature.append(float(values[0])) #reads the temperature values
    file.close() #closes file
    

newton_read() #calls the function










