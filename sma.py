import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os  # <- Este módulo permite interactuar con el sistema de archivos

#Definimos el simbolo de la accion: 
ticker_symbol = "TSLA"

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

#creo una nueva columna con los 40 dias, al que llamaremos PERIODO LARGO:
days = long_sma
sma_long_colname = 'SMA_' + str(days)
data[sma_long_colname] = data['Close'].rolling(window=days).mean()

#Y otra con el delta que sera la diferencia entre los dos ultimos valores del promedio de 40 dias(dado en el parrafo anterior): 
delta_sma_long_colname = "d_" + sma_long_colname
data[delta_sma_long_colname] = ((data[sma_long_colname] - data[sma_long_colname].shift(1)) / data[sma_long_colname]) * 100

#creo una nueva columna con los 10 dias, al que llamaremos PERIODO CORTO:
dias = short_sma # aqui configuro los dias
sma_short_colname = 'SMA_' + str(dias) # aqui creo el nombre de la futura columna
delta_sma_short_colname = 'd_' + sma_short_colname # aqui creo el nombre de la otra futura columna

data[sma_short_colname] = data['Close'].rolling(window=dias).mean()
data[delta_sma_short_colname] = ((data[sma_short_colname] - data[sma_short_colname].shift(1)) / data[sma_short_colname]) * 100

#Ahora limpiamos las NAN, sencillamente: 
data = data.dropna()

#Esto que sigue lo hemos realizado luego de hacer la gráfica, o sea, hemos vuelto 'hacia atrás', digamos, con la idea de hacer una columna que pueda recomendar el valor de predicción...

data['Recomendacion'] = 'Esperar' #Valor predeterminado de "Esperar"
#Esta es la regla para la predicción:
data.loc[(data[delta_sma_long_colname] > 0) & (data[delta_sma_short_colname] > 0), 'Recomendacion'] = 'Compra'  
data.loc[(data[delta_sma_long_colname] < 0) & (data[delta_sma_short_colname] < 0), 'Recomendacion'] = 'Venta'  



#Creamos la carpeta DATA, para guardar todo en un excel: 
output_dir = 'DATA'
if not os.path.exists(output_dir):
    os.makedirs(output_dir) #De esta forma creamos la carpeta 'DATA' si no existe...

#Guardamos en un excel: 
excel_filename = os.path.join(output_dir,f'{ticker_symbol}_historico_precios3.xlsx')
data.to_excel(excel_filename)

print(f'Excel guardado exitosamente en {excel_filename}')

#para graficar vamos a sacar dias, y le pedimos que deje el ultimo año:
data = data.tail(360)

#Grafica: 
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(data.index, data[sma_short_colname], label=sma_short_colname, linestyle='--', linewidth=1, color="blue")
ax.plot(data.index, data[sma_long_colname],label=sma_long_colname, linestyle='-.', linewidth=2, color="navy")
ax.plot(data.index, data['Close'], label='Close', linestyle='-', linewidth=2, color='gray')


for index, row in data.iterrows():
    color = 'gray'
    if row['Recomendacion'] == 'Compra':
        color = 'green'
    if row['Recomendacion'] == 'Venta':
        color = 'red'
    #print('index',index,'color',color)
    if color != 'gray':
        ax.plot(index, row['Close'], marker='o', markersize=4, color=color)




ax.set_title(f'Grafico de SMA_{short_sma}, SMA_{long_sma} y Close para {ticker_symbol}')
ax.set_xlabel('Fecha')
ax.set_ylabel('Precio')
ax.legend()

#Para mostrar el grafico: 
plt.grid(True)
plt.xticks(rotation=45) #Rotamos las fechas en el eje x para que sean mas legibles
plt.tight_layout()

plt.show()


