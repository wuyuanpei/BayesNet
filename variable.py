class Variable():
    """ A random variable"""

    def __init__(self, name, values):
        """ name: string            the name of the random variable
            values: list            possible outcomes of the random variable
        """

        self.name = name
        self.values = values

    def get_name(self):
        return self.name

    def num_outcomes(self):
        """ Number of outcomes of the random variable """
        return len(self.values)

    def outcomes(self):
        """ return the list of outcomes"""
        return self.values

# rv = Variable("A",["T","F"])
# print(rv.num_outcomes())
