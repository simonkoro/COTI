import time
from unittest import TestCase
# from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from useful_elements import CotiElements, MetaMaskElements
from utilities import Utilities

class CotiTest(TestCase):
    def setUp(self):
        self.metamask_extension_path_chrome = r"C:\Users\simon\AppData\Local\Google\Chrome\User Data\Profile 1\Extensions\nkbihfbeogaeaoehlefnkodbefgpgknn\12.10.1_1"
        self.options = Options()
        self.options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        self.options.add_argument(r"--user-data-dir=C:\Users\simon\AppData\Local\Google\Chrome\User Data")
        self.options.add_argument("--profile-directory=Profile 1")
        self.options.add_argument(f"--disable-extensions-except={self.metamask_extension_path_chrome}")
        self.options.add_argument(f"--load-extension={self.metamask_extension_path_chrome}")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.delete_all_cookies()
        self.driver.execute_script("window.localStorage.clear();")
        self.driver.execute_script("window.sessionStorage.clear();")
        self.metamask = MetaMaskElements(self.driver)
        self.coti = CotiElements(self.driver)
        self.utills = Utilities(self.driver)
        self.driver.implicitly_wait(10)
        time.sleep(3)


    def tearDown(self):
        self.driver.quit()

    # def test_continue_integration(self):
    #     self.driver.get("https://treasury-dev.coti.io/")
    #     self.coti.click_on_connect_btn()
    #     self.coti.mark_terms_checkbox()
    #     self.coti.click_on_select_btn()
    #
    #     self.utills.control_metamask_window()
    #
    #     self.metamask.insert_password()
    #     self.metamask.click_on_unlock_btn()
    #     self.metamask.click_on_signin_btn()
    #     self.metamask.click_on_confirm_btn()
    #     self.metamask.click_on_confirm_btn()
    #     self.metamask.click_on_signin_btn()
    #     self.utills.control_coti_window()
    #     self.coti.click_on_deposits_btn()
    #     self.coti.click_on_change_network_btn()
    #     self.utills.control_metamask_window()
    #
    #     self.metamask.click_on_confirm_btn()
    #     self.metamask.click_on_confirm_btn()
    #     self.utills.control_coti_window()
    #
    #     self.coti.click_on_deposit_now_btn()
    #
    #     amount = 5000
    #     self.coti.insert_deposit_amount(amount)

    def test_integration_flow(self):
        self.driver.get("https://treasury.coti.io")
        self.coti.click_on_connect_btn()
        self.coti.mark_terms_checkbox()
        self.coti.click_on_select_btn()

        self.utills.control_metamask_window()

        self.metamask.insert_password()
        self.metamask.click_on_unlock_btn()
        self.metamask.click_on_signin_btn()
        self.metamask.click_on_confirm_btn()
        self.metamask.click_on_confirm_btn()
        # self.metamask.click_on_confirm_btn()
        # self.metamask.click_on_confirm_btn()

        self.utills.control_coti_window()

        expected_error_message = "This service is unavailable in your jurisdiction"
        actual_presented_message = self.coti.locate_error_msg_element()

        self.assertEqual(expected_error_message, actual_presented_message)
        for request in self.driver.requests:
            if 'api/auth/login' in request.url:
                status_code = request.response.status_code
                break

        self.assertEqual(401, status_code)


    def test_continue_integration(self):
        self.driver.get("https://treasury-dev.coti.io/")
        self.coti.click_on_connect_btn()
        self.coti.mark_terms_checkbox()
        self.coti.click_on_select_btn()

        self.utills.control_metamask_window()

        self.metamask.insert_password()
        self.metamask.click_on_unlock_btn()
        self.metamask.click_on_signin_btn()
        self.metamask.click_on_confirm_btn()
        self.metamask.click_on_confirm_btn()
        self.metamask.click_on_signin_btn()
        self.utills.control_coti_window()
        self.coti.click_on_deposits_btn()
        self.coti.click_on_change_network_btn()
        self.utills.control_metamask_window()

        self.metamask.click_on_confirm_btn()
        self.metamask.click_on_confirm_btn()
        self.utills.control_coti_window()

        self.coti.click_on_deposit_now_btn()

        amount = 5000
        self.coti.insert_deposit_amount(amount)
