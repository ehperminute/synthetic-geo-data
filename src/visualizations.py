"""
visualizations.py
-----------------

Plotting utilities for:
- dropout distribution
- ROC curve (if model is used)
- geospatial risk map
"""

import plotly.express as px
import pandas as pd


def plot_dropout_by_semester(panel_df):
    """Simple bar chart of dropout counts by semester."""
    df = panel_df.groupby("semester")["dropped"].sum().reset_index()
    fig = px.bar(df, x="semester", y="dropped", title="Dropouts by Semester")
    return fig


def plot_risk_map(colonias_gdf, risk_df):
    """Join the risk table and plot a colored map."""
    merged = colonias_gdf.merge(risk_df, on="colonia_id", how="left")

    fig = px.choropleth(
        merged,
        geojson=merged.geometry.__geo_interface__,
        locations=merged.index,
        color="ever_dropped",
        projection="mercator",
        title="Dropout Risk by Colonia",
    )
    fig.update_geos(fitbounds="locations", visible=False)
    return fig
