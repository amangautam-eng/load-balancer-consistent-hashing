import hashlib
import bisect
from app.models.node import Node


class ConsistentHashLoadBalancer:
    def __init__(self, replicas: int = 100):
        self.replicas = replicas
        self.ring = {}
        self.sorted_keys = []

    def _hash(self, key: str) -> int:
        return int(
            hashlib.md5(key.encode()).hexdigest(),
            16
        )

    def add_node(self, node: Node):
        total_replicas = self.replicas * node.weight

        for i in range(total_replicas):
            virtual_key = f"{node.name}#{i}"
            hashed_key = self._hash(virtual_key)

            self.ring[hashed_key] = node
            bisect.insort(self.sorted_keys, hashed_key)

    def remove_node(self, node: Node):
        total_replicas = self.replicas * node.weight

        for i in range(total_replicas):
            virtual_key = f"{node.name}#{i}"
            hashed_key = self._hash(virtual_key)

            if hashed_key in self.ring:
                del self.ring[hashed_key]

            index = bisect.bisect_left(
                self.sorted_keys,
                hashed_key
            )

            if (
                index < len(self.sorted_keys)
                and self.sorted_keys[index] == hashed_key
            ):
                self.sorted_keys.pop(index)

    def select_node(self, ip: str):
        if not self.sorted_keys:
            return None

        hashed_ip = self._hash(ip)

        index = bisect.bisect(
            self.sorted_keys,
            hashed_ip
        )

        index = index % len(self.sorted_keys)

        checked = 0

        while checked < len(self.sorted_keys):
            selected_key = self.sorted_keys[index]
            node = self.ring[selected_key]

            if node.healthy:
                return node

            index = (
                index + 1
            ) % len(self.sorted_keys)

            checked += 1

        return None