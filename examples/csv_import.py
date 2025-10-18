import os
from instantly import LeadImporter


def get_current_directory():
    return os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    
    # Get your API key from https://app.instantly.ai/app/settings/integrations
    INSTANTLY_API = "*****"
    # Make sure the CSV file has the same columns as defined in the template
    # The CSV file should be in the examples folder as well
    CSV_FILE = os.path.join(get_current_directory(), "template.csv")
    
    print(f"Importing leads from {CSV_FILE}...")
    importer = LeadImporter(INSTANTLY_API)
    importer.import_csv(CSV_FILE)
    print("Done.")