
import os
import sys
import unittest
from time import sleep
from selenium import webdriver
from datetime import datetime
import HtmlTestRunner
from selenium.webdriver.common.by import By

class AdafruitIOTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('chromedriver.exe')  # Provide the path to the ChromeDriver executable
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)  # Set an implicit wait time of 5 seconds

    # Cheaking Invalid Credentials 
    def test_01_invalid_credentials(self):
        driver = self.driver
        driver.get("https://accounts.adafruit.com/users/sign_in")
        username_input = driver.find_element(By.ID, "user_login")
        password_input = driver.find_element(By.ID, "user_password")
        login_button = driver.find_element(By.NAME, "commit")

        username_input.send_keys("hggdjhgfuy")
        password_input.send_keys("tuftdu1")
        login_button.click()

        # Assert that an error message is displayed indicating invalid credentials
        error_message = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/form/div[1]").text
        self.assertEqual(error_message, "×\nInvalid Login or password.")
#=========================================================================================================================================================
   
   # Cheaking Valid Credentials and login Successfully
    def test_02_login(self):
        driver = self.driver
        driver.get('https://io.adafruit.com/')
    
        driver.get("https://accounts.adafruit.com/users/sign_in")
        # Find login elements
        username_input = driver.find_element(By.ID, "user_login")
        password_input = driver.find_element(By.ID, "user_password")
        login_button = driver.find_element(By.NAME, "commit")

        # Enter login credentials
        username_input.send_keys("davemartin010")
        password_input.send_keys("Pass1234")
        login_button.click()

        # Assert login successful
        dashboard_title = driver.find_element(By.TAG_NAME, 'h1')
        # assert dashboard_title is not None
        self.assertIsNotNone(dashboard_title)
#=========================================================================================================================================================
    
    # After login view system Dashboard
    def test_03_view_dashboard(self):
        driver = self.driver
        
        # Navigate to the Dashboard page
        driver.get('https://io.adafruit.com/davemartin010/dashboard')
        
        # Assert dashboard loaded successfully
        dashboard_title = driver.find_element(By.TAG_NAME, 'h2')
        self.assertIsNotNone(dashboard_title)
#=========================================================================================================================================================
    
    # Create feed on system
    def test_04_create_feed(self):
        driver = self.driver
        
        # Navigate to Feeds page
        driver.get('https://io.adafruit.com/davemartin010/feeds')
        
        # Find create feed button
        create_feed_button = driver.find_element(By.XPATH, '//*[@id="content-wrapper"]/div/div[1]/div[1]/button[1]')
        create_feed_button.click()

        # Find feed name and key input fields
        feed_name_input = driver.find_element(By.NAME, 'name')
        
        # Enter feed name and key
        feed_name_input.send_keys('Test Feed')
        
        # Submit the form
        submit_button = driver.find_element(By.XPATH, '//*[@id="create-feed-modal"]/div/div/div[3]/button[1]')
        submit_button.click()
        
        # Assert feed creation successful
        success_message = driver.find_element(By.XPATH, "//*[text()='Test Feed']")
        self.assertIsNotNone(success_message)
#=========================================================================================================================================================
    
    # Cheaking data is send Successfully or not
    def test_05_send_data(self):
            driver = self.driver
            
            # Navigate to the Test Feed page
            driver.get('https://io.adafruit.com/davemartin010/feeds/test-feed')
            

            # Send multiple data points
            for i in range(30,35):
                # Find the data value input field
                field = driver.find_element(By.XPATH, '//*[@id="content-wrapper"]/div[2]/div/div[2]/div[1]/a[1]')
                field.click()
                value_input = driver.find_element(By.NAME, 'value')
                value_input.clear()
                value_input.send_keys(str(i))
                # value_input.send_keys(Keys.RETURN)
                submit_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[3]/button[1]')
                submit_button.click()

            # Assert data sent successfully
            data_points = driver.find_element(By.XPATH, '//*[@id="content-wrapper"]/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[2]').text
            self.assertEqual(data_points, '34')
