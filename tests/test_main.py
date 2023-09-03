import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import logging
import sys

sys.path.append(".")

# Ourself imports
# from conftest import launcher_web
from login_page import ViewsonicLoginPage
from Params import ACCOUNT
from time import sleep

logging.basicConfig(level=logging.DEBUG)


class TestCase:
    # 輸入空白email > 電子郵件和密碼不能為空白
    @pytest.mark.empty_email
    def test_empty_email(self, launcher_web):
        "輸入空白email"
        try:
            login_page = ViewsonicLoginPage(launcher_web)
            login_page.click_email_signin()
            sleep(2)
            assert login_page.get_error_message() == "電子郵件和密碼不能為空白"
            logging.info(f"測項 {self.test_empty_email.__doc__}...ok")
        except Exception as e:
            logging.error(f"測項 {self.test_empty_email.__doc__}...fail, error: {e}")
            raise

    # 輸入錯誤email > 在該組織內部與 myViewBoard 資料庫中皆無法找到該帳戶
    @pytest.mark.error_email
    def test_error_email(self, launcher_web):
        "輸入錯誤email"
        try:
            login_page = ViewsonicLoginPage(launcher_web)
            login_page.set_viewsonic_email(ACCOUNT.INVALID_ACCOUNT)
            login_page.click_email_signin()
            sleep(2)
            assert login_page.get_error_message() == "在該組織內部與 myViewBoard 資料庫中皆無法找到該帳戶"
            logging.info(f"測項 {self.test_error_email.__doc__}...OK")
        except Exception as e:
            logging.error(f"測項 {self.test_error_email.__doc__}...fail, error: {e}")
            raise

    # 輸入未驗證viewsonic帳號後，正確密碼 > 此帳戶未使用
    @pytest.mark.unverify_account
    def test_unverify_account(self, launcher_web):
        "輸入未驗證viewsonic帳號密碼"
        try:
            login_page = ViewsonicLoginPage(launcher_web)
            login_page.set_viewsonic_email(ACCOUNT.UNVERIFY_ACCOUNT)
            login_page.click_email_signin()
            login_page.set_viewsonic_pw(ACCOUNT.UNVERIFY_PW)
            login_page.click_pw_signin()
            sleep(2)
            assert login_page.get_error_message() == "此帳戶未啟用"
            logging.info(f"測項 {self.test_unverify_account.__doc__}...OK")
        except Exception as e:
            logging.error(f"測項 {self.test_unverify_account.__doc__}...fail, error: {e}")
            raise

    # 輸入已驗證viewsonic帳號後，點擊取消 > 返回輸入帳號畫面
    @pytest.mark.cancel
    def test_cancel_login(self, launcher_web):
        "點擊取消登入"
        try:
            login_page = ViewsonicLoginPage(launcher_web)
            login_page.set_viewsonic_email(ACCOUNT.VIEWSONIC_ACCOUNT)
            login_page.click_email_signin()
            login_page.click_signin_cancel()
            sleep(2)
            assert login_page.email_exist()
            logging.info(f"測項 {self.test_cancel_login.__doc__}...OK")
        except Exception as e:
            logging.error(f"測項 {self.test_cancel_login.__doc__}...fail, error: {e}")
            raise

    # 輸入已驗證viewsonic帳號後，空白密碼 > 電子郵件和密碼不能為空白
    @pytest.mark.empty_pw
    def test_empty_pw(self, launcher_web):
        "正確email, 輸入空白密碼"
        try:
            login_page = ViewsonicLoginPage(launcher_web)
            login_page.set_viewsonic_email(ACCOUNT.VIEWSONIC_ACCOUNT)
            login_page.click_email_signin()
            login_page.click_pw_signin()
            sleep(2)
            assert login_page.get_error_message() == "電子郵件和密碼不能為空白"
            logging.info(f"測項 {self.test_empty_pw.__doc__}...OK")
        except Exception as e:
            logging.error(f"測項 {self.test_empty_email.__doc__}...fail, error: {e}")
            raise

    # 輸入已驗證viewsonic帳號後，錯誤密碼 > 密碼不正確
    @pytest.mark.error_pw
    def test_error_pw(self, launcher_web):
        "正確email, 輸入錯誤密碼"
        try:
            login_page = ViewsonicLoginPage(launcher_web)
            login_page.set_viewsonic_email(ACCOUNT.VIEWSONIC_ACCOUNT)
            login_page.click_email_signin()
            login_page.set_viewsonic_pw(ACCOUNT.INVALID_PW)
            login_page.click_pw_signin()
            sleep(2)
            assert login_page.get_error_message() == "密碼不正確"
            logging.info(f"測項 {self.test_error_pw.__doc__}...OK")
        except Exception as e:
            logging.error(f"測項 {self.test_error_pw.__doc__}...fail, error: {e}")
            raise

    # 輸入已驗證viewsonic帳號後，正確密碼 > 登入成功
    @pytest.mark.login_success
    def test_login_success(self, launcher_web):
        "正確帳號密碼登入"
        try:
            login_page = ViewsonicLoginPage(launcher_web)
            login_page.set_viewsonic_email(ACCOUNT.VIEWSONIC_ACCOUNT)
            login_page.click_email_signin()
            login_page.set_viewsonic_pw(ACCOUNT.VIEWSONIC_PW)
            login_page.click_pw_signin()
            sleep(10)
            login_page.screen_shot("success")
            assert login_page.get_error_message() == "密碼不正確"
            logging.info(f"測項 {self.test_error_pw.__doc__}...OK")
        except Exception as e:
            logging.error(f"測項 {self.test_error_pw.__doc__}...fail, error: {e}")
            raise


# 輸入空白email > 電子郵件和密碼不能為空白
# 輸入錯誤email格式及未註冊email > 在該組織內部與 myViewBoard 資料庫中皆無法找到該帳戶
# 輸入未驗證viewsonic帳號後，正確密碼 > 此帳戶未使用
# 輸入已驗證viewsonic帳號後，點擊取消 > 返回輸入帳號畫面
# 輸入已驗證viewsonic帳號後，空白密碼 > 電子郵件和密碼不能為空白
# 輸入已驗證viewsonic帳號後，錯誤密碼 > 密碼不正確
# 輸入已驗證viewsonic帳號後，正確密碼 > 登入成功

## 以下未完成
# 切換語系 > 成功切換(用中日英做範例)
# 使用gmail帳號登入(未註冊及未驗證gmail不為viewsonic測項) > 登入成功
# 點擊忘記密碼 > 跳轉到忘記密碼頁面
# 點擊立刻註冊 > 跳轉到註冊頁面
# 點擊再次發送密碼 > 跳轉到再次發送密碼頁面
