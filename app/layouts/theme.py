"""
OncoLens Theme Constants.

Centralises all visual design tokens used across layout builders and callbacks.
Changing PLOT_TEMPLATE here switches every Plotly chart theme simultaneously.
"""

# ── Plotly chart template ─────────────────────────────────────────────────────
PLOT_TEMPLATE = "plotly_white"

# ── Page / surface colors ─────────────────────────────────────────────────────
COLOR_BG        = "#F5F7FA"   # Page background
COLOR_SURFACE   = "#FFFFFF"   # Card / panel background
COLOR_BORDER    = "#E5E7EB"   # Subtle borders
COLOR_BORDER_MED = "#D1D5DB"  # Medium borders

# ── Typography ────────────────────────────────────────────────────────────────
COLOR_TEXT_PRIMARY   = "#1F2937"   # Main body text
COLOR_TEXT_SECONDARY = "#6B7280"   # Muted labels
COLOR_TEXT_MUTED     = "#9CA3AF"   # Placeholder / disabled

# ── Accent palette ────────────────────────────────────────────────────────────
COLOR_ACCENT_PRIMARY   = "#2563EB"  # Primary blue
COLOR_ACCENT_SECONDARY = "#14B8A6"  # Teal
COLOR_ACCENT_WARN      = "#F59E0B"  # Amber
COLOR_ACCENT_DANGER    = "#EF4444"  # Red

# ── Plotly figure background / grid ──────────────────────────────────────────
PLOT_PAPER_BG = COLOR_SURFACE
PLOT_PLOT_BG  = "#FAFBFC"     # Very slight off-white inside axes
PLOT_GRID     = "#E5E7EB"
PLOT_ZEROLINE = "#D1D5DB"
PLOT_TICK_COLOR = COLOR_TEXT_SECONDARY
PLOT_TITLE_COLOR = COLOR_TEXT_PRIMARY
PLOT_AXIS_LABEL_COLOR = COLOR_TEXT_SECONDARY

# ── Clinical subtype palette ──────────────────────────────────────────────────
SUBTYPE_COLORS = {
    "normal":                "#10B981",   # Emerald
    "ependymoma":            "#3B82F6",   # Blue
    "glioblastoma":          "#EF4444",   # Crimson
    "medulloblastoma":       "#8B5CF6",   # Purple
    "pilocytic_astrocytoma": "#F59E0B",   # Amber
}
