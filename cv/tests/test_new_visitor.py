from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from unittest import skip
import time

class NewVisitorTest(FunctionalTest):

    def test_navbar(self):

        # Load CV page
        self.browser.get(self.live_server_url + '/cv')

        # User sees navbar
        navbartest = self.browser.find_elements_by_class_name('nav-link')
        navbar = []
        for item in navbartest:
            navbar.append(item.text)

        navbarelements = ['Home','Blog','CV','Log in']

        self.assertEqual(navbar, navbarelements)

        #User navigates to Homepage
        self.browser.find_element_by_link_text('Home').click()
        time.sleep(1)

        currenturl = self.browser.current_url

        self.assertEqual(currenturl, self.live_server_url + '/')

        #User goes back to CV page
        target = self.browser.find_element_by_class_name('resume')

        action = ActionChains(self.browser)

        action.move_to_element(target)
        action.click(target)
        action.perform()

        time.sleep(1)

        currenturl = self.browser.current_url

        self.assertEqual(currenturl, self.live_server_url + '/cv')

        #User navigates to Blog
        self.browser.find_element_by_link_text('Blog').click()
        time.sleep(1)
        currenturl = self.browser.current_url

        self.assertEqual(currenturl, self.live_server_url + '/blog')

        #User goes back to CV page
        self.browser.find_element_by_link_text('CV').click()
        time.sleep(1)
        currenturl = self.browser.current_url

        self.assertEqual(currenturl, self.live_server_url + '/cv')


        #User is not logged in so goes to Log in page
        self.browser.find_element_by_link_text('Log in').click()
        time.sleep(1)
        currenturl = self.browser.current_url

        self.assertEqual(currenturl, self.live_server_url + '/accounts/login/')

        #User goes back to CV page
        self.browser.find_element_by_link_text('CV').click()
        time.sleep(1)
        currenturl = self.browser.current_url

        self.assertEqual(currenturl, self.live_server_url + '/cv')



    def test_title_and_intro(self):

        # Load CV page
        self.browser.get(self.live_server_url + '/cv')

        # User checks webpage title
        self.assertIn('Raef\'s CV', self.browser.title)

        #User checks Name in CV
        name = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Raef Hamdan', name)


    def test_intro_social_redirects(self):

        # Load CV page
        self.browser.get(self.live_server_url + '/cv')

        # User sees Phone number
        number = self.browser.find_element_by_link_text('07587897976').text
        self.assertIn(number, '07587897976')
        time.sleep(1)

        # User sees email link
        email = self.browser.find_element_by_link_text('mhdraef@gmail.com').text
        self.assertIn(email, 'mhdraef@gmail.com')
        time.sleep(1)


        # User clicks github link
        self.browser.find_element_by_link_text('mhdraef').click()
        time.sleep(1)

        currenturl = self.browser.current_url

        self.assertEqual(currenturl, 'https://github.com/mhdraef')

        # Go back to cv page
        self.browser.get(self.live_server_url + '/cv')
        time.sleep(1)

        # User sees linkedin link
        linkedin = self.browser.find_element_by_link_text('raefhamdan').get_attribute('href')

        self.assertEqual(linkedin, 'https://linkedin.com/in/raefhamdan')
