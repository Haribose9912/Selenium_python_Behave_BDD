import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from behave import *
from utilities import ConfigReader


def before_scenario(context, driver):
    browser_name = ConfigReader.read_configuration("basic info", "browser")
    if browser_name == "chrome":
        context.driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "firefox":
        context.driver = webdriver.Firefox(GeckoDriverManager().install())
    elif browser_name == "edge":
        context.driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))


def after_scenario(context, driver):
    context.driver.quit()  # Close the WebDriver


def after_step(context, scenario):
    if scenario.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png()
                      , name="failed_screenshot"
                      , attachment_type=AttachmentType.PNG)
