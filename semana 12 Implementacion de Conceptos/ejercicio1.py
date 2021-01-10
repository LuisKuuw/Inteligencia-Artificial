def __init__(self, table):
    percepts = []
    def program(percept):
        percepts.append(percept)
        action = table.get(tuple(percepts))
        return action
    self.program = program