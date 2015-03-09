import random

class Question:
  def __init__(self, question_dict):
    self.title = question_dict['title']
    self.answer = question_dict['answer']
    self.a1 = question_dict['a1']
    self.a2 = question_dict['a2']
    self.a3 = question_dict['a3']
    self.a4 = question_dict['a4']

  def get_answers(self):
    return [self.a1,self.a2,self.a3,self.a4]

  def get_title(self):
    return self.title

  def get_correct_answer(self):
    return self.answer

import csv,os.path,time
class QuestionImporter:
  def import_questions(self, file='questions.csv'):
    reader = csv.reader(open(file), delimiter='|')
    questions = []
    for question in reader:
      questions.append(Question({'title' : question[0],
                'answer' : question[1], 'a1' : question[2],
                'a2' : question[3], 'a3' : question[4],
                'a4' : question[5]}))
    return questions

  def new_seed(self):
    return int(round(time.time() * 1000))

  def import_random_questions(self, amount=15):
    questions = self.import_questions()
    q_list = []
    seed = self.new_seed()
    for i in range(amount):
      num = random.randint(0,len(questions)-1)
      while num in q_list:
        num = random.randint(0,len(questions)-1)
      q_list.append(num)
    questions_returned = []
    for num in q_list:
      questions_returned.append(questions[num])
    return questions_returned
