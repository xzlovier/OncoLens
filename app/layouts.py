"""
Dashboard Layouts Module for OncoLens.

This module defines the UI architecture, navigation tabs, vertical sidebars,
branding components, welcome messages, and cards showing where each visualization
will load.
"""

from dash import html, dcc

def get_overview_layout() -> html.Div:
    """
    Returns the home/overview tab layout containing the welcome banner and
    placeholder cards for all five future analytical visualizations.
    """
    return html.Div([
        # Welcome Banner
        html.Div(
            className="welcome-banner",
            children=[
                html.H2("Welcome to OncoLens", className="welcome-title"),
                html.P(
                    "OncoLens is an interactive visual analytics system designed to map "
                    "structural and molecular boundaries separating healthy brain tissue from "
                    "four aggressive CNS malignancies: Ependymoma, Glioblastoma, "
                    "Medulloblastoma, and Pilocytic Astrocytoma. Use the left sidebar to navigate "
                    "through the visual profiling panels.",
                    className="welcome-text"
                )
            ]
        ),
        
        # Section Heading
        html.H3("Visual Analytics Panels", style={"color": "#f8fafc", "marginTop": "2rem", "fontSize": "1.6rem"}),
        
        # Grid of Placeholder Cards
        html.Div(
            className="placeholders-grid",
            children=[
                # Card 1
                html.Div(
                    className="placeholder-card",
                    children=[
                        html.Div([
                            html.H4("Chromosomal Hotspot & Cytoband Mapping", className="card-title"),
                            html.P(
                                "Maps individual genetic loci (base-pair start coordinates) "
                                "against patient Dysregulation Indices (DI) to visualize structural "
                                "genomic hotspots across chromosomes.",
                                className="card-description"
                            ),
                        ]),
                        html.Span("Visualization Pending", className="card-status status--pending")
                    ]
                ),
                # Card 2
                html.Div(
                    className="placeholder-card",
                    children=[
                        html.Div([
                            html.H4("Subtype Volumetric Biomarker Profiling", className="card-title"),
                            html.P(
                                "Compares gene expression distributions (quartiles, spreads, and medians) "
                                "across clinical cohorts and tissue types via split violin and box plots.",
                                className="card-description"
                            ),
                        ]),
                        html.Span("Visualization Pending", className="card-status status--pending")
                    ]
                ),
                # Card 3
                html.Div(
                    className="placeholder-card",
                    children=[
                        html.Div([
                            html.H4("Multi-Gene Phenotypic Contour Plot", className="card-title"),
                            html.P(
                                "Draws 2D contour density maps using Kernel Density Estimations (KDE) "
                                "across dual genes to observe clinical subtype overlaps and boundaries.",
                                className="card-description"
                            ),
                        ]),
                        html.Span("Visualization Pending", className="card-status status--pending")
                    ]
                ),
                # Card 4
                html.Div(
                    className="placeholder-card",
                    children=[
                        html.Div([
                            html.H4("Gene Interaction & Co-occurrence Network", className="card-title"),
                            html.P(
                                "Plots interactive 2D node-link graphs mapping pathway correlations "
                                "and co-expression strengths based on Pearson thresholds.",
                                className="card-description"
                            ),
                        ]),
                        html.Span("Visualization Pending", className="card-status status--pending")
                    ]
                ),
                # Card 5
                html.Div(
                    className="placeholder-card",
                    children=[
                        html.Div([
                            html.H4("Expression Simulator Widget", className="card-title"),
                            html.P(
                                "Exploratory sandbox enabling researchers to adjust gene expression sliders "
                                "and observe live tumor class probability shifts using distance classifiers.",
                                className="card-description"
                            ),
                        ]),
                        html.Span("Visualization Pending", className="card-status status--pending")
                    ]
                ),
            ]
        )
    ])


def get_tab_placeholder_layout(title: str, description: str) -> html.Div:
    """
    Returns a generic layout representing a visualization panel that is under development.
    """
    return html.Div([
        # Header Banner
        html.Div(
            className="welcome-banner",
            children=[
                html.H2(title, className="welcome-title"),
                html.P(description, className="welcome-text")
            ]
        ),
        
        # Placeholder Card
        html.Div(
            className="placeholder-card",
            style={"maxWidth": "650px", "marginTop": "2rem"},
            children=[
                html.Div([
                    html.H4(f"{title} Workspace", className="card-title"),
                    html.P(
                        "This workspace is configured and ready for data binding. The reactive controls, "
                        "selection callbacks, and interactive rendering will be implemented here.",
                        className="card-description"
                    ),
                ]),
                html.Span("Data Bound / Visualization Pending", className="card-status status--pending")
            ]
        )
    ])


def create_layout() -> html.Div:
    """
    Constructs the parent dashboard layout consisting of a left navigation sidebar
    and a dynamic right main content area.
    """
    return html.Div(
        className="app-container",
        children=[
            # Sidebar Container
            html.Div(
                className="sidebar",
                children=[
                    # Branding logo & subtitle
                    html.Div(
                        className="logo-container",
                        children=[
                            html.H1("OncoLens", className="logo-title"),
                            html.Div(
                                "Multi-Dimensional Brain Tumor Characterization & Genomic Dysregulation Mapping",
                                className="logo-subtitle"
                            )
                        ]
                    ),
                    
                    # Sidebar vertical tabs navigation menu
                    dcc.Tabs(
                        id="navigation-tabs",
                        value="tab-overview",
                        vertical=True,
                        className="sidebar-tabs",
                        children=[
                            dcc.Tab(
                                label="Dashboard Overview",
                                value="tab-overview",
                                className="tab",
                                selected_className="tab--selected"
                            ),
                            dcc.Tab(
                                label="Chromosomal Hotspots",
                                value="tab-hotspots",
                                className="tab",
                                selected_className="tab--selected"
                            ),
                            dcc.Tab(
                                label="Gene Expression Profiles",
                                value="tab-profiles",
                                className="tab",
                                selected_className="tab--selected"
                            ),
                            dcc.Tab(
                                label="Multi-Gene Contour Plot",
                                value="tab-contour",
                                className="tab",
                                selected_className="tab--selected"
                            ),
                            dcc.Tab(
                                label="Gene Interaction Network",
                                value="tab-network",
                                className="tab",
                                selected_className="tab--selected"
                            ),
                            dcc.Tab(
                                label="Expression Simulator",
                                value="tab-simulator",
                                className="tab",
                                selected_className="tab--selected"
                            ),
                        ]
                    ),
                    
                    # Sidebar version info
                    html.Div(
                        "OncoLens System v1.0",
                        className="sidebar-footer"
                    )
                ]
            ),
            
            # Dynamic Main Panel
            html.Div(
                id="main-content-panel",
                className="main-content",
                children=[]  # Populated dynamically in callbacks.py
            )
        ]
    )
