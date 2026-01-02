"""
Example script demonstrating the Stock Data Loader

This script shows how to use the StockDataLoader class to fetch
historical stock price data.

Usage:
    python examples/fetch_stock_data.py
"""

import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.loaders.stock_loader import StockDataLoader, fetch_sp500_data


def main():
    """Demonstrate basic usage of the stock data loader"""
    
    print("=" * 60)
    print("Meridian - Stock Data Loader Example")
    print("=" * 60)
    print()
    
    # Example 1: Fetch data for a single stock
    print("Example 1: Fetching data for Apple (AAPL)")
    print("-" * 60)
    
    try:
        loader = StockDataLoader("AAPL", "2023-01-01", "2023-12-31")
        data = loader.fetch_data()
        
        if "AAPL" in data:
            df = data["AAPL"]
            print(f"✓ Successfully retrieved {len(df)} trading days of data")
            print(f"\nFirst 5 rows:")
            print(df.head())
            print(f"\nData columns: {', '.join(df.columns)}")
            
    except Exception as e:
        print(f"✗ Error: {str(e)}")
    
    print("\n")
    
    # Example 2: Fetch adjusted close prices for multiple stocks
    print("Example 2: Fetching adjusted close prices for a portfolio")
    print("-" * 60)
    
    try:
        tickers = ["AAPL", "MSFT", "GOOGL"]
        loader = StockDataLoader(tickers, "2023-01-01", "2023-12-31")
        adj_close = loader.fetch_adjusted_close()
        
        print(f"✓ Successfully retrieved data for {len(adj_close.columns)} stocks")
        print(f"\nFirst 5 rows of adjusted close prices:")
        print(adj_close.head())
        print(f"\nBasic statistics:")
        print(adj_close.describe())
        
    except Exception as e:
        print(f"✗ Error: {str(e)}")
    
    print("\n")
    
    # Example 3: Fetch S&P 500 index data
    print("Example 3: Fetching S&P 500 index data")
    print("-" * 60)
    
    try:
        sp500_data = fetch_sp500_data("2023-01-01", "2023-12-31")
        print(f"✓ Successfully retrieved {len(sp500_data)} trading days")
        print(f"\nS&P 500 summary:")
        print(f"  Start: {sp500_data['Close'].iloc[0]:.2f}")
        print(f"  End: {sp500_data['Close'].iloc[-1]:.2f}")
        print(f"  Change: {((sp500_data['Close'].iloc[-1] / sp500_data['Close'].iloc[0]) - 1) * 100:.2f}%")
        
    except Exception as e:
        print(f"✗ Error: {str(e)}")
    
    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
