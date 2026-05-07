from app.models.node import Node


def test_mark_unhealthy():
    node = Node("Node-A")

    node.mark_unhealthy()

    assert node.healthy is False