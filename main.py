import pytest as pytest
from selene.support.shared import browser
from selene import be, have
@pytest.fixture
def Browser():
    browser.config.window_height = 800
    browser.config.window_width = 1280

def test_google(Browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_empty_search(Browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('гшмдп на пропнп югпм').press_enter()
    browser.element('[class="card-section"]').should(have.text('Не найдено ни одного документа по запросу'))
