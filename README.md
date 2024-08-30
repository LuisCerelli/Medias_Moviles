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
  
### Estructura del Proyecto
- script.py: Código principal donde se realiza el análisis de precios y las recomendaciones.
- DATA/: Carpeta donde se guardará el archivo Excel con los datos históricos.
### Visualización del Gráfico
- El gráfico generado muestra las siguientes líneas:

  - SMA_10: Línea azul discontinua que representa la media móvil de corto plazo (10 días).
  - SMA_40: Línea azul oscuro que representa la media móvil de largo plazo (40 días).
  - Precio de Cierre: Línea gris que muestra los precios de cierre.
- Señales de Compra y Venta: Marcadores verdes para compra y rojos para venta basados en el comportamiento de las medias móviles.
### Contribuciones
Las contribuciones y sugerencias son bienvenidas. Si encuentras algún error o quieres mejorar el proyecto, no dudes en crear un pull request o abrir un issue.

### Licencia
Este proyecto está bajo la licencia MIT.
