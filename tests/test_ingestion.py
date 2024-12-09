
import unittest
from databridge.ingestion.file_ingestion import ingest_file
import os

class TestFileIngestion(unittest.TestCase):
    def test_ingest_csv(self):
        with open("test.csv", "w") as f:
            f.write("col1,col2\n1,2\n3,4")
        df = ingest_file("test.csv", "csv")
        self.assertEqual(len(df), 2)
        os.remove("test.csv")

if __name__ == "__main__":
    unittest.main()
        