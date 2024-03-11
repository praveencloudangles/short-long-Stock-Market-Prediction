import pandas as pd
import boto3


def data_load():
    path = "https://stock-market-usecase.s3.amazonaws.com/train.csv"
    df = pd.read_csv(path)

    print("rows------------", df.head)
    return df
data_load()
