from dataclasses import dataclass

from datetime import datetime
from domain.accelerometer import Accelerometer
from domain.gps import Gps
from domain.parking import Parking


@dataclass
class AggregatedData:
    accelerometer: Accelerometer
    parking: Parking
    timestamp: datetime
    user_id: int
