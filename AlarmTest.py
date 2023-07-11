from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.action_chains import ActionChains

desired_cap = {
    "platformName": "Android",
    "appium:deviceName": "HA15G3JS",
    "appium:automationName": "UiAutomator2",
    "appium:platformVersion": "10",
    "appium:appPackage": "com.google.android.deskclock",
    "appium:appActivity": "com.android.deskclock.DeskClock"
}

driver = webdriver.Remote("http://127.0.0.1:4723", desired_cap)
driver.implicitly_wait(30)

# in the clock section go to alarm

driver.find_element(By.ID, 'com.google.android.deskclock:id/tab_menu_alarm').click()

# click on add new alarm

driver.find_element(By.ID, 'com.google.android.deskclock:id/fab').click()

# select the desired time to 12:40 PM

driver.find_element(By.ID, 'com.google.android.deskclock:id/material_clock_period_pm_button').click()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(600, 884)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(476, 1105)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# press OK button

driver.find_element(By.ID, 'com.google.android.deskclock:id/material_timepicker_ok_button').click()

# check alarm was set
hour = driver.find_element(By.XPATH, "//android.widget.TextView[@bounds='[258,610][508,699]']").get_attribute('text')
assert hour == "12:40 PM", "The hour is not the same"

toggle = driver.find_element(By.XPATH, "//android.widget.Switch[@bounds='[978,699][1062,771]']").get_attribute('text')
assert toggle == "ON", "The alarm is not active"