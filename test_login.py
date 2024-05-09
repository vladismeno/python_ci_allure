from selene import browser, be
from selene.support.shared.jquery_style import s, ss


def test_login_passed():
    browser.open('https://www.saucedemo.com/v1/')
    s('//*[@id="user-name"]').type('login')
    s('//*[@id="password"]').type('password')
    s('//*[@id="login-button"]').click()
    s('//*[@id="login_button_container"]/div/form/h3').should(be.visible)


# def test_login_failed():
#     browser.open('https://www.saucedemo.com/v1/')
#     s('//*[@id="user-name"]').type('standard_user')
#     s('//*[@id="password"]').type('secret_sauce')
#     s('//*[@id="login-button"]').click()
#     s('//*[@id="login_button_container"]/div/form/h3').should(be.visible)
