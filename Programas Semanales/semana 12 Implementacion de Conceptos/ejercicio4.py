def hill_climbing(problem):
    current = Node(problem.initial)
    while True:
        neighbor = argmax(expand(node, problem), Node.value)
        if neighbor.value() <= current.value():
            return current.state
        current = neighbor