
from demoqa_tests.pages.registration_page import RegistrationPage
from datetime import date
from demoqa_tests.data.users import User, Gender, Subject, Hobby
from demoqa_tests.pages.registration_page import RegistrationPage

from datetime import date
from demoqa_tests.data.users import User, Gender, Subject, Hobby
from demoqa_tests.pages.registration_page import RegistrationPage



def test_practice_form():
    # GIVEN
    student = User(
        first_name='Sergey',
        last_name='Petrov',
        email='Petrov@mail.ru',
        genders=Gender.male.value,
        phone_number=8999777777,
        date_of_birth=date(1991, 10, 19),
        subjects=[Subject.chemistry],
        hobbies=[Hobby.sports],
        upload_filename='test.jpg',
        current_address='Moscow',
        state='NCR',
        city='Delhi',
    )

    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_form_register(student)

    # THEN
    registration_page.should_have_registered(student)




"""
def test_student_registration_form():
    # GIVEN
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Sergey')
    registration_page.fill_last_name('Petrov')
    registration_page.fill_email('Petrov@mail.ru')
    registration_page.fill_gender('Male')
    registration_page.fill_mobile('8999777777')
    registration_page.fill_date_of_birth('19', 'October', '1991')

    registration_page.fill_subjects('History')
    registration_page.fill_hobbie('Sports')
    registration_page.upload_picture('test.jpg')

    registration_page.fill_address('Moscow')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Delhi')

    registration_page.submit()

    # THEN
    registration_page.should_registered_user_with(
        'Sergey Petrov',
        'Petrov@mail.ru',
        'Male',
        '8999777777',
        '19 October,1991',
        'History',
        'Sports',
        'test.jpg',
        'Moscow',
        'NCR Delhi'
    )
"""