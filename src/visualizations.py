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
        geojson=risk_full.geometry.__geo_interface__,
        locations=risk_full.index,
        color="ever_dropped",
        projection="mercator",
        title="Dropout Risk by Colonia",
    )
    fig.update_geos(fitbounds="locations", visible=False)
    return fig

import plotly.express as px
import plotly.graph_objects as go

def plot_risk_map1(risk_full, city_name="Mexico City"):
    # Create the choropleth map
    fig = px.choropleth(
        risk_full,
        geojson=risk_full.geometry.__geo_interface__,
        locations=risk_full.index,
        color="ever_dropped",
        color_continuous_scale="Viridis",  # Better color scale
        range_color=[risk_full["ever_dropped"].min(), 
                    risk_full["ever_dropped"].max()],
        labels={"ever_dropped": "Dropout Risk Score"},
        title=f"<b>Student Dropout Risk Map</b><br><sup>{city_name} - By Neighborhood (Colonia)</sup>",
        hover_name=risk_full.index,  # Show colonia names on hover
        hover_data={"ever_dropped": ":.2f"}  # Format to 2 decimals
    )
    
    # Update layout for professional look
    fig.update_layout(
        # Reduce margins
        margin=dict(l=20, r=20, t=80, b=20),
        
        # Professional title styling
        title_font=dict(size=20, family="Arial, sans-serif"),
        title_x=0.5,  # Center title
        
        # Colorbar styling
        coloraxis_colorbar=dict(
            title="Risk Level",
            title_font=dict(size=12),
            tickfont=dict(size=10),
            thickness=15,
            len=0.75
        ),
        
        # Map background
        paper_bgcolor="white",
        plot_bgcolor="white",
        
        # Hover label styling
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Arial"
        )
    )
    
    # Update geos (map projection)
    fig.update_geos(
        fitbounds="locations",
        visible=False,
        # Optional: Show country/city boundaries faintly
        # subunitcolor="lightgray",
        # subunitwidth=0.5
    )
    
    # Optional: Add annotations for key areas/districts
    # You'll need coordinates for your city's districts
    # Example:
    # fig.add_trace(go.Scattergeo(
    #     lon=[-99.1332, -99.15],  # Example coordinates
    #     lat=[19.4326, 19.45],
    #     text=["Centro", "Polanco"],
    #     mode="text",
    #     showlegend=False,
    #     textfont=dict(size=10, color="darkblue")
    # ))
    
    return fig


def plot_risk_map2(risk_full, city_name="Mexico City", mapbox_token=None):
    """
    Mapbox version - shows roads, districts, and better basemaps
    Requires Mapbox token (free account at mapbox.com)
    """
    risk_full = risk_full.to_crs(epsg=32614)
    # Center on the data's centroid
    center_lat = risk_full.geometry.centroid.y.mean()
    center_lon = risk_full.geometry.centroid.x.mean()
    
    fig = px.choropleth_mapbox(
        risk_full,
        geojson=risk_full.geometry,
        locations=risk_full.index,
        color="ever_dropped",
        color_continuous_scale="Viridis",  # Or try "Plasma", "Inferno", "Cividis"
        range_color=[risk_full["ever_dropped"].min(), 
                    risk_full["ever_dropped"].max()],
        mapbox_style="carto-positron",  # Light, professional style
        # mapbox_style="open-street-map",  # Shows roads/streets
        # mapbox_style="stamen-terrain",  # Shows topography
        zoom=10,
        center={"lat": center_lat, "lon": center_lon},
        opacity=0.7,  # Slightly transparent
        labels={"ever_dropped": "Dropout Risk"},
        title=f"<b>Student Dropout Risk Map</b><br><sup>{city_name}</sup>",
        hover_data={"ever_dropped": ":.2f"}
    )
    
    # Professional layout updates
    fig.update_layout(
        margin=dict(l=20, r=20, t=80, b=20),
        title_font=dict(size=20, family="Arial, sans-serif"),
        title_x=0.5,
        coloraxis_colorbar=dict(
            title="Risk Level",
            title_font=dict(size=12),
            tickfont=dict(size=10),
            thickness=20,
            len=0.8,
            yanchor="middle",
            y=0.5
        ),
        paper_bgcolor="white",
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Arial"
        )
    )
    
    # If you have a Mapbox token for more styles
    if mapbox_token:
        fig.update_layout(
            mapbox=dict(
                style="light",  # or "dark", "satellite-streets", etc.
                accesstoken=mapbox_token,
                zoom=11
            )
        )
    
    return fig
