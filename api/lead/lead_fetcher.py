import random
import time

from api.lead.lead_information import LeadInformation


def get_lead_information_from_all_sources(email: str) -> LeadInformation:
    alpha: LeadInformation = get_lead_information_from_alpha(email)
    beta: LeadInformation = get_lead_information_from_beta(email)
    # Merge the two lead information
    merged = LeadInformation(
        full_name=alpha.full_name,
        title=alpha.title or beta.title,
        company_name=alpha.company_name or beta.company_name,
        location=alpha.location or beta.location,
        linkedin_url=alpha.linkedin_url or beta.linkedin_url,
        email=email,
    )
    return merged


def get_lead_information_from_alpha(email: str) -> LeadInformation:
    # This mocks a db call
    # sleep for 1 to 2 seconds randomly to simulate a slow db call
    time.sleep(random.randint(1, 2))
    return LeadInformation(
        full_name="John Doe",
        title="CEO",
        company_name=None,
        location="San Francisco",
        linkedin_url="https://www.linkedin.com/in/johndoe",
        email=email,
    )


def get_lead_information_from_beta(email: str) -> LeadInformation:
    # This mocks a db call
    # sleep for 1 to 2 seconds randomly to simulate a slow db call
    time.sleep(random.randint(1, 2))
    return LeadInformation(
        full_name="John Doe",
        title="CEO",
        company_name="Company",
        location=None,
        linkedin_url="https://www.linkedin.com/in/johndoe",
        email=email,
    )
