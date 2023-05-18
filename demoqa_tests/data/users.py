from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List
import dataclasses
from datetime import datetime, date
from enum import Enum
from typing import List
import dataclasses
from datetime import date
from enum import Enum
from typing import List


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Subject(Enum):
    accounting = 'Accounting'
    arts = 'Arts'
    biology = 'Biology'
    english = 'English'
    chemistry = 'Chemistry'
    computer_science = 'Computer Science'
    commerce = 'Commerce'
    maths = 'Maths'
    physics = 'Physics'
    economics = 'Economics'
    social_studies = 'Social Studies'


class Hobby(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    genders: Gender
    phone_number: int
    date_of_birth: date
    subjects: List[Subject]
    hobbies: List[Hobby]
    upload_filename: str
    current_address: str
    state: str
    city: str
