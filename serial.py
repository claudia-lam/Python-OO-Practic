class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """
        create serial generator beginning at start
        """
        self.start = start
        self.counter = 0

    def generate(self):
        """
        return a new sequential number
        """
        current_counter = self.counter
        self.counter += 1
        return self.start + current_counter

    def reset(self):
        """
        reset the current number back to 0
        """
        self.counter = 0
