"""
Main Application Entry Point for OncoLens.

This module initializes the Dash server, loads all processed datasets (top 1000 expressions,
genomic annotations, patient Dysregulation Index ratings, and variance rankings) into memory
during server startup, binds layouts, and registers the application callbacks.
"""

import dash
import pandas as pd
from pathlib import Path
from app.layouts import create_layout
from app.callbacks import register_callbacks

# Import configuration settings
from src.config import (
    PROCESSED_DATA_DIR,
    TOP_GENE_COUNT
)

# ------------------------------------------------------------------------------
# 1. Dataset Path Definitions
# ------------------------------------------------------------------------------
PATH_EXPRESSION = PROCESSED_DATA_DIR / f"brain_top{TOP_GENE_COUNT}.csv"
PATH_ANNOTATED = PROCESSED_DATA_DIR / f"brain_top{TOP_GENE_COUNT}_annotated.csv"
PATH_PATIENT_DI = PROCESSED_DATA_DIR / "patient_DI.csv"
PATH_VARIANCE_RANKING = PROCESSED_DATA_DIR / "gene_variance_ranking.csv"

# ------------------------------------------------------------------------------
# 2. Server Startup Data Loading
# ------------------------------------------------------------------------------
print("======================================================================")
print("ONCOLENS SERVER STARTUP: Loading Processed Datasets...")
print("======================================================================")

if not PATH_EXPRESSION.exists():
    raise FileNotFoundError(f"Expression file not found at: {PATH_EXPRESSION}. Run preprocessing first.")
if not PATH_ANNOTATED.exists():
    raise FileNotFoundError(f"Annotated file not found at: {PATH_ANNOTATED}. Run annotation first.")
if not PATH_PATIENT_DI.exists():
    raise FileNotFoundError(f"Patient DI file not found at: {PATH_PATIENT_DI}. Run dysregulation calculations first.")
if not PATH_VARIANCE_RANKING.exists():
    raise FileNotFoundError(f"Variance ranking file not found at: {PATH_VARIANCE_RANKING}. Run preprocessing first.")

# Load datasets into memory
print(f" -> Loading preprocessed expressions: {PATH_EXPRESSION.name}...")
df_expression = pd.read_csv(PATH_EXPRESSION)

print(f" -> Loading genomic annotations    : {PATH_ANNOTATED.name}...")
df_annotated = pd.read_csv(PATH_ANNOTATED)

print(f" -> Loading patient DI ratings     : {PATH_PATIENT_DI.name}...")
df_patient_di = pd.read_csv(PATH_PATIENT_DI)

print(f" -> Loading gene variance rankings : {PATH_VARIANCE_RANKING.name}...")
df_variance_ranking = pd.read_csv(PATH_VARIANCE_RANKING)

print("-" * 70)
print(f"Successfully loaded {len(df_expression)} samples and {df_expression.shape[1] - 2} features.")
print(f"Genomic annotations mapped for {len(df_annotated)} genes.")
print(f"Patient Dysregulation Index loaded for {len(df_patient_di)} patients.")
print("======================================================================")

# ------------------------------------------------------------------------------
# 3. Dash Server Initialization
# ------------------------------------------------------------------------------
# Fetch Google Fonts (Outfit, Inter) for modern layout styling
external_stylesheets = [
    "https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap"
]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    title="OncoLens - Visual Analytics Dashboard"
)

# Bind structural layout grid
app.layout = create_layout()

# Register event router callbacks
register_callbacks(app)

# Expose server wrapper for production WSGI setups
server = app.server

# ------------------------------------------------------------------------------
# 4. Local Execution
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    # Start developmental local server
    app.run(debug=True, port=8050)
