from pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='module')
def chrome_browser_instance(request):
    """
        Provide a selenium webdriver instance
    """
    
    options = Options()
    options.headless = False
    browser = webdriver.Chrome(chrome_options=options)
    yield browser
    borwser.close
    