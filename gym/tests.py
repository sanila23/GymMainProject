# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# class LoginTest(unittest.TestCase):
#     def setUp(self):
#         # Start the Selenium WebDriver
#         self.driver = webdriver.Chrome()  # Adjust based on your WebDriver configuration
#         self.driver.get('http://127.0.0.1:8000/member_login/')  # Replace with the actual URL of your login page

#     def test_login_successful(self):
#         # Find the username, password, and login button elements
#         email_input = self.driver.find_element(By.NAME, 'Email')  # Use By.NAME for the name attribute
#         password_input = self.driver.find_element(By.NAME, 'Password')
#         login_button = self.driver.find_element(By.XPATH, "//button[text()='Log in']")

#         # Enter valid credentials
#         email_input.send_keys("sanilasunny18@gmail.com")
#         password_input.send_keys("Sanila@12345")

#         # Click the login button
#         login_button.click()

#         # Wait for a while to see the result (you can adjust this based on your application's response time)
#         time.sleep(2)
#         self.assertEqual(self.driver.current_url, 'http://127.0.0.1:8000/home/')

#     def tearDown(self):
#         # Close the browser window
#         self.driver.quit()

# if __name__ == "__main__":
#     unittest.main()

# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

# # Set the path to your webdriver executable
# webdriver_path = webdriver.Chrome()

# # URL of your Django admin site
# admin_url = 'http://127.0.0.1:8000/admin/'

# # Open the browser
# driver = webdriver.Chrome()
# driver.get('http://127.0.0.1:8000/admin/login/?next=/admin/')

# # Assuming there is a login page, you may need to log in first
# # Fill in the username and password fields and submit the form
# # Example:
# username_input = driver.find_element(By.NAME, 'username')
# password_input = driver.find_element(By.NAME, 'password')
# username_input.send_keys('admin')
# password_input.send_keys('test')
# password_input.send_keys(Keys.RETURN)

# # Navigate to the "gym" app in the admin panel
# driver.get(admin_url)  # Replace 'app_name' with your actual app name

# # Register each model in the admin panel
# # models_to_register = ['Bill', 'Member', 'Trainer', 'Diet', 'Schedule', 'Store']

# # for model_name in models_to_register:
# #     model_link_text = f'Add {model_name}'
# #     add_model_link = driver.find_element(By.LINK_TEXT, model_link_text)
# #     add_model_link.click()

#     # You may want to add more code here to fill in any required fields and save the form

# # Close the browser
# driver.quit()

# if __name__ == "__main__":
#     unittest.main()

# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# # Replace 'path/to/chromedriver' with the actual path to your chromedriver executable
# driver = webdriver.Chrome()

# try:
#     # Open the web application
#     driver.get('http://127.0.0.1:8000/admin/gym/bill/add/')  # Replace with the actual URL of your Django app

#     # Example: Navigate to the 'Bills' page
#     bills_link = driver.find_element_by_link_text('Bills')  # Replace with the actual link text on your page
#     bills_link.click()

#     # Example: Create a new bill
#     create_bill_button = driver.find_element_by_id('create-bill')  # Replace with the actual ID of your create bill button
#     create_bill_button.click()

#     # Fill in the form with bill details
#     due_date_input = driver.find_element_by_name('Due_date')
#     due_date_input.send_keys('2023-12-31')  # Replace with the desired due date

#     customer_id_input = driver.find_element_by_name('Customer_id')
#     customer_id_input.send_keys('123456')  # Replace with the desired customer ID

#     # ... Continue filling in other form fields

#     # Submit the form
#     submit_button = driver.find_element_by_id('submit-bill')  # Replace with the actual ID of your submit button
#     submit_button.click()

#     # Wait for a while to see the result (you can adjust this based on your application's response time)
#     time.sleep(2)

    
#     # ... Continue navigating and interacting with other pages as needed

# finally:
#     # Close the browser window
#     driver.quit()

#     if __name__ == "__main__":
#      unittest.main()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your webdriver (e.g., chromedriver.exe for Chrome)
webdriver_path = webdriver.Chrome()

# Initialize the Chrome webdriver
driver = webdriver.Chrome()
driver.get('http://127.0.0.1:8000/member_login/')  
email_input = driver.find_element(By.NAME, 'Email')  # Use By.NAME for the name attribute
password_input = driver.find_element(By.NAME, 'Password')
login_button = driver.find_element(By.XPATH, "//button[text()='Log in']")
email_input.send_keys("sanilasunny18@gmail.com")
password_input.send_keys("Sanila@12345")
login_button.click()


# Replace 'your_url_here' with the actual URL of your webpage
url = 'http://127.0.0.1:8000/view_store/'
driver.get(url)
try:
    # Wait for the element with id 'btn1' to be clickable
    btn1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'btn1'))
    )

    # Click the 'btn1' button
    btn1.click()

    # Wait for a while (you might need to adjust the sleep time)
    driver.implicitly_wait(5)

    # Trigger the print action (assuming the print function is available in your browser)
    driver.execute_script('window.print();')

finally:
    # Close the webdriver
    driver.quit()
