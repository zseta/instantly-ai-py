# Instantly.AI Python client (WIP)

Python client for the Instantly.ai API

Currently supported endpoints:
* [Create lead](https://developer.instantly.ai/api/v2/lead/createlead)

## Installation
```bash
git clone https://github.com/zseta/instantly-ai-py
cd instantly-ai-py
pip install -e .
```

## Usage

### Create new lead
```python
from instantly import Instantly, InstantlyLead

client = Instantly(api_key="your_api_key")
lead = InstantlyLead(email="user@example.com", first_name="John")
response = client.create_lead(lead)
```

### Import leads from CSV file
```python
from instantly import LeadImporter

importer = LeadImporter(api_key="your_api_key")
importer.import_csv("leads.csv")
```

* [See example.](/examples/csv_import.py)
* [See CSV template.](/examples/template.csv)

## API Key
Get your API key from [Instantly.ai Settings](https://app.instantly.ai/app/settings/integrations)
