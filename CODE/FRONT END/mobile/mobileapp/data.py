import pandas as pd

def readD():
    global df
    df = pd.read_csv('DATASET/train (1).csv')
    return df
