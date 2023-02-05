from pageObjects.RentCamperPage import RentCamperPage
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import HtmlTestRunner


class TestRentCamperPageDisplayed(unittest.TestCase):

    def test_rent_camper_page_displayed(self):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",
                                       desired_capabilities={
                                           "deviceName": "emulator-5554",
                                           "platformName": "android",
                                           "appPackage": "com.android.chrome",
                                           "appActivity": "com.google.android.apps.chrome.Main"
                                       })
        self.driver.wait = WebDriverWait(self.driver, 30)
        self.driver.rentcamperpage = RentCamperPage(self.driver)
        self.driver.rentcamperpage.acceptandcontinue_button_present()
        assert self.driver.rentcamperpage.acceptandcontinue_button_displayed() is True
        self.driver.rentcamperpage.tap_acceptandcontinue_button()
        self.driver.rentcamperpage.nothanks_button_present()
        assert self.driver.rentcamperpage.nothanks_button_displayed() is True
        self.driver.rentcamperpage.tap_nothanks_button()
        self.driver.rentcamperpage.search_bar_present()
        assert self.driver.rentcamperpage.search_bar_displayed() is True
        self.driver.rentcamperpage.tap_searchbar()
        self.driver.rentcamperpage.url_bar_present()
        self.driver.rentcamperpage.type_url()
        self.driver.rentcamperpage.tap_enter_key()

        webview = self.driver.contexts[1]
        self.driver.switch_to.context(webview)

        self.driver.rentcamperpage.acceptall_cookies_button_present()
        self.driver.rentcamperpage.tap_acceptall_cookies_button()

        rent_camper_page = self.driver.rentcamperpage.page_title_displayed()

        if rent_camper_page.text == "Rent a campervan near you:":
            print("Rent Camper Page is Loaded/Displayed")
            assert True
        else:
            print("Rent Camper Page is not Loaded/Displayed")
            assert False

        self.driver.switch_to.context('NATIVE_APP')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports/HTML-Reports'))
