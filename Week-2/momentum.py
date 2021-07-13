import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

N = 50
T = 7
R = 0.8
M = 5
F = 0.005

def GetData(NameOfFile):
  data = pd.read_csv(NameOfFile, usecols = ['datadate','tic','adjcp'])
  return pd.DataFrame(data)

print(GetData("DATA.csv")) 