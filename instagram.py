# imports
from time import sleep

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys

# constants
CHROME_DRIVER_PATH = ""  # your chrome driver path
USERNAME = ""  # your username
PASSWORD = ""  # your password
URL = "https://www.instagram.com/"
URL2 = ""  # account url


# class block
class InstaFollower:
    """
    This class represents instafollower bot
    """

    def __init__(self):
        """
        Initializes webdriver(selenium)
        """
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        """
        Login into your instagram account
        :return: nothing
        """

        # open url
        self.driver.get(URL)
        sleep(3)

        # send email and password
        self.driver.find_element_by_xpath(
            "//*[@id=\"loginForm\"]/div/div[1]/div/label/input"
        ).send_keys(USERNAME)
        sleep(3)

        self.driver.find_element_by_xpath(
            "//*[@id=\"loginForm\"]/div/div[2]/div/label/input"
        ).send_keys(PASSWORD)
        sleep(3)

        # press the button
        self.driver.find_element_by_xpath(
            "//*[@id=\"loginForm\"]/div/div[3]/button/div"
        ).click()
        sleep(3)

        self.driver.find_element_by_xpath(
            "//*[@id=\"react-root\"]/section/main/div/div/div/div/button"
        ).click()
        sleep(3)

    def find_followers(self):
        """
        Finds the account that you want and opens the pop-up window with followers
        :return: nothing
        """
        # open wished account
        self.driver.get(URL2)
        sleep(3)

        # open the pop-up window with followers
        self.driver.find_element_by_xpath(
            "//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a"
        ).click()
        sleep(3)

    def follow(self):
        """
        Follows the profiles till the end
        :return: nothing
        """
        while True:
            # find all follow buttons
            follow_buttons = self.driver.find_elements_by_css_selector(".PZuss button")
            print(follow_buttons)

            # click on each one
            for button in follow_buttons:
                try:
                    button.click()
                    sleep(1)
                except exceptions.ElementClickInterceptedException:
                    self.driver.find_element_by_xpath(
                        "/html/body/div[7]/div/div/div/div[3]/button[2]"
                    ).click()
                    sleep(1)
                except exceptions.StaleElementReferenceException:
                    continue

            # scroll down
            self.driver.find_element_by_xpath(
                "/html/body/div[6]/div/div/div[2]//a"
            ).send_keys(Keys.END)
            sleep(3)
