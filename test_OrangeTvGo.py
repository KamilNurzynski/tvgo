from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import time
import appium


def test_open_app(desired_capabilities):
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
    # how to chck status 200 code????????
    driver.quit()


def test_verify_if_all_components_loaded(desired_capabilities):
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
    # what is complete app?
    driver.quit()


def test_count_banners(desired_capabilities):
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)

    wait = WebDriverWait(driver, 25, poll_frequency=1,
                         ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                             NoSuchElementException])

    action = TouchAction(driver)

    dismiss_button = wait.until(lambda x: x.find_element(By.ID, "com.orange.pl.orangetvgo:id/menu_login"))
    dismiss_button.click()
    agreement_checkbox = wait.until(
        lambda x: x.find_element(By.ID, "com.orange.pl.orangetvgo:id/welcome_analytics_checkbox"))
    agreement_checkbox.click()
    lets_start = wait.until(
        lambda x: x.find_element(By.ID, "com.orange.pl.orangetvgo:id/welcome_btn_start"))
    lets_start.click()

    deviceSize = driver.get_window_size()
    screenWidth = deviceSize['width']

    ######Swipe right to left#######
    startx = screenWidth * 8 / 9
    endx = screenWidth / 9
    starty = 670
    endy = 670

    titles = []
    offset = 0
    flag = True
    while flag:
        banner = wait.until(lambda x: x.find_element(By.ID, "com.orange.pl.orangetvgo:id/banner_small"))
        banner.click()
        time.sleep(1)
        title_obj = wait.until(
            lambda x: x.find_element(By.ID, "com.orange.pl.orangetvgo:id/text_expanded"))
        if title_obj.text not in titles:
            titles.append(title_obj.text)
            offset += 1
            # go back to home screen
            driver.press_keycode(4)
            for i in range(offset):
                time.sleep(2)
                action.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        else:
            flag = False

    print(f"In the app is: {len(titles)} banners.")

    driver.quit()


def test_enter_to_fourth_recommended_movie(desired_capabilities):
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)

    wait = WebDriverWait(driver, 25, poll_frequency=1,
                         ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                             NoSuchElementException])

    dismiss_button = wait.until(lambda x: x.find_element(By.ID, "com.orange.pl.orangetvgo:id/menu_login"))
    dismiss_button.click()
    agreement_checkbox = wait.until(
        lambda x: x.find_element(By.ID, "com.orange.pl.orangetvgo:id/welcome_analytics_checkbox"))
    agreement_checkbox.click()
    lets_start = wait.until(
        lambda x: x.find_element(By.ID, "com.orange.pl.orangetvgo:id/welcome_btn_start"))
    lets_start.click()
    fourth_movie_image = wait.until(
        lambda x: x.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.'
                                           'LinearLayout/android.widget.FrameLayout/android.widget.'
                                           'FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                           '/android.widget.FrameLayout/android.widget.FrameLayout/'
                                           'android.widget.FrameLayout/android.widget.LinearLayout/'
                                           'android.widget.ScrollView/android.widget.FrameLayout/'
                                           'android.widget.FrameLayout/android.widget.LinearLayout/'
                                           'android.widget.FrameLayout/android.widget.FrameLayout/'
                                           'androidx.recyclerview.widget.RecyclerView/'
                                           'android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView'
                                           '/androidx.appcompat.widget.LinearLayoutCompat[4]/android.widget.ImageView'))

    fourth_movie_image.click()
    driver.quit()


def test_grab_actors_and_print(desired_capabilities):
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
    wait = WebDriverWait(driver, 25, poll_frequency=1,
                         ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                             NoSuchElementException])

    action = TouchAction(driver)

    dismiss_button = wait.until(lambda x: x.find_element(By.ID, "com.orange.pl.orangetvgo:id/menu_login"))
    dismiss_button.click()
    agreement_checkbox = wait.until(
        lambda x: x.find_element(By.ID, "com.orange.pl.orangetvgo:id/welcome_analytics_checkbox"))
    agreement_checkbox.click()
    lets_start = wait.until(
        lambda x: x.find_element(By.ID, "com.orange.pl.orangetvgo:id/welcome_btn_start"))
    lets_start.click()
    fourth_movie_image = wait.until(
        lambda x: x.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.'
                                           'LinearLayout/android.widget.FrameLayout/android.widget.'
                                           'FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                           '/android.widget.FrameLayout/android.widget.FrameLayout/'
                                           'android.widget.FrameLayout/android.widget.LinearLayout/'
                                           'android.widget.ScrollView/android.widget.FrameLayout/'
                                           'android.widget.FrameLayout/android.widget.LinearLayout/'
                                           'android.widget.FrameLayout/android.widget.FrameLayout/'
                                           'androidx.recyclerview.widget.RecyclerView/'
                                           'android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView'
                                           '/androidx.appcompat.widget.LinearLayoutCompat[4]/android.widget.ImageView'))

    fourth_movie_image.click()

    scroll_down_to_cast = wait.until(lambda x: x.find_element(By.ANDROID_UIAUTOMATOR,
                                                              'new UiScrollable(new UiSelector()).'
                                                              'scrollIntoView(text("Obsada"))'))
    deviceSize = driver.get_window_size()
    screenWidth = deviceSize['width']
    screenHeight = deviceSize['height']

    ######Swipe Right to Left#######
    startx = screenWidth * 1 / 8
    endx = 10
    starty = screenHeight * 5 / 6
    endy = screenHeight * 5 / 6

    actors = []
    i = 0
    while i < 15:
        cast = wait.until(lambda x: x.find_elements(By.ID, "com.orange.pl.orangetvgo:id/actor_name"))
        actors.extend([actor.text for actor in cast])
        action.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        i += 1

    cast_new_list = list(set(actors))
    pairs = [el.split(' ') for el in cast_new_list]
    sorted_list = sorted(pairs, key=lambda name: name[1])

    print([name[0] + ' ' + name[1] for name in sorted_list])

    driver.quit()
