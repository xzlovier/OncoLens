# OncoLens

OncoLens is a high-performance visual analytics system designed for multi-dimensional brain tumor characterization and genomic dysregulation mapping. Differentiating between distinct clinical pathologies is a fundamental challenge in computational biology and precision oncology. Using transcriptomic profiles, OncoLens compresses thousands of genetic dimensions into a highly interactive visual application that maps molecular and structural boundaries between healthy tissue and four aggressive forms of brain cancer: Ependymoma, Glioblastoma, Medulloblastoma, and Pilocytic Astrocytoma.

## Project Structure

The project directory structure is organized as follows:

```text
OncoLens/
│
├── data/
│   ├── raw/                 # Raw datasets (e.g., GSE50161 CSV profiles)
│   └── processed/           # Processed datasets (filtered, scaled, annotated profiles)
│
├── notebooks/
│   └── EDA.ipynb            # Phase 1 Exploratory Data Analysis notebook
│
├── src/                     # Core backend source modules
│   ├── __init__.py          # Source module package initialization
│   ├── preprocessing.py     # Variance filtering and dataset loading pipeline
│   ├── annotation.py        # Probe cross-referencing and cytoband mapping
│   ├── dysregulation.py     # Calculations for the patient-specific Dysregulation Index
│   ├── utils.py             # Reusable helper functions and statistical routines
│   └── config.py            # Global path configs, thresholds, and dashboard themes
│
├── app/                     # Frontend visualization files
│   ├── __init__.py          # Dash package initialization
│   ├── app.py               # Application entry point and server startup
│   ├── layouts.py           # Dashboard layout grids and UI components
│   └── callbacks.py         # Reactive callbacks for visual analytics components
│
├── assets/                  # CSS stylesheets, static images, and custom JS scripts
│
├── requirements.txt         # Production and development dependencies
├── README.md                # Project documentation and summary overview
└── .gitignore               # Ignored local files, cache, and large binaries
```

## Setup Instructions

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Place raw genomic profiles under `data/raw/`.
3. Open `notebooks/EDA.ipynb` to explore the initial dataset summaries.
