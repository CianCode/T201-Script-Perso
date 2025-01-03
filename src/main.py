import argparse
from data_handler import CustomDataGen
from data_manager import CustomFetcher
from utility import CustomUtils

VALID_OPERATORS = ["==", "!=", "<", ">", "<=", ">="]
COLUMN_NAMES = ["Product ID", "Company", "Origin", "Category", "Stock", "Unit Price"]

def execute_script():
    """
    Execute the main script actions.
    PRE: None
    POST: Executes the specified operation (create, clean, retrieve) based on user input.
    """
    data_generator, data_fetcher, utility_tools = CustomDataGen(), CustomFetcher(), CustomUtils()

    parser = argparse.ArgumentParser(description="Data Operations Tool")
    subparsers = parser.add_subparsers(dest="action", required=True)

    gen_parser = subparsers.add_parser("create", help="Create JSON data files")
    gen_parser.add_argument("-f", "--files", type=int, default=10, help="Number of files to create")
    gen_parser.add_argument("-r", "--rows", type=int, default=200, help="Rows per file")

    subparsers.add_parser("clean", help="Remove all data files")

    fetch_parser = subparsers.add_parser("retrieve", help="Retrieve and process data")
    fetch_parser.add_argument("-f", "--filter", action="append", nargs=3, metavar=("FIELD", "OPERATOR", "VALUE"), help="Apply filters")
    fetch_parser.add_argument("-s", "--sort", choices=COLUMN_NAMES, help="Sort by field")
    fetch_parser.add_argument("-r", "--reverse", action="store_true", help="Reverse sorting order")
    fetch_parser.add_argument("-c", "--columns", action="append", choices=COLUMN_NAMES, help="Specify columns")

    args = parser.parse_args()

    if args.action == "create":
        if utility_tools.confirm_action(f"Create {args.files} files with {args.rows} rows each?"):
            data_generator.create_files(args.files, args.rows)
            print("[DataTool] Files created successfully")
        else:
            print("[DataTool] Operation aborted")

    elif args.action == "clean":
        if utility_tools.confirm_action("Confirm deletion of all files?"):
            data_generator.remove_files()
            print("[DataTool] Files deleted successfully")

    elif args.action == "retrieve":
        filters = [(key, op, value) for key, op, value in (args.filter or [])]
        data = data_fetcher.get_data(filters, args.sort, args.reverse, args.columns)
        for entry in data:
            print(entry)
        analytics = data_fetcher.generate_summary(data)
        print(analytics)
        print("[DataTool] Data retrieved successfully")

if __name__ == "__main__":
    try:
        execute_script()
    except KeyboardInterrupt:
        print("\n[DataTool] Process interrupted")