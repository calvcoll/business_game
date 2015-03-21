import unittest
import questions
import time

class TestQuestions(unittest.TestCase):
  def test_questions(self):
    question = questions.Question({'title' : 't', 'answer' : 'a','a1' : 'a1', 'a2' : 'a2', 'a3' : 'a3', 'a4' : 'a4'})
    self.assertEqual(question.get_title(), 't')
    self.assertEqual(question.get_answers(), ['a1','a2','a3','a4'])
    self.assertEqual(question.get_correct_answer(), 'a')

  def id(self):
    return 'Question tests'

  def shortDescription(self):
    return 'Test the questions'

class TestQuestionImporter(unittest.TestCase):
  def test_importer(self):
    question = questions.Question({'title' : 't', 'answer' : 'a','a1' : 'a1', 'a2' : 'a2', 'a3' : 'a3', 'a4' : 'a4'})
    iquestion = questions.QuestionImporter().import_questions('tests/test_questions.csv')[0]
    self.assertEqual(iquestion.get_title(), question.get_title())
    self.assertEqual(iquestion.get_answers(), question.get_answers())
    self.assertEqual(iquestion.get_correct_answer(), question.get_correct_answer())

  def id(self):
    return 'Question Importer tests'

  def shortDescription(self):
    return 'Test the importer'

class TestSeed(unittest.TestCase):
  def test_importer(self):
    seed1 = questions.QuestionImporter().new_seed()
    time.sleep(0.001)
    seed2 = questions.QuestionImporter().new_seed()
    self.assertNotEqual(seed1,seed2)

  def id(self):
    return 'Seed gen/save test'

  def shortDescription(self):
    return 'Test the seed code'
