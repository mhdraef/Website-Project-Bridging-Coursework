from django.test import TestCase

class CVPageTest(TestCase):

    def test_cv_page_uses_correct_template(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response,'cv.html')

    # def test_education_add_page_uses_correct_template(self):
    #     response = self.client.get('/cv/education/new')
    #     self.assertTemplateUsed(response,'add.html')
