import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# =====================================================================
# 1. CÁLCULO DINÁMICO DE RUTAS BAJO LA NUEVA ARQUITECTURA
# =====================================================================
# Path(__file__).resolve().parents[2] sube desde 'src/models/' hasta la raíz 'hydraulic-network-analytics'
BASE_DIR = Path(__file__).resolve().parents[2]

# Ruta hacia la data procesada
ruta_csv = BASE_DIR / "data" / "processed" / "nodos_perfectos.csv"
print(f"[INFO] Cargando base de datos analítica desde: {ruta_csv}")

df = pd.read_csv(ruta_csv)

# =====================================================================
# 2. FILTRADO DE DOMINIO: RECONSTRUCCIÓN DEL SISTEMA SANO
# =====================================================================
# Corrección del NameError: Se genera el DataFrame 'df_sano' antes de su manipulación
df['estado_operacional'] = np.where(
    (df['presion_psi'] < 22) | (df['presion_psi'] > 58), 
    'Anomalía', 
    'Operacional'
)
df_sano = df[df['estado_operacional'] == 'Operacional'].copy()

# =====================================================================
# 3. INGENIERÍA DE CARACTERÍSTICAS: CREACIÓN DE VARIABLES SINTÉTICAS
# =====================================================================
print("[INFO] Ejecutando Ingeniería de Características Avanzada...")

# Extraemos el número limpio del ID del nodo para simular la secuencia posicional
df_sano['nodo_num'] = df_sano['nodo_id'].str.extract(r'(\d+)').astype(int)

# Variable Sintética 1: Distancia estimada al origen (Simulación de fricción)
df_sano['distancia_origen_m'] = df_sano['nodo_num'] * 25 

# Variable Sintética 2: Interacción Física (Elevación combinada con la distancia)
df_sano['energia_potencial_relativa'] = df_sano['elevacion_m'] * df_sano['distancia_origen_m']

# Definición de matriz multivariable (Expansión de dimensiones)
X = df_sano[['elevacion_m', 'distancia_origen_m', 'energia_potencial_relativa']]
y = df_sano['presion_psi']

print(f"[OK] Matriz de características expandida a dimensiones: {X.shape}")

# =====================================================================
# 4. MODELADO ESTADÍSTICO Y AUDITORÍA
# =====================================================================
# Segmentación
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Despliegue de Regresión Lineal Múltiple
print("[INFO] Entrenando motor de Regresión Lineal Múltiple...")
modelo_multivariable = LinearRegression()
modelo_multivariable.fit(X_train, y_train)

# Predicción y extracción de métricas
y_pred = modelo_multivariable.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n" + "="*50)
print("     MÉTRICAS DEL MODELO MULTIVARIABLE (INGENIERÍA DE FEATURES)")
print("="*50)
print(f" Error Cuadrático Medio (MSE) : {mse:.4f}")
print(f" Raíz del Error (RMSE)        : {rmse:.4f} PSI")
print(f" Coeficiente de Det. (R2)      : {r2:.4f}")
print("="*50)

# =====================================================================
# 5. GENERACIÓN DE EVIDENCIA VISUAL DE PRODUCCIÓN
# =====================================================================
print("[INFO] Generando gráfico de diagnóstico para el portafolio...")

plt.figure(figsize=(10, 6))
# Graficamos la data real del set de prueba
plt.scatter(X_test['elevacion_m'], y_test, color='blue', label='Data Real (Sana)', alpha=0.7)
# Graficamos la línea de predicción del modelo
plt.scatter(X_test['elevacion_m'], y_pred, color='red', label='Predicción del Modelo', marker='x')

plt.title('Auditoría del Modelo Predictivo: Presión vs Elevación (Sistema Sano)')
plt.xlabel('Elevación del Terreno (m)')
plt.ylabel('Presión de Operación (PSI)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# Corrección de ruta de salida: Almacenamiento en 'reports/figures/'
ruta_grafico = BASE_DIR / "reports" / "figures" / "diagnostico_modelo.png"
plt.savefig(ruta_grafico, dpi=300, bbox_inches='tight')
plt.close() # Libera memoria de la interfaz gráfica
print(f"[OK] Gráfico de auditoría exportado con éxito en: {ruta_grafico}")