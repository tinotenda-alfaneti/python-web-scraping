from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


from get_pages import Getpages
from login import Login

username = "USERNAME"
password = "PASSWORD"
driver = 0


def main():
    global driver
    print("Running script...")

    # create service to stop and start the chromedriver
    service = ChromeService(executable_path="C:\\Users\\Admin\\Desktop\\projects\\chromedriver_win32\\chromedriver.exe")

    # create an instance of chrome driver
    driver = webdriver.Chrome(service=service)

    # script to login to an account
    user_login = Login(driver, username, password)
    user_login.signin()

    # navigating through the pages
    pages = Getpages(driver)
    pages.get_followers()



if __name__ == '__main__':
    main()