#=========================================================================================================================================================
    
    # Downloading data report
    def test_06_download_report(self):
            driver = self.driver
            driver.get('https://io.adafruit.com/davemartin010/feeds/test-feed')

            download_data = driver.find_element(By.XPATH, '//*[@id="content-wrapper"]/div[2]/div/div[2]/div[1]/a[2]')
            download_data.click()
        
            # select_csv= driver.find_element(By.XPATH, '//*[@id="aio-key-modal"]/div/div/div[2]/p[2]/button[2]')
            # select_csv.click()
            
            report= driver.find_element(By.XPATH, '//*[@id="aio-key-modal"]/div/div/div[2]/div/table/tbody/tr[1]/td[1]/a')
            report.click()

            # Wait for the export file to be downloaded
            sleep(5)

            # Verify the presence of the downloaded file
            download_dir = 'C:/Users/Vaibhav/Downloads'  # Specify the path to the download directory

            # Generate the expected file name based on the current date
            current_date = datetime.now().strftime('%Y%m%d')
            expected_file = os.path.join(download_dir, f'Test_Feed-{current_date}-1407.csv')

            assert os.path.exists(expected_file)  # Verify that the file exists

#=========================================================================================================================================================
    # Logout successfully
    def test_07_logout(self):
        driver = self.driver
        
        # Navigate to Dashboard page
        driver.get('https://io.adafruit.com/davemartin010/dashboards')
        
        # Find signout option in nav bar button
        nav = driver.find_element(By.XPATH, '//*[@id="account"]/div[1]/button')
        nav.click()

        # Find singout and click
        signout = driver.find_element(By.XPATH, '//*[@id="account"]/div[1]/div/ul/li[3]/a')
        signout.click()
        
        # Assert logout successful
        success_message = driver.find_element(By.XPATH, '//*[@id="new_user"]/div[1]').text
        # self.assertIsNotNone(success_message)
        self.assertEqual(success_message, "×\nSigned out successfully.")
#=========================================================================================================================================================
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

#=========================================================================================================================================================
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('chromedriver.exe')  # Provide the path to the ChromeDriver executable
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5) 
    
    # Testing data transmission between device and system
    def test_08_test_data_transmission(self):
            # Open the Adafruit Cloud login page
            self.driver.get("http://localhost/esp8266/page.php")

            # Wait for the dashboard page to load
            self.driver.implicitly_wait(10)

            # Find the temperature and humidity elements
            temperature_element = self.driver.find_element(By.XPATH, "/html/body/p[1]/span[2]")
            humidity_element = self.driver.find_element(By.XPATH, "/html/body/p[2]/span[2]")

            # Get the temperature and humidity values from the elements
            temperature = float(temperature_element.text.strip("°C"))
            humidity = float(humidity_element.text.strip("%"))

            # Define the acceptable range for temperature and humidity1
            temperature_range = (25, 50)  # Acceptable temperature range: 25°C to 50°C
            humidity_range = (5, 70)     # Acceptable humidity range: 30% to 70%

            # Perform range checks to verify if the received data is within the acceptable range
            self.assertGreaterEqual(temperature, temperature_range[0], f"Temperature is below the acceptable range. Expected minimum: {temperature_range[0]}, Actual: {temperature}")
            self.assertLessEqual(temperature, temperature_range[1], f"Temperature is above the acceptable range. Expected maximum: {temperature_range[1]}, Actual: {temperature}")
            self.assertGreaterEqual(humidity, humidity_range[0], f"Humidity is below the acceptable range. Expected minimum: {humidity_range[0]}, Actual: {humidity}")
            self.assertLessEqual(humidity, humidity_range[1], f"Humidity is above the acceptable range. Expected maximum: {humidity_range[1]}, Actual: {humidity}")

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()


if __name__ == '__main__':
    # Generate an HTML test report
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))



