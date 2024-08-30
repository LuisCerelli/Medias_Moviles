import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

#Definimos el simbolo de la accion: 
ticker_symbol = "AAPL"

#Calculamos las fechas de hace dos anos y la fecha actual: 
end_date = datetime.today().strftime('%Y-%m-%d')
star_date = (datetime.today() - timedelta(days=3650)).strftime('%Y-%m-%d')
#print(end_date, star_date)

#y esta sera la variable mas importante, donde la API de yahooFinance cargara todos los datos
data = yf.download(ticker_symbol, start=star_date, end=end_date)
#print(data)

#estas variables las usaré para el tiempo...
long_sma = 40
short_sma = 10

#creo una nueva columna con los 40 dias: 
days = long_sma
sma_long_colname = 'SMA_' + str(days)
data[sma_long_colname] = data['Close'].rolling(window=days).mean()

#Y otra con el delta que sera la diferencia entre los dos ultimos valores del promedio de 40 dias(dado en el parrafo anterior): 
delta_sma_long_colname = "d_" + sma_long_colname
data[delta_sma_long_colname] = ((data[sma_long_colname] - data[sma_long_colname].shift(1)) / data[sma_long_colname]) * 100

print(data)