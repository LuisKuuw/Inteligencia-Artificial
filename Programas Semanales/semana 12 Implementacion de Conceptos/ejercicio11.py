class DTAgent(agents.Agent):


    def __init__(self, belief_state):
        agents.Agent.__init__(self)

        def program(percept):
            belief_state.observe(action, percept)
            program.action = argmax(belief_state.actions(),
                                    belief_state.expected_outcome_utility)
            return program.action

        program.action = None
        self.program = program