import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from fixture import launcher_web


class TestCase:
    def test_a(self, launcher_web):
        # try:
        x = "hello"
        with pytest.raises(AssertionError) as info:
            assert "a" in x
        print(info.type)

    def test_b(self, launcher_web):
        x = "hello"
        assert "a" in x
