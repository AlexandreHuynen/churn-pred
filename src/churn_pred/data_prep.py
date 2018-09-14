import numpy as np
import pandas as pd
from pathlib import Path

from .constants import PKG_DIR


def read_data(dataset='train'):
    """Reading dataset"""

    file = PKG_DIR / 'data' / '{}.csv'.format(dataset)
    return pd.read_csv(file)

