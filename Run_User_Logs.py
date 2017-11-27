#James Chartouni
from multiprocessing import Pool, cpu_count
import gc; gc.enable()
import pandas as pd
import numpy as np


print("start")
user_logs = pd.read_csv('cleaned_input/user_logs_merged.csv')
print("stop")

train = pd.read_csv('cleaned_input/train_merged.csv')
test = pd.read_csv("cleaned_input/test_merged.csv")
data = pd.concat(( train, test ))

msno_values = data.msno.unique()

user_logs_cleaned = user_logs[user_logs['msno'].isin(msno_values)]
user_logs = []

user_logs_cleaned.to_csv('cleaned_input/user_logs_cleaned.csv')