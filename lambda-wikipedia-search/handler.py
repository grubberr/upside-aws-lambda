
import pydantic

from wiki import Wiki


class InputModel(pydantic.BaseModel):
    title: str


def lambda_handler(event: dict, context):
    event = InputModel(**event)
    wiki = Wiki()
    return wiki.query(event.title)
