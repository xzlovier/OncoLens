"""
OncoLens Global Control Bar.

A single row of shared controls that drive multiple visualisations.
The Gene X / Gene Y dropdowns feed the contour plot.
The Expression Gene dropdown feeds the profiles explorer.
The Network Threshold dropdown feeds the co-expression network.
The Patient Selector feeds the simulator.
"""

from dash import html, dcc
from app.layouts.theme import COLOR_BORDER, COLOR_TEXT_PRIMARY, COLOR_SURFACE


def ControlBar(
    gene_options: list,
    top_20_options: list,
    network_threshold_options: list,
    patient_options: list,
    default_x: str,
    default_y: str,
    default_profile: str,
    default_threshold: float,
    default_patient: str,
) -> html.Div:
    """
    Returns the global shared control bar.

    All IDs match what the existing callbacks already target — no callback
    changes required for these controls.
    """
    dd_style = {"color": "#1F2937", "fontSize": "0.85rem"}

    return html.Div(
        id="control-bar",
        className="controls-bar",
        children=[
            # Gene X (contour x-axis)
            _ctrl_group(
                "Gene X",
                dcc.Dropdown(
                    id="dropdown-x",
                    options=gene_options,
                    value=default_x,
                    searchable=True,
                    clearable=False,
                    placeholder="Select Gene X…",
                    style=dd_style,
                )
            ),
            # Gene Y (contour y-axis)
            _ctrl_group(
                "Gene Y",
                dcc.Dropdown(
                    id="dropdown-y",
                    options=gene_options,
                    value=default_y,
                    searchable=True,
                    clearable=False,
                    placeholder="Select Gene Y…",
                    style=dd_style,
                )
            ),
            # Suggested demo pair (syncs with dropdown-x / dropdown-y)
            _ctrl_group(
                "Demo Pair",
                dcc.Dropdown(
                    id="demo-pair-selector",
                    options=top_20_options,
                    value=1,
                    clearable=True,
                    placeholder="Top pairs…",
                    style=dd_style,
                )
            ),
            # Display mode for contour
            _ctrl_group(
                "Contour Mode",
                dcc.RadioItems(
                    id="contour-display-toggle",
                    options=[
                        {"label": " Scatter", "value": "scatter"},
                        {"label": " +Contour", "value": "both"},
                    ],
                    value="scatter",
                    inline=True,
                    labelStyle={"marginRight": "0.75rem", "fontSize": "0.85rem"},
                )
            ),
            # Expression gene (profiles explorer)
            _ctrl_group(
                "Expression Gene",
                dcc.Dropdown(
                    id="profiles-gene-selector",
                    options=gene_options,
                    value=default_profile,
                    searchable=True,
                    clearable=False,
                    placeholder="Select gene…",
                    style=dd_style,
                )
            ),
            # Network threshold
            _ctrl_group(
                "Network Threshold",
                dcc.Dropdown(
                    id="network-threshold-selector",
                    options=network_threshold_options,
                    value=default_threshold,
                    clearable=False,
                    style=dd_style,
                )
            ),
            # Patient selector (simulator)
            _ctrl_group(
                "Patient Baseline",
                dcc.Dropdown(
                    id="simulator-patient-selector",
                    options=patient_options,
                    value=default_patient,
                    clearable=False,
                    searchable=True,
                    style=dd_style,
                )
            ),
            # Chromosome selector (hotspot map)
            _ctrl_group(
                "Chromosome",
                dcc.Dropdown(
                    id="hotspots-chr-selector",
                    options=(
                        [{"label": "All Chromosomes", "value": "All"}]
                        + [{"label": f"Chr {c}", "value": str(c)} for c in range(1, 23)]
                        + [{"label": "Chr X", "value": "X"}, {"label": "Chr Y", "value": "Y"}]
                    ),
                    value="All",
                    clearable=False,
                    style=dd_style,
                )
            ),
            # Reset button (simulator)
            html.Div(
                className="ctrl-group ctrl-group--btn",
                children=[
                    html.Label("Simulator", className="ctrl-label"),
                    html.Button(
                        "↺ Reset",
                        id="simulator-reset-btn",
                        n_clicks=0,
                        className="btn-reset",
                    )
                ]
            )
        ]
    )


def _ctrl_group(label: str, control) -> html.Div:
    return html.Div(
        className="ctrl-group",
        children=[
            html.Label(label, className="ctrl-label"),
            control,
        ]
    )
