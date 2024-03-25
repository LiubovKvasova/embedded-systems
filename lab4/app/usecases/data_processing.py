from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData
from config import (
    MOVEMENT_NORMAL,
    MOVEMENT_STEEP,
    MOVEMENT_LEANING,
    MOVEMENT_UP,
    MOVEMENT_DOWN,
    MOVEMENT_LEFT,
    MOVEMENT_RIGHT
)

def get_road_status(
    previous_accelerometer_data,
    current_accelerometer_data
) -> str:
    road_state_tags = []

    previous_x = previous_accelerometer_data.x
    previous_y = previous_accelerometer_data.y
    previous_z = previous_accelerometer_data.z
    current_x = current_accelerometer_data.x
    current_y = current_accelerometer_data.y
    current_z = current_accelerometer_data.z

    z_relative_difference = abs(1 - (previous_z / current_z))

    # Change in z axis was detected
    if z_relative_difference > 0.1:
        if z_relative_difference > 0.4:
            road_state_tags.append(MOVEMENT_STEEP)

        road_state_tags.append(MOVEMENT_LEANING)

        x_abs_difference = abs(previous_x - current_x)
        y_abs_difference = abs(previous_y - current_y)

        if x_abs_difference > y_abs_difference:
            movement_direction = MOVEMENT_LEFT if current_x > previous_x else MOVEMENT_RIGHT
        else:
            movement_direction = MOVEMENT_UP if current_y > previous_y else MOVEMENT_DOWN

        road_state_tags.append(movement_direction)

    if len(road_state_tags) == 0:
        return MOVEMENT_NORMAL

    road_state = ' '.join(road_state_tags)
    return road_state

def process_agent_data(
    agent_data: AgentData,
    previous_agent_data: AgentData = None
) -> ProcessedAgentData:
    """
    Process agent data and classify the state of the road surface.
    Parameters:
        agent_data (AgentData): Agent data that containing accelerometer, GPS, and timestamp.
        previous_agent_data (AgentData): Previous agent data that containing accelerometer, GPS, and timestamp. Optional parameter.
    Returns:
        processed_data_batch (ProcessedAgentData): Processed data containing the classified state of the road surface and agent data.
    """
    if previous_agent_data is None:
        road_state = 'beginning'
    else:
        road_state = get_road_status(
            previous_agent_data.accelerometer,
            agent_data.accelerometer
        )

    return ProcessedAgentData(
        road_state=road_state,
        agent_data=agent_data
    )

