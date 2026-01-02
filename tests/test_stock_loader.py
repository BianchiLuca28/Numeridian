"""
Unit tests for Stock Data Loader

Tests the functionality of fetching stock data from Yahoo Finance.
Uses mock data where appropriate to avoid external API dependencies.
"""

import pytest
from datetime import datetime
from unittest.mock import Mock, patch
import pandas as pd

from src.loaders.stock_loader import StockDataLoader, fetch_sp500_data


class TestStockDataLoader:
    """Test suite for StockDataLoader class"""
    
    def test_initialization_single_ticker(self):
        """Test initialization with a single ticker string"""
        loader = StockDataLoader("AAPL", "2020-01-01", "2020-12-31")
        assert loader.tickers == ["AAPL"]
        assert loader.start_date == "2020-01-01"
        assert loader.end_date == "2020-12-31"
    
    def test_initialization_multiple_tickers(self):
        """Test initialization with multiple tickers"""
        tickers = ["AAPL", "MSFT", "GOOGL"]
        loader = StockDataLoader(tickers, "2020-01-01", "2020-12-31")
        assert loader.tickers == tickers
        
    def test_initialization_default_end_date(self):
        """Test that end_date defaults to today when not provided"""
        loader = StockDataLoader("AAPL", "2020-01-01")
        today = datetime.now().strftime("%Y-%m-%d")
        assert loader.end_date == today
    
    @patch('src.loaders.stock_loader.yf.Ticker')
    def test_fetch_single_ticker(self, mock_ticker):
        """Test fetching data for a single ticker"""
        # Create mock data
        mock_df = pd.DataFrame({
            'Open': [100, 101, 102],
            'High': [105, 106, 107],
            'Low': [99, 100, 101],
            'Close': [103, 104, 105],
            'Volume': [1000000, 1100000, 1200000],
            'Adj Close': [103, 104, 105]
        }, index=pd.date_range('2020-01-01', periods=3))
        
        # Configure mock
        mock_instance = Mock()
        mock_instance.history.return_value = mock_df
        mock_ticker.return_value = mock_instance
        
        loader = StockDataLoader("AAPL", "2020-01-01", "2020-01-03")
        result = loader._fetch_single_ticker("AAPL")
        
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 3
        assert isinstance(result.index, pd.DatetimeIndex)
    
    @patch('src.loaders.stock_loader.yf.Ticker')
    def test_fetch_data_success(self, mock_ticker):
        """Test successful data fetch for multiple tickers"""
        mock_df = pd.DataFrame({
            'Close': [100, 101, 102],
            'Adj Close': [100, 101, 102]
        }, index=pd.date_range('2020-01-01', periods=3))
        
        mock_instance = Mock()
        mock_instance.history.return_value = mock_df
        mock_ticker.return_value = mock_instance
        
        loader = StockDataLoader(["AAPL", "MSFT"], "2020-01-01", "2020-01-03")
        data = loader.fetch_data()
        
        assert len(data) == 2
        assert "AAPL" in data
        assert "MSFT" in data
        assert isinstance(data["AAPL"], pd.DataFrame)
    
    @patch('src.loaders.stock_loader.yf.Ticker')
    def test_fetch_data_no_valid_data(self, mock_ticker):
        """Test error handling when no valid data is retrieved"""
        mock_instance = Mock()
        mock_instance.history.return_value = pd.DataFrame()  # Empty DataFrame
        mock_ticker.return_value = mock_instance
        
        loader = StockDataLoader("INVALID", "2020-01-01", "2020-01-03")
        
        with pytest.raises(ValueError, match="Failed to retrieve data"):
            loader.fetch_data()
    
    @patch('src.loaders.stock_loader.yf.Ticker')
    def test_fetch_adjusted_close(self, mock_ticker):
        """Test fetching adjusted close prices"""
        mock_df = pd.DataFrame({
            'Close': [100, 101, 102],
            'Adj Close': [99, 100, 101]
        }, index=pd.date_range('2020-01-01', periods=3))
        
        mock_instance = Mock()
        mock_instance.history.return_value = mock_df
        mock_ticker.return_value = mock_instance
        
        loader = StockDataLoader(["AAPL", "MSFT"], "2020-01-01", "2020-01-03")
        adj_close = loader.fetch_adjusted_close()
        
        assert isinstance(adj_close, pd.DataFrame)
        assert list(adj_close.columns) == ["AAPL", "MSFT"]
        assert len(adj_close) == 3


class TestConvenienceFunctions:
    """Test convenience functions"""
    
    @patch('src.loaders.stock_loader.StockDataLoader')
    def test_fetch_sp500_data(self, mock_loader_class):
        """Test S&P 500 convenience function"""
        mock_df = pd.DataFrame({
            'Close': [3000, 3100, 3200]
        }, index=pd.date_range('2020-01-01', periods=3))
        
        mock_loader = Mock()
        mock_loader.fetch_data.return_value = {"^GSPC": mock_df}
        mock_loader_class.return_value = mock_loader
        
        result = fetch_sp500_data("2020-01-01", "2020-01-03")
        
        mock_loader_class.assert_called_once_with("^GSPC", "2020-01-01", "2020-01-03")
        assert isinstance(result, pd.DataFrame)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
