from datetime import date
from demoqa_tests.data.users import User, Gender, Subject, Hobby
from demoqa_tests.pages.registration_page import RegistrationPage



def test_practice_form():
    # GIVEN
    student = User(
        first_name='Sergey',
        last_name='Petrov',
        email='Petrov@mail.ru',
        gender=Gender.male.value,
        phone_number=8999777777,
        date_of_birth=date(1991, 10, 19),
        subjects=[Subject.chemistry.value],
        hobbies=[Hobby.sports.value],
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
    registration_page.should_registered_user_with(student)
