from selene import browser, have, command
from demoqa_tests import resource
from selene.support.shared import browser



class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def fill_form_register(self, student):
        browser.element('[id = firstName]').type(student.first_name)
        browser.element('[id = lastName]').type(student.last_name)
        browser.element('[id = userEmail]').type(student.email)
        browser.element(f'[name=gender][value={student.gender}]+label').click()
        browser.element('[id = userNumber]').type(student.phone_number)
        browser.element('#dateOfBirthInput').press()
        browser.element('.react-datepicker__month-select').send_keys(student.date_of_birth.strftime('%B'))
        browser.element('.react-datepicker__year-select').send_keys(student.date_of_birth.year)
        browser.element(f'.react-datepicker__day--0{student.date_of_birth.day}').click()
        for subject in student.subjects:
            browser.element('#subjectsInput').type(subject).press_tab()
        for hobby in student.hobbies:
            browser.all('#hobbiesWrapper .custom-checkbox').element_by(have.exact_text(hobby)).click()
        browser.element('#uploadPicture').type(resource.path(student.upload_filename))
        browser.element('#currentAddress').type(student.current_address)
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(student.state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(student.city)).click()
        browser.element('#submit').press_enter()

    def should_registered_user_with(self, student):
        full_name = f'{student.first_name} {student.last_name}',
        date_of_birth = f'{student.date_of_birth.day} {student.date_of_birth.strftime("%B")},{student.date_of_birth.year}'
        city = f'{student.state} {student.city}'

        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                student.email,
                student.gender,
                str(student.phone_number),
                date_of_birth,
                student.subjects,
                student.hobbies,
                student.upload_filename,
                student.current_address,
                city
            ))



"""
class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_gender(self, value):
        browser.element(f'[name=gender][value={value}]+label').click()

    def fill_mobile(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').press()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobbie(self, value):
        browser.all('#hobbiesWrapper .custom-checkbox').element_by(
            have.exact_text(value)).click()

    def upload_picture(self, name):
        browser.element('#uploadPicture').type(resource.path(name))

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, value):
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()


    def submit(self):
        browser.element('#submit').press_enter()

    def should_registered_user_with(self, full_name, email, gender, mobile, date_of_birth, subject, hobby, picture, address, city):
        browser.element('.table').all('td').even.should(have.exact_texts(
                full_name,
                email,
                gender,
                mobile,
                date_of_birth,
                subject,
                hobby,
                picture,
                address,
                city
            ))
"""

