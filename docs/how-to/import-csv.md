# How to import leads from a CSV file

This guide shows you how to import leads from a CSV file using Python.

## Prerequisites

- Python 3
- API key from Instantly.ai
- `instantly-ai` package installed

## CSV file structure

Your CSV file must follow the column structure defined in `template.csv`:

```csv
"email","personalization","website","last_name","first_name","company_name","phone","pl_value_lead"
```

Make sure to use double quotes for each column name and column value.

### Required columns
- `email` - Lead's email address

### Optional columns
- `personalization` - Personalized message
- `website` - Lead's website
- `last_name` - Lead's last name  
- `first_name` - Lead's first name
- `company_name` - Lead's company
- `phone` - Lead's phone number
- `pl_value_lead` - Lead value classification

More info about each field [in the docs](https://developer.instantly.ai/api/v2/lead/createlead).

### Custom columns
You can add additional columns to your CSV file. These will be stored as `custom variables` in the Instantly platform.

## Import process
```python
from instantly import LeadImporter

# Initialize the importer with your API key
importer = LeadImporter(api_key="your_api_key")

# Import leads from CSV file
importer.import_csv("path/to/your/leads.csv")
```

[See concrete example here.](/examples/csv_import.py)

## Example CSV
```csv
"email","first_name","last_name","company_name","more_info"
"john@example.com","John","Doe","Acme Corp","Premium Client"
"jane@example.com","Jane","Smith","Tech Inc","Standard Client"
```

In this example, `more_info` will be added as a custom variable for each lead.

## Reference
For detailed information about lead creation, see the [Create Lead API docs](https://docs.instantly.ai)