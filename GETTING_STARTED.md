# Meridian Project Setup - Quick Start Guide

## 🎉 What Has Been Created

This repository now contains a professional Python project scaffolding for **Meridian**, a quantitative financial intelligence platform. The setup follows modern Python best practices and is ready for development.

## 📦 Project Structure

```
Numeridian/
├── data/                      # Local storage (databases, CSVs)
│   └── .gitkeep              # Keeps directory in git
├── examples/                  # Usage examples
│   ├── README.md             # Examples documentation
│   └── fetch_stock_data.py   # Stock loader demo
├── src/                       # Main source code
│   ├── loaders/              # Data extraction (ETL: Extract)
│   │   ├── __init__.py
│   │   └── stock_loader.py   # ✅ Yahoo Finance integration
│   ├── processors/           # Data transformation (ETL: Transform)
│   ├── engine/               # Financial calculations
│   ├── dashboard/            # Streamlit UI components
│   └── __init__.py
├── tests/                     # Unit tests
│   ├── __init__.py
│   └── test_stock_loader.py  # ✅ 8 tests, 76% coverage
├── .gitignore                 # Excludes venv, __pycache__, data files
├── .python-version            # Python 3.9 requirement
├── pyproject.toml             # Project metadata & config
├── requirements.txt           # Dependencies
└── README.md                  # Full project documentation
```

## 🚀 Getting Started

### 1. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate          # On macOS/Linux
# OR
venv\Scripts\activate             # On Windows
```

### 2. Install Dependencies

```bash
# Install core dependencies
pip install -r requirements.txt

# For development (testing, linting, formatting)
pip install -e ".[dev]"
```

### 3. Verify Installation

```bash
# Run tests
pytest

# Check code formatting
black --check src/ tests/

# Lint code
ruff src/ tests/
```

## 🧩 What's Implemented

### ✅ Stock Data Loader (`src/loaders/stock_loader.py`)

**Features:**
- Fetch historical OHLCV data from Yahoo Finance
- Support for single or multiple tickers
- Adjusted close price aggregation
- S&P 500 convenience function
- Proper error handling and logging

**Usage Example:**
```python
from src.loaders.stock_loader import StockDataLoader

# Fetch single stock
loader = StockDataLoader("AAPL", "2023-01-01", "2023-12-31")
data = loader.fetch_data()

# Fetch multiple stocks
loader = StockDataLoader(["AAPL", "MSFT", "GOOGL"], "2023-01-01")
adj_close = loader.fetch_adjusted_close()
```

### ✅ Comprehensive Testing

- 8 unit tests for stock loader
- Mock data to avoid external API dependencies
- 76% code coverage
- All tests passing ✓

### ✅ Professional Configuration

**pyproject.toml includes:**
- Project metadata (name, version, description)
- Dependency management
- Tool configurations:
  - **Black**: Code formatting (line length: 100)
  - **Ruff**: Fast Python linting
  - **MyPy**: Type checking
  - **Pytest**: Testing with coverage

## 📖 Documentation

- **README.md**: Comprehensive project overview, architecture, and roadmap
- **examples/README.md**: How to run example scripts
- **Docstrings**: All classes and functions documented

## 🔧 Development Tools

### Code Formatting
```bash
# Format code
black src/ tests/

# Check formatting (no changes)
black --check src/ tests/
```

### Linting
```bash
# Run linter
ruff src/ tests/
```

### Type Checking
```bash
# Check types
mypy src/
```

### Testing
```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_stock_loader.py -v
```

## 🗺️ Next Steps (Development Roadmap)

### Phase 1: Data Loading (Current)
- [x] Stock data loader (yfinance)
- [ ] Inflation data loader (FRED API)
- [ ] Data persistence (SQLite)

### Phase 2: Data Processing
- [ ] Time-series alignment (daily stock + monthly CPI)
- [ ] Price normalization (base 100)
- [ ] Data validation and cleaning

### Phase 3: Financial Engine
- [ ] Portfolio backtesting logic
- [ ] Real yield calculation (nominal - inflation)
- [ ] Performance metrics

### Phase 4: Visualization
- [ ] Streamlit dashboard
- [ ] Interactive charts (Plotly)
- [ ] User input forms

## 🎯 MVP Goal

**Real-Yield Portfolio Backtester:**
- User selects assets, weights, time range
- System fetches stock + inflation data
- Calculates inflation-adjusted returns
- Visualizes "Paper Wealth" vs "Real Purchasing Power"
- Benchmarks against S&P 500

## 📚 Key Technologies

- **Python 3.9+**: Core language
- **Pandas**: Time-series data manipulation
- **yfinance**: Stock market data
- **pandas-datareader**: Economic data (FRED)
- **Streamlit**: Web dashboard
- **Plotly**: Interactive charts
- **SQLite**: Local database
- **Pytest**: Testing framework

## 🤝 Contributing

1. Create a feature branch
2. Write code following existing style (Black formatting)
3. Add unit tests for new functionality
4. Ensure all tests pass: `pytest`
5. Update documentation as needed

## 📞 Support

- Check `README.md` for full project documentation
- Review `examples/` for usage patterns
- Run `pytest -v` to see test examples

---

**Status**: ✅ Scaffolding Complete - Ready for Development

**Next Immediate Task**: Implement inflation data loader for FRED API
