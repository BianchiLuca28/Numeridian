# Meridian - Real-Yield Portfolio Intelligence

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Project Overview

**Meridian** is a modular, quantitative financial intelligence platform designed to provide "true" investment insights that standard trackers miss. Built as a **Data Engineering showcase**, it prioritizes robust ETL pipelines, data accuracy, and scalable architecture.

### The Core Problem

Most portfolio backtesting tools show nominal returns (e.g., "+20%"), completely ignoring the devaluation of currency through inflation. A 20% gain during a period of 15% inflation is really only a 5% real gain in purchasing power.

### The Solution (MVP)

Meridian calculates and visualizes the **Inflation-Adjusted Return** (Real Yield) of user-defined portfolios, benchmarking against:
- S&P 500 performance
- CPI (Consumer Price Index) / Inflation data

**Key Insight**: See your "Paper Wealth" vs. your "Real Purchasing Power"

---

## 🏗️ Architecture

### Design Philosophy
- **Modular Monolith**: Clean separation of concerns, ready for future microservices
- **Data Engineering First**: Focus on robust ETL pipelines over UI animations
- **Extensibility**: Designed to accommodate future modules (sentiment analysis, macro-regime detection, etc.)

### Tech Stack
- **Language**: Python 3.9+
- **Frontend**: Streamlit (rapid data visualization)
- **Data Processing**: Pandas (time-series analysis)
- **Storage**: SQLite (lightweight local database)
- **Data Sources**: yfinance, pandas-datareader (FRED API)
- **Visualization**: Plotly

---

## 📁 Project Structure

```
Numeridian/
├── data/                   # Local storage (SQLite DB, raw CSVs)
├── src/
│   ├── loaders/            # Data fetching (ETL: Extract)
│   ├── processors/         # Data cleaning/merging (ETL: Transform)
│   ├── engine/             # Financial calculations (backtesting logic)
│   └── dashboard/          # Streamlit UI components
├── tests/                  # Unit and integration tests
├── pyproject.toml          # Project metadata and dependencies (PEP 621)
├── requirements.txt        # Core dependencies
├── .python-version         # Python version specification
└── README.md              # This file
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/BianchiLuca28/Numeridian.git
   cd Numeridian
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Or for development mode with testing tools:
   ```bash
   pip install -e ".[dev]"
   ```

### Running the Application

*Coming soon - Streamlit dashboard in development*

---

## 🎓 Core Concepts

### Real Yield Calculation

The platform addresses the **Frequency Mismatch Problem**:
- **Stock data**: Daily OHLCV (Open, High, Low, Close, Volume)
- **Inflation data**: Monthly CPI values

**Solution**: Interpolation and forward-filling techniques to align time series

**Formula**:
```
Real Return = Nominal Return - Inflation Rate
```

All asset prices are normalized to a base value (100) at the portfolio start date for fair comparison.

---

## 🗺️ Roadmap

### Version 1.0 (MVP) - Current Focus
- [x] Project scaffolding
- [ ] Stock data loader (yfinance integration)
- [ ] Inflation data loader (FRED API integration)
- [ ] Time-series alignment processor
- [ ] Portfolio backtesting engine
- [ ] Interactive Streamlit dashboard

### Future Modules
- **Sentiment Engine**: NLP analysis of financial news
- **Macro-Regime Classifier**: Economic environment detection (recession vs. boom)
- **Whale Watcher**: Institutional money flow tracking
- **Tax-Adjusted Returns**: Real-world after-tax calculations

---

## 🧪 Development

### Running Tests
```bash
pytest
```

### Code Quality
```bash
# Format code
black src/ tests/

# Lint code
ruff src/ tests/

# Type checking
mypy src/
```

---

## 📊 Use Cases

1. **Realistic Portfolio Planning**: Understand true purchasing power growth
2. **Historical Analysis**: Compare different asset allocations across inflationary periods
3. **Retirement Planning**: Ensure your nest egg keeps pace with cost of living
4. **Investment Education**: Visualize the impact of inflation on wealth

---

## 🤝 Contributing

Contributions are welcome! This project follows professional data engineering practices:
- Write clean, modular code
- Include unit tests for new features
- Update documentation as needed
- Follow the existing code style (enforced by Black and Ruff)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Data Sources**: Yahoo Finance (yfinance), Federal Reserve Economic Data (FRED)
- **Inspiration**: The need for honest financial metrics in an inflationary world

---

**Status**: 🚧 Active Development - MVP in Progress