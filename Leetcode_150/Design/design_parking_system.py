# Leetcode Problem 1603: Design Parking System


class ParkingSystem:
    """Track available spaces for three parking-spot sizes."""

    def __init__(self, big, medium, small):
        self.spaces = [0, big, medium, small]

    def add_car(self, car_type):
        if self.spaces[car_type] == 0:
            return False
        self.spaces[car_type] -= 1
        return True


if __name__ == "__main__":
    parking = ParkingSystem(1, 1, 0)
    print(f"Large car accepted: {parking.add_car(1)}")