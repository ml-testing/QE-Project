class login:
    input_email_css = "input[name='email']"
    input_password_css = "input[name='password']"
    button_submit_css = "button[data-test-id='submit']"
    input_firstname_css = "input[name='firstName']"
    input_lastname_css = "input[name='lastName']"
    text_tag = 'h1'

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element_by_css_selector(self.input_email_css).clear()
        self.driver.find_element_by_css_selector(self.input_email_css).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_css_selector(self.input_password_css).clear()
        self.driver.find_element_by_css_selector(self.input_password_css).send_keys(password)

    def enter_firstname(self, firstname):
        self.driver.find_element_by_css_selector(self.input_firstname_css).clear()
        self.driver.find_element_by_css_selector(self.input_firstname_css).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element_by_css_selector(self.input_lastname_css).clear()
        self.driver.find_element_by_css_selector(self.input_lastname_css).send_keys(lastname)

    def click_submit(self):
        self.driver.find_element_by_css_selector(self.button_submit_css).click()

    def get_test(self):
        actual_text= self.driver.find_element_by_tag_name(self.text_tag).text
        return actual_text


