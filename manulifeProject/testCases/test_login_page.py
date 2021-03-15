from pagesObjects.page_objects import login
from untilities.readProperties import ReadConfig
import time


class TestLoginPage:
    url = ReadConfig.getappurl()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    firstname = ReadConfig.getfirstname()
    lastname = ReadConfig.getlasttname()

    # test if the login page is loaded by verifying if text "Step 1" is present
    def test_login_page_loaded(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.loginpage = login(self.driver)
        step1 = self.loginpage.get_test()
        assert step1 == "Step 1"
        self.driver.close()

    # test the login page works properly by verifying all input fields works as expected
    def test_enter_email_password(self, setup):
        # create a driver and launch the login page
        self.driver = setup
        self.driver.get(self.url)
        self.loginpage = login(self.driver)

        # test email and password fields
        self.loginpage.enter_email(self.email)
        self.loginpage.enter_password(self.password)
        time.sleep(1)
        self.loginpage.click_submit()
        step2 = self.loginpage.get_test()
        assert step2 == "Step 2"

        # test first name and last name fields
        self.loginpage.enter_firstname(self.firstname)
        self.loginpage.enter_lastname(self.lastname)
        time.sleep(1)
        self.loginpage.click_submit()
        step3 = self.loginpage.get_test()
        assert step3 == "Step 3"

        # click the final submit and verify the final screen is reaches
        self.loginpage.click_submit()
        time.sleep(3)
        final_text = self.loginpage.get_test()
        assert final_text == "Success!"

        # close the browser
        self.driver.close()


