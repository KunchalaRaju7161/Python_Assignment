import pytest
from selenium import webdriver
from Configs.ConfigItems import ConfigItems


# Fixture to instantiate the browser driver
@pytest.fixture(params=["chrome"], scope="class")
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    yield driver
    # driver.quit()