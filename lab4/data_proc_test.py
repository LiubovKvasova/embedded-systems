from app.entities.agent_data import AgentData, GpsData, AccelerometerData
from datetime import datetime
from app.usecases.data_processing import process_agent_data

if __name__ == '__main__':
    agent_a = AgentData(user_id=0, accelerometer=AccelerometerData(x=-17, y=4, z=15682), gps=GpsData(latitude=1, longitude=1), timestamp=datetime.now())
    agent_b = AgentData(user_id=0, accelerometer=AccelerometerData(x=-58, y=114, z=12182), gps=GpsData(latitude=1, longitude=1), timestamp=datetime.now())
    agent_c = AgentData(user_id=0, accelerometer=AccelerometerData(x=379, y=31, z=7520), gps=GpsData(latitude=1, longitude=1), timestamp=datetime.now())
    agent_d = AgentData(user_id=0, accelerometer=AccelerometerData(x=-112, y=-318, z=2689), gps=GpsData(latitude=1, longitude=1), timestamp=datetime.now())

    print(process_agent_data(agent_a))
    print(process_agent_data(agent_b, agent_a))
    print(process_agent_data(agent_c, agent_b))
    print(process_agent_data(agent_d, agent_c))
