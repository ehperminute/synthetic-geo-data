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


def plot_risk_map(risk_full):
    fig = px.choropleth(
        risk_full,
        geojson=risk_full.geometry,
        locations=risk_full.index,
        color="ever_dropped",
        projection="mercator",
        title="Dropout Risk by Colonia",
    )
    fig.update_geos(fitbounds="locations", visible=False)
    return fig
