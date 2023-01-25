from typing import List

from pydantic import BaseModel


class NewsInsight(BaseModel):
    title: str
    description: str
    url: str
    categories: List[str] # Finite set of categories


