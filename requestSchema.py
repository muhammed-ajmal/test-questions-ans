from fastapi import requests
from marshmallow import fields, Schema

class EventTypes(fields.EnumType):
    page_view = "page_view"

class Browsers(fields.EnumType):
    chrome = "chrome"

class MetaDataSchema(Schema):
    page : str = fields.String(required=True)
    browser: str = fields.Enum(Browsers)

class AnalyticsRequest(requests.Request):
    event_type  = fields.Enum(EventTypes, required=True)
    timestamp = fields.DateTime()
    metadata = MetaDataSchema()
