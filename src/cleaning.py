import numpy as np
import pandas as pd

def recode_categories(data):
    """Recode categorical claim variables into readable labels."""
    df = data.copy()

    mappings = {
        "ATTORNEY": {1: "Yes", 2: "No"},
        "CLMSEX": {1: "Male", 2: "Female"},
        "MARITAL": {
            1: "Married",
            2: "Single",
            3: "Widowed",
            4: "Divorced/Separated"
        },
        "CLMINSUR": {
            1: "Yes",
            2: "No",
            3: "Not applicable"
        },
        "SEATBELT": {
            1: "Yes",
            2: "No",
            3: "Not applicable"
        }
    }

    for col, mapping in mappings.items():
        unexpected = set(df[col].dropna().unique()) - set(mapping)
        if unexpected:
            raise ValueError(f"Unexpected codes in {col}: {unexpected}")
        df[col] = df[col].map(mapping).astype("category")

    return df


def filter_complete(data, required_columns):
    """Keep observations complete for specified variables."""
    return data.dropna(subset=required_columns).copy()


def summarize_losses(data, group_col):
    """Calculate claim counts and loss statistics by group."""
    return (
        data.groupby(group_col, observed=True)["LOSS"]
        .agg(
            count="count",
            mean="mean",
            median="median",
            std="std"
        )
        .reset_index()
    )


def add_log_loss(data):
      """Return a copy with LOG_LOSS = ln(LOSS); LOSS must be positive."""
      if (data["LOSS"] <= 0).any():
          raise ValueError("LOSS must be positive.")
      return data.assign(LOG_LOSS=np.log(data["LOSS"]))


def summarize_log_losses(data, group_col):
      """Log-scale summary by group, plus geometric mean and median in original units."""
      out = data.groupby(group_col, observed=True)["LOG_LOSS"].agg(
          count="count", mean="mean", median="median", std="std")
      out["geometric_mean"] = np.exp(out["mean"])
      out["median_original"] = np.exp(out["median"])
      return out


def add_age_band(data, bins=(-1, 17, 34, 54, 120),
                   labels=("0-17", "18-34", "35-54", "55+")):
      """Add AGE_BAND, a categorical age group, to a copy of the data."""
      return data.assign(AGE_BAND=pd.cut(data["CLMAGE"], bins=list(bins), labels=list(labels)))


def compare_missing(data, col):
      """Compare LOSS for rows where `col` is missing vs. recorded."""
      flag = np.where(data[col].isna(), "Missing", "Recorded")
      return data.groupby(flag)["LOSS"].agg(Count="count", Mean="mean", Median="median", Std="std", Maximum="max")