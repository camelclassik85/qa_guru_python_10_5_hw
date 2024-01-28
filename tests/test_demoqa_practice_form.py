import os, platform
from selene import browser, be, have, command
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_fill_registration_form_1():
    browser.open("automation-practice-form")
    browser.element('#firstName').should(be.blank).type("Good")
    browser.element('#lastName').should(be.blank).type("Game")
    browser.element('#userEmail').should(be.blank).type("gg@goga.com")
    browser.element("[for='gender-radio-1']").click()
    browser.element('#userNumber').should(be.blank).type("9876543210")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1955"]').perform(command.js.scroll_into_view).click()
    browser.element('.react-datepicker__month-select').click().element('[value="6"]').click()
    browser.element('.react-datepicker__day--020').click()
    browser.element('#subjectsInput').should(be.blank).type("comp").press_enter()
    browser.element('#subjectsInput').type('eng')
    browser.element('#react-select-2-option-0').click()
    browser.element("[for='hobbies-checkbox-1']").click()
    browser.element("[for='hobbies-checkbox-3']").click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('cat.jpg'))
    browser.element('#currentAddress').should(be.blank).type('Good for good 123456')
    browser.element('#state').click()
    browser.element('#react-select-3-option-2').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    browser.element("#submit").perform(command.js.scroll_into_view)
    browser.element("#submit").click()
    browser.element('.modal-dialog').should(be.existing)
    browser.element(".table").all('td:nth-child(2)').should(
        have.exact_texts(
            'Good Game',
            'gg@goga.com',
            'Male',
            '9876543210',
            '20 July,1955',
            'Computer Science, English',
            'Sports, Music',
            'cat.jpg',
            'Good for good 123456',
            'Haryana Karnal',
        ))


def birthday_input():
    if platform.system() == 'Windows':
        # browser.driver.find_element(By.CSS_SELECTOR, '#dateOfBirthInput').send_keys(Keys.CONTROL, "a")
        browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('20 Jul 1955').press_enter()
    elif platform.system() == 'Darwin':
        # browser.driver.find_element(By.CSS_SELECTOR, '#dateOfBirthInput').send_keys(Keys.COMMAND, "a")
        browser.element('#dateOfBirthInput').send_keys(Keys.COMMAND, 'a').type('20 Jul 1955').press_enter()
    else:
        print("Uncompatible operating system. Test stopped")
        browser.quit()
    # browser.element('#dateOfBirthInput').type('20 Jul 1955').press_enter() # нужно, если через закомменченные делать


def test_fill_registration_form_2():
    browser.open("automation-practice-form")
    browser.element('#firstName').should(be.blank).type("Good")
    browser.element('#lastName').should(be.blank).type("Game")
    browser.element('#userEmail').should(be.blank).type("gg@goga.com")
    browser.element("[for='gender-radio-1']").click()
    browser.element('#userNumber').should(be.blank).type("9876543210")
    # С очисткой поля ввода тест падает, так как сбрасываются все элементы в div с id=app. Это найденный баг
    browser.element('#dateOfBirthInput').click()
    birthday_input()
    browser.element('#subjectsInput').should(be.blank).send_keys("comp").press_enter()
    browser.element('#subjectsInput').click().send_keys('eng')
    browser.element('#react-select-2-option-0').click()
    browser.element("[for='hobbies-checkbox-1']").should(be.clickable).click()
    browser.element("[for='hobbies-checkbox-3']").click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('cat.jpg'))
    browser.element('#currentAddress').should(be.blank).type('Good for good 123456')
    browser.element('#state').click()
    browser.element('#react-select-3-option-2').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    browser.element("#submit").perform(command.js.scroll_into_view)
    browser.element("#submit").click()
    browser.element('.modal-dialog').should(be.existing)
    browser.element(".table").all('td:nth-child(2)').should(
        have.exact_texts(
            'Good Game',
            'gg@goga.com',
            'Male',
            '9876543210',
            '20 July,1955',
            'Computer Science, English',
            'Sports, Music',
            'cat.jpg',
            'Good for good 123456',
            'Haryana Karnal',
        ))
