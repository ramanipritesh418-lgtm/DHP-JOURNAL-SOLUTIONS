# ================================================================
# UNIT 4 - DATAFRAME HANDLING USING PANDAS AND NUMPY
# COMPLETE GITHUB CODE SHEET
# Based on Madam's Unit 4 Theory
# Includes: Theory + Syntax + Code + Expected Output
# ================================================================


# ================================================================
# PART A - PYTHON PANDAS LIBRARY
# ================================================================

# THEORY:
# Pandas is a Python library used for data analysis and data manipulation.
# It provides flexible and easy-to-use tools for working with data.
#
# Pandas was created by Wes McKinney in 2008.
#
# KEY FEATURES OF PANDAS:
# 1. DataFrame objects for quick and effective data analysis.
# 2. Handling and analyzing different types of data.
# 3. Data cleaning and manipulation.
# 4. Data processing.
# 5. Fast operations.
# 6. Sorting, Selection, Filtering, Data Cleaning and Data Handling.
# 7. Many functions for data analysis.
# 8. Works with other Python libraries.
# 9. Quick and efficient.
#
# TWO MAIN DATA STRUCTURES:
# 1. Series
# 2. DataFrame

import pandas as pd


# ================================================================
# 1. PANDAS SERIES
# ================================================================

# THEORY:
# Series is a one-dimensional labelled array.
# It can contain Integer, String, Float, Python objects, etc.
# Every value has an index.
# It is similar to a single Excel column.
#
# SYNTAX:
# pandas.Series(data, index, dtype, copy)
#
# PARAMETERS:
# data  -> Data used to create Series.
# index -> Unique/hashable labels for values.
# dtype -> Data type of Series.
# copy  -> Copy the data.

print("\n========== 1. SERIES FROM LIST ==========")

data = ['a', 'b', 'c', 'd']
s = pd.Series(data)
print(s)

# OUTPUT:
# 0    a
# 1    b
# 2    c
# 3    d
# dtype: object


# ================================================================
# 2. SERIES WITH INDEX
# ================================================================

print("\n========== 2. SERIES WITH INDEX ==========")

n = [1, 7, 2]
student = pd.Series(n, index=["x", "y", "z"])
print(student)

# OUTPUT:
# x    1
# y    7
# z    2
# dtype: int64


# ================================================================
# 3. SERIES FROM DICTIONARY
# ================================================================

print("\n========== 3. SERIES FROM DICTIONARY ==========")

dictionary = {'a': 0., 'b': 1., 'c': 2.}
s1 = pd.Series(dictionary)
print(s1)

# OUTPUT:
# a    0.0
# b    1.0
# c    2.0
# dtype: float64


# ================================================================
# 4. SELECTED INDEX FROM DICTIONARY
# ================================================================

print("\n========== 4. SELECTED INDEX FROM DICTIONARY ==========")

marks = {'s1': 420, 's2': 350, 's3': 400, 's4': 89}
selected = pd.Series(marks, index=['s1', 's4'])
print(selected)

# OUTPUT:
# s1    420
# s4     89
# dtype: int64


# ================================================================
# PART B - DATAFRAME
# ================================================================

# THEORY:
# DataFrame is a two-dimensional data structure.
# It contains rows and columns.
# It has two indexes:
# 1. Row index
# 2. Column index
#
# A DataFrame can contain different data types.
# It is similar to a table or spreadsheet.
#
# SYNTAX:
# pandas.DataFrame(data, index, columns, dtype, copy)
#
# PARAMETERS:
# data    -> ndarray, Series, map, constants, lists, arrays, etc.
# index   -> Row labels.
# columns -> Column labels.
# dtype   -> Data type.
# copy    -> Copy the data.


# ================================================================
# 5. DATAFRAME USING LIST / ARRAY-LIKE DATA
# ================================================================

print("\n========== 5. DATAFRAME USING LIST ==========")

data = ['Pandas', 'Data', 'BCA', 'Python']
df = pd.DataFrame(data)
print(df)

# OUTPUT:
#         0
# 0  Pandas
# 1    Data
# 2     BCA
# 3  Python


