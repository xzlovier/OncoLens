"""
Dashboard Callbacks Module for OncoLens.

This module implements the reactive event handlers and content layout switching
logic for the visual analytics application. Currently, it acts as a router switching
between dynamic layout containers based on the selected sidebar tab.
"""

from dash import Input, Output, html, Dash
from app.layouts import get_overview_layout, get_tab_placeholder_layout

def register_callbacks(app: Dash) -> None:
    """
    Registers all reactive callbacks for the Dash application.
    
    Args:
        app (Dash): The parent Dash application object.
    """
    
    @app.callback(
        Output("main-content-panel", "children"),
        Input("navigation-tabs", "value")
    )
    def render_tab_content(active_tab: str) -> html.Div:
        """
        Dynamically updates the main panel workspace depending on the active sidebar menu selection.
        """
        if active_tab == "tab-overview":
            return get_overview_layout()
            
        elif active_tab == "tab-hotspots":
            return get_tab_placeholder_layout(
                "Chromosomal Hotspot & Cytoband Mapping",
                "Linear coordinate plot displaying Dysregulation Indices across chromosomal coordinates."
            )
            
        elif active_tab == "tab-profiles":
            return get_tab_placeholder_layout(
                "Subtype Volumetric Biomarker Profiling",
                "Quartile distributions and clinical cohort benchmarking using split violin-plots."
            )
            
        elif active_tab == "tab-contour":
            return get_tab_placeholder_layout(
                "Multi-Gene Phenotypic Contour Plot",
                "Topographical Kernel Density Estimation (KDE) density maps separating healthy from cancer groups."
            )
            
        elif active_tab == "tab-network":
            return get_tab_placeholder_layout(
                "Gene Interaction & Co-occurrence Network",
                "Interactive co-expression pathways mapped via thresholded Pearson correlation networks."
            )
            
        elif active_tab == "tab-simulator":
            return get_tab_placeholder_layout(
                "Virtual Expression Assayer (The Simulator Widget)",
                "Interactive multi-bar clinical classification probability feedback using expression sliders."
            )
            
        # Fallback to home/overview
        return get_overview_layout()
