import json
import logging
from typing import List

import pydantic_core
import requests

from app.entities.processed_agent_data import ProcessedAgentData
from app.interfaces.store_gateway import StoreGateway


class StoreApiAdapter(StoreGateway):
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def save_data(self, processed_agent_data_batch: List[ProcessedAgentData]) -> bool:
        request_body_json = [agent_data.model_dump() for agent_data in processed_agent_data_batch]

        response = requests.post(
            f"{self.api_base_url}/agent_data",
            json=request_body_json
        )

        return response.ok
