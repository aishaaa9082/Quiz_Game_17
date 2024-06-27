from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_qn = Question(question_text, question_answer)
    question_bank.append(new_qn)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\nYou've completed the quiz!")
print(f"You're final score is: {quiz.score}/{len(question_bank)}")
