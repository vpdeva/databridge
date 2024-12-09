
def remove_duplicates(df):
    """
    Remove duplicate rows from the DataFrame.
    """
    return df.drop_duplicates()

def fill_missing_values(df, strategy='mean'):
    """
    Fill missing values using the specified strategy (mean, median, mode).
    """
    if strategy == 'mean':
        return df.fillna(df.mean())
    elif strategy == 'median':
        return df.fillna(df.median())
    elif strategy == 'mode':
        return df.fillna(df.mode().iloc[0])
    else:
        raise ValueError(f"Unsupported strategy: {strategy}")
            