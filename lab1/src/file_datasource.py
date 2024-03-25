from csv import reader
from datetime import datetime
from domain.accelerometer import Accelerometer
from domain.gps import Gps
from domain.parking import Parking
from domain.aggregated_data import AggregatedData
import config


class FileDatasource:
    def __init__(
        self,
        accelerometer_filename: str,
        gps_filename: str,
        parking_filename: str
    ) -> None:
        # Save filenames to attributes
        self.accelerometer_filename = accelerometer_filename
        self.gps_filename = gps_filename
        self.parking_filename = parking_filename

        # Reading flags
        self.accelerometer_stream_alive = True
        self.gps_stream_alive = True
        self.parking_stream_alive = True

    def readAccelerometerData(self) -> Accelerometer:
        if self.accelerometer_stream_alive:
            try:
                accelerometer_line = next(self.accelerometer_reader)
                return Accelerometer(*accelerometer_line)
            except:
                self.accelerometer_stream_alive = False

        # Default value
        return Accelerometer(1, 2, 3)

    def readGpsData(self) -> Gps:
        if self.gps_stream_alive:
            try:
                gps_line = next(self.gps_reader)
                return Gps(*gps_line)
            except:
                self.gps_stream_alive = False

        # Default value
        return Gps(4, 5)

    def readParkingData(self) -> Parking:
        gps_data = self.readGpsData()

        if self.parking_stream_alive:
            try:
                parking_line = next(self.parking_reader)
                return Parking(*parking_line, gps_data)
            except:
                self.parking_stream_alive = False

        # Default value
        return Parking(6, gps_data)

    def read(self) -> AggregatedData:
        """Метод повертає дані отримані з датчиків"""
        accelerometer_data = self.readAccelerometerData()
        # parking_data = self.readParkingData()
        gps_data = self.readGpsData()

        agent_data = AggregatedData(
            config.USER_ID,
            accelerometer_data,
            gps_data,
            datetime.now(),
        )

        return agent_data

    def startReading(self, *args, **kwargs):
        """Метод повинен викликатись перед початком читання даних"""
        # Accelerometer data
        self.accelerometer_file_stream = open(self.accelerometer_filename)
        self.accelerometer_reader = reader(self.accelerometer_file_stream)
        # Skip header line
        next(self.accelerometer_reader)

        # GPS data
        self.gps_file_stream = open(self.gps_filename)
        self.gps_reader = reader(self.gps_file_stream)
        next(self.gps_reader)

        # Parking data
        self.parking_file_stream = open(self.parking_filename)
        self.parking_reader = reader(self.parking_file_stream)
        next(self.parking_reader)

    def stopReading(self, *args, **kwargs):
        """Метод повинен викликатись для закінчення читання даних"""
        # Close file readers
        self.accelerometer_file_stream.close()
        self.gps_file_stream.close()
        self.parking_file_stream.close()
