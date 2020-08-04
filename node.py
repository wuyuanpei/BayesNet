class Node():
    """ A node in the BN"""

    def __init__(self, name, values, parents, children):
        """ name: string            the name of the random variable
            values: list            possible outcomes of the random variable
            parents: list of Node   parents of the node
            children: list of Node  children of the node"""

        self.name = name
        self.values = values
        self.parents = parents
        self.children = children

    
