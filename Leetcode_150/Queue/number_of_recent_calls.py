# Leetcode Problem 933: Number of Recent Calls


class RecentCounter:
    """Count requests received during the latest 3000 milliseconds."""

    def __init__(self):
        from collections import deque

        self.requests = deque()

    def ping(self, timestamp):
        self.requests.append(timestamp)
        while self.requests[0] < timestamp - 3000:
            self.requests.popleft()
        return len(self.requests)


if __name__ == "__main__":
    counter = RecentCounter()
    print(f"Requests at 3001: {counter.ping(3001)}")