# ================================================================
# 6. INDEXED DATAFRAME
# ================================================================

print("\n========== 6. INDEXED DATAFRAME ==========")

data = {
    'Name': ['Ram', 'Shyam', 'Mohan', 'Sita'],
    'Age': [20, 21, 19, 22]
}

df = pd.DataFrame(data, index=['t1', 't2', 't3', 't4'])
print(df)

# OUTPUT:
#       Name  Age
# t1     Ram   20
# t2   Shyam   21
# t3   Mohan   19
# t4    Sita   22


# ================================================================
# 7. DATAFRAME FROM NUMPY ARRAY
# ================================================================

# This demonstrates the "DataFrame using Array" concept.
# The DataFrame can be created from array-like data.

import numpy as np

print("\n========== 7. DATAFRAME USING NUMPY ARRAY ==========")

arr = np.array([
    ['Ram', 20],
    ['Shyam', 21],
    ['Mohan', 19]
])

df_array = pd.DataFrame(arr, columns=['Name', 'Age'])
print(df_array)

# OUTPUT:
#     Name Age
# 0    Ram  20
# 1  Shyam  21
# 2  Mohan  19


# ================================================================
# 8. DICTIONARY OF EQUAL-LENGTH LISTS
# ================================================================

# THEORY:
# A dictionary can be used to create a DataFrame.
# All lists should have the same length.
# If index is not supplied, default index is used.

print("\n========== 8. DICTIONARY OF EQUAL-LENGTH LISTS ==========")

data = {
    'Name': ['A', 'B', 'C'],
    'Age': [20, 21, 22]
}

df = pd.DataFrame(data)
print(df)

# OUTPUT:
#   Name  Age
# 0    A   20
# 1    B   21
# 2    C   22


# ================================================================
# 9. LIST OF DICTIONARIES
# ================================================================

# THEORY:
# In a list of dictionaries:
# - Dictionary keys become column names.
# - If a value is missing, NaN is shown.

print("\n========== 9. LIST OF DICTIONARIES ==========")

data = [
    {'x': 1, 'y': 2},
    {'x': 3, 'y': 4},
    {'x': 5}
]

df = pd.DataFrame(data)
print(df)

# OUTPUT:
#    x    y
# 0  1  2.0
# 1  3  4.0
# 2  5  NaN


# ================================================================
# 10. READ EXCEL FILE
# ================================================================

# THEORY:
# openpyxl can be installed for Excel file handling.
# Installation:
# pip install openpyxl
#
# SYNTAX:
# pd.read_excel('report.xlsx')

print("\n========== 10. READ EXCEL FILE ==========")
print("# Example:")
print("# df = pd.read_excel('report.xlsx')")
print("# print(df)")


# ================================================================
# 11. READ CSV FILE
# ================================================================

# THEORY:
# CSV files can be read using read_csv().
#
# SYNTAX:
# pd.read_csv('report.csv')

print("\n========== 11. READ CSV FILE ==========")
print("# Example:")
print("# df = pd.read_csv('report.csv')")
print("# print(df)")


# ================================================================
# PART C - DATAFRAME OPERATIONS
# ================================================================

# Common DataFrame used for demonstrations below.

data = pd.DataFrame({
    'Roll No.': [101, 102, 103, 104, 105],
    'Name': ['Amit', 'Bharat', 'Chetan', 'Dhruv', 'Esha'],
    'Age': [20, 21, 19, 22, 20],
    'Marks': [75, 82, 68, 91, 77],
    'Students': [1500, 2500, 1800, 3000, 2200]
})

print("\n========== DEMO DATAFRAME ==========")
print(data)

# OUTPUT:
#    Roll No.    Name  Age  Marks  Students
# 0       101    Amit   20     75      1500
# 1       102  Bharat   21     82      2500
# 2       103  Chetan   19     68      1800
# 3       104   Dhruv   22     91      3000
# 4       105    Esha   20     77      2200


# ================================================================
# 12. SHAPE
# ================================================================

