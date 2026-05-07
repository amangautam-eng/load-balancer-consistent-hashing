from app.models.node import Node
from app.algorithms.consistent_hash import (
    ConsistentHashLoadBalancer,
)
from app.core.logger import logger
from app.core.metrics import metrics
from app.core.rate_limiter import rate_limiter
from app.core.health import health_manager


class BalancerService:
    def __init__(self):
        self.nodes = []
        self.algorithm = ConsistentHashLoadBalancer()

        self._initialize_nodes()

    def _initialize_nodes(self):
        default_nodes = [
            Node("Node-A", weight=3),
            Node("Node-B", weight=2),
            Node("Node-C", weight=1),
        ]

        for node in default_nodes:
            self.nodes.append(node)
            self.algorithm.add_node(node)

    def route_request(self, ip: str):
        if not rate_limiter.allow_request(ip):
            metrics.record_failure()

            return {
                "success": False,
                "message": "Rate limit exceeded",
            }

        if not health_manager.has_healthy_nodes(self.nodes):
            metrics.record_failure()

            return {
                "success": False,
                "message": "No healthy nodes available",
            }

        node = self.algorithm.select_node(ip)

        if node is None:
            metrics.record_failure()

            return {
                "success": False,
                "message": "Routing failed",
            }

        node.increment_requests()
        node.increment_connections()

        metrics.record_hit(node.name)

        logger.log(
            ip=ip,
            node=node.name,
            algorithm="consistent_hash",
        )

        node.decrement_connections()

        return {
            "success": True,
            "ip": ip,
            "routed_to": node.name,
        }

    def get_nodes(self):
        return [node.to_dict() for node in self.nodes]

    def get_metrics(self):
        return metrics.get_metrics()

    def get_logs(self):
        return logger.get_logs()


balancer_service = BalancerService()