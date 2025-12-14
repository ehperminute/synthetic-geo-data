"""
geospatial_processing.py
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
    gdf = gdf[["ID", "NOMUT", "NOMDT", "geometry"]]
    colnames = ["colonia_id", "colonia_name", "alcaldia_name", "geometry"]
    gdf.columns = colnames
    gdf = calculate_area_density(gdf)
    return gdf

def calculate_area_density(gdf):
    gdf_proj = gdf.to_crs(epsg=32614)  # UTM zone for CDMX

    # 🔹 area-based population proxy
    gdf_proj["area_km2"] = gdf_proj.geometry.area / 1e6
    gdf_proj["pop_weight"] = (1 / gdf_proj["area_km2"]) ** 0.5
    gdf_proj["pop_weight"] /= gdf_proj["pop_weight"].sum()

    #🔹 back to lat/lon for plotting
    return gdf_proj.to_crs(epsg=4326)


def aggregate_risk(panel_df, students_df, colonias_df):
    """Aggregation of dropout risk by colonia."""

    # 1) Compute per-student dropout (0 or 1)
    student_dropout = panel_df.groupby("student_id")["dropped"].max().reset_index()
    student_dropout.columns = ["student_id", "ever_dropped"]

    # 2) Attach dropout to students
    merged = students_df.merge(student_dropout, on="student_id", how="left")

    # 3) Compute average risk per colonia
    risk_df = merged.groupby("colonia_id")["ever_dropped"].mean().reset_index()
    risk_map_df = risk_df.merge(colonias_df, left_on="colonia_id", right_on")


    return risk_map_df

