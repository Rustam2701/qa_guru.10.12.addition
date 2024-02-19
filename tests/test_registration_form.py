from selene import browser, be, have, by
import allure
from selene.core import command

import resource


@allure.title("Registration form")
def test_for_demoqa():
    with allure.step('Open form'):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.element('[aria-label="Consent"]').click()
        browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3))
        browser.all("[id^=google_ads][id$=container__]").perform(command.js.remove)

    with allure.step('Fill form user data'):
        browser.element('#firstName').type('Светлана')
        browser.element('#lastName').type('Федоровна')
        browser.element('#userEmail').type('bethere@example.com')
        browser.element('[for=gender-radio-2]').click()
        browser.element('#userNumber').type('7909555678')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click().element(by.text('1993')).click()
        browser.element('.react-datepicker__month-select').click().element(by.text('May')).click()
        browser.element('.react-datepicker__day--022').click()
        browser.element('#subjectsInput').should(be.blank).type('english')
        browser.element('#react-select-2-option-0').click()
        browser.element('.subjects-auto-complete__multi-value__label').should(have.text('English'))

    with allure.step('Fill form user other data'):
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('#uploadPicture').send_keys(resource.path('111.png'))
        browser.element('#currentAddress').type('Ленина 139')
        browser.element('#react-select-3-input').type('Haryana').press_enter()
        browser.element('#react-select-4-input').type('Karnal').press_enter()
        browser.element('#submit').press_enter()

    with allure.step('Check form'):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
        browser.element('.table').all('td:nth-child(2)').should(have.texts(
            'Светлана Федоровна',
            'bethere@example.com',
            'Female',
            '7909555678',
            '22 May,1993',
            'English',
            'Sports',
            '111.png',
            'Ленина 139',
            'Haryana Karnal'
        ))
        browser.element('#closeLargeModal').press_enter()
