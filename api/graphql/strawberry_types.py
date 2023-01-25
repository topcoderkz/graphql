import strawberry.experimental.pydantic

from api.message_generation.message_models import (
    MessageGenerationResponse,
    MessageGenerationInput,
    InsightsShown,
)
from api.insights.news.news_models import NewsInsight
from api.lead.lead_information import LeadInformation


# This decorator is used to convert a Pydantic model to a Strawberry type
# See https://strawberry.rocks/docs/integrations/pydantic
@strawberry.experimental.pydantic.type(model=LeadInformation, all_fields=True)
class LeadInformationGQL:
    ...


# same for news
@strawberry.experimental.pydantic.type(model=NewsInsight, all_fields=True)
class NewsInsightGQL:
    ...


# same for MessageGeneration and its nested models
@strawberry.experimental.pydantic.type(model=InsightsShown, all_fields=True)
class InsightsShownGQL:
    ...

@strawberry.experimental.pydantic.type(model=MessageGenerationResponse, all_fields=True)
class MessageGenerationResponseGQL:
    ...


# for front end to generate a message, they'll need to pass us this graphql input types
# graphql input types are different from normal graphql response types
# this generates the input types for them to use

@strawberry.experimental.pydantic.type(
    model=NewsInsight, is_input=True, all_fields=True
)
class NewsInsightInputGQL:
    ...

@strawberry.experimental.pydantic.type(
    model=InsightsShown, is_input=True, all_fields=True
)
class InsightsShownInputGQL:
    ...


@strawberry.experimental.pydantic.type(
    model=LeadInformation, is_input=True, all_fields=True
)
class LeadInformationGQLInput:
    ...


@strawberry.experimental.pydantic.type(
    model=MessageGenerationInput, is_input=True, all_fields=True
)
class MessageGenerationInputGQL:
    ...
