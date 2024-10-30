from Employee import *

def whether_to_hire(employee : Employee):
  return employee.total_work_experience > 3 and \
  employee.specialty_work_experience > 1 and \
  employee.education in [Education.master, Education.specialty] and \
  employee.isCloseToWork or employee.isFlexibleResidence and \
  [Languages.en, Languages.ru] in employee.languages and \
  employee.expected_salary < 80_000


def ask_user(ask_func, valid_values : list = None):
  while True:
    try:
      res = ask_func()
      if res == "exit": break
      if (isinstance(valid_values, dict)):
        res = valid_values[res]
        return res
    except: continue
    if not valid_values or res in valid_values: return res


def main():
  total_work_experience = 0
  specialty_work_experience = 0
  education = None
  isCloseToWork = False
  isFlexibleResidence = False
  languages = []
  expected_salary = 0

  total_work_experience     = ask_user(
    lambda: int(input("Введите ваш общий стаж работы: "))
  )
  specialty_work_experience = ask_user(
    lambda: int(input("Введите ваш стаж работы по специальности: "))
  )
  education                 = ask_user(
    lambda: input("Введите ваше образование (b - bachelor; m - master, s - specialty): "),
    {
      "b": Education.bachelor,
      "m": Education.master,
      "s": Education.specialty,
      "bachelor": Education.bachelor,
      "master": Education.master,
      "speciality": Education.specialty,
    }
  )
  isCloseToWork             = ask_user(
    lambda: int(input("Живете ли вы рядом с работой? (0 - нет, 1 - да): ")),
    [0, 1]
  )
  if (not isCloseToWork):   isFlexibleResidence = ask_user(
    lambda: int(input("Готовы ли вы переехать к месту работы? (0 - нет, 1 - да): ")),
    [0, 1]
  )
  
  lang_count = ask_user(
    lambda: int(input("Сколько языков вы знаете? "))
  )

  def getLanguages(lang_count):
    global Languages
    print("Пожалуйтса, перечислите их: ru - Русский, en - Английский")
    languages = []
    for i in range(lang_count):
      language = input(f"{i}) ")
      if (language == "ru"): languages.append(Languages.ru)
      elif (language == "en"): languages.append(Languages.en)
      else: raise Exception("Неправильный язык")
      
    return languages
  
  languages = ask_user(
    lambda: getLanguages(lang_count)
  )
  
  expected_salary           = ask_user(
    lambda: int(input("Введите ожидаемую зарплату: "))
  )
  
  employee = Employee(
    total_work_experience,
    specialty_work_experience,
    education,
    isCloseToWork,
    isFlexibleResidence,
    languages,
    expected_salary
  )

  if (whether_to_hire(employee)): print("Вы подходите нам на работу!")
  else: print("К сожалению, на работу вы нам не подходите.")


if __name__ == "__main__":
  main()