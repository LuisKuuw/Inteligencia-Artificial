def __init__(self, KB):
    t = 0
    def program(percept):
        KB.tell(self.make_percept_sentence(percept, t))
        action = KB.ask(self.make_action_query(t))
        KB.tell(self.make_action_sentence(action, t))
        t = t + 1
        return action
    self.program = program
