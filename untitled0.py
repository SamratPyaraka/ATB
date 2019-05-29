# -*- coding: utf-8 -*-
"""
Created on Mon May 20 14:05:18 2019

@author: samrat.pyaraka
"""

import pandas as pd
import os

df = pd.read_csv(os.path.join(r"D:\AutomatedTradingBot\Reinforcement_Learning_for_Stock_Prediction-master\data\\", "reliance.csv"), error_bad_lines=False, skipinitialspace=True)


df = df[~df['open'].isnull()] 

df.to_csv("new_reliance.csv", index=False)