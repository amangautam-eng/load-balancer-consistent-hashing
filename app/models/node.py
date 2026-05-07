from dataclasses import dataclass


@dataclass
class Node:
    name: str
    weight: int = 1
    healthy: bool = True
    active_connections: int = 0
    requests_served: int = 0

    def increment_connections(self):
        self.active_connections += 1

    def decrement_connections(self):
        if self.active_connections > 0:
            self.active_connections -= 1

    def increment_requests(self):
        self.requests_served += 1

    def mark_unhealthy(self):
        self.healthy = False

    def mark_healthy(self):
        self.healthy = True

    def to_dict(self):
        return {
            "name": self.name,
            "weight": self.weight,
            "healthy": self.healthy,
            "active_connections": self.active_connections,
            "requests_served": self.requests_served,
        }