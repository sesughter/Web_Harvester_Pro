import pandas as pd
import re


def clean_data(data):
    df = pd.DataFrame(data)

    #clean price remove currency and convert to float
    df["price"] = df["price"].apply(lambda x: x.replace("£", ""))
    df["price"] = df["price"].apply(lambda x: float(x.replace("Â", "")))

    #normalize availability
    df["availability"] = df["availability"].apply(
        lambda x: "Available" if "In stock" in x else "Out of stock"
    )

    # convert rating (word to number
    rating_map= {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    df["rating"] = df["rating"].map(rating_map)

    return df
