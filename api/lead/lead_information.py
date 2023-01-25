from typing import Optional

from pydantic import BaseModel


class LeadInformation(BaseModel):
    # There always is a full_name, but not the other fields
    full_name: str
    email: str
    title: Optional[str]
    company_name: Optional[str]
    location: Optional[str]
    linkedin_url: Optional[str]
