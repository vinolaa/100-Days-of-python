class QuizBrain:
	def __init__(self, q_list):
		self.question_number = 0
		self.questions_list = q_list
		self.score = 0
		self.n_of_questions = 0

	def still_has_questions(self):
		return self.question_number < len(self.questions_list)

	def check_answer(self, answer, correct_a):
		if answer.lower() == correct_a.lower():
			print("You got it right!")
			self.score += 1
			self.n_of_questions += 1
		else:
			print("That's wrong.")
			self.n_of_questions += 1
		print(f"The correct answer was: {correct_a}.")
		print(f"Your current score is: {self.score}/{self.n_of_questions}.\n")

	def final_score(self):
		print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
		print(f"You've finished the quiz. Your final score is: {self.score}/{len(self.questions_list)}")
		print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

	def next_question(self):
		c_question = self.questions_list[self.question_number]
		self.question_number += 1
		answer = input(f"Q.{self.question_number}: {c_question.text}. (True/False)? ")
		self.check_answer(answer, c_question.answer)
