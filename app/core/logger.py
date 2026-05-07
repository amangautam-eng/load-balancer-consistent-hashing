from datetime import datetime


class RequestLogger:
    def __init__(self):
        self.logs = []

    def log(self, ip: str, node: str, algorithm: str):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "ip": ip,
            "node": node,
            "algorithm": algorithm,
        }

        self.logs.append(entry)

        print(
            f"[LOG] {entry['timestamp']} | "
            f"IP={ip} | "
            f"NODE={node} | "
            f"ALGO={algorithm}"
        )

    def get_logs(self):
        return self.logs

    def clear(self):
        self.logs.clear()


logger = RequestLogger()