# Examples Directory

This directory contains example scripts demonstrating the usage of Meridian modules.

## Running Examples

Make sure you have installed the project dependencies first:

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

Then run any example:

```bash
python examples/fetch_stock_data.py
```

## Available Examples

### fetch_stock_data.py
Demonstrates how to use the `StockDataLoader` class to:
- Fetch historical OHLCV data for individual stocks
- Retrieve adjusted close prices for multiple stocks
- Get S&P 500 index data

**Note:** This example requires internet access to fetch data from Yahoo Finance.

## Network Requirements

The examples that fetch external data (stock prices, inflation data) require:
- Active internet connection
- Access to Yahoo Finance API (for stock data)
- Access to FRED API (for inflation data, when implemented)

In restricted network environments, the API calls may fail. The unit tests use mocked data to avoid this dependency.
