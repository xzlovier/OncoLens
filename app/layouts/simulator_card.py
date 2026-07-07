"""
Simulator Card – Interactive Virtual Expression Assayer.

Full-width row spanning the bottom of the dashboard.
Controls: Patient selector (in ControlBar), Gene 1/2/3 selectors and sliders (here).
"""

from dash import html, dcc
from app.layouts.viz_card import viz_card
from app.layouts.theme import COLOR_ACCENT_DANGER, COLOR_BORDER, COLOR_TEXT_SECONDARY
from app.config import DEFAULT_SIM_GENE_1, DEFAULT_SIM_GENE_2, DEFAULT_SIM_GENE_3


def SimulatorCard(
    gene_options: list,
    val1: float = 5.0,
    val2: float = 5.0,
    val3: float = 5.0,
) -> html.Div:
    """
    Returns the full-width simulator card.

    Parameters
    ----------
    gene_options : list
        List of {"label": ..., "value": ...} dicts for gene dropdowns.
    val1, val2, val3 : float
        Initial slider values (baseline expression for default patient).
    """
    # ── Left column: gene selectors + sliders ────────────────────────────────
    left_col = html.Div(
        className="sim-left-col",
        children=[
            # Gene selectors
            html.Div(
                className="sim-gene-selectors",
                children=[
                    _gene_row("Gene 1", "simulator-gene-1", gene_options, DEFAULT_SIM_GENE_1),
                    _gene_row("Gene 2", "simulator-gene-2", gene_options, DEFAULT_SIM_GENE_2),
                    _gene_row("Gene 3", "simulator-gene-3", gene_options, DEFAULT_SIM_GENE_3),
                ]
            ),
            # Sliders
            html.Div(
                className="sim-sliders",
                children=[
                    _slider_row("simulator-slider-label-1", "simulator-slider-1", val1),
                    _slider_row("simulator-slider-label-2", "simulator-slider-2", val2),
                    _slider_row("simulator-slider-label-3", "simulator-slider-3", val3),
                ]
            ),
        ]
    )

    # ── Middle column: probability bar chart ─────────────────────────────────
    mid_col = html.Div(
        className="sim-chart-col",
        children=[
            html.H4(
                "Relative Similarity to Disease Centroids",
                className="sim-chart-title"
            ),
            dcc.Loading(
                type="circle",
                color="#2563EB",
                children=dcc.Graph(
                    id="simulator-plot",
                    config={"responsive": True, "displayModeBar": False},
                    style={"height": "100%", "minHeight": "220px"},
                )
            ),
        ]
    )

    # ── Right column: prediction card + distance card ─────────────────────────
    right_col = html.Div(
        className="sim-right-col",
        children=[
            html.Div(id="simulator-prediction-card", className="sim-result-card"),
            html.Div(id="simulator-distance-card", className="sim-result-card"),
        ]
    )

    disclaimer = html.Div(
        className="sim-disclaimer",
        children=[
            html.Strong("⚠ Research Disclosure: ", style={"color": "#D97706"}),
            "Exploratory computational simulator only. Not a clinical diagnostic tool. "
            "Probabilities reflect mathematical sensitivity of a centroid-distance classifier "
            "to hypothetical expression changes, not clinical predictions."
        ]
    )

    return viz_card(
        card_id="card-simulator",
        title="Interactive Virtual Expression Assayer",
        subtitle=(
            "How does perturbing a gene's expression level shift the predicted "
            "tumor subtype similarity?"
        ),
        children=html.Div(
            className="sim-body",
            children=[left_col, mid_col, right_col]
        ),
        footer=disclaimer,
        extra_class="viz-card--full-width",
    )


# ── Private helpers ───────────────────────────────────────────────────────────

def _gene_row(label: str, dropdown_id: str, options: list, default_val: str) -> html.Div:
    return html.Div(
        className="sim-gene-row",
        children=[
            html.Label(label, className="ctrl-label"),
            dcc.Dropdown(
                id=dropdown_id,
                options=options,
                value=default_val,
                clearable=False,
                searchable=True,
                style={"color": "#1F2937", "fontSize": "0.82rem"},
            )
        ]
    )


def _slider_row(label_id: str, slider_id: str, initial_value: float) -> html.Div:
    return html.Div(
        className="sim-slider-row",
        children=[
            html.Div(
                id=label_id,
                className="sim-slider-label",
                style={"display": "flex", "justifyContent": "space-between"},
            ),
            dcc.Slider(
                id=slider_id,
                min=0,
                max=15,
                step=0.01,
                value=initial_value,
                tooltip={"placement": "bottom", "always_visible": True},
                marks=None,
            )
        ]
    )
