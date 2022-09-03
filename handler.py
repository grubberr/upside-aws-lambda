
import traceback

import pydantic

from wiki import Wiki, WikiException


class InputModel(pydantic.BaseModel):
    title: str


def hello(event: dict, context):
    try:
        event = InputModel(**event)
        wiki = Wiki()
        return wiki.query(event.title)
    except pydantic.ValidationError as e:
        return {"error": str(e)}
    except WikiException as e:
        return str(e)
    except Exception as e:
        return {"error": traceback.format_exception(e)}
