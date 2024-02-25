from marshmallow import Schema, fields
from schema.accelerometer_schema import AccelerometerSchema
from schema.parking_schema import ParkingSchema


class AggregatedDataSchema(Schema):
    accelerometer = fields.Nested(AccelerometerSchema)
    parking = fields.Nested(ParkingSchema)
    timestamp = fields.DateTime("iso")
    user_id = fields.Int()
