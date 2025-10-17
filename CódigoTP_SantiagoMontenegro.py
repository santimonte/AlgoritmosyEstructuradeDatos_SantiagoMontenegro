import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("TEST Analisis Datos.xlsx - Participant Data.csv")

# Mostrar las primeras 5 filas para verificar la carga y el formato
print("Primeras 5 filas del DataFrame:")
print(df.head())
print("-" * 50)

# Mostrar información general sobre las columnas (tipos de datos y valores no nulos)
print("Información general del DataFrame:")
print(df.info())
print("-" * 50)

# Mostrar estadísticas descriptivas para las columnas numéricas
print("Estadísticas descriptivas de las columnas numéricas:")
print(df.describe())

# 1. Renombrar columnas
df.rename(columns={
    'Total Questions Attempted': 'Total_Preguntas',
    'Accuracy': 'Precision',
    'Score': 'Puntuacion',
    'Total Time Taken': 'Tiempo_Total'
}, inplace=True)

# 2. Limpiar y convertir 'Precision' a float
# Eliminar el símbolo '%' y convertir a número.
df['Precision'] = df['Precision'].str.replace('%', '').astype(float) / 100

# 3. Convertir 'Tiempo_Total' a segundos
# Se asume el formato 'HH:MM:SS' o similar.
def tiempo_a_segundos(tiempo):
    if pd.isna(tiempo):
        return 0
    try:
        parts = str(tiempo).split(':')
        if len(parts) == 3:
            h, m, s = map(int, parts)
            return h * 3600 + m * 60 + s
        elif len(parts) == 2:
             m, s = map(int, parts)
             return m * 60 + s
        else:
             return 0
    except ValueError:
        return 0 # Manejar valores que no se ajustan al formato

df['Tiempo_Segundos'] = df['Tiempo_Total'].apply(tiempo_a_segundos)

print("\nPrimeras filas después de la limpieza y transformación:")
print(df[['First Name', 'Precision', 'Puntuacion', 'Tiempo_Total', 'Tiempo_Segundos']].head())

promedio_precision = df['Precision'].mean()
promedio_puntuacion = df['Puntuacion'].mean()
promedio_tiempo_seg = df['Tiempo_Segundos'].mean()

print("\n--- Métricas de Rendimiento General ---")
print(f"Precisión media del grupo: {promedio_precision:.2%}")
print(f"Puntuación media del grupo: {promedio_puntuacion:.2f}")
# Convertir el tiempo promedio de segundos a formato minutos:segundos
minutos = int(promedio_tiempo_seg // 60)
segundos = int(promedio_tiempo_seg % 60)
print(f"Tiempo total promedio (Min:Seg): {minutos:02d}:{segundos:02d}")

top_5_puntuacion = df.sort_values(by='Puntuacion', ascending=False).head(5)

print("\n--- Top 5 Participantes por Puntuación ---")
print(top_5_puntuacion[['Rank', 'First Name', 'Puntuacion', 'Precision', 'Tiempo_Total']])

correlacion = df['Puntuacion'].corr(df['Tiempo_Segundos'])

print("\n--- Correlación entre Puntuación y Tiempo ---")
if correlacion > 0.1:
    interpretacion = "positiva (los que puntúan más alto tienden a tomar más tiempo)."
elif correlacion < -0.1:
    interpretacion = "negativa (los que puntúan más alto tienden a tomar menos tiempo - eficiencia)."
else:
    interpretacion = "débil (no hay una relación lineal fuerte)."

print(f"Coeficiente de correlación Puntuación vs. Tiempo: {correlacion:.2f}")
print(f"Interpretación: La correlación es **{interpretacion}**")


# ------------ TP 17 DE OCTUBRE ---------------

# -------- 1. Calcular el promedio de precision de todos los participantes --------------
promedio_precision = df['Precision'].mean()
print(f"Promedio general de precisión: {promedio_precision:.2%}")


# ------- 2. Calcular el puntaje total de todos los alumnos ---------------
# 2️⃣ Puntaje total de todos los alumnos
puntaje_total = df['Puntuacion'].sum()
print(f"Puntaje total de todos los alumnos: {puntaje_total}")

# ------- 3. En base al puntaje, clasificar a los alumnos que tengan menos de 15000 puntos como "inferior" y si es mayor como "superior" --------------
df['Clasificación'] = df['Puntuacion'].apply(lambda x: 'Inferior' if x < 15000 else 'Superior')


print("\nPrimeras filas con la clasificación:")
print(df[['First Name', 'Puntuacion', 'Clasificación']].head())

conteo = df['Clasificación'].value_counts()
print("\nCantidad de alumnos por categoría:")
print(conteo)