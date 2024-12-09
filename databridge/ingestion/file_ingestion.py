
import pandas as pd

def ingest_file(file_path, file_type='csv'):
    """
    Load a file into a pandas DataFrame.
    Supports CSV, JSON, and Parquet formats.
    """
    if file_type == 'csv':
        return pd.read_csv(file_path)
    elif file_type == 'json':
        return pd.read_json(file_path)
    elif file_type == 'parquet':
        return pd.read_parquet(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")
            