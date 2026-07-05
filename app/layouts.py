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


def get_contour_layout(default_x: str, default_y: str, top_20_options: list) -> html.Div:
    """
    Returns the layout for the Multi-Gene Phenotypic Contour Plot panel.
    """
    return html.Div([
        # Header Banner
        html.Div(
            className="welcome-banner",
            children=[
                html.H2("Multi-Gene Phenotypic Contour Plot", className="welcome-title"),
                html.P(
                    "Explore the joint distribution of any two genes across patient cohorts. "
                    "Analyze overlapping diagnostic boundaries separating healthy baseline tissue "
                    "from the four malignant tumor subtypes using smooth 2D Density Contours.",
                    className="welcome-text"
                )
            ]
        ),
        
        # Control Panel area
        html.Div(
            style={
                "display": "flex", 
                "flexWrap": "wrap",
                "gap": "2rem", 
                "marginBottom": "2rem",
                "backgroundColor": "#0f172a", 
                "border": "1px solid #1e293b",
                "borderRadius": "14px", 
                "padding": "2rem"
            },
            children=[
                # Suggested Pairs Dropdown
                html.Div(
                    style={"flex": "1.2", "minWidth": "280px"},
                    children=[
                        html.Label("Suggested Demonstration Pairs", style={"fontWeight": "600", "color": "#3b82f6", "marginBottom": "0.75rem", "display": "block"}),
                        dcc.Dropdown(
                            id="demo-pair-selector",
                            options=top_20_options,
                            value=1,  # Default to Rank 1
                            clearable=True,
                            placeholder="Select pre-validated pair...",
                            style={"color": "#0b0f19"}
                        )
                    ]
                ),
                # X-axis Dropdown
                html.Div(
                    style={"flex": "1", "minWidth": "220px"},
                    children=[
                        html.Label("X-Axis Gene Selection", style={"fontWeight": "600", "color": "#f8fafc", "marginBottom": "0.75rem", "display": "block"}),
                        dcc.Dropdown(
                            id="dropdown-x",
                            searchable=True,
                            placeholder="Select X-axis gene...",
                            value=default_x,
                            style={"color": "#0b0f19"}
                        )
                    ]
                ),
                # Y-axis Dropdown
                html.Div(
                    style={"flex": "1", "minWidth": "220px"},
                    children=[
                        html.Label("Y-Axis Gene Selection", style={"fontWeight": "600", "color": "#f8fafc", "marginBottom": "0.75rem", "display": "block"}),
                        dcc.Dropdown(
                            id="dropdown-y",
                            searchable=True,
                            placeholder="Select Y-axis gene...",
                            value=default_y,
                            style={"color": "#0b0f19"}
                        )
                    ]
                ),
                # Display Toggle
                html.Div(
                    style={"minWidth": "200px"},
                    children=[
                        html.Label("Plot Display Mode", style={"fontWeight": "600", "color": "#f8fafc", "marginBottom": "0.75rem", "display": "block"}),
                        dcc.RadioItems(
                            id="contour-display-toggle",
                            options=[
                                {"label": " Scatter Only", "value": "scatter"},
                                {"label": " Scatter + Contour", "value": "both"}
                            ],
                            value="scatter",
                            labelStyle={"display": "inline-block", "marginRight": "1.5rem", "cursor": "pointer"},
                            style={"color": "#cbd5e1", "paddingTop": "6px"}
                        )
                    ]
                )
            ]
        ),
        
        # Graph Area
        html.Div(
            style={
                "backgroundColor": "#0f172a",
                "border": "1px solid #1e293b",
                "borderRadius": "14px",
                "padding": "2rem",
                "marginBottom": "2rem"
            },
            children=[
                # Automatically Selected Demonstration Pair Badge
                html.Div(
                    id="demo-badge",
                    children="★ Automatically Selected Demonstration Pair",
                    title="This pair was automatically selected during preprocessing as one of the highest subtype-separating gene pairs within the variance-filtered dataset.",
                    style={
                        "backgroundColor": "#3b82f612",
                        "color": "#3b82f6",
                        "border": "1px solid #3b82f625",
                        "borderRadius": "6px",
                        "padding": "6px 12px",
                        "fontSize": "0.8rem",
                        "fontWeight": "600",
                        "display": "inline-block",
                        "marginBottom": "1rem",
                        "textTransform": "uppercase",
                        "letterSpacing": "0.05em",
                        "cursor": "help"
                    }
                ),
                dcc.Graph(
                    id="contour-plot",
                    config={"displayModeBar": True, "responsive": True}
                )
            ]
        ),
        
        # Statistics Panel Area
        html.Div(
            style={
                "display": "grid",
                "gridTemplateColumns": "repeat(auto-fit, minmax(320px, 1fr))",
                "gap": "1.5rem"
            },
            children=[
                # Gene X Stats Card
                html.Div(
                    id="stats-card-x",
                    className="placeholder-card",
                    style={"minHeight": "auto", "border": "1px solid #1e293b", "padding": "1.75rem"},
                    children=[]
                ),
                # Gene Y Stats Card
                html.Div(
                    id="stats-card-y",
                    className="placeholder-card",
                    style={"minHeight": "auto", "border": "1px solid #1e293b", "padding": "1.75rem"},
                    children=[]
                ),
                # Gene Pair Quality Stats Card
                html.Div(
                    id="stats-card-quality",
                    className="placeholder-card",
                    style={"minHeight": "auto", "border": "1px solid #1e293b", "padding": "1.75rem"},
                    children=[]
                )
            ]
        )
    ])


