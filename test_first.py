from selene import browser, have, be


def test_google_search():
    browser.open('https://www.google.com/')
    browser.element('[name="q"]').should(be.blank).type('UmbrellaIT').press_enter()
    browser.element('[id="search"]').should(have.text('Umbrella IT | Разработка Веб и Мобильных приложений'))
