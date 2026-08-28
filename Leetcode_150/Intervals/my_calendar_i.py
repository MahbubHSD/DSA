# Leetcode Problem 729: My Calendar I


class MyCalendar:
    """Book non-overlapping half-open calendar intervals."""

    def __init__(self):
        self.bookings = []

    def book(self, start, end):
        if any(start < existing_end and end > existing_start for existing_start, existing_end in self.bookings):
            return False
        self.bookings.append((start, end))
        return True


if __name__ == "__main__":
    calendar = MyCalendar()
    print(f"Booking accepted: {calendar.book(10, 20)}")