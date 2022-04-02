from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
	text = item["question"]
	answer = item["correct_answer"]
	question = Question(text, answer)
	question_bank.append(question)

game = QuizBrain(question_bank)

while game.still_has_questions():
	game.next_question()

game.final_score()
