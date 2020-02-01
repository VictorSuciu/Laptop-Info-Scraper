
import re
import time
from datetime import datetime
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
physical_selector = '#record_2_results > div > div.tabsContainer > div.tabsContainerNotExpanded > div:nth-child(1) > div > div > ul > li.tab.hasContentInd.hasContent.jsToolTip.closeOnClick.scrollInit'
items_in_physical_selector = '#ADD_HIDERADIO_results_1_inventoryLookAheadphysicalUiHoldingResults_csearchbib_resultsnav_pane_physical_upper_actions_items > div > input'
user_id = 'weblogin_netid'
user_pass = 'weblogin_password'
left_pad = '   '
id_subtractor = 45

driver = webdriver.Chrome(executable_path='driver/chromedriver')
driver.get(alma_url)
actions = ActionChains(driver)

# FOR TESTING - DELETE WHEN DONE
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, user_id)))
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, user_pass)))
driver.find_element_by_id(user_id).send_keys('vsuciu')
driver.find_element_by_id(user_pass).send_keys('Publ1cClassWash1ngt0n')
driver.find_element_by_id(user_pass).send_keys(Keys.ENTER)
#-------------------------------

def search_uwb_laptops():
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_bar_selector)))
    time.sleep(1)
    search_bar = driver.find_element_by_css_selector(search_bar_selector)
    search_bar.send_keys('uwb laptop')
    search_bar.send_keys(Keys.ENTER)


def click_items():
    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, items_btn_selector)))
        driver.find_element_by_css_selector(items_btn_selector).click()
    except:

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, physical_selector)))
        driver.find_element_by_css_selector(physical_selector).click()
        #driver.execute_script('document.querySelector("' + physical_selector + '").click()')
        
        time.sleep(1)

        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, items_in_physical_selector)))
        #driver.find_element_by_css_selector(items_in_physical_selector).click()
        driver.execute_script('document.querySelector("' + items_in_physical_selector + '").click()')
        time.sleep(2)


def wait_to_load():
    time.sleep(2)


def convert_to_12hr(time_str):
    time_list = time_str.split(':')
    hour = int(time_list[0])
    am_or_pm = ' AM'
    if hour >= 12:
        hour = ((hour - 1) % 12) + 1
        am_or_pm = ' PM'
    if hour < 10:
        am_or_pm = " " + am_or_pm

    return str(hour) + time_str[2:-3] + am_or_pm

def format_date(date):
    month = str(date.month)
    day = str(date.day)
    if date.month < 10:
        day += " "
    if date.day < 10:
        day += " "
    return month + '-' + day

def is_due_today(due_date):
    today = datetime.today()
    return due_date.month == today.month and due_date.day == today.day

def is_late(due_date):
    today = datetime.today()
    if (today.year > due_date.year) or \
       (today.year == due_date.year and today.month > due_date.month) or \
       (today.year == due_date.year and today.month == due_date.month and today.day > due_date.day):
        return True
    return False

def click_next_page():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, page2_selector)))
    time.sleep(2)
    driver.execute_script('document.querySelector("' + page2_selector + '").click()')
    time.sleep(3)


output_stack = []
late_laptops = []
due_today_laptops = []
#24: 2-3   | 10:00 PM
#====================
def print_stack(stack):
    for i in range(len(stack)):
        print(stack.pop())

def print_notifications():
    late_laptops.sort()
    due_today_laptops.sort()
    print('=======================')
    print('\n' + left_pad + 'Late Laptops:')
    [print(left_pad + '# ' + str(num)) for num in late_laptops]
    print('\n' + left_pad + 'Laptops Due Today:')
    [print(left_pad + '# ' + str(num)) for num in due_today_laptops]
    print('\n=======================\n')

print('\n')

search_uwb_laptops()
click_items()
is_multi_page = True


try:
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, page3_selector)))
    id_subtractor = 5
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    driver.execute_script('document.querySelector("' + page3_selector + '").click()')
    time.sleep(3)
except:
    is_multi_page = False


count = -1
already_next_page = False

while(True):

    count += 1

    infolink_id = 'INPUT_SELENIUM_ID_list_ROW_' + str(count) + '_COL_processTypeForDisplay'
    barcode_id = 'INPUT_SELENIUM_ID_list_ROW_' + str(count) + '_COL_barcode'
    table_num_id = 'SPAN_SELENIUM_ID_list_ROW_' + str(count) + '_COL_description'

    
    try:
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, table_num_id)))
        laptop_num = driver.find_element_by_id(table_num_id).get_attribute('innerHTML').split('#')
        if len(laptop_num) != 2:
            continue
            
        laptop_num = int(laptop_num[1])
        laptop_num_str = str(laptop_num)
        if laptop_num < 10:
            laptop_num_str = ' ' + laptop_num_str

    except:
        print_stack(output_stack)
        if is_multi_page and not already_next_page:
            click_next_page()
            count = 0
            already_next_page = True
            continue
        else:
            break

    try:
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, infolink_id)))
        driver.execute_script('document.getElementById("' + infolink_id + '").click()')

        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, num_id)))

        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, duedate_selector)))
        duedate_info = driver.find_element_by_css_selector(duedate_selector).get_attribute('title').split(' ')

        due_date = datetime.strptime(duedate_info[0], '%m/%d/%Y')
        date = format_date(due_date)
        time_due = convert_to_12hr(duedate_info[1])

        if is_late(due_date):
            late_laptops.append(laptop_num)
        elif is_due_today(due_date):
            due_today_laptops.append(laptop_num)
        
        output_stack.append(left_pad + laptop_num_str + ': ' + date + ' | ' + time_due + '\n')

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, backbtn_selector)))
        driver.find_element_by_css_selector(backbtn_selector).click()

    except:
        output_stack.append(left_pad + laptop_num_str + ': IN\n')

print_notifications()

driver.close()


