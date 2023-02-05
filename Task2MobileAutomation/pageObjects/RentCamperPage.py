from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class RentCamperPage:
    button_acceptandcontinue_id = 'com.android.chrome:id/terms_accept'
    button_nothanks_id = 'com.android.chrome:id/negative_button'
    searchbar_id = 'com.android.chrome:id/search_box_text'
    urlbar_id = 'com.android.chrome:id/url_bar'
    button_cookiesacceptall_xpath = '//*[text()="Accept all"]'
    page_title_xpath = '//*[text()="Rent a campervan near you"]'

    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, 30)

    def acceptandcontinue_button_present(self):
        return self.driver.wait.until(EC.presence_of_element_located((By.ID, self.button_acceptandcontinue_id)))

    def acceptandcontinue_button_displayed(self):
        return self.driver.find_element(By.ID, self.button_acceptandcontinue_id)\
            .is_displayed()

    def tap_acceptandcontinue_button(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.ID, self.button_acceptandcontinue_id)))\
            .click()

    def nothanks_button_present(self):
        return self.driver.wait.until(EC.presence_of_element_located((By.ID, self.button_nothanks_id)))

    def nothanks_button_displayed(self):
        return self.driver.find_element(By.ID, self.button_nothanks_id)\
            .is_displayed()

    def tap_nothanks_button(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.ID, self.button_nothanks_id)))\
            .click()

    def search_bar_present(self):
        return self.driver.wait.until(EC.presence_of_element_located((By.ID, self.searchbar_id)))

    def search_bar_displayed(self):
        return self.driver.find_element(By.ID, self.searchbar_id)\
            .is_displayed()

    def tap_searchbar(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.ID, self.searchbar_id)))\
            .click()

    def url_bar_present(self):
        return self.driver.wait.until(EC.presence_of_element_located((By.ID, self.urlbar_id)))

    # def url_bar_displayed(self):
    #     return self.driver.find_element(By.ID, self.urlbar_id)\
    #         .is_displayed

    def type_url(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.ID, self.urlbar_id)))\
            .send_keys('https://paulcamper.com/rent-camper')

    def tap_enter_key(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(985, 2077)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def acceptall_cookies_button_present(self):
        return self.driver.wait.until(EC.presence_of_element_located((By.XPATH, self.button_cookiesacceptall_xpath)))

    # def acceptall_cookies_button_displayed(self):
    #     return self.driver.find_element(By.XPATH, self.button_cookiesacceptall_xpath)\
    #         .is_displayed()

    def tap_acceptall_cookies_button(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_cookiesacceptall_xpath)))\
            .click()

    def page_title_displayed(self):
        return self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, self.page_title_xpath)))
