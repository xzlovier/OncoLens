"""
Configuration Settings Module for OncoLens.

This module automatically resolves the project root directory and defines all essential
path constants using pathlib.Path. It also specifies global hyperparameters and metadata
column definitions for the data processing pipelines and visual analytics dashboard.
"""

from pathlib import Path

# ==============================================================================
# Path Configurations
# ==============================================================================

# Automatically resolve the project root directory (parent of src/)
PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent

# Define main subdirectory paths
DATA_DIR: Path = PROJECT_ROOT / "data"
RAW_DATA_DIR: Path = DATA_DIR / "raw"
PROCESSED_DATA_DIR: Path = DATA_DIR / "processed"
NOTEBOOKS_DIR: Path = PROJECT_ROOT / "notebooks"
APP_DIR: Path = PROJECT_ROOT / "app"
SRC_DIR: Path = PROJECT_ROOT / "src"

# Specific file paths
RAW_DATASET_PATH: Path = RAW_DATA_DIR / "Brain_GSE50161.csv"

# ==============================================================================
# Pipeline & Model Constants
# ==============================================================================

# Feature selection variance threshold hyperparameter
TOP_GENE_COUNT: int = 1000

# Target classification label column
TARGET_COLUMN: str = "type"

# ==============================================================================
# Directory Setup Initialization
# ==============================================================================

# Ensure data directories exist
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

# ==============================================================================
# Verification Entry Point
# ==============================================================================

if __name__ == "__main__":
    print("======================================================================")
    print("OncoLens Configuration Verification")
    print("======================================================================")
    print(f"PROJECT_ROOT       : {PROJECT_ROOT}")
    print(f"DATA_DIR           : {DATA_DIR}")
    print(f"RAW_DATA_DIR       : {RAW_DATA_DIR}")
    print(f"PROCESSED_DATA_DIR : {PROCESSED_DATA_DIR}")
    print(f"NOTEBOOKS_DIR      : {NOTEBOOKS_DIR}")
    print(f"APP_DIR            : {APP_DIR}")
    print(f"SRC_DIR            : {SRC_DIR}")
    print(f"RAW_DATASET_PATH   : {RAW_DATASET_PATH}")
    print("-" * 70)
    print(f"TOP_GENE_COUNT     : {TOP_GENE_COUNT}")
    print(f"TARGET_COLUMN      : '{TARGET_COLUMN}'")
    print("======================================================================")
    print("Path directories exist verification:")
    print(f" - Raw data dir exists      : {RAW_DATA_DIR.exists()}")
    print(f" - Processed data dir exists: {PROCESSED_DATA_DIR.exists()}")
    print(f" - Raw dataset file exists  : {RAW_DATASET_PATH.exists()}")
    print("======================================================================")
