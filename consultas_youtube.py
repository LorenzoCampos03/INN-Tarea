import pandas as pd

# Configuración de pandas para mejor visualización
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1200)
pd.set_option("display.colheader_justify", "center")

# Cargar dataset
df = pd.read_csv("youtube-top-100-songs-2025.csv")

print("="*100)
print("📊  INFORMACIÓN DEL DATASET")
print("="*100)
print(f"Filas: {df.shape[0]} | Columnas: {df.shape[1]}")
print("\nColumnas disponibles:")
print(df.columns.tolist())

print("\nPrimeras 5 filas:")
print(df.head(5)[["title", "channel", "view_count", "channel_follower_count"]].to_string(index=False))

# ---------- CONSULTAS ----------

print("\n" + "="*100)
print("🎵 TOP 10 CANCIONES CON MÁS VISTAS")
print("="*100)
top_views = df.nlargest(10, "view_count")[["title", "channel", "view_count"]]
print(top_views.to_string(index=False))

print("\n" + "="*100)
print("📺 CANALES CON MÁS SEGUIDORES")
print("="*100)
top_channels = df.nlargest(10, "channel_follower_count")[["channel", "channel_follower_count"]].drop_duplicates()
print(top_channels.to_string(index=False))

print("\n" + "="*100)
print("👨‍🎤 ARTISTAS (CANALES) CON MÁS VIDEOS EN EL TOP 100")
print("="*100)
channel_count = df["channel"].value_counts().head(10)
print(channel_count.to_string())

print("\n" + "="*100)
print("⏱️ PROMEDIO DE DURACIÓN DE VIDEOS")
print("="*100)
if "duration" in df.columns:
    print(f"Promedio de duración (segundos): {df['duration'].mean():.2f}")

print("\n" + "="*100)
print("🏆 CATEGORÍAS MÁS POPULARES")
print("="*100)

if "categories" in df.columns:
    # Separamos las categorías en caso de que haya varias en una celda (separadas por ; , o |)
    categorias = df["categories"].fillna("").astype(str).str.split(r"[;,\|]", regex=True).explode().str.strip()
    categorias = categorias[categorias != ""]  # eliminar vacíos

    if not categorias.empty:
        top_categorias = categorias.value_counts().head(10)
        print(top_categorias.to_string())
    else:
        print("No se encontraron categorías válidas en el dataset.")
else:
    print("La columna 'categories' no existe en este dataset.")
