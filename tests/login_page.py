from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
import logging

ele_google = "//form[@id='google']"
ele_input_viewsonic_email = "//input[@name='login']"
ele_input_viewsonic_pw = "//input[@name='password']"
ele_error_message = "//span[@id='error']"
ele_signup_url = "//a[@class='primary-color f-register']"
ele_forget_url = "//a[@class='primary-color f-pw']"
ele_resend_email_url = "//a[@class='primary-color f-rs']"
ele_signin_email_button = "//button[@class='login-submit inspect s1']"
ele_signin_pw_button = "//button[@class='login-submit submit s2']"
ele_signin_cancel = "//button[@class='login-cancel s2']"
ele_language_change = "//select[@aria-label='language selection']"
ele_japenese = "//option[@value='ja']"
ele_zh = "//option[@value='zh']"
ele_en = "//option[@value='en']"

logging.basicConfig(level=logging.DEBUG)


class ViewsonicLoginPage(object):
    def __init__(self, driver):
        self.driver: webdriver.Chrome = driver
        self.wait = 5

    def web_driver_wait(self, params):
        "等待元素出現"
        try:
            ele = WebDriverWait(self.driver, self.wait).until(
                EC.visibility_of_element_located((By.XPATH, params))
            )
            return ele
        except TimeoutException:
            logging.warning(f"元素搜尋超時, err: TimeoutException")
            # print(f"超時, err: TimeoutException")

    def screen_shot(self, file_name):
        self.driver.save_screenshot(f"./document/{file_name}.png")

    def click_gmail_login_button(self):
        "gmail登入按鈕"
        try:
            gmail_button: WebElement = self.web_driver_wait(ele_google)
            gmail_button.click()
        except NoSuchElementException as e:
            logging.warning(f"沒有符合元素, error: {e}")
        except Exception as e:
            logging.warning(f"不預期錯誤, error: {e}")

    def set_viewsonic_email(self, email):
        "設值給email欄位"
        try:
            input_email: WebElement = self.web_driver_wait(ele_input_viewsonic_email)
            input_email.send_keys(email)
        except NoSuchElementException as e:
            logging.warning(f"沒有符合元素, error: {e}")
        except Exception as e:
            logging.warning(f"不預期錯誤, error: {e}")

    def email_exist(self):
        "email欄位存在"
        try:
            input_email: WebElement = self.web_driver_wait(ele_input_viewsonic_email)
            if input_email:
                return True
        except NoSuchElementException as e:
            logging.warning(f"沒有符合元素, error: {e}")
        except Exception as e:
            logging.warning(f"不預期錯誤, error: {e}")

    def set_viewsonic_pw(self, pw):
        "設值給pw"
        try:
            input_pw: WebElement = self.web_driver_wait(ele_input_viewsonic_pw)
            input_pw.send_keys(pw)
        except NoSuchElementException as e:
            logging.warning(f"沒有符合元素, error: {e}")
        except Exception as e:
            logging.warning(f"不預期錯誤, error: {e}")

    def get_error_message(self):
        "取得錯誤訊息"
        try:
            error_message: WebElement = self.web_driver_wait(ele_error_message)
            return error_message.text
        except NoSuchElementException as e:
            logging.warning(f"沒有符合元素, error: {e}")
        except Exception as e:
            logging.warning(f"不預期錯誤, error: {e}")

    def jump_to_signup(self):
        "跳轉至註冊頁面"
        try:
            signup_url: WebElement = self.web_driver_wait(ele_signup_url)
            signup_url.click()
        except NoSuchElementException as e:
            logging.warning(f"沒有符合元素, error: {e}")
        except Exception as e:
            logging.warning(f"不預期錯誤, error: {e}")

    def jump_to_forget(self):
        "跳轉至忘記密碼"
        try:
            forget_page_url: WebElement = self.web_driver_wait(ele_forget_url)
            forget_page_url.click()
        except NoSuchElementException as e:
            logging.warning(f"沒有符合元素, error: {e}")
        except Exception as e:
            logging.warning(f"不預期錯誤, error: {e}")

    def jump_to_resend_email(self):
        "跳轉至重寄驗證信件"
        try:
            resend_url: WebElement = self.web_driver_wait(ele_resend_email_url)
            resend_url.click()
        except NoSuchElementException as e:
            logging.warning(f"沒有符合元素, error: {e}")
        except Exception as e:
            logging.warning(f"不預期錯誤, error: {e}")

    def click_email_signin(self):
        "點擊email登入"
        try:
            signin_button: WebElement = self.web_driver_wait(ele_signin_email_button)
            signin_button.click()
        except NoSuchElementException as e:
            logging.warning(f"沒有符合元素, error: {e}")
        except Exception as e:
            logging.warning(f"不預期錯誤, error: {e}")

    def click_pw_signin(self):
        "點擊密碼登入"
        try:
            signin_button: WebElement = self.web_driver_wait(ele_signin_pw_button)
            signin_button.click()
        except NoSuchElementException as e:
            logging.warning(f"沒有符合元素, error: {e}")
        except Exception as e:
            logging.warning(f"不預期錯誤, error: {e}")

    def click_signin_cancel(self):
        "點擊登入取消"
        try:
            signin_cancel_button: WebElement = self.web_driver_wait(ele_signin_cancel)
            signin_cancel_button.click()
        except NoSuchElementException as e:
            logging.warning(f"沒有符合元素, error: {e}")
        except Exception as e:
            logging.warning(f"不預期錯誤, error: {e}")

    def click_change_language(self):
        "改變語言"
        try:
            language_list: WebElement = self.web_driver_wait(ele_language_change)
            language_list.click()
        except NoSuchElementException as e:
            logging.warning(f"沒有符合元素, error: {e}")
        except Exception as e:
            logging.warning(f"不預期錯誤, error: {e}")

    def select_jp_language(self):
        "選擇日文"
        try:
            language_jp: WebElement = self.web_driver_wait(ele_japenese)
            language_jp.click()
        except NoSuchElementException as e:
            logging.warning(f"沒有符合元素, error: {e}")
        except Exception as e:
            logging.warning(f"不預期錯誤, error: {e}")

    def select_zh_language(self):
        "選擇繁體中文"
        try:
            language_zh: WebElement = self.web_driver_wait(ele_zh)
            language_zh.click()
        except NoSuchElementException as e:
            logging.warning(f"沒有符合元素, error: {e}")
        except Exception as e:
            logging.warning(f"不預期錯誤, error: {e}")

    def select_en_language(self):
        "選擇英文"
        try:
            language_en: WebElement = self.web_driver_wait(ele_en)
            language_en.click()
        except NoSuchElementException as e:
            logging.warning(f"沒有符合元素, error: {e}")
        except Exception as e:
            logging.warning(f"不預期錯誤, error: {e}")
