import pandas as pd


DATASET_PATH = "data/generated/orders_dataset.csv"


def main():

    df = pd.read_csv(DATASET_PATH)

    print("\n==============================")
    print("DATA PROFILING REPORT")
    print("==============================")

    print(f"\nTotal Rows: {len(df)}")

    # --------------------------------------------------
    # Duplicate Orders
    # --------------------------------------------------

    duplicate_count = df.duplicated(subset=["order_id"]).sum()

    print(f"\nDuplicate Rows: {duplicate_count}")

    # --------------------------------------------------
    # Missing Dates
    # --------------------------------------------------

    missing_dates = df["order_date"].isna().sum()

    print(f"Missing Order Dates: {missing_dates}")

    # --------------------------------------------------
    # Invalid Emails
    # --------------------------------------------------

    invalid_emails = (
        df["customer_email"] == "invalid_email"
    ).sum()

    print(f"Invalid Emails: {invalid_emails}")

    # --------------------------------------------------
    # Negative Revenue
    # --------------------------------------------------

    negative_revenue = (
        df["revenue"] < 0
    ).sum()

    print(f"Negative Revenue Rows: {negative_revenue}")

    # --------------------------------------------------
    # Missing Store Names
    # --------------------------------------------------

    missing_stores = (
        df["store_name"].isna()
    ).sum()

    print(f"Missing Store Names: {missing_stores}")

    # --------------------------------------------------
    # Product Variations
    # --------------------------------------------------

    product_variations = (
        df["product_name"] == "camping chair"
    ).sum()

    print(
        f"Product Name Variations: {product_variations}"
    )


if __name__ == "__main__":
    main()