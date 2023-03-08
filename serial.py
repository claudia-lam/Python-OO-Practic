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
        create serial generator with serial number beginning at start
        """
        self.start = start
        self.counter = 0

    def __repr__(self):
        return (f"<SerialGenerator start={self.start} next={self.start + self.counter + 2}>")

    def generate(self):
        """
        return a new serial number in sequence after the previously generated
        serial number
        """
        current_counter = self.counter
        self.counter += 1
        return self.start + current_counter

    def reset(self):
        """
        reset the current serial number counter back to 0
        """
        self.counter = 0

