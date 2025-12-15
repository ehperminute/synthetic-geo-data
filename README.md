# synthetic-geo-data
# Education Analytics Simulation: Student Trajectories, Dropout Prediction & Geospatial Risk Mapping

**Short**: Synthetic data project that generates student trajectories, simulates dropout risk, builds a small relational database, fits an interpretable predictive model, and maps risk by neighborhood.

This repository demonstrates a reproducible data workflow combining synthetic data generation, geospatial processing, predictive modeling, and visualization. It is designed to be run in **Google Colab** (no local installation required) and is suitable for showcasing skills relevant to data analyst, education analytics, and applied data science roles.

---

## 📂 Project structure
```
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
│ └── visualizations.py
│
├── requirements.txt
├── README.md
├── README_es.md
└── .gitignore
```
---

## 🚀 Quick start (Google Colab)

1. Open the notebook in Colab (replace `YOUR_COLAB_LINK` with the notebook link after upload):


2. Run the notebook cells in order. The notebook will:
   - download or reference small GeoJSON files (or use links),
   - generate synthetic student data,
   - create a local SQLite database (in Colab environment),
   - run a logistic regression to estimate dropout risk,
   - produce interactive maps and static figures.

No local install required when using Colab.

---

## 🧩 What this project demonstrates

- **Synthetic data generation** for longitudinal student trajectories.  
- **Data engineering & ETL** (CSV / SQLite ingestion pipeline).  
- **Predictive modeling** (interpretable logistic regression with diagnostics).  
- **Geospatial processing** (join synthetic outcomes to real neighborhood geometries).  
- **Visualization** (maps, model diagnostics, top-risk identification).  
- **Reproducible notebook workflow** suitable for sharing in Colab.

---

## 🛠️ Core files & purpose

- `src/generate_population.py` — create synthetic students and demographic attributes.  
- `src/simulate_dropout.py` — simulate semester-level records and dropout events.  
- `src/geospatial_processing.py` — load GeoJSON, normalize names, compute aggregated risk by neighborhood.  
- `src/visualizations.py` — functions to render maps and plots (Plotly/Matplotlib).  
- `notebooks/education_analytics_simulation.ipynb` — one-click Colab notebook that ties everything together.  
- `requirements.txt` — minimal dependencies to run the project.

---

## 📌 Minimal dependencies (also in `requirements.txt`)

- numpy
- pandas
- plotly
- geopandas
- shapely
- statsmodels
- faker

> Note: `sqlite3` is a Python standard library module; no extra install required. In Colab, `geopandas` may require install steps included in the notebook.

---

## 🧾 Example outputs

- Choropleth map showing average dropout probability per neighborhood.  
- Plots: observed vs predicted dropout by semester, ROC curve, top-10 high-risk students CSV.  
- A small SQLite database with `students_raw` and `inscripciones` tables.

(Images and example outputs can be added to `/notebooks/output/` or `/README_images/`.)

---

## ⚙️ Security & ethics

- Data is **synthetic** and generated within the project. No real student data is used or distributed.  
- The pipeline is intended for learning, demonstration, and methodological prototyping only.

---

## 🧭 Possible extensions (good interview talking points)

- Replace synthetic data with anonymized institutional data (if available) while maintaining privacy safeguards.  
- Add clustering (KMeans) to identify high-risk neighborhoods by features.  
- Build a simple dashboard (Plotly Dash or streamlit) to display risk maps and student lists.  
- Export a CSV or API endpoint with per-student alerts for early intervention workflows.

---

## 📄 License

MIT License — feel free to reuse or adapt the code.

---

## 👇 Spanish version

See README_es.md for a Spanish translation.
