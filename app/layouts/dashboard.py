"""
OncoLens Dashboard Assembler.

`create_layout()` is the single entry point called by app.py.
It accepts all runtime data needed to pre-populate static values and
assembles the full unified dashboard from individual layout components.

No reactive callbacks are defined here — only static component assembly.
"""

from dash import html, dcc

from app.layouts.header import Header
from app.layouts.summary_cards import SummaryCards
from app.layouts.control_bar import ControlBar
from app.layouts.contour_card import ContourCard
from app.layouts.expression_card import ExpressionCard
from app.layouts.hotspot_card import HotspotCard
from app.layouts.network_card import NetworkCard
from app.layouts.simulator_card import SimulatorCard


# Default network threshold options — kept here so ControlBar and summary cards
# share the same definition without duplication.
NETWORK_THRESHOLD_OPTIONS = [
    {"label": "r ≥ 0.70 (Dense)",    "value": 0.70},
    {"label": "r ≥ 0.75",             "value": 0.75},
    {"label": "r ≥ 0.80 (Standard)", "value": 0.80},
    {"label": "r ≥ 0.85",             "value": 0.85},
    {"label": "r ≥ 0.90 (Sparse)",   "value": 0.90},
]
DEFAULT_NETWORK_THRESHOLD = 0.80


def create_layout(
    n_patients: int = 0,
    n_genes: int = 0,
    n_classes: int = 5,
    best_pair: str = "—",
    top_gene: str = "—",
    gene_options: list = None,
    top_20_options: list = None,
    patient_options: list = None,
    default_x: str = None,
    default_y: str = None,
    default_profile: str = None,
    default_patient: str = None,
    sim_val1: float = 5.0,
    sim_val2: float = 5.0,
    sim_val3: float = 5.0,
) -> html.Div:
    """
    Assembles the complete unified OncoLens dashboard layout.

    All five visualizations are statically embedded; no tab routing required.
    Called once at application startup by app.py.

    Parameters
    ----------
    n_patients : int
        Total patients in dataset.
    n_genes : int
        Number of variance-filtered genes.
    n_classes : int
        Distinct tumor classes.
    best_pair : str
        Display string for the Rank-1 gene pair.
    top_gene : str
        Symbol of the highest-variance gene.
    gene_options : list
        Full annotated gene dropdown options.
    top_20_options : list
        Top-20 recommended pairs for demo-pair-selector.
    patient_options : list
        Patient ID dropdown options.
    default_x, default_y : str
        Default Gene X / Gene Y probe IDs.
    default_profile : str
        Default probe ID for the Expression Explorer.
    default_patient : str
        Default patient ID for the simulator.
    sim_val1, sim_val2, sim_val3 : float
        Default slider values for the simulator.
    """
    gene_options   = gene_options   or []
    top_20_options = top_20_options or []
    patient_options = patient_options or []

    return html.Div(
        id="oncolens-dashboard",
        className="oncolens-dashboard",
        children=[
            # ── Hidden stores for future cross-visualization synchronization ──
            dcc.Store(id="selected-gene"),
            dcc.Store(id="selected-patient"),

            # ── 1. Header ──────────────────────────────────────────────────────
            Header(
                n_samples=n_patients,
                n_genes=n_genes,
                n_classes=n_classes,
            ),

            # ── 2. Summary cards row ───────────────────────────────────────────
            SummaryCards(
                n_patients=n_patients,
                n_genes=n_genes,
                n_classes=n_classes,
                best_pair=best_pair,
                top_gene=top_gene,
                network_threshold="r ≥ 0.80",
            ),

            # ── 3. Global control bar ──────────────────────────────────────────
            ControlBar(
                gene_options=gene_options,
                top_20_options=top_20_options,
                network_threshold_options=NETWORK_THRESHOLD_OPTIONS,
                patient_options=patient_options,
                default_x=default_x or (gene_options[0]["value"] if gene_options else None),
                default_y=default_y or (gene_options[1]["value"] if len(gene_options) > 1 else None),
                default_profile=default_profile,
                default_threshold=DEFAULT_NETWORK_THRESHOLD,
                default_patient=default_patient,
            ),

            # ── 4. Visualization grid ──────────────────────────────────────────
            html.Div(
                className="viz-grid",
                children=[

                    # Row 1: Contour + Expression (side by side)
                    html.Div(
                        className="viz-row",
                        children=[
                            ContourCard(),
                            ExpressionCard(),
                        ]
                    ),

                    # Row 2: Hotspot + Network (side by side)
                    html.Div(
                        className="viz-row",
                        children=[
                            HotspotCard(),
                            NetworkCard(),
                        ]
                    ),

                    # Row 3: Simulator (full width)
                    html.Div(
                        className="viz-row viz-row--full",
                        children=[
                            SimulatorCard(
                                gene_options=gene_options,
                                val1=sim_val1,
                                val2=sim_val2,
                                val3=sim_val3,
                            ),
                        ]
                    ),
                ]
            ),

            # ── 5. Footer ──────────────────────────────────────────────────────
            html.Footer(
                id="dash-footer",
                className="dash-footer",
                children=[
                    html.Span(
                        "OncoLens v1.0  •  CS661 Visual Analytics Project  •  Group 11  •  "
                        "Research tool only — not a clinical diagnostic instrument.",
                        className="footer-text"
                    )
                ]
            )
        ]
    )
