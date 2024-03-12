from dataclasses import dataclass

from domain.aggregated_data import AggregatedData


@dataclass
class ProcessedAgentData:
    road_state: str
    agent_data: AggregatedData
