import operator
import csv
import os

class CustomFetcher:
    OPERATORS = {"==": operator.eq, "!=": operator.ne, "<": operator.lt, ">": operator.gt, "<=": operator.le, ">=": operator.ge}

    def __init__(self):
        """
        Initialize the data fetcher with a default data path.
        PRE: None
        POST: Sets up the data path for operations.
        """
        self.data_path = os.path.join(os.path.dirname(os.getcwd()), "data")

    def get_data(self, filters=None, sort_field=None, reverse=False, selected_columns=None):
        """
        Fetch data based on given parameters.
        PRE: Filters, sorting, and column options may be specified.
        POST: Returns a list of filtered, sorted, and selected data rows.
        """
        data_list = []
        for file in os.listdir(self.data_path):
            try:
                with open(os.path.join(self.data_path, file), "r") as file_content:
                    reader = csv.DictReader(file_content)
                    for row in reader:
                        if self.match_filters(row, filters):
                            if selected_columns:
                                row = {key: row[key] for key in selected_columns}
                            data_list.append(row)
            except Exception as err:
                print(f"Error reading {file}: {err}")
        if sort_field and data_list:
            column_type = self.get_column_type(data_list[0][sort_field])
            data_list.sort(key=lambda d: column_type(d[sort_field]), reverse=reverse)
        return data_list

    def get_column_type(self, value):
        """
        Determine the type of a column's value.
        PRE: Value is a string representation of the data.
        POST: Returns the type of the value (float or str).
        """
        try:
            float(value)
            return float
        except ValueError:
            return str

    def match_filters(self, row, filters):
        """
        Check if a row matches the given filters.
        PRE: Filters must be valid (field, operator, value).
        POST: Returns True if the row matches all filters, otherwise False.
        """
        if not filters:
            return True
        for field, op, value in filters:
            op_func = self.OPERATORS.get(op)
            if not op_func:
                raise ValueError(f"Invalid operator: {op}")
            try:
                row_value = float(row[field])
                value = float(value)
            except ValueError:
                row_value = row[field]
            if not op_func(row_value, value):
                return False
        return True

    def generate_summary(self, data):
        """
        Generate basic analytics for the data.
        PRE: Data must be a list of dictionaries with numerical fields.
        POST: Returns a summary dictionary with sum, max, min, count, and average for each field.
        """
        summary = {}
        for row in data:
            for field, value in row.items():
                try:
                    num_value = float(value)
                    if field not in summary:
                        summary[field] = {"sum": 0, "max": num_value, "min": num_value, "count": 0}
                    summary[field]["sum"] += num_value
                    summary[field]["max"] = max(summary[field]["max"], num_value)
                    summary[field]["min"] = min(summary[field]["min"], num_value)
                    summary[field]["count"] += 1
                except ValueError:
                    continue
        for field in summary:
            summary[field]["average"] = summary[field]["sum"] / summary[field]["count"]
        return summary
