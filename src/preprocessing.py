"""
Preprocessing Pipeline Module for OncoLens.

This module loads the raw transcriptomics dataset, separates clinical metadata from
numerical expression levels, computes gene-wise variance across samples, ranks genes,
selects the top variable features (based on TOP_GENE_COUNT), and saves the resulting
filtered datasets for downstream annotation and visual dashboard rendering.
"""

import time
from typing import Tuple, List, Optional
import pandas as pd
import numpy as np
from pathlib import Path

# Import configuration constants from src.config
from src.config import (
    RAW_DATASET_PATH,
    PROCESSED_DATA_DIR,
    TOP_GENE_COUNT,
    TARGET_COLUMN
)


def load_dataset() -> pd.DataFrame:
    """
    Loads the raw dataset using the path defined in the configuration.

    Returns:
        pd.DataFrame: Loaded raw dataset.
    """
    if not RAW_DATASET_PATH.exists():
        raise FileNotFoundError(f"Raw dataset not found at: {RAW_DATASET_PATH}")
    print(f"Loading raw dataset from {RAW_DATASET_PATH}...")
    df = pd.read_csv(RAW_DATASET_PATH)
    return df


def identify_columns(df: pd.DataFrame) -> Tuple[Optional[str], str, List[str]]:
    """
    Identifies and separates the metadata columns from the numeric gene expression columns.

    Args:
        df (pd.DataFrame): The raw input DataFrame.

    Returns:
        Tuple[Optional[str], str, List[str]]:
            - sample_column: Name of the sample identifier column (if present, e.g., "samples").
            - target_column: Name of the classification target column.
            - gene_columns: List of gene expression column names.
    """
    # Look for sample identifier columns
    sample_column: Optional[str] = None
    possible_sample_cols = ["samples", "sample", "id", "sample_id"]
    for col in possible_sample_cols:
        if col in df.columns:
            sample_column = col
            break

    # Resolve target column
    target_column: str = TARGET_COLUMN
    if target_column not in df.columns:
        raise ValueError(f"Configured target column '{target_column}' not found in the dataset.")

    # Exclude metadata columns to collect all gene expression columns
    metadata_cols = {target_column}
    if sample_column is not None:
        metadata_cols.add(sample_column)

    gene_columns: List[str] = [col for col in df.columns if col not in metadata_cols]

    return sample_column, target_column, gene_columns


def compute_gene_variance(df: pd.DataFrame, gene_columns: List[str]) -> pd.DataFrame:
    """
    Computes variance for every gene column.

    Args:
        df (pd.DataFrame): The raw input DataFrame.
        gene_columns (List[str]): List of gene expression column names to calculate variance for.

    Returns:
        pd.DataFrame: A DataFrame containing 'ProbeID' and 'Variance' columns.
    """
    print(f"Computing variance for {len(gene_columns)} gene expression columns...")
    
    # Select only numeric gene columns and calculate variance efficiently
    variances = df[gene_columns].var(axis=0)
    
    # Create the output dataframe
    variance_df = pd.DataFrame({
        "ProbeID": variances.index,
        "Variance": variances.values
    })
    
    return variance_df


def select_top_variable_genes(variance_df: pd.DataFrame) -> List[str]:
    """
    Sorts genes by variance in descending order and returns the top TOP_GENE_COUNT genes.

    Args:
        variance_df (pd.DataFrame): DataFrame containing 'ProbeID' and 'Variance' columns.

    Returns:
        List[str]: List of top variable ProbeIDs.
    """
    print(f"Selecting top {TOP_GENE_COUNT} variable genes...")
    top_genes_df = variance_df.sort_values(by="Variance", ascending=False).head(TOP_GENE_COUNT)
    return top_genes_df["ProbeID"].tolist()


def create_processed_dataframe(
    df: pd.DataFrame, 
    selected_genes: List[str], 
    sample_column: Optional[str], 
    target_column: str
) -> pd.DataFrame:
    """
    Builds a new DataFrame containing metadata columns and selected top variable gene expressions.

    Args:
        df (pd.DataFrame): The raw input DataFrame.
        selected_genes (List[str]): List of selected gene expression columns.
        sample_column (Optional[str]): Sample identifier column name.
        target_column (str): Target column name.

    Returns:
        pd.DataFrame: Processed filtered DataFrame.
    """
    # Build list of columns to extract in order
    cols_to_keep: List[str] = []
    if sample_column is not None:
        cols_to_keep.append(sample_column)
    
    cols_to_keep.append(target_column)
    cols_to_keep.extend(selected_genes)
    
    return df[cols_to_keep].copy()


def save_outputs(processed_df: pd.DataFrame, variance_df: pd.DataFrame) -> Tuple[Path, Path]:
    """
    Saves the processed outputs to files under the data/processed directory.

    Args:
        processed_df (pd.DataFrame): Filtered expression DataFrame.
        variance_df (pd.DataFrame): Gene-wise variance ranking DataFrame.

    Returns:
        Tuple[Path, Path]: Paths to the saved files (processed_path, variance_ranking_path).
    """
    # Construct output paths
    processed_path = PROCESSED_DATA_DIR / f"brain_top{TOP_GENE_COUNT}.csv"
    variance_ranking_path = PROCESSED_DATA_DIR / "gene_variance_ranking.csv"
    
    # Save files
    print(f"Saving processed expression dataset to: {processed_path}...")
    processed_df.to_csv(processed_path, index=False)
    
    print(f"Saving variance ranking dataset to: {variance_ranking_path}...")
    # Sort variance ranking descending for better readability
    variance_df_sorted = variance_df.sort_values(by="Variance", ascending=False)
    variance_df_sorted.to_csv(variance_ranking_path, index=False)
    
    return processed_path, variance_ranking_path


def main() -> None:
    """
    Executes the complete preprocessing pipeline.
    """
    start_time = time.time()
    
    # 1. Load the raw dataset
    df = load_dataset()
    
    # 2. Identify and separate column groups
    sample_col, target_col, gene_cols = identify_columns(df)
    original_gene_count = len(gene_cols)
    
    print(f"Identified Metadata:")
    print(f" - Sample ID column: {sample_col}")
    print(f" - Target column   : {target_col}")
    print(f" - Gene columns    : {original_gene_count} total columns")
    print("-" * 60)
    
    # 3. Compute gene expression variance
    variance_df = compute_gene_variance(df, gene_cols)
    
    # 4. Select top variable genes
    selected_genes = select_top_variable_genes(variance_df)
    selected_gene_count = len(selected_genes)
    
    # 5. Extract filtered columns into final dataframe
    processed_df = create_processed_dataframe(df, selected_genes, sample_col, target_col)
    
    # 6. Save dataframes to disk
    processed_file, ranking_file = save_outputs(processed_df, variance_df)
    
    # 7. Compute execution metadata & report metrics
    elapsed_time = time.time() - start_time
    reduction_pct = (1.0 - (selected_gene_count / original_gene_count)) * 100
    
    # Calculate total variance retained
    total_var_all = variance_df["Variance"].sum()
    top_variances = variance_df.sort_values(by="Variance", ascending=False).head(TOP_GENE_COUNT)["Variance"]
    total_var_top = top_variances.sum()
    variance_retained_pct = (total_var_top / total_var_all) * 100 if total_var_all > 0 else 0.0
    
    print("\n" + "=" * 60)
    print("ONCOLENS PREPROCESSING PIPELINE SUMMARY REPORT")
    print("=" * 60)
    print(f"Original Number of Genes: {original_gene_count}")
    print(f"Selected Number of Genes: {selected_gene_count}")
    print(f"Dimensionality Reduction: {reduction_pct:.2f}%")
    print(f"Variance Retained       : {variance_retained_pct:.2f}%")
    print(f"Processing Duration     : {elapsed_time:.3f} seconds")
    print(f"Processed Dataset Saved : {processed_file}")
    print(f"Variance Ranking Saved  : {ranking_file}")
    print("=" * 60)


if __name__ == "__main__":
    main()
