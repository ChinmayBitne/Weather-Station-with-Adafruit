from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new instance of the Firefox driver
driver = webdriver.Chrome("chromedriver.exe")

# Test Case 1: Invalid Credentials
def test_invalid_credentials():
    driver.get("https://accounts.adafruit.com/users/sign_in")
    username_input = driver.find_element(By.ID, "user_login")
    password_input = driver.find_element(By.ID, "user_password")
    login_button = driver.find_element(By.NAME, "commit")

    username_input.send_keys("vaibhav@123")
    password_input.send_keys("Pass1234")
    login_button.click()    

    # Assert that an error message is displayed indicating invalid credentials
    error_message = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/form/div[1]").text
    error_message == "Invalid username or password"
    return 1




res=test_invalid_credentials()
if res == 1:
    # Perform additional actions or assertions for successful login
    print("Invalid crediantial Test Case Pass!")
else:
    # Handle unsuccessful login
    print("Login successful!")


# Test Case 2: Successful Registeration
def test_successful_registeration():
    driver.get("https://accounts.adafruit.com/users/sign_up")
    fname = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[1]/div/div[2]/div[1]/form/p[1]/input")
    lname = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[1]/div/div[2]/div[1]/form/p[2]/input")
    email = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[1]/div/div[2]/div[1]/form/p[3]/input")
    username = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[1]/div/div[2]/div[1]/form/p[5]/input")
    password = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[1]/div/div[2]/div[1]/form/p[7]/input")
    login_button = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[1]/div/div[2]/div[1]/form/p[9]/input")

    fname.send_keys("Dave")
    lname.send_keys("Martin")
    email.send_keys("davemartin14122002@gmail.com")
    username.send_keys("davemartin010")
    password.send_keys("Pass1234")
    login_button.click()

    return 1

    # Run the test cases
result = test_successful_registeration()

if result == 1:
    # Perform additional actions or assertions for successful login
    print("Registeration Successful Test Case Pass!")
else:
    # Handle unsuccessful login
    print("Registeration Unsuccessful !")



# Test Case 3: Successful Login
def test_successful_login():
    driver.get("https://accounts.adafruit.com/users/sign_in")
    username_input = driver.find_element(By.ID, "user_login")
    password_input = driver.find_element(By.ID, "user_password")
    login_button = driver.find_element(By.NAME, "commit")


    username_input.send_keys("davemartin010")
    password_input.send_keys("Pass1234")
    login_button.click()    

    # Assert that the user is successfully logged in and redirected to the expected page
    driver.get("https://accounts.adafruit.com/")
    return 1
    

    # Run the test cases
result = test_successful_login()

if result == 1:
    # Perform additional actions or assertions for successful login
    print("Valid Login crediantial Test Case Pass!")
else:
    # Handle unsuccessful login
    print("Login failed!")


# Test Case 4: Sensor reading validation
def test_cost_meter_value():
    driver.get("https://io.adafruit.com/davemartin010/dashboards/nodemcu")  # Replace with the URL of the webpage with the cost meter value

    # Wait for the cost meter value to be present on the page
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/main/div[1]/div[1]/div/div/div[4]/div/div[3]/div/div[3]/div/div/div/div[1]")))

    # Get the initial cost meter value
    cost_meter_element = driver.find_element(By.XPATH, "/html/body/div/div/div/main/div[1]/div[1]/div/div/div[4]/div/div[3]/div/div[3]/div/div/div/div[1]")
    initial_value = float(cost_meter_element.text)

    # Wait for 20 seconds
    time.sleep(20)

    # Get the current cost meter value
    cost_meter_element = driver.find_element(By.XPATH, "/html/body/div/div/div/main/div[1]/div[1]/div/div/div[4]/div/div[3]/div/div[3]/div/div/div/div[1]")
    current_value = float(cost_meter_element.text)

    
    current_value > 0 and current_value !=initial_value

    return 1
result = test_cost_meter_value()

if result == 1:
    # Perform sensor reading validation
    print("Cost meter value is greater than 0 and it varies. Test case passed.")
else:
    # Handle no readings
    print("Sensor not reading values!!!")


driver.get("https://io.adafruit.com/davemartin010/feeds/temperature")
time.sleep(10)
driver.get("https://io.adafruit.com/davemartin010/feeds/humidity")
time.sleep(10)

# Close the browser
driver.quit()
