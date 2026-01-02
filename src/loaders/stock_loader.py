"""
Stock Data Loader

Fetches historical stock price data using yfinance.
Provides OHLCV (Open, High, Low, Close, Volume) data for specified tickers.
"""

import logging
from datetime import datetime
from typing import Dict, List, Optional, Union

import pandas as pd
import yfinance as yf

# Configure module logger
logger = logging.getLogger(__name__)


class StockDataLoader:
    """
    Loads historical stock market data from Yahoo Finance.
    
    This class handles the extraction of daily OHLCV data for stocks,
    ETFs, and indices. It includes basic error handling and validation.
    
    Attributes:
        tickers (List[str]): List of stock ticker symbols to fetch
        start_date (str): Start date for historical data (YYYY-MM-DD)
        end_date (str): End date for historical data (YYYY-MM-DD)
    """
    
    def __init__(
        self,
        tickers: Union[str, List[str]],
        start_date: str,
        end_date: Optional[str] = None
    ):
        """
        Initialize the stock data loader.
        
        Args:
            tickers: Single ticker or list of ticker symbols (e.g., "AAPL" or ["AAPL", "MSFT"])
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format (defaults to today)
        """
        self.tickers = [tickers] if isinstance(tickers, str) else tickers
        self.start_date = start_date
        self.end_date = end_date or datetime.now().strftime("%Y-%m-%d")
        
    def fetch_data(self) -> Dict[str, pd.DataFrame]:
        """
        Fetch historical OHLCV data for all configured tickers.
        
        Returns:
            Dictionary mapping ticker symbols to their respective DataFrames.
            Each DataFrame contains columns: Open, High, Low, Close, Volume, Adj Close
            
        Raises:
            ValueError: If no valid data is retrieved for any ticker
        """
        data = {}
        
        for ticker in self.tickers:
            try:
                df = self._fetch_single_ticker(ticker)
                if not df.empty:
                    data[ticker] = df
                else:
                    logger.warning(f"No data retrieved for {ticker}")
            except Exception as e:
                logger.error(f"Error fetching data for {ticker}: {str(e)}")
                
        if not data:
            raise ValueError("Failed to retrieve data for any ticker")
            
        return data
    
    def _fetch_single_ticker(self, ticker: str) -> pd.DataFrame:
        """
        Fetch data for a single ticker symbol.
        
        Args:
            ticker: Stock ticker symbol
            
        Returns:
            DataFrame with OHLCV data
        """
        stock = yf.Ticker(ticker)
        df = stock.history(start=self.start_date, end=self.end_date)
        
        # Ensure the index is a DatetimeIndex
        if not isinstance(df.index, pd.DatetimeIndex):
            df.index = pd.to_datetime(df.index)
            
        return df
    
    def fetch_adjusted_close(self) -> pd.DataFrame:
        """
        Fetch only adjusted close prices for all tickers.
        
        This is useful for portfolio analysis where we primarily care
        about the adjusted close price (which accounts for splits and dividends).
        
        Returns:
            DataFrame with tickers as columns and dates as index
        """
        all_data = self.fetch_data()
        
        adj_close_data = {}
        for ticker, df in all_data.items():
            # Use 'Adj Close' if available, otherwise fall back to 'Close'
            if 'Adj Close' in df.columns:
                adj_close_data[ticker] = df['Adj Close']
            else:
                adj_close_data[ticker] = df['Close']
                
        return pd.DataFrame(adj_close_data)


def fetch_sp500_data(start_date: str, end_date: Optional[str] = None) -> pd.DataFrame:
    """
    Convenience function to fetch S&P 500 index data.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format (defaults to today)
        
    Returns:
        DataFrame with S&P 500 historical data
    """
    loader = StockDataLoader("^GSPC", start_date, end_date)
    data = loader.fetch_data()
    return data["^GSPC"]


if __name__ == "__main__":
    # Example usage
    print("Fetching sample stock data...")
    
    # Fetch data for a single stock
    loader = StockDataLoader("AAPL", "2020-01-01", "2023-12-31")
    data = loader.fetch_data()
    
    print(f"\nRetrieved data for: {list(data.keys())}")
    print(f"\nSample data for AAPL:")
    print(data["AAPL"].head())
    
    # Fetch adjusted close for multiple stocks
    multi_loader = StockDataLoader(["AAPL", "MSFT", "GOOGL"], "2020-01-01", "2023-12-31")
    adj_close = multi_loader.fetch_adjusted_close()
    
    print(f"\nAdjusted close prices (first 5 rows):")
    print(adj_close.head())
