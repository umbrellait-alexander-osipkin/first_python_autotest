from selene import browser, be, have


def test_register():
    browser.open('https://demowebshop.tricentis.com/register')
    browser.element('[id="gender-male"]').click()
    # should.be - не обязательно
    browser.element('[id="FirstName"]').should(be.blank).type('Alexander')
    browser.element('[id="LastName"]').should(be.blank).type('Osipkin')
    browser.element('[id="Email"]').should(be.blank).type('alextestuser@usertest.com') # емеил должен быть уникальным
    browser.element('[id="Password"]').should(be.blank).type('1234567890')
    browser.element('[id="ConfirmPassword"]').should(be.blank).type('1234567890')
    browser.element('[id="register-button"]').click()
    # пример проверки успешной регистрации
    # в первом варианте проверяем что зарегистрировались
    # во втором, что в хедере отображается зарегистрированные емеил
    browser.element('.page-body .result').should(have.text('Your registration completed'))
    browser.element('.header-links .account').should(have.text('alextestuser@usertest.com'))
