"""
Contour Card – Multi-Gene Phenotypic Contour Plot.
"""

from dash import html, dcc
from app.layouts.viz_card import viz_card


def ContourCard(
    gene_options: list,
    top_20_options: list,
    default_x: str,
    default_y: str,
) -> html.Div:
    """
    Returns the self-contained viz card for the Multi-Gene Phenotypic Contour Plot.

    Includes its own controls (Gene X, Gene Y, Demo Pair, Contour Mode) at the top,
    and a compact footer for gene and separation metadata below the plot.
    """
    dd_style = {"color": "#1F2937", "fontSize": "0.85rem"}
    
    # Card-specific controls row
    controls_row = html.Div(
        className="contour-toolbar",
        children=[
            html.Div(
                className="toolbar-left",
                children=[
                    # Gene X
                    html.Div(className="toolbar-control", children=[
                        html.Label("Gene X", className="ctrl-label"),
                        dcc.Dropdown(
                            id="dropdown-x",
                            options=gene_options,
                            value=default_x,
                            clearable=False,
                            searchable=True,
                            style=dd_style,
                        )
                    ]),
                    # Gene Y
                    html.Div(className="toolbar-control", children=[
                        html.Label("Gene Y", className="ctrl-label"),
                        dcc.Dropdown(
                            id="dropdown-y",
                            options=gene_options,
                            value=default_y,
                            clearable=False,
                            searchable=True,
                            style=dd_style,
                        )
                    ]),
                    # Demo Pair
                    html.Div(className="toolbar-control", children=[
                        html.Label("Demo Pair", className="ctrl-label"),
                        dcc.Dropdown(
                            id="demo-pair-selector",
                            options=top_20_options,
                            value=1,
                            clearable=True,
                            style=dd_style,
                        )
                    ]),
                ],
            ),
            html.Div(
                className="toolbar-right",
                children=[
                    dcc.RadioItems(
                        id="contour-display-toggle",
                        options=[
                            {"label": " Points", "value": "scatter"},
                            {"label": " Points + Contours", "value": "both"},
                        ],
                        value="scatter",
                        inline=False,
                        className="contour-radio",
                    ),
                ],
            ),
        ],
    )

    # Demo badge (hidden until default pair is active)
    demo_badge = html.Div(
        id="demo-badge",
        children="★ Best Demonstration Pair",
        title=(
            "This pair was automatically selected during preprocessing as one of "
            "the highest subtype-separating gene pairs within the variance-filtered dataset."
        ),
        style={
            "display": "none",
            "backgroundColor": "#EFF6FF",
            "color": "#2563EB",
            "border": "1px solid #BFDBFE",
            "borderRadius": "6px",
            "padding": "4px 10px",
            "fontSize": "0.78rem",
            "fontWeight": "600",
            "marginBottom": "0.5rem",
            "letterSpacing": "0.04em",
            "cursor": "help",
        }
    )



    plot_area = html.Div(
        children=[
            dcc.Loading(
                type="circle",
                color="#2563EB",
                children=dcc.Graph(
                    id="contour-plot",
                    config={
                        "displayModeBar": True,
                        "responsive": True,
                    },
                    style={
                        "height": "340px",      # try 340–350
                        "width": "100%",
                        "display": "block",
                    },
                ),
            )
        ],
        style={
            "margin-top": "2px",
        },
    )

    return viz_card(
        card_id="card-contour",
        title="Multi-Gene Phenotypic Contour",
        subtitle="Do the expression patterns of two genes cleanly separate tumor subtypes?",
        children=html.Div(
            style={
                "display": "flex",
                "flexDirection": "column",
                "flex": "1",
                "minHeight": "0",
            },
            children=[

                # ---------------------------------------------------------
                # Toolbar
                # ---------------------------------------------------------
                controls_row,

                # ---------------------------------------------------------
                # Plot
                # ---------------------------------------------------------
                html.Div(
                    style={
                        "flex": "1",
                        "minHeight": "0",
                        "marginTop": "0",
                    },
                    children=[plot_area],
                ),

                # ---------------------------------------------------------
                # Footer Statistics
                # ---------------------------------------------------------
                html.Div(
                    id="contour-footer",
                    className="contour-footer",
                ),

            ]
        ),
    )
