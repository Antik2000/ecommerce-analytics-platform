from faker import Faker
import pandas as pd
import random

fake = Faker()

# ==========================================================
# Reference Data
# ==========================================================

STORES = [
    "OutdoorHub",
    "PatioWorld",
    "HomeEssentials",
    "GardenPro",
    "CampMaster"
]

PRODUCTS = {
    "Camping Gear": [
        "Camping Chair",
        "Sleeping Bag",
        "Tent",
        "Portable Stove"
    ],
    "Patio Furniture": [
        "Patio Table",
        "Outdoor Sofa",
        "Garden Bench"
    ],
    "Garden Tools": [
        "Shovel",
        "Pruning Shears",
        "Garden Hose"
    ],
    "Lighting": [
        "LED Lantern",
        "Solar Light",
        "Outdoor Lamp"
    ],
    "Home Decor": [
        "Wall Art",
        "Decorative Vase",
        "Area Rug"
    ]
}

PAYMENT_METHODS = [
    "Credit Card",
    "PayPal",
    "Apple Pay",
    "Google Pay"
]

ORDER_STATUSES = [
    "Completed",
    "Returned",
    "Cancelled"
]

# ==========================================================
# Customer Generation
# ==========================================================

def generate_customers(num_customers=2500):
    """
    Generate reusable customer master data.
    """

    customers = []

    for customer_num in range(1, num_customers + 1):
        customers.append(
            {
                "customer_id": f"CUST{customer_num:05d}",
                "customer_name": fake.name(),
                "customer_email": fake.email()
            }
        )

    return customers


# ==========================================================
# Order Generation
# ==========================================================

def generate_orders(customers, num_orders=10000):
    """
    Generate ecommerce orders.
    """

    orders = []

    for order_num in range(1, num_orders + 1):

        customer = random.choice(customers)

        category = random.choice(list(PRODUCTS.keys()))
        product_name = random.choice(PRODUCTS[category])

        quantity = random.randint(1, 5)

        unit_price = round(
            random.uniform(20, 500),
            2
        )

        revenue = round(
            quantity * unit_price,
            2
        )

        orders.append(
            {
                "order_id": f"ORD{order_num:06d}",

                "customer_id": customer["customer_id"],
                "customer_name": customer["customer_name"],
                "customer_email": customer["customer_email"],

                "order_date": fake.date_between(
                    start_date="-3y",
                    end_date="today"
                ).strftime("%Y-%m-%d"),

                "shipping_city": fake.city(),
                "shipping_state": fake.state(),
                "shipping_country": "USA",

                "shipping_cost": round(
                    random.uniform(5, 30),
                    2
                ),

                "product_id": f"PROD{random.randint(1000, 9999)}",
                "product_name": product_name,
                "category": category,

                "quantity": quantity,
                "unit_price": unit_price,
                "revenue": revenue,

                "store_name": random.choice(STORES),

                "payment_method": random.choice(
                    PAYMENT_METHODS
                ),

                "order_status": random.choice(
                    ORDER_STATUSES
                )
            }
        )

    return orders


# ==========================================================
# Inject Data Quality Issues
# ==========================================================

def inject_data_quality_issues(df):
    """
    Introduce intentional data quality issues
    for testing and validation exercises.
    """

    df = df.copy()

    # ------------------------------------------------------
    # 1. Duplicate Orders
    # ------------------------------------------------------

    duplicate_rows = df.sample(
        n=50,
        random_state=42
    )

    df = pd.concat(
        [df, duplicate_rows],
        ignore_index=True
    )

    # ------------------------------------------------------
    # 2. Missing Order Dates
    # ------------------------------------------------------

    missing_date_idx = df.sample(
        n=100,
        random_state=43
    ).index

    df.loc[
        missing_date_idx,
        "order_date"
    ] = None

    # ------------------------------------------------------
    # 3. Invalid Emails
    # ------------------------------------------------------

    invalid_email_idx = df.sample(
        n=75,
        random_state=44
    ).index

    df.loc[
        invalid_email_idx,
        "customer_email"
    ] = "invalid_email"

    # ------------------------------------------------------
    # 4. Negative Revenue
    # ------------------------------------------------------

    negative_revenue_idx = df.sample(
        n=50,
        random_state=45
    ).index

    df.loc[
        negative_revenue_idx,
        "revenue"
    ] = -100

    # ------------------------------------------------------
    # 5. Missing Store Names
    # ------------------------------------------------------

    missing_store_idx = df.sample(
        n=50,
        random_state=46
    ).index

    df.loc[
        missing_store_idx,
        "store_name"
    ] = None

    # ------------------------------------------------------
    # 6. Product Name Variations
    # ------------------------------------------------------

    variation_idx = df.sample(
        n=50,
        random_state=47
    ).index

    df.loc[
        variation_idx,
        "product_name"
    ] = "camping chair"

    return df


# ==========================================================
# Export Dataset
# ==========================================================

def export_dataset(df, output_path):
    """
    Export dataframe to CSV.
    """

    df.to_csv(
        output_path,
        index=False
    )

    print(
        f"\nDataset exported successfully: {output_path}"
    )


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    print("\nGenerating Customers...")

    customers = generate_customers()

    print(f"Customers Generated: {len(customers)}")

    print("\nGenerating Orders...")

    orders = generate_orders(
        customers,
        num_orders=10000
    )

    orders_df = pd.DataFrame(orders)

    # Inject bad data intentionally
    orders_df = inject_data_quality_issues(
        orders_df
    )

    print("\nSample Orders:")
    print(orders_df.head())

    print(f"\nTotal Orders: {len(orders_df)}")

    export_dataset(
        orders_df,
        "data/generated/orders_dataset.csv"
    )