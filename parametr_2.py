import pytest
import selenium
from selenium import webdriver
import allure
from selenium.webdriver.common.by import By     
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.mark.parametrize("browser", ["chrome", "firefox"])
@pytest.mark.parametrize("num1,num2,expected_value",
                        [(10,10,20),
                            (20,30,60),
                            (30,40,70)])
@allure.feature("Addition functionality")
@allure.severity("p1")
def test_addition(browser, num1, num2, expected_value):
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service())
    elif browser == "firefox":
        driver = webdriver.Firefox(service=Service())
    else:
        raise ValueError("Unsupported browser")

    driver.get("https://lambdatest.com/selenium-playground/simple-form-demo")
    #  10)
    driver.maximize_window()
    driver.implicitly_wait(5)


    
    # wait = WebDriverWait(driver,   10)
    # wait.until(EC.presence_of_element_located(By.XPATH, "//input[@placeholder='Please enter first value']"))
    # num1_input=driver.find_element(By.XPATH, "//input[@placeholder='Please enter first value']")
    num1_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Please enter first value']")))
    num1_input.send_keys(num1)
    num2_input=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Please enter second value']")))
    num2_input.send_keys(num2)

    # Assuming there is a button to add the numbers
    sum_btn=driver.find_element(By.XPATH,"//button[text()='Get Sum']")
    sum_btn.click()

    result = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'addmessage')))
    

    # Example operation, replace with actual logic
    result = num1 + num2
    assert result == expected_value, f"Expected {expected_value}, but got {result}"

    allure.attach(driver.get_screenshot_as_png(), 
                      name="result_screenshot",
                      attachment_type=allure.attachment_type.PNG)
    
    driver.quit()