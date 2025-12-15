"""
visualizations.py
"""

import plotly.express as px
import plotly.graph_objects as go


def plot_dropout_by_semester(panel_df):
    """Simple bar chart of dropout counts by semester."""
    df = panel_df.groupby("semester")["dropped"].sum().reset_index()
    fig = px.bar(df, x="semester", y="dropped", title="Dropouts by Semester")
    return fig





def plot_risk_map(risk_full, city_name="Mexico City"):
    """Map with OpenStreetMap background showing roads and streets"""
    
    # Convert to lat/lon
    risk_plot = risk_full.to_crs(epsg=4326)
    
    # Get center coordinates
    bounds = risk_plot.total_bounds
    center_lon = (bounds[0] + bounds[2]) / 2
    center_lat = (bounds[1] + bounds[3]) / 2
    
    fig = px.choropleth_mapbox(
        risk_plot,
        geojson=risk_plot.geometry,
        locations=risk_plot.index,
        color="ever_dropped",
        color_continuous_scale="YlOrRd", 
        mapbox_style="carto-positron",  # ← THIS SHOWS ROADS!
        zoom=11,  # Adjust zoom level (higher = more detailed)
        center={"lat": center_lat, "lon": center_lon},
        opacity=0.8,  # Make polygons slightly transparent to see roads
        labels={"ever_dropped": "Dropout Rate", "NOMDT": "Alcaldia"},
        title=f"<b>Dropout Risk Map - {city_name}</b>",
        hover_name=risk_plot.NOMUT,  # Show neighborhood names
        hover_data={"ever_dropped": ":.1%", "NOMDT": True}
    )
    
    # Professional styling
    fig.update_layout(
        margin=dict(l=20, r=20, t=80, b=20),
        title_font=dict(size=20, family="Arial, sans-serif"),
        title_x=0.5,
        coloraxis_colorbar=dict(
            title="Risk Level",
            title_font=dict(size=12),
            tickfont=dict(size=10),
            thickness=20,
            len=0.8
        ),
        paper_bgcolor="white",
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Arial"
        )
    )
    
    return fig
