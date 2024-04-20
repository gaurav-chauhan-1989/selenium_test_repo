import inspect

import pytest
from selenium import webdriver
from Config.TestData import Test_Data
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import logging

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope='class')
def init_driver(request):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    service = ChromeService(executable_path=Test_Data.executable_path)
    browser = request.config.getoption("--browser")
    if browser == 'Chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'Firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == 'Edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    #driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture
def custom_logger(level=logging.DEBUG):
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    fh = logging.FileHandler("test_log.logs")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger