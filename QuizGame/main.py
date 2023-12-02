from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

# Fetch the data and form the question bank

question_bank =[]
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question = Question(question_text, question_answer)
    question_bank.append(question)

quizz = QuizzBrain(question_bank)

while quizz.still_has_questions():
    quizz.next_question()
        
print(f"Total Score {quizz.score}/{len(question_bank)}")
