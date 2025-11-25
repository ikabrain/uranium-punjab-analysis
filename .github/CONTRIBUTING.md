# Contributing to Research

Thank you for your interest in contributing to this scientific research project. This work aims to advance our understanding of groundwater contamination in Punjab, with a focus on Uranium and associated hydrogeochemical factors. Every contribution—whether analytical, organizational, or conceptual—helps strengthen the research and improve the scientific rigor of the final publication.

This guide outlines how to collaborate effectively, maintain consistency, and support transparent, reproducible research workflows.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Repository Philosophy](#repository-philosophy)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Contributing Guidelines](#contributing-guidelines)
- [Issue Reporting](#issue-reporting)
- [Pull Request Process](#pull-request-process)
- [Code Style and Standards](#code-style-and-standards)
- [Data and Research Ethics](#data-and-research-ethics)
- [Testing and Validation](#testing-and-validation)
- [Documentation](#documentation)

## Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please read [CODE_OF_CONDUCT.md](.github/CODE_OF_CONDUCT.md) before contributing.

## Repository Philosophy

This repository serves as a **research lab in code form**.
Its goals are:

- To organize experimental ideas, micro-studies, and analyses.
- To maintain a transparent, reproducible workflow.
- To support continuous improvement toward a publishable research paper.
- To create a well-documented, traceable path from raw data $\rightarrow$ insight $\rightarrow$ modeling $\rightarrow$ the final paper.

The workflow is inspired by strong engineering practices like SCRUM adapted for scientific inquiry.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/uranium-punjab-analysis.git
   cd uranium-punjab-analysis
   ```
3. **Add the upstream remote**:
   ```bash
   git remote add upstream https://github.com/original-owner/uranium-punjab-analysis.git
   ```

## Development Setup

### Environment Setup

This project supports both `pip` and `conda` for dependency management.

#### Using pip:

```bash
pip install -r requirements.txt
```

#### Using conda (recommended):

```bash
conda env create -f environment.yml -n uranium
conda activate uranium
```

### Verifying Your Setup

1. Ensure all dependencies are installed correctly
2. Verify you can run Jupyter notebooks:
   ```bash
   jupyter notebook
   ```
3. Test that you can import key libraries:
   ```python
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   import seaborn as sns
   ```

## Project Structure

```
uranium-punjab-analysis/
├── .github/              # GitHub configuration files
├── groundwater_quality_pdfs/  # Source PDF documents
├── micro-study-1/        # First micro-study analysis
│   ├── uranium1.csv      # Dataset for study 1
│   └── visualizer.ipynb  # Visualization notebook
├── micro-study-2/        # Second micro-study analysis
│   ├── uranium2.csv      # Dataset for study 2
│   ├── relation.ipynb    # Relationship analysis
│   └── testing-interpolation/
│       └── interpolator.ipynb
├── scraper.py            # Web scraper for research papers
├── requirements.txt      # pip dependencies
├── environment.yml       # conda environment
├── README.md             # Project overview
├── LICENSE.md            # License information
└── CITATION.cff          # Citation metadata
```

## Contributing Guidelines

### Before You Start

1. **Check existing issues**: Look through open issues to see if your work is already being addressed
2. **Check the Project Kanban board**: Review the project board to understand current priorities
3. **Create an issue**: For significant changes, create an issue first to discuss your approach
4. **Assign yourself**: If you're working on an issue, assign it to yourself on the Kanban board

### Issue Naming Convention

When creating issues, please follow this naming format:

- **Bug reports**: `[BUG] Description of the bug`
- **Feature requests**: `[FEATURE] Description of the feature`
- **Documentation**: `[DOCS] Description of documentation need`
- **Research/Analysis**: `[RESEARCH] Description of analysis`
- **Data**: `[DATA] Description of data-related task`
- **Enhancement**: `[ENHANCEMENT] Description of improvement`

Examples:

- `[BUG] Visualizer notebook fails with missing latitude data`
- `[FEATURE] Add statistical significance testing to micro-study-2`
- `[RESEARCH] Analyze correlation between depth and uranium concentration`
- `[DATA] Add 2024 groundwater quality data`

### Branch Naming Convention

Create branches using the following format:

```
<type>/<issue-number>-<short-description>
```

Types:

- `feature/` - New features
- `bugfix/` - Bug fixes
- `docs/` - Documentation updates
- `research/` - Research/analysis work
- `data/` - Data-related changes
- `refactor/` - Code refactoring

Examples:

- `feature/42-add-interpolation-methods`
- `bugfix/15-fix-csv-parsing-error`
- `research/28-depth-uranium-correlation`

## Issue Reporting

We use **Issue Forms and Templates** for:

- Literature suggestions
- Dataset suggestions
- Analysis tasks
- Research ideas or hypotheses

When creating an issue, please provide as much detail as possible to help maintainers understand and address the issue effectively.

Naming format:

- `[LIT] Title`
- `[DATA] Title`
- `[RESEARCH] Title`
- `[ANALYSIS] Title`
- `[BUG] Title`
- `[FEATURE] Title`
- `[DOCS] Title`

Example:

`[RESEARCH] Investigate redox-linked uranium mobilization patterns`

## Pull Request Process

### Before Submitting

1. **Update your fork**: Sync with upstream before creating a PR

   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Create a feature branch** from `main`:

   ```bash
   git checkout -b feature/issue-number-description
   ```

3. **Make your changes** following the code style guidelines

4. **Test your changes**: Ensure notebooks run without errors

5. **Update documentation**: If needed, update README or add docstrings

6. **Commit your changes** with clear, descriptive commit messages:
   ```bash
   git commit -m "Add feature: description of change"
   ```

### Commit Message Format

Use clear, descriptive commit messages:

```
<type>: <short summary>

<optional detailed description>

Fixes #<issue-number>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `research`, `data`

### Pull Request Checklist

- [ ] Code follows the project's style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated (if needed)
- [ ] No new warnings or errors introduced
- [ ] Changes tested locally
- [ ] Issue number referenced in PR description
- [ ] PR description explains the "what" and "why"
- [ ] Linked to relevant issue(s) and Kanban board

### PR Description Template

```markdown
## Description

Brief description of changes

## Related Issue

Closes #<issue-number>

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Research/analysis
- [ ] Data update
- [ ] Refactoring

## Testing

Describe how you tested your changes

## Checklist

- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings introduced
```

### Review Process

1. **Automated checks**: Ensure all CI checks pass (if applicable)
2. **Code review**: Address reviewer feedback
3. **Update Kanban board**: Move the issue to "In Review" or "Done"
4. **Merge**: Once approved, maintainers will merge your PR

## Code Style and Standards

### Python Code Style

- Follow **PEP 8** style guidelines
- Use **4 spaces** for indentation (no tabs)
- Maximum line length: **88 characters** (Black formatter standard)
- Use descriptive variable names
- Add docstrings for functions and classes

### Jupyter Notebook Guidelines

1. **Clear structure**: Use markdown cells to explain your analysis
2. **Cell organization**:
   - Import statements in first cell
   - Data loading in separate cells
   - Analysis steps clearly separated
3. **Output preservation**: Clear outputs before committing (unless outputs are essential)
4. **Documentation**: Add markdown cells explaining methodology
5. **Reproducibility**: Ensure notebooks can run from top to bottom

### Example Code Style

```python
def calculate_uranium_risk(concentration: float, threshold: float = 30.0) -> float:
    """
    Calculate health risk based on uranium concentration.

    Parameters:
    -----------
    concentration : float
        Uranium concentration in ppb (µg/L)
    threshold : float, optional
        Safe threshold value (default: 30.0 ppb)

    Returns:
    --------
    float
        Risk quotient (concentration / threshold)
    """
    if concentration < 0:
        raise ValueError("Concentration cannot be negative")
    return concentration / threshold
```

### Import Organization

Organize imports in this order:

1. Standard library imports
2. Third-party imports
3. Local application imports

Example:

```python
import os
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

## Data and Research Ethics

### Data Usage

- **Respect copyright**: All data is sourced from publicly available research papers
- **Cite sources**: Always cite original sources when using data
- **Non-commercial use**: Data derivatives should not be used for commercial purposes without permission
- **Attribution**: Give proper credit to original data sources

### Research Integrity

- **Reproducibility**: Ensure all analyses can be reproduced
- **Transparency**: Document data sources and methodology clearly
- **Accuracy**: Verify calculations and visualizations
- **Ethical considerations**: Consider the implications of research findings

### Adding New Data

When adding new datasets:

1. **Document the source**: Include source information in the dataset or README
2. **Update data tracking**: Update the Google Sheets workbook if applicable
3. **Validate data**: Check for missing values, outliers, and data quality
4. **Create documentation**: Document data structure and any preprocessing steps

## Testing and Validation

### Notebook Testing

Before submitting:

1. **Run all cells**: Ensure the notebook executes from top to bottom
2. **Check outputs**: Verify outputs are reasonable and expected
3. **Validate results**: Cross-check calculations where possible
4. **Test edge cases**: Consider boundary conditions and missing data

### Data Validation

- Check for missing values and document how they're handled
- Verify data types are correct
- Check for outliers and document any exclusions
- Validate coordinate data (latitude/longitude ranges)

## Documentation

### Code Documentation

- Add docstrings to functions and classes
- Use clear variable names that are self-documenting
- Add inline comments for complex logic
- Document assumptions and limitations

### Notebook Documentation

- Include markdown cells explaining:
  - Purpose of the analysis
  - Data sources
  - Methodology
  - Key findings
  - Limitations

### README Updates

If your contribution adds new features or changes project structure:

- Update the README.md with relevant information
- Update this CONTRIBUTING.md, if necessary
- Add installation instructions if new dependencies are added
- Update examples if API or usage changes

## Questions?

If you have questions or need clarification:

1. **Check existing issues** - your question might already be answered!
2. **Use GitHub discussions** for broad questions
3. **Open an issue** for specific tasks

## Recognition

Contributors will be recognized in:

- Project README (if significant contributions)
- Release notes
- Research publications (if applicable)

Thank you for supporting this research effort and contributing to meaningful, regionally-impactful science.
