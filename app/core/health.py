from typing import List
from app.models.node import Node


class HealthManager:
    def get_healthy_nodes(self, nodes: List[Node]) -> List[Node]:
        return [node for node in nodes if node.healthy]

    def mark_unhealthy(self, nodes: List[Node], node_name: str):
        for node in nodes:
            if node.name == node_name:
                node.mark_unhealthy()
                return True
        return False

    def mark_healthy(self, nodes: List[Node], node_name: str):
        for node in nodes:
            if node.name == node_name:
                node.mark_healthy()
                return True
        return False

    def has_healthy_nodes(self, nodes: List[Node]) -> bool:
        return any(node.healthy for node in nodes)


health_manager = HealthManager()