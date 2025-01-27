from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time as t

class CotiElements:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def click_on_connect_btn(self):
        try:
            connect_wallet_button = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 "div.WalletConnectButton_wrapper__Kbgbr > button.Button_button-component__zTGW4.Button_wallet-button-connect__4nyrg.Button_wallet-button__xmYF-")
            ))
            connect_wallet_button.click()
        except Exception as e:
            print("Error acquired while clicking on 'Connect' button:", e)

    def mark_terms_checkbox(self):
        try:
            checkbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='CheckBox_checkmark__w4fqa']")))
            checkbox.click()
        except Exception as e:
            print("Error acquired while marking the terms checkbox:", e)

    def click_on_select_btn(self):
        try:
            select_btn = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.ConnectType_wrapper__lQiRl > button.Button_button-component__zTGW4")))
            select_btn.click()
        except Exception as e:
            print("Error acquired while clicking on the 'Select' button:", e)

    def locate_error_msg_element(self):
        try:
            error_message_element = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//p[contains(text(), 'This service is unavailable in your jurisdiction')]")
            ))
            return error_message_element.text
        except Exception as e:
            print("Error: The message did not appear or could not be located.", e)

    def click_on_deposits_btn(self):
        try:
            deposit_btn = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.link-16-medium[href='/deposits']")))
            deposit_btn.click()
        except Exception as e:
            print("Error acquired while clicking on 'Deposits' button", e)

    def click_on_change_network_btn(self):
        try:
            change_network_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Unlock']")))
            change_network_btn.click()
        except Exception as e:
            print("Error acquired while clicking on 'Change Network' button:", e)

    def click_on_deposit_now_btn(self):
        try:
            deposit_now_btn = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.DepositNowButton_button__5tQZK"))
            )
            deposit_now_btn.click()
        except Exception as e:
            print("Error acquired while clicking on 'Deposit Now' button:", e)

    def insert_deposit_amount(self, amount):
        try:
            amount_input_elem = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='text-1-14-regular Input_input-class__xD8P+']")))
            amount_input_elem.send_keys(amount)
        except Exception as e:
            print("Error acquired while inserting amount:", e)




class MetaMaskElements:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def insert_password(self):
        # t.sleep(2)
        try:
            password_input = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
            password_input.send_keys("SimonJoiningCOTI")  # ;)
        except Exception as e:
            print("Error acquired while inserting the password:", e)

    def click_on_unlock_btn(self):
        try:
            t.sleep(2)
            unlock_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Unlock']")))
            unlock_button.click()
        except Exception as e:
            print("Error acquired while click the 'Unlock' button:", e)

    def click_on_confirm_btn(self):
        try:
            t.sleep(2)
            confirm_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Confirm']")))
            confirm_button.click()
        except Exception as e:
            print("Error acquired while clicking on the 'Confirm' button:", e)


    def click_on_signin_btn(self):
        try:
            t.sleep(2)
            signin_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button btn--rounded btn-primary page-container__footer-button']")))
            signin_btn.click()
        except Exception as e:
            print(f"Error acquired while click on 'Sign' button", e)





