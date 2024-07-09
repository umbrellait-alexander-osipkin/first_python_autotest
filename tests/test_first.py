import allure
from selene import browser, have, be


@allure.epic("Search")
@allure.title("Search by name")
@allure.label('owner', 'Alexander Osipkin')
@allure.label('layer', 'web')
@allure.tag('regress', 'web')
@allure.severity('critical')
def test_google_search():
    with allure.step("Открываем главную страницу google"):
        browser.open('/')
    with allure.step("Вводим в поле поиска UmbrellaIT"):
        browser.element('[name="q"]').should(be.blank).type('UmbrellaIT').press_enter()
    with allure.step("Проверяем корректность полученной информации"):
        browser.element('[id="search"]').should(have.text('Umbrella IT | Разработка Веб и Мобильных приложений'))