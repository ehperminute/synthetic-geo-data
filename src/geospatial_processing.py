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
    print(gdf.columns)
    gdf["colonia_name_clean"] = gdf["nombre"].apply(normalize)

    gdf["colonia_id"] = range(1, len(gdf) + 1)

    return gdf[["colonia_id", "colonia_name_clean", "geometry"]]



def aggregate_risk(panel_df, colonias_df):
    """Compute mean dropout risk per colonia."""
    risk_per_student = panel_df.groupby("student_id")["dropped"].max()

    # attach risk to students
    students_risk = risk_per_student.reset_index()
    students_risk.columns = ["student_id", "ever_dropped"]

    # merge with colonias
    merged = students_risk.merge(colonias_df, on="colonia_id", how="left")

    return merged.groupby("colonia_id")["ever_dropped"].mean().reset_index()
