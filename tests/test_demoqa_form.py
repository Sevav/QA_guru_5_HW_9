from demoqa_tests.pages.registration_page import RegistrationPage

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
