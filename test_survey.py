import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
	def test_store_single_reponse(self):
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		my_survey.store_response('English')
		self.assertIn('English', my_survey.responses)

	def test_three_responses(self):
		question = "What languages did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		answers = ['English', 'Chinese', 'Japanese']
		for answer in answers:
			my_survey.store_response(answer)
		for answer in answers:
			self.assertIn(answer, my_survey.responses)


unittest.main
