
import re
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

items_btn_selector = '#recordContainerresults99161966433701452 > div.media-body > div.media-heading.flex > div > div > a:nth-child(4)'
page2_selector = '#PAGING_UL_down > li:nth-child(3) > a'
page3_selector = '#PAGING_UL_down > li:nth-child(3) > a'
list_selector = '#TABLE_DATA_list > tbody'
backbtn_selector = '#generic_back_button'
duedate_selector = '#pageBeandueDate'
num_id = 'pageBeandescription'
alma_url = 'https://na01.alma.exlibrisgroup.com/mng/login?institute=01ALLIANCE_UW&auth=SAML'
search_bar_selector = '#ALMA_MENU_TOP_NAV_Search_Text'
user_id = 'weblogin_netid'
user_pass = 'weblogin_password'
id_subtractor = 45

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(alma_url)
actions = ActionChains(driver)


def search_uwb_laptops():
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_bar_selector)))
    time.sleep(1)
    search_bar = driver.find_element_by_css_selector(search_bar_selector)
    search_bar.send_keys('uwb laptop')
    search_bar.send_keys(Keys.ENTER)


def click_items():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, items_btn_selector)))
    driver.find_element_by_css_selector(items_btn_selector).click()


def wait_to_load():
    time.sleep(2)


def convert_to_12hr(time_str):
    time_list = time_str.split(':')
    hour = int(time_list[0])
    if hour >= 12:
        hour = ((hour - 1) % 12) + 1
        return str(hour) + time_str[2:] + ' PM'
    return str(hour) + time_str + ' AM'


search_uwb_laptops()
click_items()
is_multi_page = True


try:
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, page3_selector)))
    id_subtractor = 5
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    driver.execute_script('document.querySelector("' + page3_selector + '").click()')
    time.sleep(1)
except:
    is_multi_page = False

print 

for i in range(25):
    if is_multi_page and i == 6:
        id_subtractor = 25
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, page2_selector)))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        driver.execute_script('document.querySelector("' + page2_selector + '").click()')
        time.sleep(1)

    infolink_id = 'INPUT_SELENIUM_ID_list_ROW_' + str(id_subtractor - i) + '_COL_processTypeForDisplay'
    
    try:
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, infolink_id)))
        driver.execute_script('document.getElementById("' + infolink_id + '").click()')
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, num_id)))
        laptop_num = driver.find_element_by_id(num_id).get_attribute('innerHTML').split('#')[1]

        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, duedate_selector)))
        duedate_info = driver.find_element_by_css_selector(duedate_selector).get_attribute('title').split(' ')


        date = duedate_info[0]
        time_due = convert_to_12hr(duedate_info[1])

        if(time_due == '11:59:00 PM'):
            time_due += ' <-- Change Due Date'
            
        print(str(i+1) + ": " + date + " | " + time_due)

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, backbtn_selector)))
        driver.find_element_by_css_selector(backbtn_selector).click()

    except TimeoutException:
        print(str(i+1) + ": IN")
    
    print


driver.close()
