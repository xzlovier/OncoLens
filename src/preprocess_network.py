"""
Offline Preprocessing Utility to Compute Co-Expression Network Edges.

This utility loads the top-1000 variance-filtered gene dataset, computes pairwise
Pearson correlations, retains all strong positive co-expression relationships,
resolves their annotations, and saves the edge list to the processed data directory.
"""

import time
import pandas as pd
import numpy as np
from pathlib import Path

from src.config import (
    PROCESSED_DATA_DIR,
    TOP_GENE_COUNT
)

def main():
    start_time = time.time()
    
    path_expression = PROCESSED_DATA_DIR / f"brain_top{TOP_GENE_COUNT}.csv"
    path_annotated = PROCESSED_DATA_DIR / f"brain_top{TOP_GENE_COUNT}_annotated.csv"
    path_variance = PROCESSED_DATA_DIR / "gene_variance_ranking.csv"
    path_output = PROCESSED_DATA_DIR / "gene_network_edges.csv"
    
    print("=" * 80)
    print("GENE CO-EXPRESSION NETWORK PREPROCESSING UTILITY")
    print("=" * 80)
    
    # 1. Verify existence of required source datasets
    for p in [path_expression, path_annotated, path_variance]:
        if not p.exists():
            raise FileNotFoundError(f"Missing required preprocessing input dataset: {p}")
            
    # 2. Load expressions, annotations, and variance rankings
    print(f" -> Loading patient expressions : {path_expression.name}...")
    df_expr = pd.read_csv(path_expression)
    
    print(f" -> Loading annotations         : {path_annotated.name}...")
    df_annot = pd.read_csv(path_annotated)
    
    print(f" -> Loading variance rankings   : {path_variance.name}...")
    df_rank = pd.read_csv(path_variance)
    
    # Pre-merge rankings directly into annotated dataframe for simplified mapping
    df_rank["Rank"] = df_rank.index + 1
    df_annot_merged = df_annot.merge(df_rank, on="ProbeID", how="left")
    
    # 3. Compute Pearson correlation matrix
    print(" -> Computing pairwise Pearson correlations...")
    # Drop sample metadata columns to isolate gene expression values
    df_genes = df_expr.drop(columns=["samples", "type"])
    corr_matrix = df_genes.corr(method="pearson")
    
    # 4. Extract upper triangle index coordinates meeting threshold (correlation >= 0.70)
    # 0.70 is chosen to support all options (0.70, 0.75, 0.80, 0.85, 0.90) in the dashboard controls
    threshold = 0.70
    print(f" -> Extracting upper-triangle co-expression edges (correlation >= {threshold})...")
    
    upper_tri_mask = np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
    edges_mask = (corr_matrix.values >= threshold) & upper_tri_mask
    row_idx, col_idx = np.where(edges_mask)
    
    probe_x = corr_matrix.index[row_idx]
    probe_y = corr_matrix.columns[col_idx]
    correlations = corr_matrix.values[row_idx, col_idx]
    
    # 5. Build raw edges dataframe
    df_edges = pd.DataFrame({
        "Probe X": probe_x,
        "Probe Y": probe_y,
        "Correlation": correlations
    })
    
    # 6. Map annotations for Gene X
    print(" -> Mapping genomic annotations and co-expression metadata...")
    df_edges = df_edges.merge(
        df_annot_merged[["ProbeID", "Gene Symbol", "Rank", "Chromosome"]],
        left_on="Probe X",
        right_on="ProbeID",
        how="left"
    ).rename(columns={
        "Gene Symbol": "Gene X",
        "Rank": "Variance Rank X",
        "Chromosome": "Chromosome X"
    }).drop(columns=["ProbeID"])
    
    # 7. Map annotations for Gene Y
    df_edges = df_edges.merge(
        df_annot_merged[["ProbeID", "Gene Symbol", "Rank", "Chromosome"]],
        left_on="Probe Y",
        right_on="ProbeID",
        how="left"
    ).rename(columns={
        "Gene Symbol": "Gene Y",
        "Rank": "Variance Rank Y",
        "Chromosome": "Chromosome Y"
    }).drop(columns=["ProbeID"])
    
    # 8. Reorder and clean columns
    df_edges = df_edges[[
        "Gene X", "Probe X",
        "Gene Y", "Probe Y",
        "Correlation",
        "Variance Rank X", "Variance Rank Y",
        "Chromosome X", "Chromosome Y"
    ]]
    
    # 9. Save edge list to CSV
    print(f" -> Saving co-expression edge list ({len(df_edges)} edges) to: {path_output.name}...")
    df_edges.to_csv(path_output, index=False)
    
    runtime = time.time() - start_time
    print("-" * 80)
    print("Preprocessing Completed Successfully!")
    print(f"Total Edges Extracted : {len(df_edges)}")
    print(f"Correlation Bound     : >= {threshold}")
    print(f"Total Runtime         : {runtime:.2f} seconds")
    print("=" * 80)

if __name__ == "__main__":
    main()
