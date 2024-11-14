import csv


class CSVFile:
    """Writes/reads data line by line to/from a CSV file."""

    def __init__(self, path):
        self.path = path

    def read(self) -> list[dict]:
        """Returns a list of dictionaries representing each line in the file."""
        with open(self.path, newline='') as f:
            contents = list(csv.DictReader(f))
        return contents

    def write(self, lines: list[dict], mode='w') -> None:
        """Takes a list of dictionaries and writes each one to successive lines in the file."""
        with open(self.path, mode=mode, newline='') as f:
            writer = csv.DictWriter(f, fieldnames=lines[0].keys())
            writer.writeheader()
            for line in lines:
                writer.writerow(line)
