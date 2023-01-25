from api.graphql.strawberry_types import MessageGenerationInputGQL
from api.message_generation.message_models import MessageGenerationResponse, MessageGenerationInput


def generate_message_from_selected(
    generation_input: MessageGenerationInputGQL,
) -> MessageGenerationResponse:
    # convert to a pydantic model
    converted: MessageGenerationInput = generation_input.to_pydantic()
    # This a mock function that generates a message from the insights shown
    uuid = "1234"
    message = f"""
    To: {converted.lead_information.email}
    Subject: {converted.lead_information.company_name} is hiring!
    Body: This is a message using {converted.insights_shown.news_shown}
    """
    return MessageGenerationResponse(
        uuid=uuid,
        message=message,
        lead_information=converted.lead_information,
        insights=converted.insights_shown,
    )


def save_generated_message(message_generation: MessageGenerationResponse) -> None:
    # This is a mock function that saves the generated message.
    # You don't need to implement this function
    print(f"Saved message {message_generation.uuid}")
