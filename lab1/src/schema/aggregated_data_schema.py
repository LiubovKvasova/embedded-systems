from marshmallow import Schema, fields
from schema.accelerometer_schema import AccelerometerSchema
# from schema.parking_schema import ParkingSchema
from schema.gps_schema import GpsSchema


class AggregatedDataSchema(Schema):
    user_id = fields.Int()
    accelerometer = fields.Nested(AccelerometerSchema)
    # parking = fields.Nested(ParkingSchema)
    gps = fields.Nested(GpsSchema)
    timestamp = fields.DateTime("iso")
