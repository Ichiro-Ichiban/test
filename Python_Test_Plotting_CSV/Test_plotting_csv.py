# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:20:09 2015

@author: 一郎
"""

import numpy as np
import matplotlib.pyplot as plt

file_id = 'receipt.csv'
file_path = 'C:/Python27/test2/'

rfile = file_path + file_id
data = np.loadtxt(rfile, comments='#' ,delimiter=',')

x_csv = data[:,0]
y_csv = data[:,1]

plt.figure(figsize=(5,5))
plt.plot(x_csv,y_csv)
plt.show()