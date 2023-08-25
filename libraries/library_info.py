# Standard Library Libraries
import os  # Operating System Interface
import sys  # System-specific parameters and functions
import datetime  # Date and Time Manipulation

# Using the os library to get the current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# Using the sys library to access command-line arguments
print("Command Line Arguments:", sys.argv)

# Using the datetime library to get the current date and time
current_time = datetime.datetime.now()
print("Current Time:", current_time)

# Data Manipulation Libraries
import numpy as np  # Numerical Computing
import pandas as pd  # Data Analysis and Manipulation

# Using numpy to create and manipulate arrays
arr = np.array([1, 2, 3, 4, 5])
print("Sum of Array:", np.sum(arr))

# Using pandas to create and manipulate DataFrames
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Web Development Libraries
import requests  # HTTP Library
from bs4 import BeautifulSoup  # HTML Parsing

# Using requests to make HTTP requests
response = requests.get("https://www.example.com")
print("Status Code:", response.status_code)

# Using BeautifulSoup to parse HTML content
soup = BeautifulSoup(response.text, "html.parser")
print("Title:", soup.title)

# Scientific Computing Libraries
import scipy  # Scientific Computing
import matplotlib.pyplot as plt  # Data Visualization

# Using scipy for scientific computing tasks
eigenvalues = scipy.linalg.eigvals(np.random.rand(3, 3))
print("Eigenvalues:", eigenvalues)

# Using matplotlib to create plots
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Wave')
plt.show()

# Machine Learning and AI Libraries
import sklearn  # Machine Learning
import tensorflow as tf  # Deep Learning

# Using scikit-learn for machine learning tasks
from sklearn.datasets import load_iris
data = load_iris()
print("Iris Dataset Target Names:", data.target_names)

# Using TensorFlow for deep learning
print("TensorFlow Version:", tf.__version__)

# GUI Libraries
import tkinter as tk  # GUI Development

# Creating a simple tkinter window
root = tk.Tk()
label = tk.Label(root, text="Hello, GUI!")
label.pack()
root.mainloop()
