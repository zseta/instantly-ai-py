from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Dict, Optional
from uuid import UUID

class LeadInterestStatus(Enum):
    OUT_OF_OFFICE = 0
    INTERESTED = 1
    MEETING_BOOKED = 2
    MEETING_COMPLETED = 3
    CLOSED = 4
    NOT_INTERESTED = -1
    WRONG_PERSON = -2
    LOST = -3

@dataclass
class InstantlyLead:
    campaign: Optional[UUID] = None
    email: Optional[str] = None
    personalization: Optional[str] = None
    website: Optional[str] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    company_name: Optional[str] = None
    phone: Optional[str] = None
    lt_interest_status: Optional[LeadInterestStatus] = None
    pl_value_lead: Optional[str] = None
    list_id: Optional[UUID] = None
    assigned_to: Optional[UUID] = None
    skip_if_in_workspace: bool = False
    skip_if_in_campaign: bool = False
    skip_if_in_list: bool = False
    blocklist_id: Optional[UUID] = None
    verify_leads_for_lead_finder: bool = False
    verify_leads_on_import: bool = False
    custom_variable: Dict[str, Optional[str]] = field(default_factory=dict)
    
    def to_dict(self) -> dict:
        """Convert the object to a dictionary, excluding None and empty values."""
        data = asdict(self)
        result = {k: v for k, v in data.items() if v is not None}
        if result.get("custom_variable") == {}:
            result.pop("custom_variable")
        return result
