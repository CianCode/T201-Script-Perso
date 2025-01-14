import argparse
from data_handler import CustomDataGen
from data_manager import CustomFetcher
from utility import CustomUtils

VALID_OPERATORS = ["==", "!=", "<", ">", "<=", ">="]
COLUMN_NAMES = ["Product ID", "Company", "Origin", "Category", "Stock", "Unit Price"]


def display_menu():
    print("\nWelcome to the Data Operations Tool")
    print("1. Create JSON data files")
    print("2. Clean all data files")
    print("3. Retrieve and process data")
    print("4. Exit")

    choice = input("Select an option (1-4): ").strip()
    return choice


def execute_menu():
    data_generator, data_fetcher, utility_tools = CustomDataGen(), CustomFetcher(), CustomUtils()

    while True:
        choice = display_menu()

        if choice == "1":
            files = int(input("Enter the number of files to create (default 10): ") or 10)
            rows = int(input("Enter the number of rows per file (default 200): ") or 200)

            if utility_tools.confirm_action(f"Create {files} files with {rows} rows each?"):
                data_generator.create_files(files, rows)
                print("[DataTool] Files created successfully")
            else:
                print("[DataTool] Operation aborted")

        elif choice == "2":
            if utility_tools.confirm_action("Confirm deletion of all files?"):
                data_generator.remove_files()
                print("[DataTool] Files deleted successfully")
            else:
                print("[DataTool] Operation aborted")

        elif choice == "3":
            filters = []
            while True:
                add_filter = input("Add a filter? (y/n): ").strip().lower()
                if add_filter == "y":
                    field = input(f"Enter field to filter ({', '.join(COLUMN_NAMES)}): ").strip()
                    operator = input(f"Enter operator ({', '.join(VALID_OPERATORS)}): ").strip()
                    value = input("Enter value: ").strip()
                    filters.append((field, operator, value))
                else:
                    break

            sort = input(f"Sort by field ({', '.join(COLUMN_NAMES)} or leave blank): ").strip()
            reverse = input("Reverse sort order? (y/n): ").strip().lower() == "y"
            columns = input(f"Specify columns to display ({', '.join(COLUMN_NAMES)} or leave blank): ").strip().split(
                ",")
            columns = [col.strip() for col in columns if col.strip() in COLUMN_NAMES] or None

            data = data_fetcher.get_data(filters, sort if sort else None, reverse, columns)
            for entry in data:
                print(entry)

            analytics = data_fetcher.generate_summary(data)
            print(analytics)
            print("[DataTool] Data retrieved successfully")

        elif choice == "4":
            print("[DataTool] Exiting...")
            break

        else:
            print("[DataTool] Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        execute_menu()
    except KeyboardInterrupt:
        print("\n[DataTool] Process interrupted")