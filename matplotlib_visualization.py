#   TASK 1: IMPORTING THE NECESSARY LIBRARIES

import numpy as np
import matplotlib.pyplot as plt


#   TASK 2: GENERATING THE 3 NumPy 1D ARRAYS

# Generate the first array
x = np.arange(1, 101)
'''The 'np.arange()' function is used to create a NumPy array that consists of a sequence of numbers, where the step size between the numbers in the sequence is 1 by default.'''

# Generate the second array
y1 = x**2

# Generate the third array
y2 = x**3

print(x)
print(y1)
print(y2)


#   TASK 3: LINE PLOT

# Create the plot
plt.plot(x, y1, color='blue', linestyle='solid', label='y1 = x^2')
'''The 'plt.plot()' function is used to create a line plot.'''
'''The first two arguments to the function are the x and y values of the data points to be plotted.'''
'''The third argument is the color of the line, and the fourth argument is the line style.'''
'''The fifth argument is the label for the line.'''

# Add labels to the axes
plt.xlabel('x')
plt.ylabel('y1')
'''These functions are used to add labels to the x and y axis.'''

# Add a title to the plot
plt.title('y1 vs. x')

# Show the plot
plt.show()


#   TASK 4: SCATTER PLOT

# Create the plot
plt.scatter(x, y2, color='red', marker='o', label='y2 = x^3')
'''The 'plt.scatter()' function is used to create a scatter plot.'''
'''The fourth argument is the marker style.'''

# Add labels to the axes
plt.xlabel('x')
plt.ylabel('y2')

# Add a title to the plot
plt.title('y2 vs. x')

# Show the plot
plt.show()


#   TASK 5: HISTOGRAM

# Generate the random array
z = np.random.randn(1000)
'''The 'np.random.randn()' function is used to generate a NumPy array of random numbers from the standard normal distribution.'''

# Create the histogram
plt.hist(z, bins=100)
'''The 'plt.hist()' function is used to create a histogram.'''
'''The first argument to the function is the array of data to be plotted.'''
'''The second argument is the number of bins to be used.'''

# Add labels to the axes
plt.xlabel('z')
plt.ylabel('Count')

# Add a title to the plot
plt.title('Histogram of z')

# Show the plot
plt.show()


#   TASK 6: SUBPLOTS

# Create the figure
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
'''The 'plt.subplots()' function is used to create a figure with subplots.'''
'''The first argument to the function is the number of rows of subplots'''
'''The second argument is the number of columns of subplots'''
'''The third argument is the size of the figure.'''
'''The 'ax1' and 'ax2' variables are Axis objects that represent the two subplots.'''

# Plot the line plot
ax1.plot(x, y1, color='blue', linestyle='solid', label='y1 = x^2')

# Plot the scatter plot
ax2.scatter(x, y2, color='red', marker='o', label='y2 = x^3')

# Add labels to the axes
ax1.set_xlabel('x')
ax1.set_ylabel('y1')
ax2.set_xlabel('x')
ax2.set_ylabel('y2')
'''The 'set_xlabel()' and 'set_ylabel()' functions are used to add labels to the axis of the two subplots.'''

# Add a title to the figure
fig.suptitle('y1 vs. x, y2 vs. x')

# Add a legend to the figure
plt.legend()

# Show the plot
plt.show()

plt.savefig("my_figure.png", dpi=300)

#   TASK 7: CUSTOMIZATION AND STYLING / TASK 8: SAVING FIGURES

# Create the plot
plt.plot(x, y1, color='blue', linestyle='solid', label='y1 = x^2')
plt.plot(x, y2, color='red', linestyle='dashed', label='y2 = x^3')

# Add gridlines
plt.grid(color='gray', linestyle='dotted')

# Add a legend
plt.legend(loc='upper right')

# Change the font size of the labels
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)

# Show the plot
#plt.show()

# Save the figure
plt.savefig("Task_7_&_8_figure.png", dpi=300)
'''The 'savefig()' function takes two arguments: the filename of the file to be saved, and the resolution of the file in dots per inch (dpi).'''
'''In this case, the filename of the file is 'my_figure.png' and the resolution of the file is '300 dpi'.'''