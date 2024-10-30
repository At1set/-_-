class Education():
  bachelor = "bachelor"
  master = "master"
  specialty = "specialty"


class Languages():
  ru = "russian"
  en = "english"


class Employee:
  def __init__(self, total_work_experience : int, specialty_work_experience : int, education : Education, isCloseToWork : bool, isFlexibleResidence : bool, languages : Languages, expected_salary : int) -> None:
    self.total_work_experience = total_work_experience
    self.specialty_work_experience = specialty_work_experience
    self.education = education
    self.isCloseToWork = isCloseToWork
    self.isFlexibleResidence = isFlexibleResidence
    self.languages = languages
    self.expected_salary = expected_salary