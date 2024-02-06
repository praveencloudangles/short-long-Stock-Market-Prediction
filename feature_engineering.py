from data_preprocessing import data_preproc
# from sklearn.preprocessing import LabelEncoder
import pandas as pd
from imblearn.over_sampling import SMOTE
# from imblearn.under_sampling import RandomUnderSampler

def fea_eng():
    data = data_preproc()
    x = data.drop('Target', axis=1)
    y = data['Target']
    print("--------------------------------------",data['Target'].value_counts())
    oversample = SMOTE()
    #undersample = RandomUnderSampler()
    X, Y = oversample.fit_resample(x, y)
    data = pd.concat([X, pd.Series(Y, name='Target')], axis=1)

    print("after sampling nulls------------",data.dropna(inplace=True))
    print("after nulls -------", data.isnull().sum())
    print("balance dataa----",data['Target'].value_counts())
    data.to_csv("short-long stock predictions.csv", index=False)

    return data

fea_eng()