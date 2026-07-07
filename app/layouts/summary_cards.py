"""
OncoLens Summary Cards Row.

Displays six static KPI cards beneath the header.
All values are computed once at startup and embedded directly —
no callback required because the dataset never changes between sessions.
"""

from dash import html
from app.layouts.theme import COLOR_ACCENT_PRIMARY, COLOR_ACCENT_SECONDARY, COLOR_TEXT_SECONDARY


def SummaryCards(
    n_patients: int,
    n_genes: int,
    n_classes: int,
    best_pair: str,
    top_gene: str,
    network_threshold: str,
) -> html.Div:
    """
    Returns a horizontal row of six stat cards.

    Parameters
    ----------
    n_patients : int
        Total patient count.
    n_genes : int
        Number of variance-selected genes.
    n_classes : int
        Distinct tumor subtypes (5).
    best_pair : str
        Display string for the Rank-1 gene pair, e.g. "CDK1 & NACC2".
    top_gene : str
        Symbol of the highest-variance gene.
    network_threshold : str
        Default Pearson threshold for the co-expression network, e.g. "r ≥ 0.80".
    """
    cards = [
        _stat("Patients", str(n_patients), "👥", COLOR_ACCENT_PRIMARY),
        _stat("Genes Analysed", str(n_genes), "🧬", "#8B5CF6"),
        _stat("Tumor Classes", str(n_classes), "🔬", "#EF4444"),
        _stat("Best Gene Pair", best_pair, "⭐", "#F59E0B"),
        _stat("Top Variance Gene", top_gene, "📈", COLOR_ACCENT_SECONDARY),
        _stat("Network Threshold", network_threshold, "🕸️", "#6B7280"),
    ]

    return html.Div(
        id="summary-cards-row",
        className="summary-row",
        children=cards
    )


def _stat(label: str, value: str, icon: str, accent: str) -> html.Div:
    return html.Div(
        className="stat-card",
        children=[
            html.Div(
                className="stat-card-icon",
                children=icon,
                style={"color": accent}
            ),
            html.Div(
                className="stat-card-body",
                children=[
                    html.Div(value, className="stat-card-value", style={"color": accent}),
                    html.Div(label, className="stat-card-label"),
                ]
            )
        ]
    )
