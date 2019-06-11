
import os as os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_path = os.curdir
print(data_path)
train_file_name = "train_backup.csv"
test_file_name = "test_backup.csv"
gender_submission_file_name = "gender_submission_backup.csv"

train = pd.read_csv(data_path + "\\" + train_file_name)
print("train.head")
print(train.head())
print("train.shape")
print(train.shape)


def print_head_and_shape(file: str) -> None:
    """first 5 index(row) & the shape of csv file
    
    Arguments:
        file {str} -- file name with extension like .csv
    
    Returns:
        None
    """

    df = pd.read_csv(data_path + "\\" + file)
    print(file + "__head__")
    print(df.head())
    print(file + "__shape__")
    print(df.shape)


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


