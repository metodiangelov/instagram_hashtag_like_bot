from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:
    def __init__(self, username , password):#constructor
        self.username = "username"                                                        #Change username and pw to ur ig username and pw.
        self.password = "password"                                                        #DONT FORGET TO CHANGE THAT
        self.driver = webdriver.Firefox(executable_path=r"D:\Python\...\...\geckodriver.exe") #PATH to ur geckodriver.exe


    def login(self):
        driver = self.driver #managing the geckodriver to a local variable
        driver.get('https://www.instagram.com')#define the link
        time.sleep(1)#wait the page to load
        driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click() #aOOlW   HoLwm разрешавам основните бисквити
        time.sleep(1)
        user_element = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')#login input path
        user_element.clear()#clear login
        user_element.send_keys(self.username)#write the user
        password_element = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')#password input path
        password_element.clear()#clear password
        password_element.send_keys(self.password)#write the password
        password_element.send_keys(Keys.RETURN)#press the ENTER key
        time.sleep(5)#wait the page to load
        if driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').is_displayed():
            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click() #не сега butona
            time.sleep(3)
        # driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click #не сега butona   
        else:
            pass
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click() #не сега butona
        self.like_posts('underwater') #избери хаштаг


    def like_posts(self,hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')#search the link of the hashtag
        time.sleep(3)#wait the page to load

        for i in range(2):#scroll the page to the bottom X times to load more posts        КОЛКО ПЪТИ ДА СКРОЛВА
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(2)
        hrefs = driver.find_elements_by_tag_name('a')#catch every post
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [elem.get_attribute('href') for elem in hrefs]
        print(hashtag + 'fotos: ' + str(len(pic_hrefs)))#show how much posts have been saved
        obshto=1
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')#scroll to the bottom of the page
            try:                
                time.sleep(1)
                now = time.strftime("%H:%M:%S") #save the time
                if driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').is_displayed():
                    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click() #не сега butona
                    time.sleep(5)
                    driver.find_element_by_class_name("fr66n").click() #click the like button инспектира се в html-а на сайта.
                    print(f'count:{obshto} {pic_href} liked! at ' + now) #show the confirmation and the time "wpO6b  " fr66n
                    obshto+=1
                    time.sleep(19) #wait to restart the cycle
                else:
                    pass
                driver.find_element_by_class_name("fr66n").click() #click the like button инспектира се в html-а на сайта.
                print(f'count:{obshto} {pic_href} liked! at ' + now) #show the confirmation and the time "wpO6b  " fr66n
                obshto+=1
                time.sleep(19) #wait to restart the cycle                
            except Exception as e:
                driver.find_element_by_class_name("fr66n").click() #click the like button инспектира се в html-а на сайта.
                print(f'count:{obshto} {pic_href} liked! at ' + now) #show the confirmation and the time "wpO6b  " fr66n
                obshto+=1     
                print(f'error! Exception at '+ now)#show the fail and the time 
                # da natisne ne iskam izvestiq   
                time.sleep(19)#wait to retry
        

LucasBot = InstagramBot('@yourUser','@yourPassword')#define the bot and it's parameters 
LucasBot.login()#excute the bot