def get_hotspots_layout() -> html.Div:
    """
    Returns the layout for the Chromosomal Hotspot & Cytoband Mapping panel.
    """
    # Create static options list for the chromosome dropdown
    chr_options = [{"label": "All Chromosomes", "value": "All"}] + \
                  [{"label": f"Chr {c}", "value": str(c)} for c in range(1, 23)] + \
                  [{"label": "Chr X", "value": "X"}, {"label": "Chr Y", "value": "Y"}]

    return html.Div([
        # Header Banner
        html.Div(
            className="welcome-banner",
            children=[
                html.H2("Chromosomal Hotspot & Cytoband Mapping", className="welcome-title"),
                html.P(
                    "Visualize the distribution and expression variance of the top 1000 genes "
                    "across the human genome. Select a chromosome to zoom in and click any gene "
                    "marker to analyze its molecular details.",
                    className="welcome-text"
                )
            ]
        ),
        
        # Main content grid
        html.Div(
            style={"display": "flex", "flexDirection": "row", "flexWrap": "wrap", "gap": "1.5rem"},
            children=[
                # Left Panel (Plot and Selector) - 70% width
                html.Div(
                    style={"flex": "2.3", "minWidth": "600px", "display": "flex", "flexDirection": "column", "gap": "1.5rem"},
                    children=[
                        # Controls
                        html.Div(
                            style={
                                "backgroundColor": "#0f172a", 
                                "border": "1px solid #1e293b",
                                "borderRadius": "14px", 
                                "padding": "1.5rem"
                            },
                            children=[
                                html.Label("Select Chromosome Track", style={"fontWeight": "600", "color": "#f8fafc", "marginBottom": "0.75rem", "display": "block"}),
                                dcc.Dropdown(
                                    id="hotspots-chr-selector",
                                    options=chr_options,
                                    value="All",
                                    clearable=False,
                                    style={"color": "#0b0f19", "maxWidth": "400px"}
                                )
                            ]
                        ),
                        # Plot Card
                        html.Div(
                            style={
                                "backgroundColor": "#0f172a",
                                "border": "1px solid #1e293b",
                                "borderRadius": "14px",
                                "padding": "1.5rem"
                            },
                            children=[
                                dcc.Graph(
                                    id="hotspots-plot",
                                    config={"displayModeBar": True, "responsive": True}
                                )
                            ]
                        )
                    ]
                ),
                # Right Panel (Gene Details Card) - 30% width
                html.Div(
                    style={"flex": "1", "minWidth": "300px"},
                    children=[
                        html.Div(
                            id="hotspots-details-card",
                            className="placeholder-card",
                            style={
                                "height": "100%", 
                                "border": "1px solid #1e293b", 
                                "padding": "2rem",
                                "backgroundColor": "#0f172a",
                                "minHeight": "400px"
                            },
                            children=[]
                        )
                    ]
                )
            ]
        )
    ])


def get_network_layout() -> html.Div:
    """
    Returns the layout for the Gene Interaction & Co-expression Network panel.
    """
    threshold_options = [
        {"label": "r ≥ 0.70 (Dense)", "value": 0.70},
        {"label": "r ≥ 0.75", "value": 0.75},
        {"label": "r ≥ 0.80 (Standard)", "value": 0.80},
        {"label": "r ≥ 0.85", "value": 0.85},
        {"label": "r ≥ 0.90 (Sparse)", "value": 0.90}
    ]
    
    return html.Div([
        # Header Banner
        html.Div(
            className="welcome-banner",
            children=[
                html.H2("Gene Interaction & Co-expression Network", className="welcome-title"),
                html.P(
                    "Explore co-expression networks among the top variance-filtered genes. "
                    "Select a correlation threshold to filter interactions and click a node to highlight "
                    "its direct neighbor co-expression pathways.",
                    className="welcome-text"
                )
            ]
        ),
        
        # Main content grid
        html.Div(
            style={"display": "flex", "flexDirection": "row", "flexWrap": "wrap", "gap": "1.5rem"},
            children=[
                # Left Panel (Plot and Controls) - 70% width
                html.Div(
                    style={"flex": "2.3", "minWidth": "600px", "display": "flex", "flexDirection": "column", "gap": "1.5rem"},
                    children=[
                        # Controls Card
                        html.Div(
                            style={
                                "backgroundColor": "#0f172a", 
                                "border": "1px solid #1e293b",
                                "borderRadius": "14px", 
                                "padding": "1.5rem"
                            },
                            children=[
                                html.Label("Select Pearson Correlation Threshold (r)", style={"fontWeight": "600", "color": "#f8fafc", "marginBottom": "0.75rem", "display": "block"}),
                                dcc.Dropdown(
                                    id="network-threshold-selector",
                                    options=threshold_options,
                                    value=0.80,
                                    clearable=False,
                                    style={"color": "#0b0f19", "maxWidth": "400px"}
                                )
                            ]
                        ),
                        # Plot Card
                        html.Div(
                            style={
                                "backgroundColor": "#0f172a",
                                "border": "1px solid #1e293b",
                                "borderRadius": "14px",
                                "padding": "1.5rem"
                            },
                            children=[
                                dcc.Graph(
                                    id="network-plot",
                                    config={"displayModeBar": True, "responsive": True},
                                    style={"height": "650px"}
                                )
                            ]
                        )
                    ]
                ),
                # Right Panel (Gene/Node Details Card) - 30% width
                html.Div(
                    style={"flex": "1", "minWidth": "300px"},
                    children=[
                        html.Div(
                            id="network-details-card",
                            className="placeholder-card",
                            style={
                                "height": "100%", 
                                "border": "1px solid #1e293b", 
                                "padding": "2rem",
                                "backgroundColor": "#0f172a",
                                "minHeight": "400px"
                            },
                            children=[]
                        )
                    ]
                )
            ]
        )
    ])
