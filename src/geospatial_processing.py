"""
geospatial_processing.py
------------------------

Loads and preprocesses GeoJSON files, normalizes colonia names,
and merges aggregated risk indicators for mapping.

This file assumes small GeoJSON files for CDMX-like regions.
"""

import geopandas as gpd
import pandas as pd
import unicodedata


def normalize(text):
    """Remove accents and uppercase for stable merges."""
    if pd.isna(text):
        return text
    text = text.lower()
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return text.strip()


def load_colonias(geojson_path):
    gdf = gpd.read_file(geojson_path)
    gdf["colonia_name_clean"] = gdf["colonia"].apply(normalize)
    gdf["colonia_id"] = range(1, len(gdf) + 1)
    gdf["alcaldia"] = gdf["alc"]
    return gdf[["colonia_id", "colonia_name_clean", "geometry", "alcaldia"]]


def aggregate_risk(panel_df, students_df, colonias_df):
    """Correct aggregation of dropout risk by colonia."""

    # 1) Compute per-student dropout (0 or 1)
    student_dropout = panel_df.groupby("student_id")["dropped"].max().reset_index()
    student_dropout.columns = ["student_id", "ever_dropped"]

    # 2) Attach dropout to students
    merged = students_df.merge(student_dropout, on="student_id", how="left")

    # 3) Compute average risk per colonia
    risk = merged.groupby("colonia_id")["ever_dropped"].mean().reset_index()

    # 4) Merge with full colonia list (so holes disappear)
    risk_full = colonias_df.merge(risk, on="colonia_id", how="left")

    # colonias with no students → assign 0 (or NaN if you prefer)
    risk_full["ever_dropped"] = risk_full["ever_dropped"].fillna(0)

    return risk_full

