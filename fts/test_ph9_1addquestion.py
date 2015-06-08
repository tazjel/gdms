# These tests are all based on the tutorial at http://killer-web-development.com/
# if registration is successful this may work but lets
# try and get user logged in first


from functional_tests import FunctionalTest, ROOT, USERS
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class AddBasicQuestion (FunctionalTest):

    def setUp(self):
        self.url = ROOT + '/default/user/login'        
        get_browser=self.browser.get(self.url)

        #username = self.browser.find_element_by_name("username")
        username = WebDriverWait(self, 10).until(lambda self : self.browser.find_element_by_name("username"))   
        username.send_keys(USERS['USER2'])   

        password = self.browser.find_element_by_name("password")    
        password.send_keys(USERS['PASSWORD2'])    
  
        submit_button = self.browser.find_element_by_css_selector("#submit_record__row input")
        submit_button.click()  
        time.sleep(1)  
        
        self.url = ROOT + '/submit/new_question'        
        get_browser=self.browser.get(self.url)
        time.sleep(1)


    def test_question(self):        
        #questiontext = self.browser.find_element_by_name('questiontext')
        questiontext = WebDriverWait(self, 10).until(lambda self : self.browser.find_element_by_name('questiontext')) 
        questiontext.send_keys("Selenium phase9 Std Vote Time based")

        resmethod = WebDriverWait(self, 10).until(lambda self : self.browser.find_element_by_id
        ("question_resolvemethod"))

        resmethod.send_keys("StdVoteTime")

        # So thinking this would be time plus 5 minutes for now and just answer and save a question to test if worked 
        # may eventually move to just triggering the scoring at the end of the final response 

        due = WebDriverWait(self, 10).until(lambda self : self.browser.find_element_by_id("question_duedate"))
        due.send_keys("StdVoteTime")

        ans1 = WebDriverWait(self, 10).until(lambda self : self.browser.find_element_by_id("question_answers"))
        ans1.send_keys("be")
        ans1.send_keys(Keys.RETURN)

        #ans2 = self.browser.find_element_by_name('ans2')
        #ans2.send_keys("not to be")
        ans2 = WebDriverWait(self, 10).until(lambda self : self.browser.find_element_by_xpath("(//input[@id='question_answers'])[2]"))
        ans2.send_keys("not to be")

        submit_button = self.browser.find_element_by_css_selector("#submit_record__row input")
        submit_button.click()
        time.sleep(5)

        welcome_message = self.browser.find_element_by_css_selector(".flash")
        self.assertEqual(u'Details Submitted\n\xd7', welcome_message.text)
