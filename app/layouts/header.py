"""
OncoLens Header Component.

Builds the compact top header bar containing the branding and a dataset
status pill on the right. Accepts no reactive inputs — fully static.
"""

from dash import html
from app.layouts.theme import (
    COLOR_SURFACE, COLOR_BORDER, COLOR_TEXT_PRIMARY,
    COLOR_TEXT_SECONDARY, COLOR_ACCENT_PRIMARY
)


def Header(n_samples: int, n_genes: int, n_classes: int) -> html.Div:
    """
    Returns the top dashboard header.

    Parameters
    ----------
    n_samples : int
        Total patient / sample count loaded at startup.
    n_genes : int
        Number of variance-filtered genes.
    n_classes : int
        Number of tumor subtypes (always 5 for this dataset).
    """
    return html.Header(
        id="dash-header",
        children=[
            # Left: branding
            html.Div(
                className="header-brand",
                children=[
                    html.Span("Onco", className="brand-onco"),
                    html.Span("Lens", className="brand-lens"),
                    html.Span(
                        "Brain Tumor Visual Analytics Dashboard",
                        className="brand-subtitle"
                    ),
                ]
            ),
            # Right: compact dataset pill
            html.Div(
                className="header-meta",
                children=[
                    _pill(str(n_samples), "Samples"),
                    _pill(str(n_genes), "Genes"),
                    _pill(str(n_classes), "Classes"),
                    html.Span(
                        "CS661 • Group 11",
                        style={
                            "fontSize": "0.78rem",
                            "color": COLOR_TEXT_SECONDARY,
                            "marginLeft": "1rem",
                            "fontWeight": "500"
                        }
                    )
                ]
            )
        ]
    )


def _pill(value: str, label: str) -> html.Div:
    return html.Div(
        className="header-pill",
        children=[
            html.Span(value, className="pill-value"),
            html.Span(label, className="pill-label"),
        ]
    )
