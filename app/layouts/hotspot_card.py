"""
Hotspot Card – Chromosomal Hotspot Mapping.
"""

from dash import html, dcc
from app.layouts.viz_card import viz_card


def HotspotCard() -> html.Div:
    """
    Returns the viz card for Chromosomal Hotspot & Cytoband Mapping.

    The chromosome selector lives in the global ControlBar (id="hotspots-chr-selector").
    This card contains the scatter plot and the gene detail side panel.
    """
    plot_col = html.Div(
        style={"flex": "1", "minWidth": "0"},
        children=[
            dcc.Loading(
                type="circle",
                color="#2563EB",
                children=dcc.Graph(
                    id="hotspots-plot",
                    config={"displayModeBar": True, "responsive": True},
                    style={"height": "100%", "minHeight": "280px"},
                )
            )
        ]
    )

    details_col = html.Div(
        id="hotspots-details-card",
        className="side-details-panel",
        children=[],
        style={"width": "220px", "flexShrink": "0"},
    )

    return viz_card(
        card_id="card-hotspot",
        title="Chromosomal Hotspot Mapping",
        subtitle="Where are the highest-variance genes physically located across the genome?",
        children=html.Div(
            style={"display": "flex", "gap": "1rem", "flex": "1"},
            children=[plot_col, details_col]
        ),
    )
