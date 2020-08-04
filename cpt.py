class CPT():
    """ Conditional Probability Table"""
    
    def __init__(self, rv, parents):
        """ rv: Variable                 the random variable
            parents: list of Variable    all the condition variables
        """
        
        self.table = dict()
        self.parents = parents
        self.rv = rv

        def add_dict(i, tmp):
            for outcome in parents[i].outcomes():
                if i < len(parents) - 1:
                    tmp[outcome] = dict()
                    add_dict(i + 1, tmp[outcome])
                else:
                    tmp[outcome] = dict()
                    for rv_outcome in rv.outcomes():
                        tmp[outcome][rv_outcome] = 1 / rv.num_outcomes() #assume uniform distribution initially
        
        add_dict(0, self.table)
        
    def size(self):
        """ size of the table """
        size = 1
        for parent in self.parents:
            size *= parent.num_outcomes()

        size *= self.rv.num_outcomes()
        return size

    def assign_prob(self, prob, rv_value, parents_values):
        """ prob: float        probability
            rv_value: value    the outcome of rv
            parents_values: list of values  the outcomes of the parents
        """
        tmp = self.table
        for p_value in parents_values:
            tmp = tmp[p_value]

        tmp[rv_value] = prob

    def get_prob(self, rv_value, parents_values):
        """
            rv_value: value    the outcome of rv
            parents_values: list of values  the outcomes of the parents
        """
        tmp = self.table
        for p_value in parents_values:
            tmp = tmp[p_value]

        return tmp[rv_value]
    

from variable import Variable
rv1 = Variable("A",["T","F"])
rv2 = Variable("B",["a","b","c"])
rv3 = Variable("C",["d","e","f"])
rv4 = Variable("D",["g","h"])
cpt = CPT(rv1, [rv2, rv3, rv4])
print(str(cpt))
print(cpt.size())
cpt.assign_prob(0.2, "T", ["a", "e", "h"])
print(cpt.table)
