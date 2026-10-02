# ================================================================
# UNIT 5 - DATA VISUALIZATION USING DATAFRAME
# COMPLETE CODE SHEET
# Based on Madam's Notes
# Theory + Syntax + Code + Expected Output/Graph Notes
# ================================================================

# ================================================================
# 1. DATA VISUALIZATION
# ================================================================
# Data Visualization is the technique to represent data
# in a pictorial or graphical format.
#
# It enables stakeholders and decision makers to analyze data visually.
#
# Graphical data helps to identify new trends and patterns easily.


# ================================================================
# 2. MATPLOTLIB PYTHON LIBRARY
# ================================================================
# Matplotlib is a low-level graph plotting library in Python.
# It serves as a visualization utility.
#
# Created by: John D. Hunter
# Open source and freely usable.
# Python two-dimensional plotting library.
# Used for data visualization and creating interactive graphs/plots.
#
# Installation:
# pip install matplotlib
#
# Check version:
# import matplotlib
# print(matplotlib.__version__)


# ================================================================
# 3. IMPORT PYPLOT
# ================================================================
# Most Matplotlib utilities are under pyplot.
# pyplot is usually imported using the plt alias.

import matplotlib.pyplot as plt
import numpy as np


# ================================================================
# 4. CHECK MATPLOTLIB VERSION
# ================================================================
print("\n========== MATPLOTLIB VERSION ==========")

import matplotlib
print(matplotlib.__version__)

# OUTPUT:
# Installed Matplotlib version is displayed.


# ================================================================
# 5. EXAMPLE P_1 - LINE FROM (0,0) TO (6,250)
# ================================================================
print("\n========== P_1 - BASIC LINE ==========")

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

# GRAPH:
# A line is drawn from position (0,0) to (6,250).


# ================================================================
# 6. PLOTTING X AND Y POINTS
# ================================================================
# plot() is used to draw points/markers in a diagram.
# By default, plot() draws a line from point to point.
#
# Parameter 1 -> array containing X-axis points.
# Parameter 2 -> array containing Y-axis points.

print("\n========== PLOTTING X AND Y POINTS ==========")

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()

# GRAPH:
# A line is drawn from (1,3) to (8,10).


# ================================================================
# 7. MARKERS
# ================================================================
# marker is used to emphasize each point
# with a specified marker.

print("\n========== MARKERS ==========")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o')
plt.show()

# GRAPH:
# Each point is emphasized using a circle marker 'o'.


# ================================================================
# 8. LEGEND - BASIC
# ================================================================
# legend() places a legend on the axes.
#
# loc specifies the location of the legend.
# Default loc = "best".
#
# Common locations:
# upper left
# upper right
# lower left
# lower right
#
# bbox_to_anchor=(x,y) specifies legend coordinates.
# ncol specifies number of columns.
# Default ncol = 1.
#
# Syntax:
# matplotlib.pyplot.legend(
#     ["blue", "green"],
#     bbox_to_anchor=(0.75, 1.15),
#     ncol=2
# )
#
# Legend attributes:
# shadow     -> shadow behind legend
# markerscale -> relative marker size
# numpoints  -> number of marker points
# fontsize   -> font size
# facecolor  -> legend background color
# edgecolor  -> legend background edge color

print("\n========== LEGEND BASIC ==========")

xp = [1, 2, 3, 4, 5, 6, 7]
yp = [1, 3, 5, 0, 9, 5, 13]

plt.plot(xp, yp)
plt.legend(['single element'])
plt.show()

# GRAPH:
# The graph is displayed with a legend named "single element".


# ================================================================
# 9. LEGEND - MULTIPLE LINES
# ================================================================
print("\n========== LEGEND MULTIPLE LINES ==========")

x = np.linspace(0, 10, 1000)

fig, ax = plt.subplots()

ax.plot(x, np.sin(x), '--b', label='sine')
ax.plot(x, np.cos(x), c='r', label='cosine')

ax.axis('equal')

leg = ax.legend(loc="lower left")

plt.show()

# GRAPH:
# Two lines are displayed:
# sine
# cosine
#
# Legend location = lower left.


# ================================================================
# 10. SUBPLOT
# ================================================================
# subplot() is used to draw multiple plots in one figure.
#
# Syntax used here:
# plt.subplot(rows, columns, position)

print("\n========== SUBPLOT ==========")

