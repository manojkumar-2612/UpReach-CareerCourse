from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path='C:\drivers\Chrome WebDriver\chromedriver.exe')
driver.get(
    "https://www.linkedin.com/uas/login?session_redirect=%2Foauth%2Fv2%2Flogin-success%3Fapp_id%3D10935516%26auth_type%3DAC%26flow%3D%257B%2522scope%2522%253A%2522r_liteprofile%2Br_emailaddress%2522%252C%2522appId%2522%253A10935516%252C%2522authorizationType%2522%253A%2522OAUTH2_AUTHORIZATION_CODE%2522%252C%2522redirectUri%2522%253A%2522https%253A%252F%252Freact-my.upreach.org.uk%252Fauth%252Flinkedin%252Fcallback%2522%252C%2522currentStage%2522%253A%2522LOGIN_SUCCESS%2522%252C%2522currentSubStage%2522%253A0%252C%2522authFlowName%2522%253A%2522generic-permission-list%2522%252C%2522state%2522%253A%2522pVXTXZyC8eobXz8fgPatDrstwK65RR00u8CqFsrS%2522%252C%2522creationTime%2522%253A1646991081261%257D&fromSignIn=1&trk=oauth&cancel_redirect=%2Foauth%2Fv2%2Flogin-cancel%3Fapp_id%3D10935516%26auth_type%3DAC%26flow%3D%257B%2522scope%2522%253A%2522r_liteprofile%2Br_emailaddress%2522%252C%2522appId%2522%253A10935516%252C%2522authorizationType%2522%253A%2522OAUTH2_AUTHORIZATION_CODE%2522%252C%2522redirectUri%2522%253A%2522https%253A%252F%252Freact-my.upreach.org.uk%252Fauth%252Flinkedin%252Fcallback%2522%252C%2522currentStage%2522%253A%2522LOGIN_SUCCESS%2522%252C%2522currentSubStage%2522%253A0%252C%2522authFlowName%2522%253A%2522generic-permission-list%2522%252C%2522state%2522%253A%2522pVXTXZyC8eobXz8fgPatDrstwK65RR00u8CqFsrS%2522%252C%2522creationTime%2522%253A1646991081261%257D")
print(driver.title)
driver.maximize_window()
driver.find_element_by_id("username").send_keys("testupreach@gmail.com")
driver.find_element_by_id("password").send_keys("upRCAN78!")
driver.find_element_by_css_selector("button[aria-label='Sign in']").click()
driver.find_element_by_css_selector("button[class='btn btn-linkedin btn-lg']").click()
time.sleep(5)
driver.find_element_by_xpath("(//a[normalize-space()='Build your Skills'])[1]").click()
driver.find_element_by_xpath("(//a[normalize-space()='Career Courses'])[1]").click()
time.sleep(5)
driver.find_element_by_xpath("//a[@id='careerModule_1']/div/div").click()
element = driver.find_element_by_name("career_stream_id")
drp = Select(element)
drp.select_by_visible_text("Consultancy")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='careerModule_3']/div/span").click()
time.sleep(2)
# driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div[3]/div/div[2]/div[3]/div[1]/div/a/button").click()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div[3]/div/div[2]/div[5]/div[1]/div/a/button").click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element_by_id("option_answer_361").click()
driver.find_element_by_id("option_answer_368").click()
driver.find_element_by_id("option_answer_375").click()
driver.find_element_by_xpath("//*[@id='msform']/button").click()
time.sleep(2)
driver.find_element_by_xpath("//button[normalize-space()='Next']").click()
