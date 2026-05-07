from app.models.node import Node
from app.algorithms.consistent_hash import (
    ConsistentHashLoadBalancer,
)


def test_same_ip_same_node():
    lb = ConsistentHashLoadBalancer()

    node1 = Node("Node-A")
    node2 = Node("Node-B")

    lb.add_node(node1)
    lb.add_node(node2)

    ip = "192.168.1.1"

    first = lb.select_node(ip)
    second = lb.select_node(ip)

    assert first.name == second.name