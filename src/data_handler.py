import csv
import os
import random
from faker import Faker

class CustomDataGen:
    def __init__(self):
        """
        Initialize the data generator.
        PRE: None
        POST: Sets up the data path and initializes the Faker instance.
        """
        self.data_path = os.path.expanduser("~/data_tool")
        os.makedirs(self.data_path, exist_ok=True)
        self.faker = Faker()
        Faker.seed(717)  # Fixed the deprecated instance seed issue

    def create_files(self, num_files, num_rows):
        """
        Generate specified number of CSV files with random data.
        PRE: num_files and num_rows must be integers.
        POST: Creates num_files files, each with num_rows rows of data.
        """
        for i in range(num_files):
            file_name = os.path.join(self.data_path, f"file_{i + 1}.csv")
            with open(file_name, "w") as file:
                writer = csv.writer(file)
                writer.writerow(["Product ID", "Company", "Origin", "Category", "Stock", "Unit Price"])
                for row in range(num_rows):
                    writer.writerow([self.faker.uuid4(), self.faker.company(), self.faker.country(), self.faker.word(), random.randint(1, 1000), random.uniform(1.0, 100.0)])

    def remove_files(self):
        """
        Delete all generated files in the data path.
        PRE: None
        POST: All files in the data directory are removed.
        """
        for file in os.listdir(self.data_path):
            os.remove(os.path.join(self.data_path, file))
            print(f"Deleted: {file}")
