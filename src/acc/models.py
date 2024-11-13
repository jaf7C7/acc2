import csv


class CSVFile:
    """Writes/reads data line by line to/from a CSV file."""

    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            with open(self.path, newline='') as f:
                contents = list(csv.DictReader(f))
        except FileNotFoundError:
            contents = [{}]
        return contents

    def write(self, lines):
        with open(self.path, mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=lines[0].keys())
            writer.writeheader()
            for line in lines:
                writer.writerow(line)
