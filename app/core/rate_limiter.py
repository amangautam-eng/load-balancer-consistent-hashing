from collections import defaultdict
from datetime import datetime, timedelta


class RateLimiter:
    def __init__(self, limit=10, window_seconds=60):
        self.limit = limit
        self.window = timedelta(seconds=window_seconds)
        self.requests = defaultdict(list)

    def allow_request(self, ip: str) -> bool:
        now = datetime.now()
        valid_time = now - self.window

        self.requests[ip] = [
            t for t in self.requests[ip]
            if t > valid_time
        ]

        if len(self.requests[ip]) >= self.limit:
            return False

        self.requests[ip].append(now)
        return True

    def reset(self):
        self.requests.clear()


rate_limiter = RateLimiter()