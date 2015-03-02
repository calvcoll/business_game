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

import csv
class QuestionImporter:
  def import_questions(file='questions.csv'):
    reader = csv.reader(open(file), delimiter='|')
    questions = []
    for question in reader:
      questions.append(Question({'title' : question[0],
                'answer' : question[1], 'a1' : question[2],
                'a2' : question[3], 'a3' : question[4],
                'a4' : question[5]}))
    return questions
