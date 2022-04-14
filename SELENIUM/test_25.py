import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome(executable_path="C:/Users/Vlad/Desktop/TESTER/SELENIUM/chromedriver.exe")
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')
   try:
      wait = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
      yield
   finally:
      pytest.driver.quit()

#################################################################################

def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('admin@mail.ru')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('admin1')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

   pytest.driver.implicitly_wait(10)
   images = pytest.driver.find_element_by_css_selector('.card-deck .card-img-top')
   pytest.driver.implicitly_wait(10)
   names = pytest.driver.find_element_by_css_selector('.card-deck .card-title')
   pytest.driver.implicitly_wait(10)
   description = pytest.driver.find_element_by_css_selector('.card-deck .card-text')

   try:

      assert images.get_attribute("src") != ""
      assert names.text != ''
      assert description.text != ''

   finally:
      pytest.driver.quit()

