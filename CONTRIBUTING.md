# Contributing to Claude-Codex-Duo

Thank you for your interest in contributing to Claude-Codex-Duo! This document provides guidelines for contributing to this project.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## How to Contribute

### Reporting Issues

1. Check existing issues to avoid duplicates
2. Use a clear, descriptive title
3. Provide steps to reproduce the issue
4. Include your Python version and OS

### Submitting Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Write tests** for any new functionality
3. **Ensure all tests pass** before submitting
4. **Follow the code style** (we use `ruff` for linting)
5. **Update documentation** if needed

### Pull Request Process

1. All PRs require approval from a maintainer before merging
2. PRs must pass all CI checks (tests, linting)
3. Keep PRs focused - one feature or fix per PR
4. Write clear commit messages following conventional commits

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/claude-codex-duo.git
cd claude-codex-duo

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Run linter
ruff check src/ tests/
```

### Code Style

- We use `ruff` for linting and formatting
- Follow PEP 8 conventions
- Use type hints for function signatures
- Keep functions focused and under 50 lines when possible

### Commit Messages

Follow conventional commits format:

```
type(scope): description

[optional body]
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
- `feat(session): add timeout configuration`
- `fix(bridge): handle file lock race condition`
- `docs: update installation instructions`

### Testing

- Write tests for all new functionality
- Maintain test coverage
- Use descriptive test names
- Test both success and error cases

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=claude_codex_duo
```

## Maintainers

This project is maintained by [Sigma5C](https://github.com/Sigma5C-Corp). All pull requests require maintainer approval.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
