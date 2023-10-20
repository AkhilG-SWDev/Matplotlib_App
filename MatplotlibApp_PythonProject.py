#------------------------------------------------------------------------
# Matplotlib Inflation Application

import numpy as np
import csv  
import matplotlib.pyplot as plt
from numpy import random
from matplotlib.animation import FuncAnimation
import sys

#Global variables
limit = 30
x_axes_data = []
y_axes_data = []
x_years = []
y_inflation = []
figure,axes = plt.subplots()

# Reads the data source file name from the command line argument value provided
# If the data source file name is not provided app throws an error

if len(sys.argv)>1:
    data_source = sys.argv[1]
else:
    raise Exception("Please pass the data source file name as the environment variable")

# Generate random inflation data against corresponding years and store the same in a file
# numpy library is used for generating random data and the csv module is used to write the randomly generated data by numpy to a file

for i in range(1900,2023):
    x_years.append(i)
    #Invoking random method of numpy library to generate random floating number
    y_inflation.append(str(round(random.uniform(1,20),1)))

# Opening the data source file in write mode to write the generated random data to the file
with open(data_source, 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
   
    for i in range(len(y_inflation)):
        text = x_years[i],y_inflation[i] 
        writer.writerow(text) 

#Clear the contents in the list to fetch the 
x_years.clear()
y_inflation.clear()

# Fetch the records from the data source file and populate the lists for data processing
with open(data_source) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader:
        x_years.append(int(row[0]))
        y_inflation.append(float(row[1]))

# Adding Axes Labels
axes.set_xlim(1900,1930)
axes.set_ylim(-1,30)

# Setting title name
axes.set_title('Inflation over a Centennial', {"fontsize": "18"})

plt.xlabel("YEARS FROM 1900 to 1930", {"fontsize": "14"})
plt.ylabel("INFLATION \nMaximum Value - "+str(max(y_inflation))+" | Minimum Value - "+str(min(y_inflation)), {"fontsize": "14"})

line, = axes.plot(0,0)

# Method to verify whether the given file exits or not 
def check_file_exist():
    try:
        with open(data_source, "r") as file:
            reader = csv.DictReader(file)
            new_reader = [item for item in list(reader.reader) if item!=[]][1:]
    except FileNotFoundError as e:
        raise e("Datasource file not found!.") 
    return new_reader

def animate(i):
    global limit 

    if(i == len(x_years)-1) :

        # Displaying 30 values at a time
        limit=30

        # Setting Axes limits
        axes.set_xlim(1900,1930) 
        plt.xlabel("YEARS FROM 1900 to 1930", {"fontsize": "14"}) 

        # Record is appended to the data list
        x_axes_data.append(x_years[i])
        y_axes_data.append(float(y_inflation[i]))

        # Displaying the current data in consideration on the line
        line.set_xdata(x_axes_data)
        line.set_ydata(y_axes_data)
        
        # Clearing the axes data lists
        x_axes_data.clear()
        y_axes_data.clear()
  
    elif(i == limit):
        # Record is appended to the data list
        x_axes_data.append(x_years[i])
        y_axes_data.append(float(y_inflation[i]))

        # Displaying the current data in consideration on the line
        line.set_xdata(x_axes_data)
        line.set_ydata(y_axes_data)

        # Updating Axes limits
        axes.set_xlim(x_years[i],x_years[i]+30)

        # Updating Axes Labels
        plt.xlabel("YEARS FROM "+str(x_years[i])+" to "+str(x_years[i]+30), {"fontsize": "14"})
     
        # Incrementing the limit by 30 to display the next set of values
        limit = limit+30
        
        # Clearing the axes data lists
        x_axes_data.clear()
        y_axes_data.clear()

        # Populating the axes data list with the current record under consideration
        x_axes_data.append(x_years[i])
        y_axes_data.append(float(y_inflation[i]))

        # Displaying the current data in consideration on the line
        line.set_xdata(x_axes_data)
        line.set_ydata(y_axes_data)
    
    else :
        # Populating the axes data list with the current record under consideration
        x_axes_data.append(x_years[i])
        y_axes_data.append(float(y_inflation[i]))

        # Displaying the current data in consideration on the line
        line.set_xdata(x_axes_data)
        line.set_ydata(y_axes_data)
     
    return line,

#Checking whether the given file exits or not 
check_file_exist()

# Animating the graph to show the varying data
animation = FuncAnimation(figure, func=animate,frames=np.arange(0,123,1), interval=150)

# Calling the show method of pyplot module of matplotlib library to display the graph
plt.show()

#------------------------------------------------------------------------
