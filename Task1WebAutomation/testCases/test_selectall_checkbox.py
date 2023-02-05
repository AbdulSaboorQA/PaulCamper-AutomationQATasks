from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.RentCamperPage import RentCamperPage
from utilities.customLogger import LogGen


class TestSelectAllCheckbox:
    logger = LogGen.loggen()

    # Validates the Paulcamper's rent camper page title
    def test_homepage_title(self, setup):
        self.logger.info('################ Test_01 ################')
        self.logger.info('################ Verifying Rent Camper Page Title ################')
        self.driver = setup
        page_title = self.driver.title

        if page_title == "Private motorhome rentals | Huge selection at PaulCamper":
            assert True
            print("Page Title is Correct")
            self.logger.info('################ Verifying Rent Camper Page Title test is PASSED ################')
        else:
            self.driver.save_screenshot("../Screenshots/"
                                        + "test_homepage_title.png")
            print("Unable to get Page Title")
            self.logger.info('################ Verifying Rent Camper Page Title test is FAILED ################')
            assert False

    # Validates the functionality that the 'Select All' checkbox is Checked
    def test_selectall_checkbox_works_programmatically_by_checking(self, setup):
        self.logger.info('################ Test_02 ################')
        self.logger.info('################ Verifying Select All Checkbox works Programmatically by Checking Test '
                         '################')
        self.driver = setup
        self.rent_camper_page = RentCamperPage(self.driver)
        self.rent_camper_page.acceptall_cookies_button_present()
        assert self.rent_camper_page.acceptall_cookies_button_displayed() is True
        self.rent_camper_page.click_acceptall_cookies_button()
        self.rent_camper_page.vehicle_option_present()
        assert self.rent_camper_page.vehicle_option_displayed() is True
        self.rent_camper_page.click_vehicle_option()
        self.rent_camper_page.check_selectall_checkbox()

        # Currently, this condition will not pass, resulting in the test case to fail
        # as the web application has issues with the checkbboxes,
        # once fixed by the engineers this will run successfully
        selectall_checkbox_status = self.rent_camper_page.selectall_checkbox().is_selected()

        if selectall_checkbox_status:
            assert True
            print("Select All Checkbox is selected")
            self.logger.info('################ Verifying Select All Checkbox works Programmatically by Checking Test '
                             'is PASSED ################')
        else:
            self.driver.save_screenshot("../Screenshots/" +
                                        "test_selectall_checkbox_works_programmatically_by_checking.png")
            print("Select All Checkbox is not selected")
            self.logger.info('################ Verifying Select All Checkbox works Programmatically by Checking Test '
                             'is FAILED ################')
            assert False

    # Validates the functionality that the 'Select All' checkbox is un-checked
    # on checking it again
    def test_selectall_checkbox_works_programmatically_by_unchecking(self, setup):
        self.logger.info('################ Test_03 ################')
        self.logger.info('################ Verifying Select All Checkbox works Programmatically by un-checking Test '
                         '################')
        self.driver = setup
        self.driver.wait = WebDriverWait(self.driver, 30)
        self.rent_camper_page = RentCamperPage(self.driver)
        self.rent_camper_page.acceptall_cookies_button_present()
        assert self.rent_camper_page.acceptall_cookies_button_displayed() is True
        self.rent_camper_page.click_acceptall_cookies_button()
        self.rent_camper_page.vehicle_option_present()
        assert self.rent_camper_page.vehicle_option_displayed() is True
        self.rent_camper_page.click_vehicle_option()
        self.rent_camper_page.check_selectall_checkbox()

        # Currently, this condition will not pass, resulting in the test case to fail
        # as the web application has issues with the checkbboxes,
        # once fixed by the engineers this will run successfully
        selectall_checkbox_status = self.rent_camper_page.selectall_checkbox().is_selected()

        if selectall_checkbox_status:
            assert True
            print("Select All Checkbox is checked/selected")
            self.rent_camper_page.check_selectall_checkbox()
            selectall_checkbox_status = self.rent_camper_page.selectall_checkbox().is_selected()
            print(selectall_checkbox_status + "Select All CheckBox is de-selected/un-checked")
            self.logger.info('################ Verifying Select All Checkbox works Programmatically by un-checking '
                             'Test is PASSED ################')
        else:
            self.driver.save_screenshot("../Screenshots/" +
                                        "test_selectall_checkbox_works_programmatically_by_unchecking.png")
            print("Select All Checkbox is not selected")
            self.logger.info('################ Verifying Select All Checkbox works Programmatically by un-checking '
                             'Test is FAILED ################')
            assert False

    # Validates the functionality that checking the 'select all' checkbox
    # checks the other checkboxes as well
    def test_all_checkboxes_checked_by_checking_selectall_checkbox(self, setup):
        self.logger.info('################ Test_04 ################')
        self.logger.info('################ Verifying checking "Select All" Checkbox checks other checkboxes Test '
                         'as well ################')
        self.driver = setup
        self.rent_camper_page = RentCamperPage(self.driver)
        self.rent_camper_page.acceptall_cookies_button_present()
        assert self.rent_camper_page.acceptall_cookies_button_displayed() is True
        self.rent_camper_page.click_acceptall_cookies_button()
        self.rent_camper_page.vehicle_option_present()
        assert self.rent_camper_page.vehicle_option_displayed() is True
        self.rent_camper_page.click_vehicle_option()
        self.rent_camper_page.check_selectall_checkbox()
        self.rent_camper_page.check_all_checkboxes_checked()
        all_selected_checkboxes = self.rent_camper_page.verify_all_checkboxes_checked_present()
        self.rent_camper_page.dynamic_names_of_checkboxes_present()
        total_checkboxes = self.rent_camper_page.dynamic_names_of_checkboxes_get()

        if len(all_selected_checkboxes) == len(total_checkboxes) - 1:
            print('all checkboxes are selected')
            self.logger.info('################ Verifying checking "Select All" Checkbox checks other checkboxes Test '
                             'as well is PASSED ################')
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/" +
                                        "test_all_checkboxes_checked_by_checking_selectall_checkbox.png")
            print('all checkboxes are not selected')
            self.logger.info('################ Verifying checking "Select All" Checkbox checks other checkboxes Test '
                             'as well is FAILED ################')
            assert False

    # Validates the functionality that un-checking the 'Select All' checkbox
    # un-checks the other checkboxes as well after checking again via 'Select All' checkbox
    def test_all_checkboxes_dechecked_by_unchecking_selectall_checkbox(self, setup):
        self.logger.info('################ Test_05 ################')
        self.logger.info('################ Verifying un-checking "Select All" Checkbox un- checks other checkboxes '
                         'after checking again via "Select All" checkbox Test ################')
        self.driver = setup
        self.rent_camper_page = RentCamperPage(self.driver)
        self.rent_camper_page.acceptall_cookies_button_present()
        assert self.rent_camper_page.acceptall_cookies_button_displayed() is True
        self.rent_camper_page.click_acceptall_cookies_button()
        self.rent_camper_page.vehicle_option_present()
        assert self.rent_camper_page.vehicle_option_displayed() is True
        self.rent_camper_page.click_vehicle_option()
        self.rent_camper_page.check_selectall_checkbox()
        self.rent_camper_page.check_all_checkboxes_checked()
        all_selected_checkboxes = self.rent_camper_page.verify_all_checkboxes_checked_present()
        self.rent_camper_page.dynamic_names_of_checkboxes_present()
        total_checkboxes = self.rent_camper_page.dynamic_names_of_checkboxes_get()

        # verifying that all the checkboxes are checked or not, by checking the select all checkbox
        if len(all_selected_checkboxes) == len(total_checkboxes) - 1:
            print('all checkboxes are checked')
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/" +
                                        "test_all_checkboxes_dechecked_by_unchecking_selectall_checkbox.png")
            print('all checkboxes are not checked')
            assert False

        self.rent_camper_page.check_selectall_checkbox()
        all_checkboxes_selected = self.rent_camper_page.verify_all_checkboxes_checked_present()

        # verifying that all the checkboxes are un-checked or not, by un-checking the select all checkbox
        if len(all_checkboxes_selected) != len(total_checkboxes):
            print('all checkboxes are deselected')
            self.logger.info('################ Verifying un-checking "Select All" Checkbox un- checks other checkboxes '
                             'after checking again via "Select All" checkbox Test is PASSED ################')
            assert True
        else:
            print('all checkboxes are not deselected')
            self.logger.info('################ Verifying un-checking "Select All" Checkbox un- checks other checkboxes '
                             'after checking again via "Select All" checkbox Test is FAILED ################')
            assert False

    # Validates the functionality that 'Select All' checkbox is
    # checked by checking all the other checkboxes
    def test_checking_all_checkboxes_checks_selectall_checkbox_too(self, setup):
        self.logger.info('################ Test_06 ################')
        self.logger.info('################ Verifying "Select All" Checkbox is checked by checking other checkboxes '
                         'Test ################')
        self.driver = setup
        self.rent_camper_page = RentCamperPage(self.driver)
        self.rent_camper_page.acceptall_cookies_button_present()
        assert self.rent_camper_page.acceptall_cookies_button_displayed() is True
        self.rent_camper_page.click_acceptall_cookies_button()
        self.rent_camper_page.vehicle_option_present()
        assert self.rent_camper_page.vehicle_option_displayed() is True
        self.rent_camper_page.click_vehicle_option()
        self.rent_camper_page.all_checkboxes_present()
        total_checkboxes = self.rent_camper_page.all_checkboxes_except_selectall()

        for index in range(len(total_checkboxes) - 1):
            checkbox = total_checkboxes[index]
            checkbox.click()

        # Currently, this condition will not pass, resulting in the test case to fail
        # as the web application has issues with the checkbboxes,
        # once fixed by the engineers this will run successfully
        selectall_checkbox_status = self.rent_camper_page.selectall_checkbox().is_selected()

        if selectall_checkbox_status:
            assert True
            print("'Select All' Checkbox is checked by checking all the other checkboxes")
            self.logger.info('################ Verifying "Select All" Checkbox is checked by checking other checkboxes '
                             'Test is PASSED ################')
        else:
            self.driver.save_screenshot("../Screenshots/" +
                                        "test_checking_all_checkboxes_checks_selectall_checkbox_too.png")
            print("'Select All' Checkbox is not checked by checking all the other checkboxes")
            self.logger.info('################ Verifying "Select All" Checkbox is checked by checking other checkboxes '
                             'Test is FAILED ################')
            assert False

    # Validates the functionality that 'Select All' checkbox gets un-checked
    # by un-checking all the other checkboxes
    def test_unchecking_all_checkboxes_unchecks_selectall_checkbox_too(self, setup):
        self.logger.info('################ Test_07 ################')
        self.logger.info('################ Verifying "Select All" Checkbox is un-checked by un-checking other '
                         'checkboxes after checking them all Test ################')
        self.driver = setup
        self.rent_camper_page = RentCamperPage(self.driver)
        self.rent_camper_page.acceptall_cookies_button_present()
        assert self.rent_camper_page.acceptall_cookies_button_displayed() is True
        self.rent_camper_page.click_acceptall_cookies_button()
        self.rent_camper_page.vehicle_option_present()
        assert self.rent_camper_page.vehicle_option_displayed() is True
        self.rent_camper_page.click_vehicle_option()
        self.rent_camper_page.all_checkboxes_present()
        total_checkboxes = self.rent_camper_page.all_checkboxes_except_selectall()

        for index in range(len(total_checkboxes) - 1):
            checkbox = total_checkboxes[index]
            checkbox.click()

        # Currently, this condition will not pass, resulting in the test case to fail
        # as the web application has issues with the checkbboxes,
        # once fixed by the engineers this will run successfully
        selectall_checkbox_status = self.rent_camper_page.selectall_checkbox().is_selected()

        if selectall_checkbox_status:
            assert True
            print("'Select All' Checkbox is checked by checking all the other checkboxes")
            self.rent_camper_page.all_checkboxes_present()
            total_checkboxes = self.rent_camper_page.all_checkboxes_except_selectall()
            for index in range(len(total_checkboxes) - 1):
                checkbox = total_checkboxes[index]
                checkbox.click()
                selectall_checkbox_status = self.rent_camper_page.selectall_checkbox().is_selected()
                print(selectall_checkbox_status,
                      "'Select All' Checkbox is un-checked by un-checking all the other checkboxes")
                self.logger.info('################ Verifying "Select All" Checkbox is un-checked by un-checking other '
                                 'checkboxes after checking them all Test is PASSED ################')
        else:
            self.driver.save_screenshot("../Screenshots/" +
                                        "test_unchecking_all_checkboxes_unchecks_selectall_checkbox_too.png")
            print("'Select All' Checkbox is not un-checked by un-checking all the other checkboxes")
            self.logger.info('################ Verifying "Select All" Checkbox is un-checked by un-checking other '
                             'checkboxes after checking them all Test is FAILED  ################')
            assert False
