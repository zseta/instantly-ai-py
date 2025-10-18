from dataclasses import fields
from uuid import uuid4
from faker import Faker
from instantly import InstantlyLead
import csv


def fake_value(field_name: str) -> str:
    f = Faker()
    if field_name in {"campaign", "list_id", "assigned_to", "blocklist_id"}:
        value = uuid4()
    elif field_name == "email":
        value = f.email()
    elif field_name == "website":
        value = f.url()
    elif field_name in {"first_name", "last_name"}:
        value = getattr(f, field_name)()
    elif field_name == "company_name":
        value = f.company()
    elif field_name == "personalization":
        value = f.random_element(elements=["Hi there!", "Hello!", "Greetings!", "Hey Friend!"])
    elif field_name == "phone":
        value = f.phone_number()
    elif field_name == "lt_interest_status":
        value = f.random_element(elements=[1, -1])
    elif field_name == "pl_value_lead":
        value = f.random_element(elements=["High", "Medium", "Low"])
    elif field_name.startswith("skip_if_") or field_name.startswith("verify_"):
        value = f.boolean()
    elif field_name == "custom_variable":
        value = {"custom_key": f.word()}
    else:
        raise ValueError(f"Unknown field name: {field_name}")
    return value


def remove_unused_columns(columns: list[str]):
    id_cols = ["campaign", "assigned_to", "blocklist_id", "list_id"]
    bool_cols = ["skip_if_in_workspace", "skip_if_in_campaign", "skip_if_in_list", 
                 "verify_leads_for_lead_finder", "verify_leads_on_import"]
    enum_cols = ["lt_interest_status"]
    custom_vars_cols = ["custom_variable"]
    to_remove = id_cols + bool_cols + enum_cols + custom_vars_cols
    for col in to_remove:    
        columns.remove(col)

with open("example.csv", "w", newline="", encoding="utf-8") as f_out:
    columns = [f.name for f in fields(InstantlyLead)]
    remove_unused_columns(columns)
    writer = csv.DictWriter(f_out, fieldnames=columns, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for _ in range(5):
        lead_data = {}
        for column in columns:
            lead_data[column] = fake_value(column)
        writer.writerow(lead_data)
