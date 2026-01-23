# 🔍 GitHub Repos Collector

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/yourusername/github-repos-collector/workflows/Tests/badge.svg)](https://github.com/yourusername/github-repos-collector/actions)
[![Lint](https://github.com/yourusername/github-repos-collector/workflows/Lint/badge.svg)](https://github.com/yourusername/github-repos-collector/actions)
[![codecov](https://codecov.io/gh/yourusername/github-repos-collector/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/github-repos-collector)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A powerful and user-friendly tool to collect, filter, and export GitHub repository information.

## ✨ Features

- 🎨 **Interactive Menu** - No command-line knowledge required
- 📊 **Multiple Export Formats** - CSV (Excel-ready) and JSON
- 🔍 **Advanced Filters** - Filter by date, stars, and more
- 💾 **Smart Caching** - Avoid repeated API calls
- 🌈 **Colorful Interface** - Beautiful terminal UI
- 🚀 **Fast & Efficient** - Collect hundreds of repos in seconds
- 📈 **Progress Bars** - Real-time feedback with visual progress indicators (NEW in v2.1.0)
- ⏱️ **Time Estimates** - Know exactly how long operations will take (NEW in v2.1.0)
- 🔔 **Rate Limit Monitoring** - Track GitHub API usage in real-time (NEW in v2.1.0)

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/github-repos-collector.git
cd github-repos-collector

# Install dependencies
pip install -r requirements.txt
```

### Usage

#### Interactive Mode (Recommended)

Simply run without arguments:

```bash
python app.py
```

The program will guide you through:
1. Choose programming language
2. Select sorting criteria
3. Set number of pages to fetch
4. Apply filters (optional)
5. Export results

#### Command Line Mode

```bash
# Basic search
python app.py --linguagem=Python --num-paginas=2

# With filters
python app.py --linguagem=JavaScript --dias=7 --min-estrelas=100

# With export
python app.py --linguagem=Python --exportar=csv --usar-cache
```

## 📖 Documentation

- 🇧🇷 **Portuguese Documentation**: See [docs/](docs/) folder for complete documentation in Portuguese
- 📚 **Quick Start Guide**: [docs/COMECE_AQUI.md](docs/COMECE_AQUI.md)
- 📝 **Examples**: [docs/EXEMPLOS.md](docs/EXEMPLOS.md)
- 📋 **Changelog**: [docs/CHANGELOG.md](docs/CHANGELOG.md)

## 🎯 Use Cases

### For Recruiters
Find popular projects in specific languages and export to Excel for analysis.

```bash
python app.py --linguagem=Python --ordenacao=stars --exportar=csv
```

### For Developers
Discover recent and trending projects.

```bash
python app.py --linguagem=Rust --dias=30 --min-estrelas=500
```

### For Researchers
Collect large datasets for analysis.

```bash
python app.py --linguagem=Python --num-paginas=10 --exportar=ambos
```

## 📊 Command Line Options

| Option | Description | Example |
|--------|-------------|---------|
| `--linguagem` | Programming language | `--linguagem=Python` |
| `--ordenacao` | Sort criteria (stars/forks/updated) | `--ordenacao=stars` |
| `--num-paginas` | Number of pages (~30 repos per page) | `--num-paginas=3` |
| `--dias` | Filter repos created in last X days | `--dias=7` |
| `--min-estrelas` | Minimum number of stars | `--min-estrelas=100` |
| `--exportar` | Export format (csv/json/ambos) | `--exportar=csv` |
| `--usar-cache` | Use cached data | `--usar-cache` |
| `-i, --interativo` | Interactive menu mode | `-i` |

## 📁 Project Structure

```
github-repos-collector/
├── app.py                 # Main application
├── requirements.txt       # Python dependencies
├── LICENSE               # MIT License
├── README.md             # This file
├── .gitignore           # Git ignore rules
├── cache/               # Cached results (auto-created)
├── exports/             # Exported files (auto-created)
└── docs/                # Documentation (Portuguese)
    ├── COMECE_AQUI.md
    ├── GUIA_RAPIDO.md
    ├── EXEMPLOS.md
    └── ...
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Running Tests

```bash
# Install test dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run tests with coverage
pytest --cov=app --cov-report=html

# View coverage report
# Open htmlcov/index.html in your browser
```

### Code Quality

This project uses:
- **pytest** for testing
- **black** for code formatting
- **flake8** for linting
- **isort** for import sorting

```bash
# Format code
black app.py tests/

# Check linting
flake8 app.py

# Sort imports
isort app.py tests/
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Click](https://click.palletsprojects.com/) for CLI interface
- Uses [GitHub REST API](https://docs.github.com/en/rest) for data collection
- Inspired by the need for easy repository discovery

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Made with ❤️ by the community**
