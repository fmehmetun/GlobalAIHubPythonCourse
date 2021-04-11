# 1 - Final project, knowledge competition
import random

# Question-answer pairs
QA_pairs = [
	{
		"question": "What's the name of the celestial body that excluded from list of solar system planets by IAU at 2006?",
		"answer": "Pluto"
	},
	{
		"question": "Which high-level programming language is used to program this competition?",
		"answer": "Python"
	},
	{
		"question": "What's the distance between Earth and Sun (approximately) in kilometers?",
		"answer": "150.000.000"
	},
	{
		"question": "What's was the name of the space mission that first landed humans on the Moon?",
		"answer": "Apollo 11"
	},
	{
		"question": "What's the speed of light (approximately) in kilometers per second?",
		"answer": "300.000"
	},
	{
		"question": "What's the name of the planet that is closest to Sun?",
		"answer": "Mercury"
	},
	{
		"question": "Who created Python programming language?",
		"answer": "Guido van Rossum"
	},
	{
		"question": "What's the name of the Python module/framework that lets us create, store and manipulate n-dimensional arrays?",
		"answer": "NumPy"
	},
	{
		"question": "What's the name of the Python framework that's developed by Google and let's us develop, train and deploy machine learning models?",
		"answer": "TensorFlow"
	},
	{
		"question": "What's the terminology used for describing 2-dimensional arrays in Mathematics?",
		"answer": "Matrix"
	}
]

# Competition entry
input("--- Welcome to competition, you have to answer %d questions in total ---\n\tpress enter to start, you can quit by answering 'exit'..." % (len(QA_pairs)))

# Shuffle question-answer list.
random.shuffle(QA_pairs)

# Competition loop
totalPoints = 0
everyQuestionPoint = 10
for questionIdx in range(len(QA_pairs)):
	print("\n[*] Current point: %d" % (totalPoints))

	# Get next question-answer pair.
	currentQA = QA_pairs[questionIdx]

	# Get answer from user.
	print(
		"[Question %d/%d] %s" % (questionIdx+1, len(QA_pairs), currentQA["question"])
	)
	userAnswer = input("[Answer] ")

	# Exit condition.
	if userAnswer == "exit":
		break

	## Check if answer is correct.
	
	# Not using .lower() or like anything for case sensitivity.
	# Answers are already capitalized while creating the dictionary, so I'm expecting competitor to capitalize their words.
	if userAnswer == currentQA["answer"]:
		print("[+] Your answer is correct! You got %d points." % (everyQuestionPoint))
		totalPoints += everyQuestionPoint
	else:
		print("[x] Your answer is not correct.")

win_threshold_question_count = (len(QA_pairs) // 2)

# Print competition results.
userHasWon = (totalPoints > int(win_threshold_question_count*everyQuestionPoint))
input(
	"\n[***] End of the competition, you %s! Final points: %d\n\tpress enter to exit..." % (
		# lost or won string determined by one line if condition
		("won" if userHasWon else "lost"),
		totalPoints
	)
)
