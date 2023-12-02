from question_model import Question

# TODO Asking the questions
# TODO checking if the answer was correct
# TODO checking if we are at the end of the quizz.

class QuizzBrain:

    def __init__(self, q_question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_question_list

    def still_has_questions(self):
        no_of_questions = len(self.question_list)
        if self.question_number < no_of_questions:
            return True
        else:
            return False
        
    # Retrieve the item of the current question number from the question_list
    # Use input() function to show the user Question text and ask for the user's answer
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Your are correct")
        else:
            print("Your are wrong")

    


