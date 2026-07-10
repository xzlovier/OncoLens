"""
Expression Card – Gene Expression Profile Explorer.
"""

from dash import html, dcc
from app.layouts.viz_card import viz_card


def ExpressionCard(
    gene_options: list,
    default_profile: str,
) -> html.Div:
    """
    Returns the viz card for the Gene Expression Profile Explorer.

    Gene selector dropdown is placed on the right side of the card header.
    """
    dd_style = {"color": "#1F2937", "fontSize": "0.85rem"}
    
    # Dropdown to be placed on the right side of the card header
    gene_dropdown = html.Div(
        style={"width": "180px", "marginTop": "2px"},
        children=[
            dcc.Dropdown(
                id="profiles-gene-selector",
                options=gene_options,
                value=default_profile,
                searchable=True,
                clearable=False,
                placeholder="Select gene…",
                style=dd_style,
            )
        ]
    )

    # Plot area stretching to full width and height
    plot_area = html.Div(
        style={
            "flex": "1",
            "display": "flex",
            "flexDirection": "column",
            "minWidth": "0",
            "minHeight": "0"
        },
        children=[
            dcc.Loading(
                type="circle",
                color="#2563EB",
                parent_style={
                    "height": "100%",
                    "flex": "1 1 0",
                    "display": "flex",
                    "flexDirection": "column",
                },
                children=dcc.Graph(
                    id="profiles-plot",
                    className="dash-graph",
                    config={"displayModeBar": True, "responsive": True},
                    style={
                        "height": "100%",
                        "width": "100%",
                        "flex": "1 1 0",
                        "minHeight": "0",
                    },
                )
            )
        ]
    )

    # Footer element for highlighted statistics details (updated via callback)
    footer_details = html.Div(
        id="profiles-details-card",
        className="profiles-footer-content"
    )

    return viz_card(
        card_id="card-expression",
        title="Gene Expression Profiles",
        subtitle="How does a gene's expression vary across the five clinical cohorts?",
        children=plot_area,
        footer=footer_details,
        header_right=gene_dropdown
    )
