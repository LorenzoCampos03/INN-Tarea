# 🎵 YouTube Top 100 Songs 2025  

## 📌 Descripción del dataset  
El dataset **YouTube Top 100 Songs 2025** contiene información de los **100 videos musicales más populares en YouTube** durante el año 2025.  

Este dataset fue recopilado de **Kaggle** y proporciona métricas relevantes de cada video, como:  
- Número de visualizaciones  
- Duración del video  
- Canal y seguidores del canal  
- Categorías y etiquetas  

Es ideal para realizar **análisis de tendencias musicales, popularidad de artistas y métricas digitales**.  

---

## 📊 Contenido del dataset  

Cada fila representa un **video musical** y las columnas contienen la siguiente información:  

| Columna                  | Descripción                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `title`                  | Título del video.                                                           |
| `fulltitle`              | Título completo (incluye *Official Video*, *Lyrics*, etc.).                 |
| `description`            | Descripción proporcionada por el canal.                                     |
| `view_count`             | Número total de visualizaciones.                                            |
| `categories`             | Categorías asociadas al video.                                              |
| `tags`                   | Etiquetas asignadas al video.                                               |
| `duration`               | Duración en segundos.                                                       |
| `duration_string`        | Duración en formato `hh:mm:ss`.                                             |
| `live_status`            | Estado del video (si es transmisión en vivo o no).                          |
| `thumbnail`              | URL de la miniatura del video.                                              |
| `channel`                | Nombre del canal que publicó el video.                                      |
| `channel_url`            | URL del canal de YouTube.                                                   |
| `channel_follower_count` | Número de seguidores del canal.                                              |

---

## 🎯 Objetivos del análisis  

✔️ Identificar las **canciones con más vistas** en el Top 100.  
✔️ Conocer los **canales con más seguidores**.  
✔️ Analizar qué **artistas aparecen más veces** en el ranking.  
✔️ Calcular la **duración promedio de los videos**.  
✔️ Explorar las **categorías y etiquetas más comunes**.  

---

## ⚙️ Uso del script en Python  

Se incluye un archivo `consultas_youtube.py` que permite:  

- Mostrar información general del dataset.  
- Listar el **Top 10 de canciones con más vistas**.  
- Identificar los **canales con más seguidores**.  
- Contar qué canales tienen más videos en el ranking.  
- Calcular la duración promedio de los videos.  




link del dataset: https://www.kaggle.com/datasets/vedikagupta0/youtube-top-100-songs-2025-dataset


(venv) PS C:\Users\campo\OneDrive\Desktop\tarea> history

  Id CommandLine
  -- -----------
   1 try { . "c:\Users\campo\AppData\Local\Programs\Microsoft VS Code\resources\app\out\vs\workbench\contrib\terminal\common\scripts\... 
   2 python -m venv venv
   3 .\venv\Scripts\activate
   4 python -m pip install --upgrade pip
   5 pip install pandas matplotlib openpyxl
   6 python consultas_youtube.py
   7 python consultas_youtube.py
   8 python consultas_youtube.py
   9 clear
  10 python consultas_youtube.py
  11 clear
  12 python consultas_youtube.py
  13 clear
  14 python consultas_youtube.py