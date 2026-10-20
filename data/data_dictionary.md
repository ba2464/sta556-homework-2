## 1. Dataset Description

### 1.1 Data Source and Background

This analysis uses the Automobile Bodily Injury Claims (AutoBI) dataset, originally obtained from the Insurance Research Council (IRC). The data were collected in 2002 as part of a study of automobile injury insurance claims. The full study included over 70,000 closed claims reported by 32 insurers, while the dataset used in this analysis consists of 1,340 claims from a single US state.

The dataset contains information on claimant characteristics, attorney involvement, insurance status, seatbelt usage, and economic losses. Economic loss is measured in thousands of US dollars.

The objective of this analysis is to explore the distribution of economic losses and examine how these losses vary with selected claimant characteristics, particularly attorney involvement and claimant age.

**Source:** Frees, E. W., *Regression Modeling with Actuarial and Financial Applications*, accompanying data descriptions, Table 2. Original data source: Insurance Research Council (IRC).

### 1.2 Description of Variables

| Variable | Description |
|---|---|
| CASENUM | Unique case number used to identify a claim |
| ATTORNEY | Whether the claimant was represented by an attorney (1 = Yes, 2 = No) |
| CLMSEX | Claimant's gender (1 = Male, 2 = Female) |
| MARITAL | Marital status (1 = Married, 2 = Single, 3 = Widowed, 4 = Divorced/Separated) |
| CLMINSUR | Whether the driver of the claimant's vehicle was uninsured (1 = Yes, 2 = No, 3 = Not applicable) |
| SEATBELT | Whether the claimant wore a seatbelt or child restraint (1 = Yes, 2 = No, 3 = Not applicable) |
| CLMAGE | Claimant's age in years |
| LOSS | Total economic loss, measured in thousands of US dollars |

### 1.3 Initial Data Inspection

The dataset is imported using Python's pandas library. Initial inspection includes examining the dataset dimensions, variable types, missing values, and potential duplicate records. These checks provide a basis for subsequent cleaning and exploratory analysis.