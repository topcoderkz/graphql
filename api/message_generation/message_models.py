from typing import List, Optional

from pydantic import BaseModel

from api.insights.news.news_models import NewsInsight
from api.lead.lead_information import LeadInformation


class InsightsShown(BaseModel):
    # We need to track which insights are shown to the user
    news_shown: List[NewsInsight]
    news_selected: List[NewsInsight]
    # We need to track the filters that the user selected
    news_filters_used: List[str]

class MessageGenerationResponse(BaseModel):
    uuid: str
    message: str
    lead_information: LeadInformation
    insights: InsightsShown


class MessageGenerationInput(BaseModel):
    insights_shown: InsightsShown
    lead_information: LeadInformation
