from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    # page elemnts path
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    LOCATOR_PSWD_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_ERROR_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')
    LOCATOR_LOGIN_RESULT = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')
    LOCATOR_CREATE_NEW_POST = (By.XPATH, '//*[@id="create-btn"]')
    LOCATOR_POST_TITLE = (By.XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label/input')
    LOCATOR_POST_DESCRIPTION = (By.XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea')
    LOCATOR_POST_CONTENT = (By.XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea')
    LOCATOR_SAVE_BTN = (By.XPATH, '//*[@id="create-item"]/div/div/div[7]/div/button/span')
    LOCATOR_EXIST_POST = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')
    LOCATOR_CONTACTUS_BTN = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[2]/a')
    LOCATOR_YOU_NAME_FIELD = (By.XPATH, '//*[@id="contact"]/div[1]/label/input')
    LOCATOR_YOU_EMAIL_FIELD = (By.XPATH, '//*[@id="contact"]/div[2]/label/input')
    LOCATOR_CONTENT_FIELD = (By.XPATH, '//*[@id="contact"]/div[3]/label/span/textarea')
    LOCATOR_CONTACTUS_SEND_BTN = (By.XPATH, '//*[@id="contact"]/div[4]/button/span')

class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f'send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pswd(self, word):
        logging.info(f'send {word} to element {TestSearchLocators.LOCATOR_PSWD_FIELD[1]}')
        pswd_field = self.find_element(TestSearchLocators.LOCATOR_PSWD_FIELD)
        pswd_field.clear()
        pswd_field.send_keys(word)

    def click_login_button(self):
        logging.info('Click logging button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f'We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text

    def get_login_text(self):
        login_ok = self.find_element(TestSearchLocators.LOCATOR_LOGIN_RESULT, time=3)
        text = login_ok.text
        logging.info(f'We find text {text} in login page {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text

    def click_new_post_button(self):
        logging.info('Click new post button')
        self.find_element(TestSearchLocators.LOCATOR_CREATE_NEW_POST).click()

    def enter_title_post(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_POST_TITLE[1]}')
        title_post = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE)
        title_post.clear()
        title_post.send_keys(word)

    def enter_description_post(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_POST_DESCRIPTION[1]}')
        description_post = self.find_element(TestSearchLocators.LOCATOR_POST_DESCRIPTION)
        description_post.clear()
        description_post.send_keys(word)

    def enter_content_post(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_POST_CONTENT[1]}')
        content_post = self.find_element(TestSearchLocators.LOCATOR_POST_CONTENT)
        content_post.clear()
        content_post.send_keys(word)

    def click_save_new_post_button(self):
        logging.info('Click save new post button')
        self.find_element(TestSearchLocators.LOCATOR_SAVE_BTN).click()

    def check_exist_post(self):
        find_post = self.find_element(TestSearchLocators.LOCATOR_EXIST_POST, time=3)
        text = find_post.text
        logging.info(f'We find text {text} in login page {TestSearchLocators.LOCATOR_EXIST_POST[1]}')
        return text

    def click_contactus_button(self):
        logging.info('Click Contact button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACTUS_BTN).click()

    def enter_name_field(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_YOU_NAME_FIELD[1]}')
        name_field = self.find_element(TestSearchLocators.LOCATOR_YOU_NAME_FIELD)
        name_field.clear()
        name_field.send_keys(word)

    def enter_email_field(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_YOU_EMAIL_FIELD[1]}')
        email_field = self.find_element(TestSearchLocators.LOCATOR_YOU_EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(word)

    def enter_content_field(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_CONTENT_FIELD[1]}')
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(word)

    def click_contactus_send_button(self):
        logging.info('Click Send button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACTUS_SEND_BTN).click()

    def text_alert(self):
        logging.info('Switch alert')
        return self.switch_to_alert()
