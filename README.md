# Author: BRIGHT ANTWI
# STA 556 — STATISTICS AND DATA SCIENCE COMPUTING WORKFLOWS
# STA 556 Homework 2: Exploratory Analysis of Automobile Bodily Injury Claims

## Purpose

This project builds a small, reproducible data-analysis pipeline in Python. It reads an external CSV file, cleans it with reusable functions, and examines two questions about economic losses in automobile bodily injury claims:

1. How do economic losses differ between attorney-represented and non-attorney-represented claims?
2. What is the relationship between claimant age and economic loss?

## Data Source

- **Dataset:** Automobile Bodily Injury Claims (AutoBI)
- **Original source:** Insurance Research Council (IRC), 2002
- **Accessed via:** Frees, E. W., *Regression Modeling with Actuarial and Financial Applications*, accompanying data (Table 2) 
- **Size:** 1,340 closed claims from a single US state, 8 variables
- **Units:** `LOSS` is measured in thousands of US dollars

The file is included at `data/AutoBi_original.csv`. Variable definitions and coding schemes are in [`data/data_dictionary.md`](data/data_dictionary.md).

## Repository Structure

```
sta556-homework-2/
├── data/
│   ├── AutoBi_original.csv
│   └── data_dictionary.md
├── figures/
│   ├── loss_distribution.png
│   ├── loss_by_attorney.png
│   └── age_vs_loss.png
├── notebooks/
│   └── exploratory_data_analysis.ipynb
├── src/
│   ├── __init__.py
│   └── cleaning.py
├── requirements.txt
└── README.md
```

## How to Run

1. Clone the repository:
```bash
   git clone https://github.com/ba2464/sta556-homework-2
   cd sta556-homework-2
```
2. (Recommended) Create and activate a virtual environment:
```bash
   python -m venv .venv
   source .venv/bin/activate      
```
3. Install the dependencies:
```bash
   pip install -r requirements.txt
```
4. Open `notebooks/exploratory data analysis.ipynb` and choose **Run All**. The notebook finds the project root automatically, reads the data with relative paths, and saves the figures to `figures/`.

## Reusable Functions (`src/cleaning.py`)

| Function | Purpose |
|---|---|
| `recode_categories(data)` | Converts numeric category codes (e.g., ATTORNEY 1/2) to readable labels and raises an error on unexpected codes |
| `filter_complete(data, required_columns)` | Keeps only rows with no missing values in the specified columns |
| `summarize_losses(data, group_col)` | Returns the count, mean, median, and standard deviation of loss by group |

## Main Findings

- **Losses are strongly right-skewed.** The mean loss (about $5,953) is more than twice the median (about $2,331), and the largest claim exceeds $1 million. Log scales are used for the plots.
- **Attorney-represented claims have higher losses.** The mean is about $9,863 versus $1,865 without an attorney (about 5.3 times higher), and the median is $3,417 versus $986. The attorney group also contains the most extreme claims.
- **Age has a weak association with loss.** The Pearson correlation is 0.066 and the Spearman correlation is 0.21047, so there is a weak positive association that is partly masked by extreme losses on the raw scale and a modest positive rank relationship.
- **Missing ages matter.** 189 claims (14.1%) have no recorded age, so the age analysis uses 1,151 complete claims. Claims with missing ages have a higher mean loss but a lower median, driven partly by the single largest claim.

- **Log-transformed analysis.** On a log scale, the attorney/no-attorney gap narrows from 5.3× (raw means) to about 4.1× (geometric means) but remains large, and the age correlation rises from 0.066 to 0.183.

These results describe associations only. They do not show that attorney involvement causes higher losses; for example, more severe injuries may make claimants more likely to hire attorneys.

## Figures

- `figures/loss_distribution.png`: distribution of economic losses
- `figures/loss_by_attorney.png`: losses by attorney involvement
- `figures/age_vs_loss.png`: claimant age versus economic loss