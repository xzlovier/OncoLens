"""
OncoLens Configuration Module.

Stores configurable constants such as default genes for the
Interactive Virtual Expression Assayer.
"""

# Default genes for the Virtual Expression Assayer (Simulator Widget)
# C9orf24 (ProbeID: 229012_at)
# NACC2 (ProbeID: 212993_at)
# RAB31 (ProbeID: 217763_s_at)
DEFAULT_SIM_GENE_1 = "229012_at"
DEFAULT_SIM_GENE_2 = "212993_at"
DEFAULT_SIM_GENE_3 = "217763_s_at"

# Softmax temperature parameter for centroid distance conversion
SIMULATOR_TEMPERATURE = 20.0
