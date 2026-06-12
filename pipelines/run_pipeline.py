from pathlib import Path
from datetime import datetime

from load_raw import load_raw
from run_staging import run_staging
from run_mart import run_mart
from run_data_quality import run_data_quality
from run_validation import run_validation


CSV_FILE = "data/generated/orders_dataset.csv"


def run_pipeline() -> None:
    """
    Execute end-to-end pipeline.
    """

    start_time = datetime.now()

    try:

        print("\n" + "=" * 60)
        print("ECOMMERCE ANALYTICS PIPELINE STARTED")
        print("=" * 60)

        csv_path = Path(CSV_FILE)

        if not csv_path.exists():
            raise FileNotFoundError(
                f"Source file not found: {CSV_FILE}"
            )

        print("\n[STEP 1] Loading Raw Layer")
        load_raw(CSV_FILE)

        print("\n[STEP 2] Running Staging Layer")
        run_staging()

        print("\n[STEP 3] Running Mart Layer")
        run_mart()

        print("\n[STEP 4] Running Data Quality Checks")
        run_data_quality()

        print("\n[STEP 5] Running Validation Checks")
        run_validation()

        end_time = datetime.now()

        print("\n" + "=" * 60)
        print("PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 60)

        print(
            f"\nExecution Time: "
            f"{end_time - start_time}"
        )

    except Exception as e:

        print("\n" + "=" * 60)
        print("PIPELINE FAILED")
        print("=" * 60)

        print(f"\nError: {e}")

        raise


if __name__ == "__main__":
    run_pipeline()