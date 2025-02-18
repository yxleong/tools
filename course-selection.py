import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# ChromeDriver corresponding to the version
driver = webdriver.Chrome(service=Service())
driver.maximize_window()

# Open the course selection page
driver.get("https://courseselection.ntust.edu.tw/") # replace
time.sleep(5)
username_input = driver.find_element(By.ID, "Ecom_User_ID")
password_input = driver.find_element(By.ID, "Ecom_Password")

# Fill in the credentials
username_input.send_keys("REPLACE_URS")  # Replace with actual username
password_input.send_keys("REPLACE_URS")  # Replace with actual password

password_input.send_keys(Keys.RETURN)
time.sleep(3)

driver.get("https://courseselection.ntust.edu.tw/AddAndSub/B01/B01")
time.sleep(2)

while True:
    try:
        add_button = driver.find_element(By.XPATH, "//span[contains(@class, 'addbtn') and text()='加選']")
        add_button.click()
        time.sleep(5)
        alert = Alert(driver)
        alert.accept() # click OK
    except Exception as e:
        print(f"Error: {str(e)}")
        break

    time.sleep(30)

driver.quit()
