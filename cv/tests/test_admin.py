from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip
from django.contrib.auth.models import User
from selenium.common.exceptions import NoSuchElementException


import time

class AdminTests(FunctionalTest):

    #Override for admin login
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.user = User.objects.create_user(username='username', password='password')
        self.user.save()


    def test_section_education(self):

        #Logging in as admin
        self.browser.get(self.live_server_url + '/accounts/login/')
        time.sleep(1)
        self.browser.find_element_by_name("username").send_keys('username')
        self.browser.find_element_by_name("password").send_keys('password')
        self.browser.find_element_by_xpath('//input[@value="login"]').click()
        time.sleep(1)

        #Going back to CV page
        self.browser.get(self.live_server_url + '/cv')
        time.sleep(1)

        #Clicking add education button
        self.browser.find_element_by_xpath('/html/body/div/section[1]/div[1]/a').click()
        time.sleep(1)
        self.assertEqual(self.browser.current_url,self.live_server_url + '/cv/education/new/')

        #Filling out add education form
        self.browser.find_element_by_xpath('/html/body/form/div/p[1]/input').send_keys('test')
        self.browser.find_element_by_xpath('/html/body/form/div/p[2]/input').send_keys('test')
        self.browser.find_element_by_xpath('/html/body/form/div/p[3]/input').send_keys('test')
        self.browser.find_element_by_xpath('/html/body/form/div/p[4]/input').send_keys('test')
        self.browser.find_element_by_xpath('/html/body/form/div/button').click()
        time.sleep(1)

        #Verifying added education item
        obj1 = self.browser.find_element_by_xpath('/html/body/div/section[1]/div[2]/div[1]/h4[1]').text
        self.assertEqual(obj1,'test')
        obj2 = self.browser.find_element_by_xpath('/html/body/div/section[1]/div[2]/div[1]/h4[2]').text
        self.assertEqual(obj2,'test')
        obj3 = self.browser.find_element_by_xpath('/html/body/div/section[1]/div[2]/div[2]/h5[1]').text
        self.assertEqual(obj3,'test')
        obj4 = self.browser.find_element_by_xpath('/html/body/div/section[1]/div[2]/div[2]/h5[2]').text
        self.assertEqual(obj4,'test')

        # Tesing education item Edit
        self.browser.find_element_by_xpath('/html/body/div/section[1]/div[2]/div[1]/a[1]').click()
        time.sleep(2)
        self.browser.find_element_by_xpath('/html/body/form/div/p[1]/input').send_keys('edit')
        self.browser.find_element_by_xpath('/html/body/form/div/button').click()
        time.sleep(1)

        # Verifying edited object1 name
        obj1edited = self.browser.find_element_by_xpath('/html/body/div/section[1]/div[2]/div[1]/h4[1]').text
        self.assertEqual(obj1edited,'testedit')

        # Testing education item Remove
        self.browser.find_element_by_xpath('/html/body/div/section[1]/div[2]/div[1]/a[2]').click()
        time.sleep(2)
        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_xpath('/html/body/div/section[1]/div[2]/div[1]/h4[1]')

    def test_section_experience(self):

        #Logging in as admin
        self.browser.get(self.live_server_url + '/accounts/login/')
        time.sleep(1)
        self.browser.find_element_by_name("username").send_keys('username')
        self.browser.find_element_by_name("password").send_keys('password')
        self.browser.find_element_by_xpath('//input[@value="login"]').click()
        time.sleep(1)

        #Going back to CV page
        self.browser.get(self.live_server_url + '/cv')
        time.sleep(1)

        #Clicking add experience button
        self.browser.find_element_by_xpath('/html/body/div/section[2]/div[1]/a').click()
        time.sleep(1)
        self.assertEqual(self.browser.current_url,self.live_server_url + '/cv/experience/new/')

        #Filling out add experience form
        self.browser.find_element_by_xpath('/html/body/form/div/p[1]/input').send_keys('test')
        self.browser.find_element_by_xpath('/html/body/form/div/p[2]/input').send_keys('test')
        self.browser.find_element_by_xpath('/html/body/form/div/p[3]/input').send_keys('test')
        self.browser.find_element_by_xpath('/html/body/form/div/p[4]/input').send_keys('test')
        self.browser.find_element_by_xpath('/html/body/form/div/button').click()
        time.sleep(1)

        #Verifying added experience item
        obj1 = self.browser.find_element_by_xpath('/html/body/div/section[2]/div[2]/div[1]/h4[1]').text
        self.assertEqual(obj1,'test')
        obj2 = self.browser.find_element_by_xpath('/html/body/div/section[2]/div[2]/div[1]/h4[2]').text
        self.assertEqual(obj2,'test')
        obj3 = self.browser.find_element_by_xpath('/html/body/div/section[2]/div[2]/div[2]/h5[1]').text
        self.assertEqual(obj3,'test')
        obj4 = self.browser.find_element_by_xpath('/html/body/div/section[2]/div[2]/div[2]/h5[2]').text
        self.assertEqual(obj4,'test')

        # Tesing experience item Edit
        self.browser.find_element_by_xpath('/html/body/div/section[2]/div[2]/div[1]/a[1]').click()
        time.sleep(2)
        self.browser.find_element_by_xpath('/html/body/form/div/p[1]/input').send_keys('edit')
        self.browser.find_element_by_xpath('/html/body/form/div/button').click()
        time.sleep(1)

        # Verifying edited object1 name
        obj1edited = self.browser.find_element_by_xpath('/html/body/div/section[2]/div[2]/div[1]/h4[1]').text
        self.assertEqual(obj1edited,'testedit')

        # Testing experience item Remove
        self.browser.find_element_by_xpath('/html/body/div/section[2]/div[2]/div[1]/a[2]').click()
        time.sleep(2)
        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_xpath('/html/body/div/section[2]/div[2]/div[1]/h4[1]')

    def test_section_project(self):

        #Logging in as admin
        self.browser.get(self.live_server_url + '/accounts/login/')
        time.sleep(1)
        self.browser.find_element_by_name("username").send_keys('username')
        self.browser.find_element_by_name("password").send_keys('password')
        self.browser.find_element_by_xpath('//input[@value="login"]').click()
        time.sleep(1)

        #Going back to CV page
        self.browser.get(self.live_server_url + '/cv')
        time.sleep(1)

        #Clicking add project button
        self.browser.find_element_by_xpath('/html/body/div/section[3]/div[1]/a').click()
        time.sleep(1)
        self.assertEqual(self.browser.current_url,self.live_server_url + '/cv/project/new/')

        #Filling out add project form
        self.browser.find_element_by_xpath('/html/body/form/div/p[1]/input').send_keys('test')
        self.browser.find_element_by_xpath('/html/body/form/div/p[2]/input').send_keys('test')
        self.browser.find_element_by_xpath('/html/body/form/div/p[3]/input').send_keys('test')
        self.browser.find_element_by_xpath('/html/body/form/div/p[4]/input').send_keys('test')
        self.browser.find_element_by_xpath('/html/body/form/div/button').click()
        time.sleep(1)

        #Verifying added project item
        obj1 = self.browser.find_element_by_xpath('/html/body/div/section[3]/div[2]/div[1]/h4[1]').text
        self.assertEqual(obj1,'test')
        obj2 = self.browser.find_element_by_xpath('/html/body/div/section[3]/div[2]/div[1]/h4[2]').text
        self.assertEqual(obj2,'test')
        obj3 = self.browser.find_element_by_xpath('/html/body/div/section[3]/div[2]/div[2]/h5[1]').text
        self.assertEqual(obj3,'test')
        obj4 = self.browser.find_element_by_xpath('/html/body/div/section[3]/div[2]/div[2]/h5[2]').text
        self.assertEqual(obj4,'test')

        # Tesing project item Edit
        self.browser.find_element_by_xpath('/html/body/div/section[3]/div[2]/div[1]/a[1]').click()
        time.sleep(2)
        self.browser.find_element_by_xpath('/html/body/form/div/p[1]/input').send_keys('edit')
        self.browser.find_element_by_xpath('/html/body/form/div/button').click()
        time.sleep(1)

        # Verifying edited project name
        obj1edited = self.browser.find_element_by_xpath('/html/body/div/section[3]/div[2]/div[1]/h4[1]').text
        self.assertEqual(obj1edited,'testedit')

        # Testing project item Remove
        self.browser.find_element_by_xpath('/html/body/div/section[3]/div[2]/div[1]/a[2]').click()
        time.sleep(2)
        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_xpath('/html/body/div/section[3]/div[2]/div[1]/h4[1]')

    def test_section_certificate(self):

        #Logging in as admin
        self.browser.get(self.live_server_url + '/accounts/login/')
        time.sleep(1)
        self.browser.find_element_by_name("username").send_keys('username')
        self.browser.find_element_by_name("password").send_keys('password')
        self.browser.find_element_by_xpath('//input[@value="login"]').click()
        time.sleep(1)

        #Going back to CV page
        self.browser.get(self.live_server_url + '/cv')
        time.sleep(1)

        #Clicking add certificate button
        self.browser.find_element_by_xpath('/html/body/div/section[4]/div[1]/a').click()
        time.sleep(1)
        self.assertEqual(self.browser.current_url,self.live_server_url + '/cv/certificate/new/')

        #Filling out add certificate form
        self.browser.find_element_by_xpath('/html/body/form/div/p[1]/input').send_keys('test')
        self.browser.find_element_by_xpath('/html/body/form/div/p[2]/input').send_keys('test')
        self.browser.find_element_by_xpath('/html/body/form/div/p[3]/input').send_keys('test')
        self.browser.find_element_by_xpath('/html/body/form/div/button').click()
        time.sleep(1)

        #Verifying added certificate item
        obj1 = self.browser.find_element_by_xpath('/html/body/div/section[4]/div[2]/div[1]/h4[1]').text
        self.assertEqual(obj1,'test')
        obj2 = self.browser.find_element_by_xpath('/html/body/div/section[4]/div[2]/div[1]/h4[2]').text
        self.assertEqual(obj2,'test')
        obj3 = self.browser.find_element_by_xpath('/html/body/div/section[4]/div[2]/div[2]/h5[1]').text
        self.assertEqual(obj3,'test')

        # Tesing certificate item Edit
        self.browser.find_element_by_xpath('/html/body/div/section[4]/div[2]/div[1]/a[1]').click()
        time.sleep(2)
        self.browser.find_element_by_xpath('/html/body/form/div/p[1]/input').send_keys('edit')
        self.browser.find_element_by_xpath('/html/body/form/div/button').click()
        time.sleep(1)

        # Verifying edited certificate name
        obj1edited = self.browser.find_element_by_xpath('/html/body/div/section[4]/div[2]/div[1]/h4[1]').text
        self.assertEqual(obj1edited,'testedit')

        # Testing certificate item Remove
        self.browser.find_element_by_xpath('/html/body/div/section[4]/div[2]/div[1]/a[2]').click()
        time.sleep(2)
        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_xpath('/html/body/div/section[4]/div[2]/div[1]/h4[1]')

    def test_section_skill(self):

        #Logging in as admin
        self.browser.get(self.live_server_url + '/accounts/login/')
        time.sleep(1)
        self.browser.find_element_by_name("username").send_keys('username')
        self.browser.find_element_by_name("password").send_keys('password')
        self.browser.find_element_by_xpath('//input[@value="login"]').click()
        time.sleep(1)

        #Going back to CV page
        self.browser.get(self.live_server_url + '/cv')
        time.sleep(1)

        #Clicking add skill button
        self.browser.find_element_by_xpath('/html/body/div/section[5]/div[1]/a').click()
        time.sleep(1)
        self.assertEqual(self.browser.current_url,self.live_server_url + '/cv/skill/new/')

        #Filling out add skill form
        self.browser.find_element_by_xpath('/html/body/form/div/p[1]/input').send_keys('test')
        self.browser.find_element_by_xpath('/html/body/form/div/p[2]/textarea').send_keys('test')
        self.browser.find_element_by_xpath('/html/body/form/div/button').click()
        time.sleep(2)

        #Verifying added skill item
        obj1 = self.browser.find_element_by_xpath('/html/body/div/section[5]/table/tbody/tr[1]/td[1]').text
        self.assertEqual(obj1,'test')
        obj2 = self.browser.find_element_by_xpath('/html/body/div/section[5]/table/tbody/tr[1]/td[2]').text
        self.assertEqual(obj2,'test')

        # Tesing skill item Edit
        self.browser.find_element_by_xpath('/html/body/div/section[5]/table/tbody/tr[1]/td[3]/a').click()
        time.sleep(2)
        self.browser.find_element_by_xpath('/html/body/form/div/p[1]/input').send_keys('edit')
        self.browser.find_element_by_xpath('/html/body/form/div/button').click()
        time.sleep(1)

        # Verifying edited skill name
        obj1edited = self.browser.find_element_by_xpath('/html/body/div/section[5]/table/tbody/tr[1]/td[1]').text
        self.assertEqual(obj1edited,'testedit')

        # Testing skill item Remove
        self.browser.find_element_by_xpath('/html/body/div/section[5]/table/tbody/tr[1]/td[4]/a').click()
        time.sleep(2)
        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_xpath('/html/body/div/section[5]/table/tbody/tr[1]/td[1]')



    # Test to see if non logged in users can see cv sections
    def test_cv_section_headings(self):

      #Logging in as admin
      self.browser.get(self.live_server_url + '/accounts/login/')
      time.sleep(1)
      self.browser.find_element_by_name("username").send_keys('username')
      self.browser.find_element_by_name("password").send_keys('password')
      self.browser.find_element_by_xpath('//input[@value="login"]').click()
      time.sleep(1)

      #Going back to CV page
      self.browser.get(self.live_server_url + '/cv')
      time.sleep(1)

      #Clicking add education button
      self.browser.find_element_by_xpath('/html/body/div/section[1]/div[1]/a').click()
      time.sleep(1)
      self.assertEqual(self.browser.current_url,self.live_server_url + '/cv/education/new/')

      #Filling out add education form
      self.browser.find_element_by_xpath('/html/body/form/div/p[1]/input').send_keys('test')
      self.browser.find_element_by_xpath('/html/body/form/div/p[2]/input').send_keys('test')
      self.browser.find_element_by_xpath('/html/body/form/div/p[3]/input').send_keys('test')
      self.browser.find_element_by_xpath('/html/body/form/div/p[4]/input').send_keys('test')
      self.browser.find_element_by_xpath('/html/body/form/div/button').click()
      time.sleep(1)

      #Clicking add project button
      self.browser.find_element_by_xpath('/html/body/div/section[3]/div[1]/a').click()
      time.sleep(1)
      self.assertEqual(self.browser.current_url,self.live_server_url + '/cv/project/new/')

      #Filling out add project form
      self.browser.find_element_by_xpath('/html/body/form/div/p[1]/input').send_keys('test')
      self.browser.find_element_by_xpath('/html/body/form/div/p[2]/input').send_keys('test')
      self.browser.find_element_by_xpath('/html/body/form/div/p[3]/input').send_keys('test')
      self.browser.find_element_by_xpath('/html/body/form/div/p[4]/input').send_keys('test')
      self.browser.find_element_by_xpath('/html/body/form/div/button').click()
      time.sleep(1)

      #Clicking add skill button
      self.browser.find_element_by_xpath('/html/body/div/section[5]/div[1]/a').click()
      time.sleep(1)
      self.assertEqual(self.browser.current_url,self.live_server_url + '/cv/skill/new/')

      #Filling out add skill form
      self.browser.find_element_by_xpath('/html/body/form/div/p[1]/input').send_keys('test')
      self.browser.find_element_by_xpath('/html/body/form/div/p[2]/textarea').send_keys('test')
      self.browser.find_element_by_xpath('/html/body/form/div/button').click()
      time.sleep(2)

      #Logging out
      self.browser.find_element_by_link_text('Log out').click()
      time.sleep(1)

      #Going back to CV page
      self.browser.get(self.live_server_url + '/cv')
      time.sleep(1)

      # Checking sections
      self.browser.get(self.live_server_url + '/cv')
      headings = self.browser.find_elements_by_tag_name('h1')

      headers = []
      for heading in headings:
          headers.append(heading.text)

      self.assertTrue(set(headers).issuperset(set(['Education', 'Projects', 'Skills'])))
