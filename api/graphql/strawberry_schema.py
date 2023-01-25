from typing import List

import strawberry

from api.graphql.strawberry_types import (
    LeadInformationGQL,
    NewsInsightGQL,
    MessageGenerationInputGQL,
    MessageGenerationResponseGQL,
)
from api.insights.news.news_fetcher import get_news_for_company
from api.lead.lead_fetcher import get_lead_information_from_all_sources
from api.message_generation.generate_message import (
    generate_message_from_selected,
    save_generated_message,
)
from api.message_generation.message_models import MessageGenerationResponse


@strawberry.type
class Query:
    @strawberry.field
    def lead_information(self, email: str) -> LeadInformationGQL:
        lead_information = get_lead_information_from_all_sources(email)
        # need to convert the LeadInformation to a LeadInformationGQL
        return LeadInformationGQL.from_pydantic(instance=lead_information)

    @strawberry.field
    def news(
        self, company_name: str, news_categories: List[str]
    ) -> List[NewsInsightGQL]:
        news = get_news_for_company(
            company_name=company_name, categories=news_categories
        )
        # need to convert the NewsInsight to a NewsInsightGQL
        return [
            NewsInsightGQL.from_pydantic(instance=news_insight) for news_insight in news
        ]

    @strawberry.field
    def generate_message(
        self, generation_input: MessageGenerationInputGQL
    ) -> MessageGenerationResponseGQL:
        generated_message: MessageGenerationResponse = generate_message_from_selected(
            generation_input=generation_input
        )
        # insert it into the database
        save_generated_message(message_generation=generated_message)
        return MessageGenerationResponseGQL.from_pydantic(instance=generated_message)


@strawberry.type
class Mutation:
    @strawberry.field
    def sample_mutation(self, string: str) -> str:
        return string


graphql_schema = strawberry.Schema(query=Query, mutation=Mutation)
