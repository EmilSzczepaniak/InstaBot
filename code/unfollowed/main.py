from selenium import webdriver
from time import sleep
from secrets import pw
from keyboard import press

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username;
        tag = "#travel"
        self.driver.get("https://instagram.com")
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/button[1]").\
            click()
        sleep(2)
        login_field = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")\
            .send_keys(username)
        sleep(2)
        password_field = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")\
            .send_keys(pw)
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")\
            .click()
        
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/section/div/button")\
        .click()

        sleep(2)    
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")\
        .click()

        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]")\
        .click()

        sleep(4)    
        self.driver.find_element_by_xpath("//html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")\
        .send_keys(tag)

        press('enter')


        sleep(40)




        # def get_unfollowers(self):


InstaBot('emilowy', pw)


