from selenium import webdriver
from time import sleep

USERNAME = "Name"
PASSWORD = "Password"

WEB_DRIVER_PATH = 'C:\Develop\chromedriver.exe'
TWITTER_PAGE_LINK = "https://twitter.com/login"
SPEED_TEST_LINK = "https://www.speedtest.net/"



class Twitter_bot:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)
        self.down = 0
        self.up = 0
        self.speed_complain=0

    def internet_speed(self):
        self.driver.get(SPEED_TEST_LINK)
        sleep(3)
        speed = self.driver.find_element_by_class_name("js-start-test")
        speed.click()
        sleep(40)
        speed_result = self.driver.find_element_by_class_name("overall-progress")
        speed_text = speed_result.text
        print(speed_text)
        speed_text_split = (speed_text.split(" "))
        download = float(speed_text_split[9].strip(","))
        upload = float(speed_text_split[14].strip(","))
        print(f"down:{download}")
        print(f"up: {upload}")
        self.speed_complain =f"internet speed is quite slower than what was promised, here is the down{download} up{upload}...still happy though!!"

    def login(self):
        sleep(3)
        self.driver.get(TWITTER_PAGE_LINK)
        sleep(5)
        login_name = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        login_name.send_keys(USERNAME)
        login_password = self.driver.find_element_by_css_selector("input.r-1niwhzg[type='password']")
        login_password.send_keys(PASSWORD)
        sign_in = self.driver.find_element_by_css_selector("div.r-lrvibr[data-testid='LoginForm_Login_Button']")
        sign_in.click()


    def tweet(self):
        tweet = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet.click()
        sleep(2)
        write_tweet = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        write_tweet.send_keys(self.speed_complain)
        send_tweet = self.driver.find_element_by_css_selector('div.css-18t94o4[data-testid="tweetButton"]')
        send_tweet.click()


bot = Twitter_bot(WEB_DRIVER_PATH)
bot.internet_speed()
bot.login()
bot.tweet()






















# def apply_for_jobs(self):
#     pass
#
# def apply_for_all(self):
#     pass
# bot.apply_for_jobs()
# bot.apply_for_all()
