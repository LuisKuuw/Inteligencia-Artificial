import random

def evaluate_predictions(y_test, yhat):
	return accuracy_score(y_test, yhat)

def random_predictions(n_examples):
	return [random.randint(0, 1) for _ in range(n_examples)]

def random_predictions(n_examples):
	return [random.randint(0, 1) for _ in range(n_examples)]
def montaña(X_test, y_test, max_iterations):
	scores = list()
	solution = random_predictions(X_test.shape[0])
	score = evaluate_predictions(y_test, solution)
	scores.append(score)
	for i in range(max_iterations):
		scores.append(score)
		if score == 1.0:
			break

		candidate = modify_predictions(solution)

		value = evaluate_predictions(y_test, candidate)

		if value >= score:
			solution, score = candidate, value
			print('>%d, score=%.3f' % (i, score))
	return solution, scores