# THEORY:
# shape gives the number of rows and columns.
# Result is returned as (rows, columns).

print("\n========== 12. SHAPE ==========")

print(data.shape)

r, c = data.shape
print("Rows =", r)
print("Columns =", c)

# OUTPUT:
# (5, 5)
# Rows = 5
# Columns = 5


# ================================================================
# 13. HEAD()
# ================================================================

# THEORY:
# head() returns the first 5 rows by default.
# head(n) returns the first n rows.

print("\n========== 13. HEAD ==========")

print(data.head())
print(data.head(3))

# OUTPUT:
# data.head() -> first 5 rows
# data.head(3) -> first 3 rows


# ================================================================
# 14. TAIL()
# ================================================================

# THEORY:
# tail() returns the last 5 rows by default.
# tail(n) returns the last n rows.

print("\n========== 14. TAIL ==========")

print(data.tail())
print(data.tail(3))

# OUTPUT:
# data.tail() -> last 5 rows
# data.tail(3) -> last 3 rows


# ================================================================
# 15. RETRIEVE ROWS USING SLICING
# ================================================================

print("\n========== 15. ROW SLICING ==========")

print(data[2:6])

# OUTPUT:
# Returns rows from index 2 up to index 5.


# Alternate slicing
print("\n========== ALTERNATE ROW SLICING ==========")

print(data[0::2])

# OUTPUT:
# Returns every second row starting from index 0.


# Reverse slicing example
print("\n========== REVERSE ROW SLICING ==========")

print(data[4:0:-1])

# OUTPUT:
# Returns rows in reverse order from index 4 to index 1.


# ================================================================
# 16. RETRIEVE COLUMNS
# ================================================================

print("\n========== 16. COLUMNS ==========")

print(data.columns)

# OUTPUT:
# Index(['Roll No.', 'Name', 'Age', 'Marks', 'Students'], dtype='object')


# ================================================================
# 17. SELECT ONE COLUMN
# ================================================================

print("\n========== 17. SELECT ONE COLUMN ==========")

print(data["Name"])

# OUTPUT:
# Prints only the Name column.


# ================================================================
# 18. SELECT MULTIPLE COLUMNS
# ================================================================

print("\n========== 18. SELECT MULTIPLE COLUMNS ==========")

print(data[["Roll No.", "Name"]])

# OUTPUT:
# Prints Roll No. and Name columns.


# ================================================================
# 19. TO_NUMPY()
# ================================================================

# THEORY:
# to_numpy() converts a DataFrame into a NumPy array.

print("\n========== 19. TO_NUMPY ==========")

small_df = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4]
})

array_data = small_df.to_numpy()
print(array_data)

# OUTPUT:
# [[1 3]
#  [2 4]]


# ================================================================
# 20. MAX()
# ================================================================

print("\n========== 20. MAX ==========")

print("Maximum Marks =", data["Marks"].max())

# OUTPUT:
# Maximum Marks = 91


# ================================================================
# 21. MIN()
# ================================================================

print("\n========== 21. MIN ==========")

print("Minimum Marks =", data["Marks"].min())

# OUTPUT:
# Minimum Marks = 68


# ================================================================
# 22. LOC[]
# ================================================================

# THEORY:
# loc[] retrieves rows, columns or values by labels.
# It uses labels/index names.

print("\n========== 22. LOC ==========")

df_loc = pd.DataFrame({
    'Marks': [70, 80, 90, 75, 85],
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Age': [20, 21, 55, 19, 22]
}, index=['Row_1', 'Row_2', 'Row_3', 'Row_4', 'Row_5'])

print(df_loc.loc['Row_3', 'Age'])

# OUTPUT:
# 55


# ================================================================
# 23. ILOC[]
# ================================================================

# THEORY:
# iloc[] uses integer positions.
# Position starts from 0.

print("\n========== 23. ILOC ==========")

print(df_loc.iloc[1])
print(df_loc.iloc[0])

# OUTPUT:
# iloc[1] -> second row
# iloc[0] -> first row


# ================================================================
# 24. DESCRIBE()
# ================================================================

