def policy_evaluation(policy, environment, discount_factor=1.0, theta=1e-9, max_iterations=1e9):

    evaluation_iterations = 1

    V = np.zeros(environment.nS)

    for i in range(int(max_iterations)):

        delta = 0

        for state in range(environment.nS):

            v = 0

            for action, action_probability in enumerate(policy[state]):

                for state_probability, next_state, reward, terminated in environment.P[state][action]:

                    v += action_probability * state_probability * (reward + discount_factor * V[next_state])


            delta = max(delta, np.abs(V[state] - v))

            V[state] = v
        evaluation_iterations += 1


        if delta < theta:
            print(f'Policy evaluated in {evaluation_iterations} iterations.')
            return V