# Contributing to GitHub Repos Collector

First off, thank you for considering contributing to GitHub Repos Collector! It's people like you that make this tool better for everyone.

## 🚀 Quick Start

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/github-repos-collector.git`
3. Create a branch: `git checkout -b feature/amazing-feature`
4. Make your changes
5. Run tests: `pytest`
6. Commit: `git commit -m 'Add amazing feature'`
7. Push: `git push origin feature/amazing-feature`
8. Open a Pull Request

## 📋 Development Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Git

### Installation

```bash
# Clone your fork
git clone https://github.com/yourusername/github-repos-collector.git
cd github-repos-collector

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest pytest-cov black flake8 isort
```

## 🧪 Running Tests

We use pytest for testing. All tests must pass before a PR can be merged.

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_app.py

# Run specific test
pytest tests/test_app.py::TestConverterData::test_converter_data_valida

# View coverage report
# Open htmlcov/index.html in your browser
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files as `test_*.py`
- Name test functions as `test_*`
- Use descriptive test names
- Aim for high code coverage (>80%)

Example:

```python
def test_filtrar_por_estrelas_com_minimo():
    """Testa filtragem por número mínimo de estrelas"""
    repos = [
        {'nome': 'repo1', 'estrelas': 1000},
        {'nome': 'repo2', 'estrelas': 50}
    ]
    resultado = filtrar_por_estrelas(repos, min_estrelas=100)
    assert len(resultado) == 1
    assert resultado[0]['estrelas'] >= 100
```

## 🎨 Code Style

We follow PEP 8 style guide with some modifications.

### Formatting

```bash
# Format code with black
black app.py tests/

# Check formatting
black --check app.py tests/
```

### Linting

```bash
# Run flake8
flake8 app.py tests/

# Check specific file
flake8 app.py
```

### Import Sorting

```bash
# Sort imports with isort
isort app.py tests/

# Check import sorting
isort --check-only app.py tests/
```

## 📝 Commit Messages

Write clear and meaningful commit messages:

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests when relevant

Examples:
```
Add filter by repository language
Fix cache loading bug when file is empty
Update README with new examples
```

## 🔀 Pull Request Process

1. **Update documentation** - If you add features, update README.md and docs/
2. **Add tests** - New features should include tests
3. **Run tests** - Ensure all tests pass
4. **Update CHANGELOG** - Add your changes to docs/CHANGELOG.md
5. **One feature per PR** - Keep PRs focused on a single feature or fix
6. **Describe your changes** - Write a clear PR description

### PR Checklist

- [ ] Tests pass locally
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] CHANGELOG updated
- [ ] No merge conflicts
- [ ] Descriptive PR title and description

## 🐛 Reporting Bugs

### Before Submitting

- Check if the bug has already been reported
- Try to reproduce with the latest version
- Collect relevant information (OS, Python version, error messages)

### Bug Report Template

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce:
1. Run command '...'
2. Enter input '...'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
- OS: [e.g. Windows 10, Ubuntu 20.04]
- Python version: [e.g. 3.9.5]
- App version: [e.g. 2.0.0]

**Additional context**
Any other relevant information.
```

## 💡 Suggesting Features

We love feature suggestions! Please:

1. Check if the feature has already been suggested
2. Explain the use case clearly
3. Describe the expected behavior
4. Consider implementation complexity

### Feature Request Template

```markdown
**Is your feature request related to a problem?**
A clear description of the problem.

**Describe the solution you'd like**
What you want to happen.

**Describe alternatives you've considered**
Other solutions you've thought about.

**Additional context**
Any other relevant information.
```

## 📚 Documentation

Good documentation is crucial:

- Update README.md for user-facing changes
- Update docs/ for detailed documentation
- Add docstrings to new functions
- Include examples when helpful

### Docstring Format

```python
def function_name(param1, param2):
    """Brief description of function.
    
    Longer description if needed.
    
    Args:
        param1 (type): Description of param1.
        param2 (type): Description of param2.
    
    Returns:
        type: Description of return value.
    
    Raises:
        ExceptionType: When this exception is raised.
    """
    pass
```

## 🌍 Internationalization

We support multiple languages:

- English (primary) - README.md
- Portuguese - docs/ folder

When adding features:
- Update English documentation first
- Update Portuguese documentation if possible
- Mark untranslated sections clearly

## 🔒 Security

If you discover a security vulnerability:

1. **DO NOT** open a public issue
2. Email the maintainers directly
3. Include detailed information
4. Allow time for a fix before disclosure

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all.

### Our Standards

**Positive behavior:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community

**Unacceptable behavior:**
- Trolling, insulting/derogatory comments
- Public or private harassment
- Publishing others' private information
- Other conduct which could reasonably be considered inappropriate

## ❓ Questions?

- Open an issue with the "question" label
- Check existing issues and documentation first
- Be specific and provide context

## 🎉 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing! 🙏

---

**Happy Coding!** 💻
