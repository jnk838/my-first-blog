from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from django.contrib.auth.models import User
# from django.test import Client, TransactionTestCase
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Safari()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://127.0.0.1:8000')
        
        self.assertIn('Jamie King', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('t1').text  
        self.assertIn('Jamie King', header_text)
        pre_header_text = self.browser.find_element_by_tag_name('t2').text  
        self.assertIn('I\'m', pre_header_text)

    def test_check_cv_page(self):
        #User can see CV tab
        cv_tab = self.browser.find_elements_by_xpath('//*[contains(text(),'"CV"')]')
        if (len(cv_tab)>0):
            pass
        else:
            self.fail("Not a CV tab")
        
    def test_can_click_on_cv_tab(self):
        #User can click on CV tab
        cv_tab = self.browser.find_elements_by_xpath('//*[contains(text(),'"CV"')]')[0]
        cv_tab.click()

        title = self.browser.find_elements_by_xpath('//*[contains(text(),'"About"')]')
        if (len(title)>0):
            pass
        else:
            self.fail("Didnt change page")

    def test_can_see_cv_content(self): 
        #User can see CV content on page after click
        self.browser.get('http://127.0.0.1:8000/cv/#posts')

        title = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('About', title)

        cv_post = self.browser.find_element_by_xpath('//*[contains(text(),'"Jewish"')]')
        pass

    def test_user_can_edit(self):
        #User can click on edit icon if admin and taken to cv_edit page
        self.browser.get('http://127.0.0.1:8000/admin/')
        username = self.browser.find_element_by_xpath('//*[@id="id_username"]')
        username.send_keys('jimboking')
        time.sleep(2)
        password = self.browser.find_element_by_xpath('//*[@id="id_password"]')
        password.send_keys('Fl0werP0wer12!')
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(2)

        self.browser.get('http://127.0.0.1:8000/cv/#posts')

        time.sleep(3)
        python_button = self.browser.find_element_by_id('button').send_keys(Keys.ENTER)
        self.browser.implicitly_wait(5)
        time.sleep(2)
        self.assertEqual(self.browser.current_url, 'http://127.0.0.1:8000/cv/11/edit/#posts')

        #User can change CV information in form
        inputbox = self.browser.find_element_by_xpath('//*[@id="id_title"]')
        time.sleep(2)
        inputbox.send_keys('THISISANEWTESTCASE')
        inputbox.send_keys(Keys.ENTER)

        #User is redirected to CV page once save pressed
        time.sleep(2)
        url = self.browser.current_url
        self.assertIn('http://127.0.0.1:8000/cv/#posts', url)
        
        #CV information is updated
        content = self.browser.find_elements_by_xpath('//*[contains(text(),'"THISISANEWTESTCASE"')]')
        if (len(content)>0):
            pass
        else:
            self.fail("Content not changed")

    def test_user_can_add_cv_item(self):
        #User can click on add icon if admin and taken to blank cv_edit page
        self.browser.get('http://127.0.0.1:8000/admin/')
        username = self.browser.find_element_by_xpath('//*[@id="id_username"]')
        username.send_keys('jimboking')
        time.sleep(2)
        password = self.browser.find_element_by_xpath('//*[@id="id_password"]')
        password.send_keys('Fl0werP0wer12!')
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(2)

        self.browser.get('http://127.0.0.1:8000/cv/#posts')

        time.sleep(3)
        python_button = self.browser.find_element_by_id('plus').send_keys(Keys.ENTER)
        self.browser.implicitly_wait(5)
        time.sleep(2)
        self.assertEqual(self.browser.current_url, 'http://127.0.0.1:8000/cv/new/#posts')

        #User can add CV information in form
        inputbox0 = self.browser.find_element_by_xpath('//*[@id="id_title"]')
        inputbox2 = self.browser.find_element_by_xpath('//*[@id="id_date"]')
        inputbox3 = self.browser.find_element_by_xpath('//*[@id="id_location"]')
        inputbox4 = self.browser.find_element_by_xpath('//*[@id="id_text"]')
        inputbox5 = self.browser.find_element_by_xpath('//*[@id="id_l1"]')
        inputbox6 = self.browser.find_element_by_xpath('//*[@id="id_l2"]')
        inputbox7 = self.browser.find_element_by_xpath('//*[@id="id_l3"]')
        submit = self.browser.find_element_by_xpath('//*[@id="posts"]/div/div/div/form/button')
        time.sleep(2)
        inputbox0.send_keys('THISISANEWTESTCASE2')
        inputbox2.send_keys('DATEGOESHERE')
        inputbox3.send_keys('LOCATIONHERE')
        inputbox4.send_keys('TEXTHERE')  
        inputbox5.send_keys('L1') 
        inputbox6.send_keys('L2')  
        inputbox7.send_keys('L3')
        time.sleep(3)
        submit.send_keys(Keys.ENTER)

        #User is redirected to CV page once save pressed
        time.sleep(10)
        url = self.browser.current_url
        self.assertIn('http://127.0.0.1:8000/cv/#posts', url)
        
        #CV information is updated
        content = self.browser.find_elements_by_xpath('//*[contains(text(),'"THISISANEWTESTCASE2"')]')
        if (len(content)>0):
            pass
        else:
            self.fail("Content not changed")


if __name__ == '__main__':
    unittest.main(warnings='ignore')