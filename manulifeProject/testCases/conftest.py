from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="../testCases/chromedriver.exe")
    return driver
