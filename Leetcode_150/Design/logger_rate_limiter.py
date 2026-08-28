# Leetcode Problem 359: Logger Rate Limiter


class Logger:
    """Allow a message only once during each ten-second interval."""

    def __init__(self):
        self.last_printed = {}

    def should_print_message(self, timestamp, message):
        if timestamp - self.last_printed.get(message, -10) >= 10:
            self.last_printed[message] = timestamp
            return True
        return False


if __name__ == "__main__":
    logger = Logger()
    print(f"Print message: {logger.should_print_message(1, 'foo')}")