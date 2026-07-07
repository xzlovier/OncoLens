"""
Expression Card – Gene Expression Profile Explorer.
"""

from dash import html, dcc
from app.layouts.viz_card import viz_card


def ExpressionCard() -> html.Div:
    """
    Returns the viz card for the Gene Expression Profile Explorer.

    The gene selector lives in the global ControlBar (id="profiles-gene-selector").
    This card contains the violin/box plot and the stats sidebar panel.
    """
    plot_col = html.Div(
        style={"flex": "1", "minWidth": "0"},
        children=[
            dcc.Loading(
                type="circle",
                color="#2563EB",
                children=dcc.Graph(
                    id="profiles-plot",
                    config={"displayModeBar": True, "responsive": True},
                    style={"height": "100%", "minHeight": "280px"},
                )
            )
        ]
    )

    details_col = html.Div(
        id="profiles-details-card",
        className="side-details-panel",
        children=[],
        style={"width": "220px", "flexShrink": "0"},
    )

    return viz_card(
        card_id="card-expression",
        title="Gene Expression Profiles",
        subtitle="How does a gene's expression vary across the five clinical cohorts?",
        children=html.Div(
            style={"display": "flex", "gap": "1rem", "flex": "1"},
            children=[plot_col, details_col]
        ),
    )
