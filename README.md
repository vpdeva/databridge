
# DataBridge

DataBridge is an open-source Python library for handling data ingestion, transformation, analytics, and cloud integrations. It provides modular components for building scalable data workflows.

## Features
- File and API-based ingestion
- Data cleaning and transformation
- Time-series forecasting
- Integration with AWS S3

## Installation
Run the following command:
```
pip install .
```

## Usage
### Example: Ingest File
```python
from databridge.ingestion.file_ingestion import ingest_file

df = ingest_file("data.csv", "csv")
print(df.head())
```

### Example: Forecasting
```python
from databridge.analytics.forecasting import time_series_forecasting

data = [100, 120, 130, 150]
forecast = time_series_forecasting(data, look_back=2)
print(forecast)
```

## Contributing
Contributions are welcome! Please submit issues and pull requests on GitHub.
    