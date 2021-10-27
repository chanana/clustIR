# functions.py contains functions that don't return html
from brukeropusreader.opus_parser import parse_data, parse_meta
import pandas as pd
import numpy as np


def read_opus_data(opus_bytes):
    meta_data = parse_meta(opus_bytes)
    opus_data = parse_data(opus_bytes, meta_data)
    x = [round(i) for i in opus_data.get_range("AB")[:-1]]
    y = [round(i, 4) for i in opus_data["AB"][0 : len(x)]]

    return x, y


def make_and_cleanup_dataframe(dataframe, columns):
    dataframe = dataframe.transpose()
    dataframe.columns = columns
    dataframe = dataframe.round(decimals=4)
    dataframe.sort_index(inplace=True)
    dataframe = dataframe[dataframe.columns[::-1]]
    return dataframe


def calculate_L2_norm_all_v_all(dataframe):
    # dataframe = pd.DataFrame(data=[[1,3,4],[5,6,8]])
    # assuming number of samples is number of rows
    diagonal_array = np.tri(dataframe.shape[0])

    for i in range(diagonal_array.shape[0]):
        a = dataframe.iloc[i, :].to_numpy()
        for j in range(diagonal_array.shape[1]):
            print(i, dataframe.index[i], j, dataframe.index[j])
            if diagonal_array[i][j] == 1 and i != j:
                b = dataframe.iloc[j, :].to_numpy()
                diagonal_array[i][j] = np.linalg.norm(a - b)
                print(diagonal_array)
    return diagonal_array
