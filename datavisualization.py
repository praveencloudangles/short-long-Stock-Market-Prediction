from data_preprocessing import data_preproc
import pandas as pd
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.io as pio
import plotly.graph_objects as go
import io
from PIL import Image

def data_vis():
    data = data_preproc()
    column = list(data.columns)
    print("----------------", column)
    
    categ = []
    numer = []
    
    for col in data.columns:
        if data[col].dtype == 'object':  # Check if the data type is object (string)
            categ.append(col)
        else:
            numer.append(col)
            
    print("categ-------", categ)
    print("numer--------", numer)

            
    column_to_remove = ["Bollinger_signal", "Bollinger_upper_band", "pivot_support_1", "SAR_relative", "Target", "ATR", "MACD", "RSI_signal"]
    for col_to_remove in column_to_remove:
        column.remove(col_to_remove)
    print(column)
#     
    columns_to_remove_outliers = ["exchange", "fibonacci_signal", "ichimoku_c_base_line", "ichimoku_c_conversion_line", "ichimoku_c_signal", "s&p500_move_15m", "Stoch_O_d_value", "VWAP_relative_long", "VWAP_relative_short"]

    for col in columns_to_remove_outliers:
        q1 = data[col].quantile(0.25)
        q3 = data[col].quantile(0.75)
        iqr = q3 - q1
        upper_limit = q3 + (1.5 * iqr)
        lower_limit = q1 - (1.5 * iqr)

        # Apply the filtering conditions to the original DataFrame
        data = data.loc[(data[col] < upper_limit) & (data[col] > lower_limit)]

    
    for i in column:
        fig = px.histogram(data, y=i)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=False, zeroline=False)
        fig.write_image(f"{i}_hist.jpg")
    
    for i in column:
        fig = px.box(data, y=i)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        fig.write_image(f"{i}_box.jpg")

    columns_to_remove = ["Target", ]
    df=data.drop(columns=columns_to_remove,axis=1)
    y=df.corr().columns.tolist()
    z=df.corr().values.tolist()
    z_text = np.around(z, decimals=4) # Only show rounded value (full value on hover)
    fig = ff.create_annotated_heatmap(z,x=y,y=y,annotation_text=z_text,colorscale=px.colors.sequential.Cividis_r,showscale=True)
    fig.update_layout(template='plotly_dark', width=1500, height=1000)
    # fig.show()
    fig.write_image("heat_map.jpg")

    return data
data_vis()