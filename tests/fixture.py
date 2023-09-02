import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


@pytest.fixture()
def launcher_web():
    service = Service()
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=option)
    driver.get(
        "https://auth.myviewboard.com/oidc/v1/auth/identifier?response_type=code&client_id=mvb-core-service&state=dnJ-djRsdEJVc2R-M2ZOMldQc0RRNWtCbjFoc1phUWw0RktQaFcucTIzQmtQ&redirect_uri=https%3A%2F%2Fmyviewboard.com%2Fhome&scope=openid%20profile%20email&code_challenge=eo6Pj8bi64PC1YPXXtF0ElF-_bALdkaMV7VZwc5Sh5U&code_challenge_method=S256&nonce=dnJ-djRsdEJVc2R-M2ZOMldQc0RRNWtCbjFoc1phUWw0RktQaFcucTIzQmtQ"
    )
