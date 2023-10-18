from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel3XL'
desired_caps['app'] = 'C:/Users/Radek/Downloads/orange3-29.apk'
desired_caps['appPackage'] = 'com.orange.pl.orangetvgo'
desired_caps['appActivity'] = 'pl.orange.ypt.gui.activity.ActivitySplash'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

action = TouchAction(driver)

time.sleep(5)

dismiss = wait.until(lambda x: x.find_element(By.ID, "com.orange.pl.orangetvgo:id/menu_login"))
dismiss.click()

time.sleep(1)

agreement = wait.until(lambda x: x.find_element(By.ID, "com.orange.pl.orangetvgo:id/welcome_analytics_checkbox"))
agreement.click()

lets_start = wait.until(lambda x: x.find_element(By.ID, "com.orange.pl.orangetvgo:id/welcome_btn_start"))
lets_start.click()

###############################################################
######################!!!!!!BANER!!!!!!########################
###############################################################


deviceSize = driver.get_window_size()
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']

######Right to Left#######
startx = screenWidth * 8 / 9
endx = screenWidth / 9
starty = 670
endy = 670

titles = []
multiplier = 0
while True:
    banner = wait.until(lambda x: x.find_element(By.ID, "com.orange.pl.orangetvgo:id/banner_small"))
    banner.click()
    title_obj = wait.until(lambda x: x.find_element(By.ID, "com.orange.pl.orangetvgo:id/text_expanded"))
    if title_obj.text not in titles:
        titles.append(title_obj.text)
        multiplier += 1
        # go back to home screen
        driver.press_keycode(4)
        for i in range(multiplier):
            time.sleep(2)
            action.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
    else:
        break

print(titles)

ele_by_Xpath = wait.until(lambda x: x.find_element(
    By.XPATH,
    '/hierarchy/android.widget.FrameLayout/android.widget.'
    'LinearLayout/android.widget.FrameLayout/android.widget.'
    'FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
    '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
    '/android.widget.LinearLayout/android.widget.ScrollView/android.widget.FrameLayout'
    '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
    '/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView'
    '/android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView'
    '/androidx.appcompat.widget.LinearLayoutCompat[4]/android.widget.ImageView'))

ele_by_Xpath.click()

scroll_down_to_cast = wait.until(lambda x: x.find_element(
    By.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector()).scrollIntoView(text("Obsada"))'))

######Right to Left#######
startx = screenWidth * 1 / 8
endx = 10
starty = screenHeight * 5 / 6
endy = screenHeight * 5 / 6

if scroll_down_to_cast:
    actors = []
    i = 0
    while i < 15:
        actors_by_id = wait.until(lambda x: x.find_elements(By.ID, "com.orange.pl.orangetvgo:id/actor_name"))
        actors.extend([actor.text for actor in actors_by_id])
        action.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        i += 1
    actors_new_list = list(set(actors))
    pairs = [el.split(' ') for el in actors_new_list]
    sorted_list = sorted(pairs, key=lambda name: name[1])
    print([name[0] + ' ' + name[1] for name in sorted_list])
else:
    print("No cast added")
time.sleep(5)
driver.quit()
