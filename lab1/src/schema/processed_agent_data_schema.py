from marshmallow import Schema, fields
from schema.aggregated_data_schema import AggregatedDataSchema


class ProcessedAgentDataSchema(Schema):
    road_state = fields.Str()
    agent_data = fields.Nested(AggregatedDataSchema)
