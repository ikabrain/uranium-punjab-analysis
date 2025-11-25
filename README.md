# Uranium in Punjab Groundwater

![Anaconda Badge](https://img.shields.io/badge/conda-grey?logo=anaconda)
![Python Badge](https://img.shields.io/badge/python-3.11%2B-blue?logo=python)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/ikabrain/uranium-punjab-analysis?logo=github)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/ikabrain/uranium-punjab-analysis?logo=github)
[![commitlint](https://github.com/ikabrain/uranium-punjab-analysis/actions/workflows/commitlint.yml/badge.svg)](https://github.com/ikabrain/uranium-punjab-analysis/actions/workflows/commitlint.yml?logo=github)

[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]


> _Data has been sourced & scraped from multiple resources. To view the links, open the [Google Sheet Workbook](<(https://docs.google.com/spreadsheets/d/1YLMoh0YfT4zJe-DiPFVBRuhHBOm8oWjn5NrmUx8y-74/edit?usp=sharing)>); each sheet has a cell with the source link._

Download depenedencies using:

1. **pip**
   ```bash
   pip install -r requirements.txt
   ```
2. **conda**
   ```bash
   conda env create -f environment.yml -n uranium
   conda activate uranium
   ```

Export your dependencies using:

1. **pip**

```bash
pip list --format=freeze > requirements.txt
```

2. **conda**

```bash
conda env export --no-builds | grep -v "^prefix" > environment.yml
```

#### 🔗 Links to dataset

- [Google Sheets](https://docs.google.com/spreadsheets/d/1YLMoh0YfT4zJe-DiPFVBRuhHBOm8oWjn5NrmUx8y-74/edit?usp=sharing)
- [Kaggle Dataset](https://www.kaggle.com/datasets/thegenesis/uranium-in-punjabs-groundwater/)

### ✅ Screenshot of Result of first microstudy

<img width="768" height="643" alt="Result of first microstudy" src="https://github.com/user-attachments/assets/f3cf9e1c-1856-4709-abba-6b708789c58a" />

## License
This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa]


[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg