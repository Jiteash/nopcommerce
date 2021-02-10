from selenium import webdriver
import pytest
import pytest_html
import pytest_metadata

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver= webdriver.Chrome("E:\chr\chromedriver.exe")
        print("launching chrome")
    else:
        driver=webdriver.Firefox("E:\mr\geckodriver.exe")
        print ("launching firefox")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

##################HTML Report###########

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'customers'
    config._metadata['Tester'] = 'Jiteash'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java_Home",None)
    #metadata.pop("Plugins", None)


