# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 23:16:43 2019

@author: Daniel Erb
"""

# In[Load Libraries]
import pandas as pd



# In[Load Data]
cred_csv = 'https://www.dropbox.com/s/qac84v449rjytv5/credit_default_model_data.csv?dl=1'
cred = pd.read_csv(cred_csv)