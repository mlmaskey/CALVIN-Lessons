# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 22:43:02 2020

@author: Water Management Lab
"""

import pandas as pd
dataMerge = pd.DataFrame()
for i in range(1922,2004):
  print('\nNow running WY %d' % i)
  fileName = 'calvin/data/dataRecharge2/linksWY%d-final.csv' % i
  F = pd.read_csv(fileName, index_col=0, parse_dates=True)
  dataMerge = pd.concat([dataMerge, F], axis = 0)
  
dataMerge.to_csv('Single/calvin/data/dataRecharge2.csv', index=True)