# THEORY:
# describe() gives statistical information about Series/DataFrame.
# It includes values such as:
# count, mean, standard deviation, minimum, quartiles and maximum.

print("\n========== 24. DESCRIBE ==========")

print(data.describe())

# OUTPUT:
# Statistical summary including count, mean, std, min, 25%, 50%, 75%, max.


# ================================================================
# 25. QUERY / FILTERING
# ================================================================

# THEORY:
# DataFrame can be filtered using a condition.

print("\n========== 25. QUERY / FILTERING ==========")

filtered = data[data.Students > 2000]
print(filtered)

# OUTPUT:
# Returns rows where Students > 2000.


# ================================================================
# 26. SORT_VALUES()
# ================================================================

# THEORY:
# sort_values() sorts a DataFrame according to selected column(s).
#
# SYNTAX:
# DataFrame.sort_values(
#     by,
#     axis=0,
#     ascending=True,
#     inplace=False,
#     kind='quicksort',
#     na_position='last'
# )

print("\n========== 26. SORT_VALUES ==========")

sort_df = pd.DataFrame({
    'Age': [22, 19, 21, 20],
    'Qualified': ['Yes', 'No', 'Yes', 'Yes']
})

print(sort_df.sort_values(by='Age'))

# OUTPUT:
# Rows are arranged according to Age in ascending order.


# ================================================================
# 27. MISSING DATA
# ================================================================

# THEORY:
# Missing data can create problems during data cleaning and analysis.
# Sometimes missing data can be useful, so it should be handled carefully.

print("\n========== 27. MISSING DATA ==========")

missing_df = pd.DataFrame({
    'Name': ['A', 'B', None, 'D'],
    'Students': [100, None, 300, 400],
    'Department': ['BCA', 'BCA', None, 'BCA']
})

print(missing_df)

# OUTPUT:
# Missing values are displayed as NaN/None depending on column type.


# ================================================================
# 28. FILLNA()
# ================================================================

# THEORY:
# fillna() replaces missing values.

print("\n========== 28. FILLNA ==========")

filled_df = missing_df.fillna(0)
print(filled_df)

# OUTPUT:
# Missing values are replaced by 0.


# Dictionary replacement example
print("\n========== FILLNA USING DICTIONARY ==========")

filled_dict = missing_df.fillna({
    'Name': 'Unknown',
    'Students': 0,
    'Department': 'Not Available'
})

print(filled_dict)

# OUTPUT:
# Missing Name -> Unknown
# Missing Students -> 0
# Missing Department -> Not Available


# ================================================================
# 29. DROPNA()
# ================================================================

# THEORY:
# dropna() removes rows containing missing data.

print("\n========== 29. DROPNA ==========")

dropped_df = missing_df.dropna()
print(dropped_df)

# OUTPUT:
# Rows containing missing values are removed.


# ================================================================
# 30. DATA CLEANING
# ================================================================

# THEORY:
# Data cleaning means removing unwanted or missing data
# and preparing data for analysis.

print("\n========== 30. DATA CLEANING ==========")

clean_df = missing_df.fillna({
    'Name': 'Unknown',
    'Students': 0,
    'Department': 'Not Available'
})

print(clean_df)

# OUTPUT:
# Data after replacing missing values.


# ================================================================
# PART D - NUMPY
# ================================================================

# THEORY:
# NumPy means Numerical Python.
# It is a fundamental Python library for scientific computing.
#
# NumPy supports:
# - Single-dimensional arrays
# - Multi-dimensional arrays
# - High-performance numerical calculations
#
# A NumPy array is a grid of values of the same type.
#
# NumPy was created by Travis Oliphant in 2005 from earlier
# numerical modules.
#
# NumPy is mostly written in C.
#
# It provides:
# - High-speed numerical computation
# - Multidimensional arrays and matrices
# - Mathematical and logical operations
# - Fourier Transform
# - Reshaping multidimensional arrays
# - Linear algebra functions
# - Random number generation
#
# NumPy works with SciPy and Matplotlib for scientific/numerical tasks.
#
# ADVANTAGES:
# 1. Array-oriented computing.
# 2. Efficient multidimensional arrays.
# 3. Scientific computations.
# 4. Fourier Transform.
# 5. Reshape multidimensional arrays.
# 6. Linear algebra functions.
# 7. Random number generation.
#
# INSTALLATION:
# pip install numpy


