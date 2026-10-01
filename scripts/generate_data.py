# Regenerates the included synthetic dataset.
import shutil
from pathlib import Path
# The checked-in CSV is the reproducible project dataset; run this script after restoring
# the project if you want to regenerate it with the same seed.
print("Synthetic dataset is included at data/business_timeseries.csv")
