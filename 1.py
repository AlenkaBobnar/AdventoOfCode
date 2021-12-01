# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:07:10 2021

@author: alenk
"""

import pandas as pd

data = pd.read_csv('input.txt', header = None)
data.columns = ['data']
data['difference'] = data.data.diff()
solution =len( data.loc[data.difference > 0])

data['slidingDiff'] = data.data.rolling(window=3).sum().diff()
solution2 =len( data.loc[data.slidingDiff > 0])
