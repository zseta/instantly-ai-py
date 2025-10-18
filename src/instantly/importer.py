from dataclasses import fields
from typing import List
import csv
from instantly import Instantly, InstantlyLead

class LeadImporter:
    def __init__(self, api_key):
        self.instantly = Instantly(api_key)
        
    def _process_row(self, csv_row: dict) -> InstantlyLead:
        """Process a single CSV row to fit the model."""
        lead_data = {}
        custom_vars = {}
        known_fields = {f.name for f in fields(InstantlyLead)}
        for key, value in csv_row.items():
            key = key.strip().lower()
            if key in known_fields:
                lead_data[key] = value or None
            else:
                custom_vars[key] = value or None
            lead_data["custom_variable"] = custom_vars
        return InstantlyLead(**lead_data)
        
    def import_csv(self, csv_path: str) -> List[InstantlyLead]:
        """
        Reads a CSV file, parses the rows into InstantlyLead objects and
        inserts them into the Instantly platform.
        
        Any extra columns in the CSV will be stored in `custom_variable`.
        Args:
            csv_path (str): Path to the CSV file containing lead data.
        """
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                processed_lead = self._process_row(row)
                self.instantly.create_lead(processed_lead)