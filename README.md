# Viewsonic_login_test

## 所需套件
    1. pytest
    2. selenium

## 注意事項
    clone 整包git之後，需要再創建"Params.py"，格式如下
        class _AccountParams(object):
            GMAIL_ACCOUNT = ""
            GMAIL_PW = ""
            VIEWSONIC_ACCOUNT = ""
            VIEWSONIC_PW = ""
            UNVERIFY_ACCOUNT = ""
            UNVERIFY_PW = ""
            INVALID_ACCOUNT = ""
            INVALID_PW = ""
        ACCOUNT = _AccountParams

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