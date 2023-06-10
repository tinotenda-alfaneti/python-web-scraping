from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Login:

    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password

    def signin(self):
        
        # opening the web page to manipulate
        self.driver.get("https://www.instagram.com/accounts/login/")

        # make the web page wait for the specified element
        uid = WebDriverWait(self.driver, 300).until(EC.presence_of_element_located((By.NAME, "username")))
        # click the element to make it active for writing
        uid.click()
        # paste the user name
        uid.send_keys(self.username)

        # locate the password entry field
        pswd = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input")
        # click to activate the field
        pswd.click()
        # paste the password
        pswd.send_keys(self.password)

        # locate and click the login button
        btn = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3)")
        btn.click()

