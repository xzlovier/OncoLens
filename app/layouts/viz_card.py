"""
Shared viz-card builder for OncoLens.

Every visualization lives inside an identical card component built by viz_card().
Consistent padding, typography, and shadows across all five panels.
"""

from dash import html, dcc
from app.layouts.theme import COLOR_SURFACE, COLOR_BORDER, COLOR_TEXT_PRIMARY, COLOR_TEXT_SECONDARY


def viz_card(
    card_id: str,
    title: str,
    subtitle: str,
    children,
    footer=None,
    extra_class: str = "",
    header_right=None,
) -> html.Div:
    """
    Returns a white rounded card containing a viz panel.

    Parameters
    ----------
    card_id : str
        HTML id for the outer card div.
    title : str
        Card title (short, no punctuation).
    subtitle : str
        One-sentence description: "What question does this answer?"
    children : Dash component or list
        Main content (graph, sliders, etc.).
    footer : optional
        Optional compact footer element.
    extra_class : str
        Additional CSS class names for the card.
    header_right : optional
        Optional element placed on the right side of the card header.
    """
    header_left = html.Div(
        style={"flex": "1", "minWidth": "0"},
        children=[
            html.H3(title, className="viz-card-title"),
            html.P(subtitle, className="viz-card-subtitle"),
        ]
    )

    header_children = [header_left]
    if header_right is not None:
        header_children.append(
            html.Div(
                className="viz-card-header-right",
                style={"marginLeft": "1rem", "flexShrink": "0"},
                children=header_right
            )
        )

    header = html.Div(
        className="viz-card-header",
        children=header_children,
    )

    body = html.Div(
        className="viz-card-body",
        children=children,
    )

    inner = [header, body]
    if footer is not None:
        inner.append(html.Div(className="viz-card-footer", children=footer))

    return html.Div(
        id=card_id,
        className=f"viz-card {extra_class}".strip(),
        children=inner,
    )