# ================================================================
# 31. NUMPY ARRAY
# ================================================================

print("\n========== 31. NUMPY ARRAY ==========")

arr = np.array([1, 2, 3, 4, 5])
print(arr)

# OUTPUT:
# [1 2 3 4 5]


# ================================================================
# 32. NUMPY ALIAS
# ================================================================

# THEORY:
# NumPy can be imported with the short name np.

print("\n========== 32. NUMPY ALIAS ==========")

import numpy as np

arr = np.array([10, 20, 30])
print(arr)

# OUTPUT:
# [10 20 30]


# ================================================================
# 33. 1-D ARRAY
# ================================================================

print("\n========== 33. 1-D ARRAY ==========")

arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# OUTPUT:
# [1 2 3 4 5]


# ================================================================
# 34. 2-D ARRAY
# ================================================================

print("\n========== 34. 2-D ARRAY ==========")

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr2)

# OUTPUT:
# [[1 2 3]
#  [4 5 6]]


# ================================================================
# 35. NDIM
# ================================================================

# THEORY:
# ndim gives the number of dimensions of an array.
# Scalar -> 0 dimension
# 1-D array -> 1 dimension
# 2-D array -> 2 dimensions
# 3-D array -> 3 dimensions

print("\n========== 35. NDIM ==========")

scalar = np.array(10)
one_d = np.array([1, 2, 3])
two_d = np.array([[1, 2], [3, 4]])
three_d = np.array([[[1, 2], [3, 4]]])

print("Scalar ndim =", scalar.ndim)
print("1-D ndim =", one_d.ndim)
print("2-D ndim =", two_d.ndim)
print("3-D ndim =", three_d.ndim)

# OUTPUT:
# Scalar ndim = 0
# 1-D ndim = 1
# 2-D ndim = 2
# 3-D ndim = 3


# ================================================================
# 36. SHAPE AND SIZE
# ================================================================

# THEORY:
# shape tells the dimensions/size of each dimension.
# size tells the total number of elements.

print("\n========== 36. SHAPE AND SIZE ==========")

arr = np.array([10, 12, 13])

print("ndim =", arr.ndim)
print("size =", arr.size)
print("shape =", arr.shape)

# OUTPUT:
# ndim = 1
# size = 3
# shape = (3,)


# ================================================================
# 37. NUMPY.ARRAY() SYNTAX AND PARAMETERS
# ================================================================

# THEORY:
#
# numpy.array(
#     object,
#     dtype=None,
#     copy=True,
#     order=None,
#     subok=False,
#     ndmin=0
# )
#
# PARAMETERS:
# object -> Input object/data.
# dtype  -> Desired data type.
# copy   -> Whether to copy the data.
# order  -> Memory layout/order.
# subok  -> Allows subclasses.
# ndmin  -> Minimum number of dimensions.


# ================================================================
# 38. MEAN
# ================================================================

# THEORY:
# Mean is the arithmetic average.
#
# Mean = Sum of values / Number of values
#
# SYNTAX:
# numpy.mean(arr, axis=None, dtype=None, out=None)

print("\n========== 38. MEAN ==========")

mean_data = np.array([
    80, 85, 90, 75, 95, 88, 92,
    87, 91, 86, 89, 84, 95
])

mean_value = np.mean(mean_data)
print(mean_value)

# OUTPUT:
# 89.76923076923077
#
# Calculation:
# Sum of values / 13 = 89.76923076923077
# Approximately = 89.77


# ================================================================
# 39. MEDIAN
# ================================================================

# THEORY:
# Median is the middle value of sorted data.
#
# For odd number of values:
# Middle value is the median.
#
# For even number of values:
# Average of the two middle values is the median.

