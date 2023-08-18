import pandas as pd
from lightweight_charts import Chart
from finta import TA
import zipfile
import os

zipfile_name = 'BTCUSDT-5m-2023-08-11.zip'
file_name = 'BTCUSDT-5m-2023-08-11.csv'
data_path = os.path.join('btc_fvg', zipfile_name)
# btc_fvg\BTCUSDT-5m-2023-08-11.zip

def read_csv(data_path, file_name):
    """
    Function to read csv inside zip.
    Input path strings
    Output: Pandas Dataframe
    """ 
    with zipfile.ZipFile(data_path, 'r') as zip_ref:
        with zip_ref.open(file_name) as csv_file:
            # Lee el archivo CSV utilizando Pandas
            dataframe = pd.read_csv(csv_file)
            return dataframe

# Function to clean data to what i need

def prep_data(dataframe):
    # Eliminating irrelevant columns
    dataframe = dataframe[['open_time', 'open', 'high', 'low','close', 'volume']]
    dataframe['open_time'] = pd.to_datetime(dataframe['open_time'],unit='ms')
    return dataframe

data = read_csv(data_path, file_name)
aa = prep_data(data)

# Charting
bb = aa.copy()
bb = bb.rename(columns={"open_time": "time"})



if __name__ == '__main__':

    chart = Chart()
        
    # Columns: | time | open | high | low | close | volume (if volume is enabled) |
    #df = pd.read_csv('ohlcv.csv')
    chart.set(bb)
    chart.show(block=True)

    img = chart.screenshot()
    with open('screenshot.png', 'wb') as f:
        f.write(img)


if __name__ == '__main__':
    chart = Chart()
    df = pd.read_csv('ohlcv.csv')
    chart.set(df)
    chart.show()
    
    img = chart.screenshot()
    with open('screenshot.png', 'wb') as f:
        f.write(img)

# Funciona!
# Para la version que funciona en jupyter, https://github.com/TechfaneTechnologies/pytvlwcharts/tree/main 
