# synthetic-geo-data
# Education Analytics Simulation: Student Trajectories, Dropout Prediction & Geospatial Risk Mapping

## 👇 Spanish version

See [README_es.md](README_es.md) for a Spanish translation.

**Short**: Synthetic data project that generates student trajectories, simulates dropout risk and maps risk by neighborhood.

This repository demonstrates a reproducible data workflow combining synthetic data generation, geospatial processing, predictive modeling, and visualization. It is designed to be run in **Google Colab** (no local installation required).

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
![](2025-12-1421-37-58.png)
![](2025-12-1421-35-29.png)

---

## 🚀 Quick start (Google Colab)

1. Open the notebook in Colab [CDMX synthetic dropout.ipynb](https://colab.research.google.com/drive/1sneX2ZAtxctFCfk7WDqiMGeSuMmE_BJU?usp=sharing)


2. Run the notebook cells in order (`Runtime -> Run all` or `Ctrl + F9`). The notebook will:
   - reference official GeoData,
   - generate synthetic student data,
   - create a local SQLite database (in Colab environment),
   - run a logistic regression to estimate dropout risk,
   - produce interactive maps and static figures.

No local install required when using Colab.

---

## What this project demonstrates

- **Synthetic data generation** for longitudinal student trajectories.  
- **Data engineering & ETL** (CSV / SQLite ingestion pipeline).  
- **Predictive modeling** (interpretable logistic regression with diagnostics).  
- **Geospatial processing** (join synthetic outcomes to real neighborhood geometries).  
- **Visualization** (maps, model diagnostics, top-risk identification).  
- **Reproducible notebook workflow** suitable for sharing in Colab.

Assumptions & limitations

Dropout probabilities are synthetic and illustrative

No causal interpretation is intended

Geographic weighting uses area as a proxy for population density

## Core files & purpose

- `src/generate_population.py` — create synthetic students and demographic attributes.  
- `src/simulate_dropout.py` — simulate semester-level records and dropout events.  
- `src/geospatial_processing.py` — load GeoJSON, normalize names, compute aggregated risk by neighborhood.  
- `src/visualizations.py` — functions to render maps and plots (Plotly/Matplotlib).  
- `CDMX synthetic dropout.ipynb` — one-click Colab notebook that ties everything together.  
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

---

## 🧾 Example outputs

- Choropleth map showing average dropout probability per neighborhood.  
- Plots: observed vs predicted dropout by semester, ROC curve, top-10 high-risk students CSV.  
- A small SQLite database with `students_raw` and `inscripciones` tables.


---

## ⚙️ Security & ethics

- Data is **synthetic** and generated within the project. No real student data is used or distributed.  
- The pipeline is intended for learning, demonstration, and methodological prototyping only.

---

## 🧭 Possible extensions

- Replace synthetic data with anonymized institutional data (if available) while maintaining privacy safeguards.  
- Add clustering (KMeans) to identify high-risk neighborhoods by features.  
- Build a simple dashboard (Plotly Dash or streamlit) to display risk maps and student lists.  
- Export a CSV or API endpoint with per-student alerts for early intervention workflows.

---

## 📄 License

MIT License — feel free to reuse or adapt the code.

