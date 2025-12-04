# Simulación Analítica Educativa: Trayectorias Estudiantiles, Predicción de Abandono y Mapeo de Riesgo Geoespacial

**Breve**: Proyecto con datos sintéticos que genera trayectorias estudiantiles, simula riesgo de abandono, construye una pequeña base de datos relacional, ajusta un modelo interpretativo y mapea el riesgo por colonia.

Este repositorio demuestra un flujo reproducible que combina generación de datos sintéticos, procesamiento geoespacial, modelado predictivo y visualización. Está diseñado para ejecutarse en **Google Colab** (no requiere instalación local) y es apropiado para mostrar habilidades relevantes a roles de analista de datos, analítica educativa o ciencia de datos aplicada.

---

## 📂 Estructura del proyecto


synthetic-geo-data/
│
├── data/
│ ├── raw/
│ ├── interim/
│ └── processed/
│
├── notebooks/
│ └── education_analytics_simulation.ipynb
│
├── src/
│ ├── generate_population.py
│ ├── simulate_dropout.py
│ ├── geospatial_processing.py
│ ├── visualizations.py
│ └── utils.py
│
├── requirements.txt
├── README.md
├── README_es.md
└── .gitignore

2. Ejecuta las celdas del notebook en orden. El notebook:
   - descarga o referencia archivos GeoJSON pequeños (o usa enlaces),
   - genera datos sintéticos de estudiantes,
   - crea una base de datos SQLite local (en el entorno Colab),
   - ajusta una regresión logística para estimar riesgo de abandono,
   - produce mapas interactivos y figuras estáticas.

No se requiere instalación local cuando se usa Colab.

---

## 🧩 Qué demuestra este proyecto

- **Generación de datos sintéticos** para trayectorias estudiantiles.  
- **Ingeniería de datos & ETL** (ingesta CSV / SQLite).  
- **Modelado predictivo** (regresión logística interpretable con diagnósticos).  
- **Procesamiento geoespacial** (unir resultados sintéticos a geometrías reales).  
- **Visualización** (mapas, diagnósticos del modelo, identificación de estudiantes de alto riesgo).  
- **Flujo reproducible** en notebook para compartir en Colab.

---

## 🛠️ Archivos principales y propósito

- `src/generate_population.py` — crea estudiantes sintéticos y atributos demográficos.  
- `src/simulate_dropout.py` — simula registros por semestre y eventos de abandono.  
- `src/geospatial_processing.py` — carga GeoJSON, normaliza nombres y agrega riesgo por colonia.  
- `src/visualizations.py` — funciones para generar mapas y gráficos.  
- `notebooks/education_analytics_simulation.ipynb` — notebook Colab que integra todo.  
- `requirements.txt` — dependencias mínimas.

---

## 📌 Dependencias mínimas (igual en `requirements.txt`)

- numpy
- pandas
- plotly
- geopandas
- shapely
- statsmodels
- faker

> Nota: `sqlite3` es parte de la librería estándar; no necesita instalación. En Colab, `geopandas` puede requerir pasos de instalación incluidos en el notebook.

---

## 📈 Salidas de ejemplo

- Mapa coroplético con probabilidad promedio de abandono por colonia.  
- Gráficas: observado vs predicho por semestre, curva ROC, CSV con top-10 estudiantes de riesgo.  
- Base SQLite con tablas `students_raw` e `inscripciones`.

---

## ⚙️ Ética y seguridad

- Los datos son **sintéticos** y se generan dentro del proyecto. No se usa ni distribuye información real de estudiantes.  
- El pipeline es para aprendizaje, demostración y prototipado metodológico únicamente.

---

## 🧭 Extensiones sugeridas (buenos temas para entrevistas)

- Sustituir datos sintéticos por datos institucionales anonimizados (bajo medidas de privacidad).  
- Agregar clustering (KMeans) para identificar agrupaciones de riesgo por colonia.  
- Construir un pequeño dashboard (Plotly Dash o streamlit) con mapas y listas.  
- Exponer un endpoint o CSV con alertas por estudiante para intervenciones tempranas.

---

## 📄 Licencia

MIT License — siéntete libre de adaptar el código.
