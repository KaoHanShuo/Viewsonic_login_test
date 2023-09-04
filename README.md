# Viewsonic_login_test

## 所需套件
    1. pytest
    2. selenium

## 注意事項
    clone 整包git之後，需要再創建"Params.py"，並依序輸入資料，格式如下
    
        class __AccountParams(object):
            GMAIL_ACCOUNT = "輸入gmail帳號"
            GMAIL_PW = "輸入gmail密碼"
            VIEWSONIC_ACCOUNT = "輸入已驗證viewsonic帳號"
            VIEWSONIC_PW = "輸入已驗證viewsonic密碼"
            UNVERIFY_ACCOUNT = "輸入已註冊未驗證viewsonic帳號"
            UNVERIFY_PW = "輸入已註冊未驗證viewsonic密碼"
            INVALID_ACCOUNT = "輸入隨意錯誤email"
            INVALID_PW = "輸入隨意錯誤密碼"
        ACCOUNT = __AccountParams

## 如何執行
    到Viewsonic_login_test目錄資料夾，使用終端機執行 "pytest"
    或者個別執行測試項目    
        pytest -m empty_email
        pytest -m error_email
        pytest -m unverify_account
        pytest -m cancel
        pytest -m empty_pw
        pytest -m error_pw
        pytest -m login_success