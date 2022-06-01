#!C:/python/python

from matplotlib import pyplot as plt
import numpy as np
 
 
# Creating dataset
print("Report")
cars = ['Origional content', 'Unique content']
 
data = [23, 77]
 
# Creating plot
fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = cars)
 
# show plot
plt.show()