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
    
    # Get all unique subtypes + "All" for cohort comparisons
    subtypes = ["All"] + sorted(df_expr["type"].unique().tolist())
    threshold = 0.70
    
    all_edges = []
    
    for subtype in subtypes:
        print(f" -> Processing cohort: {subtype}...")
        if subtype == "All":
            df_sub = df_expr
        else:
            df_sub = df_expr[df_expr["type"] == subtype]
            
        # 3. Compute Pearson correlation matrix
        # Exclude Affymetrix control probes (AFFX-*) — these are spike-in RNA controls,
        # not real human genes, and create biologically meaningless correlations
        df_genes = df_sub.drop(columns=["samples", "type"])
        df_genes = df_genes[[c for c in df_genes.columns if not c.startswith("AFFX-")]]
        corr_matrix = df_genes.corr(method="pearson")
        
        # 4. Extract upper triangle index coordinates meeting threshold (correlation >= 0.70)
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
        
        # Add Subtype column
        df_edges["Subtype"] = subtype
        
        # 8. Reorder and clean columns
        df_edges = df_edges[[
            "Subtype",
            "Gene X", "Probe X",
            "Gene Y", "Probe Y",
            "Correlation",
            "Variance Rank X", "Variance Rank Y",
            "Chromosome X", "Chromosome Y"
        ]]
        
        all_edges.append(df_edges)
        print(f"    - Extracted {len(df_edges)} co-expression edges.")
        
    # Concatenate all cohorts
    df_final_edges = pd.concat(all_edges, ignore_index=True)
    
    # 9. Save edge list to CSV
    print(f" -> Saving complete co-expression edge list ({len(df_final_edges)} edges) to: {path_output.name}...")
    df_final_edges.to_csv(path_output, index=False)
    
    runtime = time.time() - start_time
    print("-" * 80)
    print("Preprocessing Completed Successfully!")
    print(f"Total Edges Extracted Across Cohorts : {len(df_final_edges)}")
    print(f"Correlation Bound                    : >= {threshold}")
    print(f"Total Runtime                        : {runtime:.2f} seconds")
    print("=" * 80)

if __name__ == "__main__":
    main()
