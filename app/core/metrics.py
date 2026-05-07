from collections import defaultdict


class Metrics:
    def __init__(self):
        self.total_requests = 0
        self.node_hits = defaultdict(int)
        self.failed_requests = 0

    def record_hit(self, node_name: str):
        self.total_requests += 1
        self.node_hits[node_name] += 1

    def record_failure(self):
        self.failed_requests += 1

    def get_metrics(self):
        return {
            "total_requests": self.total_requests,
            "failed_requests": self.failed_requests,
            "node_hits": dict(self.node_hits),
        }

    def reset(self):
        self.total_requests = 0
        self.node_hits.clear()
        self.failed_requests = 0


metrics = Metrics()