print("\n========== 39. MEDIAN - ODD DATA ==========")

odd_data = np.array([7, 1, 5, 3, 9])
print("Sorted:", np.sort(odd_data))
print("Median:", np.median(odd_data))

# OUTPUT:
# Sorted: [1 3 5 7 9]
# Median: 5.0


print("\n========== MEDIAN - EVEN DATA ==========")

even_data = np.array([7, 1, 5, 3])
print("Sorted:", np.sort(even_data))
print("Median:", np.median(even_data))

# OUTPUT:
# Sorted: [1 3 5 7]
# Median: 4.0
#
# Calculation:
# (3 + 5) / 2 = 4


# ================================================================
# 40. MODE
# ================================================================

# THEORY:
# Mode is the value that occurs most frequently.
#
# SciPy can be used to calculate mode.
#
# Installation:
# pip install scipy
#
# Syntax:
# scipy.stats.mode(array, axis=0)

print("\n========== 40. MODE ==========")

from scipy import stats

mode_data = np.array([2, 3, 3, 4, 5, 3, 6, 2])

mode_result = stats.mode(mode_data, axis=0, keepdims=False)
print("Mode =", mode_result.mode)
print("Count =", mode_result.count)

# OUTPUT:
# Mode = 3
# Count = 3


# ================================================================
# 41. STANDARD DEVIATION
# ================================================================

# THEORY:
# Standard deviation measures how much values differ from the average.
#
# Syntax:
# numpy.std(arr, axis=None, dtype=None, out=None)
#
# PARAMETERS:
# arr   -> Input array.
# axis  -> Axis along which calculation is performed.
# dtype -> Data type.
# out   -> Output location.

print("\n========== 41. STANDARD DEVIATION ==========")

std_data = np.array([10, 12, 14, 16, 18])

std_value = np.std(std_data)
print("Standard Deviation =", std_value)

# OUTPUT:
# Standard Deviation = 2.8284271247461903


# ================================================================
# 42. VARIANCE
# ================================================================

# THEORY:
# Variance indicates how much values differ from the average.
# It is the average of squared deviations from the mean.
#
# Square root of variance gives standard deviation.
#
# Syntax:
# numpy.var(arr, axis=None, dtype=None, out=None)
#
# PARAMETERS:
# arr   -> Input array.
# axis  -> Axis along which calculation is performed.
# dtype -> Data type.
# out   -> Output location.

print("\n========== 42. VARIANCE ==========")

var_data = np.array([10, 12, 14, 16, 18])

var_value = np.var(var_data)
print("Variance =", var_value)

# OUTPUT:
# Variance = 8.0


# ================================================================
# UNIT 4 QUICK REVISION MAP
# ================================================================
#
# PANDAS
# 1. Python Pandas Library
# 2. Key Features
# 3. Series
# 4. Series Syntax/Parameters
# 5. Series from List
# 6. Series with Index
# 7. Series from Dictionary
# 8. Selected Index
# 9. DataFrame
# 10. DataFrame Syntax/Parameters
# 11. DataFrame using Array
# 12. DataFrame using List
# 13. Dictionary of Equal-Length Lists
# 14. List of Dictionaries
# 15. Excel
# 16. CSV
# 17. shape
# 18. head
# 19. tail
# 20. Retrieve Rows
# 21. Retrieve Columns
# 22. Selected Columns
# 23. to_numpy
# 24. max
# 25. min
# 26. loc
# 27. iloc
# 28. describe
# 29. Query/Filtering
# 30. sort_values
# 31. Missing Data
# 32. fillna
# 33. dropna
# 34. Data Cleaning
#
# NUMPY
# 35. Introduction
# 36. Advantages
# 37. Setup
# 38. numpy.array
# 39. Parameters
# 40. np
# 41. 1-D
# 42. 2-D
# 43. ndim
# 44. shape
# 45. size
# 46. Mean
# 47. Median
# 48. Mode
# 49. Standard Deviation
# 50. Variance
#
# ================================================================
# END OF UNIT 4 COMPLETE CODE SHEET
# ================================================================
