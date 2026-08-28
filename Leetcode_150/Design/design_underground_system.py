# Leetcode Problem 1396: Design Underground System


class UndergroundSystem:
    """Track average travel times between subway stations."""

    def __init__(self):
        self.check_ins = {}
        self.trips = {}

    def check_in(self, customer_id, station, timestamp):
        self.check_ins[customer_id] = (station, timestamp)

    def check_out(self, customer_id, station, timestamp):
        start, start_time = self.check_ins.pop(customer_id)
        route = (start, station)
        total, count = self.trips.get(route, (0, 0))
        self.trips[route] = (total + timestamp - start_time, count + 1)

    def get_average_time(self, start, end):
        total, count = self.trips[(start, end)]
        return total / count


if __name__ == "__main__":
    system = UndergroundSystem()
    system.check_in(1, "A", 3)
    system.check_out(1, "B", 8)
    print(f"Average travel time: {system.get_average_time('A', 'B')}")