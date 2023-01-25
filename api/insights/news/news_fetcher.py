import random
import time
from typing import List

from api.insights.news.news_models import NewsInsight


def get_news_for_company(company_name: str, categories: List[str]) -> List[NewsInsight]:
    # This mocks a db call
    # sleep for 1 to 2 seconds randomly to simulate a slow db call
    # Pretend that it does filter by categories
    time.sleep(random.randint(1, 2))
    return [
        NewsInsight(
            title=f"{company_name} raises $100M",
            url="https://www.google.com",
            categories=["funding"],
            description="Company raises $100M",
        ),
        NewsInsight(
            title=f"{company_name} acquires company",
            url="https://www.google.com",
            categories=["acquisition"],
            description="Company acquires company",
        ),
    ]
