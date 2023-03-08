class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Create a WordFinder from words located at path"""
        self.path = path
        self.words = self.get_words()

    # def __repr__(self):
    #     return f"<path= {path}"

    def get_words(self):
        """Read file at path and return list of words from text"""
        file = open(self.path)
        text = file.read()
        words = text.split("\n") #use strip, \n isn't always new line
        print(f"{len(words)} words read")
        return words

    def random(self):
        """Return a random word from the list of words"""
        from random import choice #move into global space
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words from a dictionary
    uses blank lines and # symbols for comments"""

    def __init__(self, path):
        """Create new Special Word Finder from file with comments/blank lines"""
        super().__init__(path)
        self.words = self.filter_out(self.words)

    def filter_out(self, words): #could use polymorphism with super().get_words
        """Take word list and return new version with comments and blank lines
        filtered out"""
        # parent_words = super().get_words()
        return [word for word in words if word != "" and
                not word.startswith("#")]


