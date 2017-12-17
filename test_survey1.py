import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
	def setUp(self):
		question="What language did you first learn to speak?"
		self.my_survey=AnonymousSurvey(question)
		self.answers=['English','Chinese','Japanese']
	def test_store_single_reponse(self):
		self.my_survey.store_response(self.answers[0])
		self.assertIn(self.answers[0], self.my_survey.responses)
	def test_three_responses(self):
		for answer in self.answers:
			self.my_survey.store_response(answer)
		for answer in self.answers:
			self.assertIn(answer,self.my_survey.responses)

unittest.main
