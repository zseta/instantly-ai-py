import requests
from requests import Response
from instantly import InstantlyLead

class Instantly:
    """Client for interacting with the Instantly API."""
    
    API_URL = "https://api.instantly.ai/api/v2/"
    
    def __init__(self, api_key: str, api_url: str = API_URL):
        self.api_key = api_key
        self.api_url = api_url
        
    def _get_endpoint(self, endpoint: str) -> str:
        return f"{self.api_url}{endpoint}"
    
    def _default_headers(self) -> dict:
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
    
    def create_lead(self, lead: InstantlyLead) -> Response:
        """Create a new lead in Instantly.

        Args:
            lead (InstantlyLead): lead data

        Returns:
            Response: Response from server
        """
        url = self._get_endpoint("leads")
        headers = self._default_headers()
        payload = lead.to_dict()
        return requests.post(url, json=payload, headers=headers)
