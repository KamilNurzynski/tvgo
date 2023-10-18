import pytest
import time


@pytest.fixture
def desired_capabilities():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = 'Pixel3XL'
    desired_caps['app'] = 'C:/Users/Radek/Downloads/orange3-29.apk'
    desired_caps['appPackage'] = 'com.orange.pl.orangetvgo'
    desired_caps['appActivity'] = 'pl.orange.ypt.gui.activity.ActivitySplash'
    return desired_caps


@pytest.fixture(autouse=True)
def slow_down_tests():
    yield
    time.sleep(5)