# Plot 1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 3, 1)
plt.plot(x, y)

# Plot 2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 3, 2)
plt.plot(x, y)

# Plot 3
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 3, 3)
plt.plot(x, y)

plt.show()

# GRAPH:
# Three plots are displayed in one figure.


# ================================================================
# 11. SCATTER PLOT
# ================================================================
# Scatter plots are useful for visualizing data in two dimensions.
# They are particularly useful for showing:
# - correlations
# - groupings
#
# Syntax:
# matplotlib.pyplot.scatter(
#     x_axis_data,
#     y_axis_data,
#     s=None,
#     c=None,
#     marker=None,
#     linewidths=None,
#     edgecolors=None
# )
#
# Parameters:
# x_axis_data -> array containing X-axis data
# s            -> marker size
# c            -> color sequence for markers
# marker       -> marker style
# linewidths   -> width of marker border
# edgecolor    -> marker border color

print("\n========== SCATTER PLOT ==========")

x = [
    5, 7, 8, 7, 2, 17, 2, 9,
    4, 11, 12, 9, 6
]

y = [
    99, 86, 87, 88, 100, 86,
    103, 87, 94, 78, 77, 85, 86
]

plt.scatter(x, y, c="blue")
plt.show()

# GRAPH:
# A scatter plot is displayed using the given X and Y values.


# ================================================================
# 12. LINE CHART
# ================================================================
# A line chart/line graph displays information as a series
# of data points called markers connected by straight line segments.
#
# It represents the relation between X and Y data on different axes.
#
# Syntax:
# plt.plot(x_values, y_values)

print("\n========== LINE CHART ==========")

x = np.array([1, 2, 3, 4])
y = x * 2

plt.plot(x, y)
plt.show()

# GRAPH:
# A line chart is displayed for X and Y values.


# ================================================================
# 13. MULTIPLE LINES IN ONE CHART
# ================================================================
# Matplotlib allows multiple lines in the same chart.
#
# Line styles:
# '-'  -> Solid
# '--' -> Dashed
# '-.' -> Dash-dot
# ':'  -> Dotted
#
# Line width:
# linewidth or lw
#
# Line color:
# color

print("\n========== MULTIPLE LINE STYLE ==========")

x = np.array([1, 2, 3, 4])
y = x * 2

plt.plot(
    x,
    y,
    linestyle='--',
    color='red',
    linewidth=2
)

plt.show()

# GRAPH:
# A dashed red line with line width 2 is displayed.


# ================================================================
# 14. HISTOGRAM
# ================================================================
# Histograms provide a graphical representation of data distribution.
#
# They are useful for continuous data such as:
# - numerical measurements
# - sensor readings
#
# A histogram represents data in groups.
#
# X-axis -> bin ranges
# Y-axis -> frequency
#
# It is a type of bar plot used for numerical data distribution.


# ================================================================
# 15. CREATING A HISTOGRAM
# ================================================================
# Steps:
# 1. Create bins of ranges.
# 2. Distribute values into intervals.
# 3. Count values in each interval.
#
# Bins are consecutive, non-overlapping intervals.
#
# hist() is used to compute and create a histogram of x.

print("\n========== HISTOGRAM ==========")

array = np.array([
    23, 56, 87, 87, 98,
    12, 76, 98, 34, 87,
    67, 23, 87, 56, 34,
    26, 85, 47, 35, 86,
    76, 45, 86, 34, 37
])

figure, axis = plt.subplots(figsize=(8, 3))

axis.hist(
    array,
    bins=[20, 40, 60, 80, 100]
)

plt.show()

# GRAPH:
# Histogram is displayed using bins:
# 20-40
# 40-60
# 60-80
# 80-100


# ================================================================
# 16. HISTOGRAM PARAMETERS
# ================================================================
# hist() accepts the following parameters:
#
# x:
#     Array or sequence of arrays.
#
# bins:
#     Optional integer, sequence or strings.
#
# density:
#     Optional Boolean value.
#
# range:
#     Optional upper and lower range of bins.
#
# histtype:
#     Type of histogram:
#     bar, barstacked, step, stepfilled
#     Default = bar
#
# align:
#     left, right, mid
#
# weights:
#     Array of weights having same dimensions as x.
#
# bottom:
#     Location of baseline of each bin.
#
# rwidth:
#     Relative width of bars with respect to bin width.
#
# color:
#     Color or sequence of color specifications.
#
# label:
#     String or sequence of strings for multiple datasets.
#
# log:
#     Used to set histogram axis on log scale.


# ================================================================
# 17. BAR PLOT
# ================================================================
# A bar plot/bar chart represents category data
# with rectangular bars.
#
# Bar lengths/heights are proportional to values.
#
# Bar plots can be:
# - horizontal
# - vertical
#
# Bar chart describes comparisons between discrete categories.
#
# One axis -> categories
# Other axis -> measured values
#
# Syntax:
# plt.bar(x, height, width, bottom, align)

print("\n========== BAR PLOT ==========")

data = {
    'C': 20,
    'C++': 15,
    'Java': 30,
    'Python': 35
}

courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10, 5))

plt.bar(
    courses,
    values,
    color='maroon',
    width=0.4
)

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")

plt.show()

# GRAPH:
# Bar chart shows students enrolled in:
# C     -> 20
# C++   -> 15
# Java  -> 30
# Python -> 35


# ================================================================
# 18. PIE CHART
# ================================================================
# A Pie Chart is a circular statistical plot
# that can display only one series of data.
#
# The area of the chart is the total percentage of given data.
#
# Common uses:
# - Sales
# - Operations
# - Survey results
# - Resources
#
# Matplotlib pyplot provides pie() to create a pie chart.


# ================================================================
# 19. PIE() SYNTAX
# ================================================================
# Syntax:
#
# matplotlib.pyplot.pie(
#     data,
#     explode=None,
#     labels=None,
#     colors=None,
#     autopct=None,
#     shadow=False
# )
#
# Parameters:
#
# data:
#     Array of data values to be plotted.
#     Fractional area of each slice = data/sum(data).
#
# If sum(data) < 1:
#     The data values return fractional area directly,
#     resulting in an empty wedge of size 1-sum(data).
#
# labels:
#     List/sequence of strings used as labels of wedges.
#
# color:
#     Provides color to wedges.
#
# autopct:
#     String used to label wedges with numerical value.
#
# shadow:
#     Used to create shadow of wedge.


# ================================================================
# 20. PIE CHART EXAMPLE
# ================================================================
print("\n========== PIE CHART ==========")

cars = [
    'AUDI',
    'BMW',
    'FORD',
    'TESLA',
    'JAGUAR',
    'MERCEDES'
]

data = [23, 17, 35, 29, 12, 41]

fig = plt.figure(figsize=(10, 7))

plt.pie(
    data,
    labels=cars
)

plt.show()

# GRAPH:
# Pie chart is displayed for the given car data.


# ================================================================
# 21. SAVE PLOT AS A FILE
# ================================================================
# show() displays a graph as output,
# but the graph is not saved on disk.
#
# To save a Matplotlib figure, use savefig().
#
# Syntax:
#
# import matplotlib.pyplot as plt
# plt.savefig("filename.png")


# ================================================================
# 22. SAVE A SIMPLE PLOT
# ================================================================
print("\n========== SAVE PLOT ==========")

x = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 8])

plt.plot(x, y)

plt.savefig("line_chart.png")
plt.show()

# OUTPUT:
# The graph is displayed.
# A file named line_chart.png is saved.


# ================================================================
# 23. COMPLETE QUICK REVISION
# ================================================================
#
# DATA VISUALIZATION
# - Pictorial/graphical representation of data.
# - Helps stakeholders and decision makers analyze data visually.
# - Helps identify trends and patterns.
#
# MATPLOTLIB
# - Low-level graph plotting library.
# - Created by John D. Hunter.
# - Open source.
# - Two-dimensional plotting library.
#
# IMPORTANT FUNCTIONS:
#
# 1. plot()
#    -> Line graph / plotting X and Y points
#
# 2. marker
#    -> Emphasize points
#
# 3. legend()
#    -> Describe graph elements
#
# 4. subplot()
#    -> Multiple plots in one figure
#
# 5. scatter()
#    -> Two-dimensional scatter plot
#
# 6. hist()
#    -> Histogram
#
# 7. bar()
#    -> Bar chart
#
# 8. pie()
#    -> Pie chart
#
# 9. savefig()
#    -> Save graph as a file
#
# ================================================================
# END OF UNIT 5 COMPLETE CODE SHEET
# ================================================================
