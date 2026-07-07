"""
Network Card – Gene Interaction & Co-expression Network.
"""

from dash import html, dcc
from app.layouts.viz_card import viz_card


def NetworkCard() -> html.Div:
    """
    Returns the viz card for the Gene Interaction & Co-expression Network.

    The threshold selector lives in the global ControlBar (id="network-threshold-selector").
    This card contains the network graph and the node details side panel.
    """
    plot_col = html.Div(
        style={"flex": "1", "minWidth": "0"},
        children=[
            dcc.Loading(
                type="circle",
                color="#2563EB",
                children=dcc.Graph(
                    id="network-plot",
                    config={"displayModeBar": True, "responsive": True},
                    style={"height": "100%", "minHeight": "280px"},
                )
            )
        ]
    )

    details_col = html.Div(
        id="network-details-card",
        className="side-details-panel",
        children=[],
        style={"width": "220px", "flexShrink": "0"},
    )

    return viz_card(
        card_id="card-network",
        title="Gene Co-expression Network",
        subtitle="Which genes are strongly co-expressed, and how do they cluster by chromosome?",
        children=html.Div(
            style={"display": "flex", "gap": "1rem", "flex": "1"},
            children=[plot_col, details_col]
        ),
    )
