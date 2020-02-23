"""Tasks for checking knowledge about classes."""


class BaseProcessor:
    """Checks if student can use ABC package.

    Using the ABC package mark this class and its `process` function
    to be abstract.
    """

    def __init__(self):
        """Inits BaseClass."""
        self._num_processed = 0

    def process(self, item: int) -> int:
        """Maps each given integer value to a new integer value."""
        pass

    def num_processed(self) -> int:
        """Retrieved the number of processed items."""
        return self._num_processed


class MultiplyingProcessor:
    """Checks if the student can use inheritance.

    Modify this class to inherit from the `BaseProcessor` class.
    Implement the `process` function to it multiplies each item by `a` and
    it increments the number of processed items.
    Override `num_processed` method from base class and if the are no
    processed items yet, then print following message: 'NO ITEMS PROCESSED',
    then call the base class implementation for this method.
    """

    def __init__(self, a):
        """Inits MultiplyingProcessor."""
        self._a = a

