import random
from collections import defaultdict
from fastapi import APIRouter

from app.services.balancer_service import (
    balancer_service,
)


router = APIRouter()


@router.get("/route")
def route_request():
    ip = ".".join(
        str(random.randint(0, 255))
        for _ in range(4)
    )

    return balancer_service.route_request(ip)


@router.get("/nodes")
def get_nodes():
    return balancer_service.get_nodes()


@router.get("/metrics")
def get_metrics():
    return balancer_service.get_metrics()


@router.get("/logs")
def get_logs():
    return balancer_service.get_logs()


@router.post("/nodes/{node_name}/down")
def mark_node_down(node_name: str):
    target = None

    for node in balancer_service.nodes:
        if node.name == node_name:
            target = node
            break

    if target is None:
        return {
            "success": False,
            "message": "Node not found",
        }

    target.mark_unhealthy()
    balancer_service.algorithm.remove_node(target)

    return {
        "success": True,
        "message": f"{node_name} removed from ring",
    }


@router.post("/nodes/{node_name}/up")
def mark_node_up(node_name: str):
    target = None

    for node in balancer_service.nodes:
        if node.name == node_name:
            target = node
            break

    if target is None:
        return {
            "success": False,
            "message": "Node not found",
        }

    target.mark_healthy()
    balancer_service.algorithm.add_node(target)

    return {
        "success": True,
        "message": f"{node_name} added back to ring",
    }


@router.get("/simulate")
def simulate(n: int = 100):
    distribution = defaultdict(int)

    for _ in range(n):
        ip = ".".join(
            str(random.randint(0, 255))
            for _ in range(4)
        )

        result = balancer_service.route_request(ip)

        if result["success"]:
            distribution[result["routed_to"]] += 1

    return {
        "requests": n,
        "distribution": dict(distribution),
    }