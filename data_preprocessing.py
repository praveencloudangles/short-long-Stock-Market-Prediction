from data_extraction import data_load

def data_preproc():
    data = data_load()

    value_count = data['result'].value_counts()
    for value, count in value_count.items():
        print(f"{value}, {count}")

    data['exchange'] = data['exchange'].replace(['Bybit', 'Binance', 'OKX', 'Huobi'], ['0', '1', '2', '3'])
    data['RSI_signal'] = data['RSI_signal'].replace(['Hold', 'Sell', 'Buy'], ['0', '1', '2'])
    data['Stoch_O_signal'] = data['RSI_signal'].replace(['Hold', 'Sell', 'Buy'], ['0', '1', '2'])
    data['fibonacci_signal'] = data['fibonacci_signal'].replace(['Hold', 'Sell', 'Buy'], ['0', '1', '2'])
    data['Bollinger_signal'] = data['Bollinger_signal'].replace(['Hold', 'Sell', 'Buy'], ['0', '1', '2'])
    data['ichimoku_c_signal'] = data['ichimoku_c_signal'].replace(['Hold', 'Sell', 'Buy'], ['0', '1', '2'])

    data = data.rename(columns={"result": "Target"})

    columns_to_drop = ["RSI", "EMA_relative","SMA_relative", "MACD_relative_signal", "Stoch_O_signal", "MACD_relative_histogram", "MACD_relative", "pivot_point", "pivot_resistance_3", "Bollinger_lower_band", "MA_relative", "WMA_relative", "Stoch_O_k_smoothed", "Stoch_O_signal_value", "ichimoku_c_leading_span_a", "ichimoku_c_leading_span_b", "pivot_resistance_1", "pivot_support_2", "pivot_resistance_2", "pivot_support_3", "Bollinger_lower_band"]

    data.drop(columns=columns_to_drop, inplace=True, axis=1)

    convert_dict = {'exchange': int,'fibonacci_signal': int, 'Bollinger_signal': int, 'ichimoku_c_signal': int, 'RSI_signal': int}
    data = data.astype(convert_dict)

    return data

data_preproc()