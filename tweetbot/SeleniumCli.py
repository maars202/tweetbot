from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

class SeleniumClient(object):
    """SeleniumClient initiated with path to chrome driver downloaded from 
        https://chromedriver.chromium.org/downloads
        e.g. of initiating: 
        sel_obj = SeleniumClient("/path/to/chromedriver")"""
    def __init__(self, path, sleep_time = 2):
        self.sleep_time = sleep_time
        # #Initialization method. 
        # self.chrome_options = webdriver.ChromeOptions()
        # self.chrome_options.add_argument('--headless')
        # self.chrome_options.add_argument('--no-sandbox')
        # self.chrome_options.add_argument('--disable-setuid-sandbox')

        # # you need to provide the path of chromdriver in your system
        # self.browser = webdriver.Chrome('D:/chromedriver_win32/chromedriver', options=self.chrome_options)

        # self.base_url = 'https://twitter.com/search?q='

        url = "https://www.twitter.com/login"
        # path = "/Users/maarunipandithurai/Desktop/maars202/selen_pro/chromedriver" # do remember to edit the path if it's in a different place
        self.driver = webdriver.Chrome(path)
        self.driver.get(url) # a new browser window should pop up

    def _get_data_page(self):
        timeline = self.driver.find_elements_by_xpath('//div[@aria-label="Timeline: Search timeline"]/div/div')
        print(len(timeline))
        data = []
        for el in timeline:
            current_data = el.get_attribute("innerText")
            current_time = el.find_element_by_xpath("//time").get_attribute("datetime")
            d = {
                "data": current_data,
                "time": current_time
            }
            data.append(d)
        return data

    def _get_posts(self, number_of_posts, SCROLL_PAUSE_TIME = 6):
        
        posts = []
        last_height = 2
        # driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)


            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            # all_ = driver.find_elements_by_xpath('//div[@lang="en"]')
            # datetimes = driver.find_elements_by_xpath('//time')
            # all_posts |=  set(all_)
            # all_times |= set(datetimes)
            data = self._get_data_page()
            print(len(data))
            for item in data:
                # print(item)
                if item not in posts:
                    posts.append(item)


            print( len(data), len(posts))
            # latest_time_str = posts[-1]["time"]
            # latest_time = datetime.strptime(latest_time_str, dtformat)
            # if latest_time < before_10:
            #     break

            if len(data) == 0:
                break
            if len(posts) > number_of_posts:
                break
            last_height = new_height
        return posts


    def search_query(self, query, number_of_posts = 50):
        """params: 
                query: information to search on twitter, 
                number_of_posts to retrieve is 50 by default
                
            Please ensure the chrome driver window and the script are running in the same window to
            ensure the search_query does not run infinitely.
            
            Might need to repeat the searches and increase sleep_time when initiating client"""
        print(self.driver.current_url)
        explore = self.driver.find_element_by_xpath('//a[@href="/explore"]')
        explore.click()
        print(self.driver.current_url)
        search_engine = self.driver.find_element_by_xpath('//input[@aria-label="Search query"]')
        # query = "tesla"
        # search_engine.clear()
        # search_engine.send_keys(Keys.CONTROL + "k")
        search_engine.send_keys(query)
        search_engine.send_keys(Keys.ENTER)
        print(self.driver.current_url)
        posts = self._get_posts(number_of_posts)
        posts_df = pd.DataFrame(posts)
        posts_df['time']= pd.to_datetime(posts_df['time'])
        return posts_df
        

        
    def login(self, username, password):
        time.sleep(self.sleep_time)

        usernameInput = self.driver.find_element_by_xpath('//input')
        usernameInput.send_keys(username)
        usernameInput.send_keys(Keys.ENTER)

        time.sleep(self.sleep_time)
        passwordInput = self.driver.find_element_by_xpath('//input')
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.ENTER)
        return self.driver

    def keep_searching(self, query, number_of_posts = 50):

            
        df = None
        counter = 0
        # print("number_of_posts: {number_of_posts}")
        while True:
            try:
                df = self.search_query(query, number_of_posts)
                # print(f"Successful executed!!!!: {df}")
                break
            except Exception as e:
                print("Oops!", e.__class__, "occurred.")
                print("error.. trying again")
                pass
            counter += 1
            time.sleep(2)
            if counter > 10:
                break

        return df

