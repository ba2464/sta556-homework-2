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