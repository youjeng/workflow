from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewUserTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_set_up_new_account(self):
    # Josh is getting stressed out at work trying to stay on top of his workflow at work
    # He is tired of using a spreadsheet and has decided to find another solution for 
    # managing a workflow with his small team.  He goes to the workflow home page
        self.browser.get('http://localhost:8000')

    # He is welcome by a beautiful website and asked to open an account to get started making 
    # a work flow in just a minute

    # He click the open account button and is taken to 
    # create new accoutn page

    # He enters a user name and password and clicks enter

    # He is asked to verify his email address

    # He verifies his email address and is auto logged into what looks like a "dashboard"

    # He see's a banner prompting him to finish his profile

    # He enters his role as "video production specialist"

    # He is asked to upload a picture for his avatar - which he does and it gets emoji-ized

    # He sees a button to start his first content work flow and clicks it

    # He is asked to add the content type

    # He sees a description of what a content work flow is and is asked to add "next steps"
    # He see the first next step is "Not Started"
    # He adds a next steps 'Needs Feedback'

    # He see's 'Needs Feedback' is now added to the list"

    # He adds a next steps 'Needs Adjusted'

    # He see's 'Needs Adjusted' is now added to the list"

    # He adds a next steps 'Needs Reviewed'

    # He see's 'Needs Reviewed' is now added to the list"

    # He adds a next steps 'Review Complete'

    # He see's 'Needs Complete' is now added to the list"









    ######################################################################

    # Josh just started his new job and is told to setup an account 
    # with worflow.io, a tool he is told that will help him work with his
    # teammates coordinate on projects.  He open the URL gievn to him by 
    # his supervisor

    # Josh sees a place to sign up

    # Josh enters his work email and a password and creates his account

    # Josh is promoted to verify his email address

    # Josh verifies his email address and is autologged in from the email link
    # and appears to be in a "dashboard"

    # Josh is asked to complete his profile and create a personal emoji of himself as his user avatar.
    # He uploads a picture of himself which gets "emoji-ized"

    # Josh receives an email from his supervisor that has a link to join the teams workflow database
    # called "ProtoJo"

    # Josh clicks the link and is brought back to his dash board, but now he sees an icon on his dashboard
    # called "production"

    # Josh clicks the icon and is taken to what looks like a spread sheet
    

if __name__ == '__main__':
    unittest.main(warnings='ignore')



