
import os as os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_path = "c:\\Users\\kaoru\\Documents\\Python Scripts"

train = pd.read_csv(data_path + "\\train.csv")
print("train.head")
print(train.head())
print("train.shape")
print(train.shape)
test = pd.read_csv(data_path + "\\test.csv")
print("test.head")
print(test.head())
print("test.shape")
print(test.shape)


def kesson_table(df: pd.DataFrame) -> pd.DataFrame:
    """generate table that contains lack count and percentage
    
    Arguments:
        df {pd.DataFrame} -- source data
    
    Returns:
        pd.DataFrame -- columns={0: "欠損数", 1: "%"}
    """
    null_val = df.isnull().sum()
    percent = 100 * df.isnull().sum() / len(df)
    kesson_table = pd.concat([null_val, percent], axis=1)
    kesson_table_ren_columns = kesson_table.rename(columns={0: "欠損数", 1: "%"})
    return kesson_table_ren_columns


print(kesson_table(train))
print(kesson_table(test))
