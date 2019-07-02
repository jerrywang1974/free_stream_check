from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pickle
import time
import datetime
from random import randint
#browser = webdriver.Chrome()
browser = webdriver.Firefox()
browser.set_page_load_timeout(30)
browser.get('https://wmspanel.com/dispersa/free_stream_checker')
try: 
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
except Exception:
    pass
#assert “Online Shopping” in browser.title
search = browser.find_element_by_id("stream") # Find the search box by class
search.send_keys("https://broadcast-ettoday.cdn.hinet.net/ettoday-broadcast/smil:etmalltest.smil/playlist.m3u8 ") #send the value of search field
submit_button = browser.find_element_by_name("commit")
submit_button.click()
#Lets wait for lobby page to load
delay = 50 # seconds max wait
myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, "stream_status")))
el=browser.find_element_by_tag_name('body')
time.sleep(15)
now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
el.screenshot('screencapture'+now+'.png')
#browser.save_screenshot("loggedIn.png") ## This will be stored in the location/path mentioned or the current directory
#myElem.save_screenshot("loggedIn.png") ## This will be stored in the location/path mentioned or the current directory
try: 
    pickle.dump( browser.get_cookies() , open("cookies.pkl","wb"))
except Exception:
    pass
browser.close() # close browser
