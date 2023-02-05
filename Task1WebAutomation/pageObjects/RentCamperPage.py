from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class RentCamperPage:
    button_acceptallcookies_xpath = '//*[@id="onetrust-accept-btn-handler"]'
    button_vehicle_xpath = '//*[text() = "Vehicle"]'
    checkbox_selectall_xpath = '//*[text() = "Select all"]'
    checkboxes_all_description_xpath = '//*[@class="typeDesc___1XkZC"]'
    checkboxes_all_titles_xpath = '//*[@class= "typeName___2zx4T"]'
    checkboxes_all_xpath = '//*[@class="checkbox___2AreI"]'

    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, 30)

    def acceptall_cookies_button_present(self):
        return self.driver.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                      self.button_acceptallcookies_xpath)))

    def vehicle_option_present(self):
        return self.driver.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                      self.button_vehicle_xpath)))

    def selectall_checkbox(self):
        return self.driver.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                  self.checkbox_selectall_xpath)))

    def check_all_checkboxes_checked(self):
        return self.driver.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                           self.checkboxes_all_description_xpath)))

    def verify_all_checkboxes_checked_present(self):
        return self.driver.find_elements(By.XPATH,
                                         self.checkboxes_all_description_xpath)

    def dynamic_names_of_checkboxes_present(self):
        return self.driver.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                           self.checkboxes_all_titles_xpath)))

    def dynamic_names_of_checkboxes_get(self):
        return self.driver.find_elements(By.XPATH,
                                         self.checkboxes_all_titles_xpath)

    def all_checkboxes_present(self):
        return self.driver.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                      self.checkboxes_all_xpath)))

    def all_checkboxes_except_selectall(self):
        return self.driver.find_elements(By.XPATH,
                                         self.checkboxes_all_xpath)

    def acceptall_cookies_button_displayed(self):
        return self.driver.find_element(By.XPATH,
                                        self.button_acceptallcookies_xpath).is_displayed()

    def vehicle_option_displayed(self):
        return self.driver.find_element(By.XPATH,
                                        self.button_vehicle_xpath).is_displayed()

    def click_acceptall_cookies_button(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                           self.button_acceptallcookies_xpath))).click()

    def click_vehicle_option(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                           self.button_vehicle_xpath))).click()

    def check_selectall_checkbox(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                           self.checkbox_selectall_xpath))).click()
