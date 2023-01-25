import pytest_mock

from api.lead.lead_fetcher import get_lead_information_from_all_sources
from api.lead.lead_information import LeadInformation


def test_get_lead_information_from_all_sources(mocker: pytest_mock.MockerFixture):
    # Use mock to patch get_lead_information_from_alpha and get_lead_information_from_beta
    # to return the alpha_info and beta_info respectively
    alpha_info = LeadInformation(
        full_name="John Doe",
        title=None,
        company_name="Company",
        location="California",
        linkedin_url=None,
        email="john@doe.com",
    )
    beta_info = LeadInformation(
        full_name="John Doe",
        title="CEO",
        company_name=None,
        location=None,
        linkedin_url="www.linkedin.com",
        email="john@doe.com",
    )
    mocker.patch(
        "api.lead.lead_fetcher.get_lead_information_from_alpha",
        return_value=alpha_info,
    )
    mocker.patch(
        "api.lead.lead_fetcher.get_lead_information_from_beta",
        return_value=beta_info,
    )
    # Call get_lead_information_from_all_sources with the email
    result = get_lead_information_from_all_sources(email="john@doe.com")
    # Assert that the result is the merged lead information
    assert result == LeadInformation(
        full_name="John Doe",
        title="CEO",
        company_name="Company",
        location="California",
        linkedin_url="www.linkedin.com",
        email="john@doe.com",
    ), "The result should be the merged lead information. Also, both alpha_info and beta_info should be called."
