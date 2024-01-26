import os
from selene import browser, be, have, command


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
    browser.element('#subjectsInput').type('eng').press_enter()
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