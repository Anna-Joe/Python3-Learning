import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
       # 写了这个方法以后，下面的test_方法就不用再创建对象了
        question="What language did you first learn to speak?"
        self.my_survey=AnonymousSurvey(question)
        self.responses=['English','Spanish','Mandarin']
        
    def test_store_single_response(self):
       # question="What language did you first learn to speak?"
       # my_survey=AnonymousSurvey(question)
        self.my_survey.store_response('English')

        self.assertIn('English',self.my_survey.responses)

    def test_store_three_response(self):
       # question="What language did you first learn to speak?"
       # my_survey=AnonymousSurvey(question)
       # responses=['English','Spanish','Mandarin']
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

unittest.main()
