from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
import yagmail
import time
import sys
from threading import Thread
#########################################################

url = 'https://www.amazonuniversity.jobs/dashboard'
target = '1'

def target_locations(target):
    num_target = int(target)
    locs = {}
    for i in range(num_target):
        name = input('Name of Target ' + str(i+1) + ': ')
        xpath = input('Location of target(xpath): ')
        locs[name] = xpath
    return locs

def animation(loading_animation="|\-/"):
    i = 0
    while True:
        sys.stdout.write("\r"  + loading_animation[i % len(loading_animation)])
        time.sleep(.5)
        sys.stdout.flush()
        i+=1

def email(name, url):
    yag = yagmail.SMTP(user_email)
    yag.send(
                    to={recipient_email:recipient_name},
                    subject=name + ' Updated',
                    contents=url
                    )

def search(items, url, driver=webdriver.Safari()):
    complete = False
    username_str = input('Portal Username: ')
    password_str = input('User Password: ')
    load_anim = Thread(target=animation)
    load_anim.start()
    driver.get(url)
    time.sleep(3)
    username = driver.find_element_by_xpath('//*[@id="j_id0:j_id10:username"]')
    driver.implicitly_wait(2)
    password = driver.find_element_by_xpath('//*[@id="j_id0:j_id10:password"]')
    driver.implicitly_wait(2)
    button = driver.find_element_by_xpath('//*[@id="j_id0:j_id10:loginButton"]')
    driver.implicitly_wait(2)
    username.send_keys(username_str)
    driver.implicitly_wait(3)
    password.send_keys(password_str)
    driver.implicitly_wait(3)
    button.send_keys(Keys.RETURN)
    driver.implicitly_wait(3)

    time.sleep(3)
    # driver.minimize_window()
    xpath_search = lambda xpath: driver.find_element_by_xpath(xpath)
    prev = {key: xpath_search(val) for key, val in items.items()}
    items_updated = prev
    while not complete:
        # for name in items_updated.keys():
        #     print(items_updated[name].get_attribute('text'), prev[name].get_attribute('text'))
        #     if items_updated[name] != prev[name]:
        #         email(name, url)
        #         complete = True
        #     else:
        #         driver.refresh()
        #         driver.implicitly_wait(5)
        #         time.sleep(2)
        #         prev[name] = xpath_search(items[name])
        time.sleep(2)
        driver.refresh()
    quit()




