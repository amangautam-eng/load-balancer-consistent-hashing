# Consistent Hash Load Balancer

A beginner-friendly production-style Load Balancer built in Python using FastAPI.

## Features

- Consistent Hashing
- Virtual Nodes
- Weighted Routing
- Node Health Checks
- Add / Remove Nodes Dynamically
- Request Logging
- Metrics Dashboard
- Rate Limiting
- Traffic Simulation Endpoint
- Unit Tests

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pytest

## Project Structure

load_balancer/
│
├── app/
│   ├── algorithms/
│   ├── api/
│   ├── core/
│   ├── models/
│   └── services/
│
├── tests/
├── requirements.txt
├── README.md
└── run.py

## Installation

pip install -r requirements.txt

## Run

python run.py

## Open API Docs

http://localhost:8000/docs

## Endpoints

GET /route
GET /nodes
GET /metrics
GET /logs
POST /nodes/{node_name}/down
POST /nodes/{node_name}/up
GET /simulate?n=1000

## Example

GET /simulate?n=1000

Response:

{
  "requests": 1000,
  "distribution": {
    "Node-A": 503,
    "Node-B": 332,
    "Node-C": 165
  }
}

## Main Learning

This project demonstrates:

- Hashing
- Binary Search
- Consistent Hashing
- Virtual Nodes
- Weighted Load Balancing
- Health-aware Routing
- Rate Limiting
- Backend API Design