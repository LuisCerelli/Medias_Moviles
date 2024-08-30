# Análisis de Precios Históricos con Yahoo Finance API y Media Móvil Simple (SMA)
Este repositorio contiene un script en Python que utiliza la API de Yahoo Finance para descargar y analizar los precios históricos de una acción, aplicando cálculos de medias móviles simples (SMA) de corto y largo plazo. El código también genera una recomendación basada en los cambios de las medias móviles y genera un gráfico visual con las señales de compra y venta.

### Funcionalidades
Descarga de Datos Históricos: El script descarga los datos históricos de una acción específica (en este caso, Tesla - TSLA) durante un período de 10 años utilizando la librería yfinance.

### Cálculo de Medias Móviles Simples (SMA):
- SMA de 40 días: Media móvil a largo plazo.
- SMA de 10 días: Media móvil a corto plazo.
### Generación de Señales de Compra/Venta:
- Si las medias móviles a largo y corto plazo muestran tendencias positivas, se emite una señal de "Compra".
- Si ambas muestran tendencias negativas, se emite una señal de "Venta".
- En cualquier otro caso, la recomendación predeterminada es "Esperar".

### Exportación a Excel: 
- Los datos analizados se guardan en un archivo Excel para su posterior revisión.
- Gráfica del Comportamiento: Se genera una gráfica que muestra las medias móviles y los precios de cierre, junto con las señales de compra y venta resaltadas en verde y rojo.
