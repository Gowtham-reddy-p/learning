# Selemium => UI automation framework
import time

# Selenium webdriver => which controls the web browsers (chrome,edge)

# It is used automate the web applications mainly
# it contains a module called webdriver.
# Webdriver is an API which  contains classes of Chrome(), Edge(), Firefox()

#Selenium locators: id, name, class, Xpath, css selector, Tag name, link text

#CLASS NAME:
# style =>we are going to access with style name
# if we found gap in the class name => we replace with . in selenium
# class name or tag name are used to find multiple web elements



#CSS Selector (Cascading style sheet)

# we can find element by css selector in 4 ways:

#tag & id                  => tagname#value of Id
# tag & class              => tagname.Class value
# tag & attribite          => tagname [Attribute=Value]
# tag & class & attribite  => tagname.ClassValue[attribute=value]   # we use this selector when two web elements have same id & class




#Xpath - xml path

# During the run time the attributes change dynamically. So we use xpath
#it is a syntax for finding an element on the web using an xml path expression
#Xpath is used to find the location of any element using html DOM (document object model) structure
# xpath is the address of an element

# Types of xpath: Absolute xpath (full xpath)    Ex: /html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button
#                 Relative xpath (partial xpath) Ex: //*[@id="u_0_5_x/"]

# Diff between Absolute&Relative Xpaths
# 1)Absolute xpath starts from root html node
#    Relative xpath directly jump to element on DOM.
# 2)Absolute xpath start with/
#   Relative xpath start with //
# 3)in Absolute xpath we use only tags/nodes
#    In Relative xpath we use attributes.


#X Path options:

# and
# or
# contains()     => //button[contains(@id,'menu')]
# starts-with()  => //*[starts-with(@id, 'react')]
# text()


#X path axes

# these are the keywords we use in xpath to access the DOM structure top to bottom

# self
# parent             => //*[attribute='value']/parent:: tagname
# child              => //*[attribute='value']/child:: tagname
# ancestor           => //*[attribute='value']/ancestor:: tagname
# descendant         => //*[attribute='value']/descendant:: tagname
# following          => //*[attribute='value']/following:: tagname
# preceding          => //*[attribute='value']/preceding:: tagname
# following-sibling  => // current html tag[attribute='value']/following-sibling:: sibling tag[@attribute='value]
# preceding-sibling  => // current html tag[attribute='value']/preceding-sibling:: previous tag[@attribute='value]


# Different types of commands:

# Application/get commands - title, current url, page source
# Conditional commands
# Browser commands
# Navigational commands
# Wait commands




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path=r'C:\Users\Gowtham\PycharmProjects\pythonProject2\Selenium\chromedriver-win64\chromedriver.exe')

driver.maximize_window()


# driver.get("http://www.flipkart.com")
# close_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button")
# close_button.click()
# a = driver.find_element(By.CLASS_NAME, "xtXmba").click()
# open_item = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div[3]/div/a/div[1]/div/img').click()

# driver.get("https://www.facebook.com")
# driver.find_element(By.XPATH,'//*[@id="u_0_0_8A"]').click()

# #tag id
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("fbkadff")

# # #tag class
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("dfgksdb")

# # #tag attribute
# driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_pass]").send_keys("25235t25")

# # #tag,class,attribute
# driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("gowtham")
# driver.find_element(By.CSS_SELECTOR, "button._42ft[data-testid=royal_login_button]").click()

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome(executable_path=r'C:\Users\Gowtham\PycharmProjects\pythonProject2\Selenium\chromedriver-win64\chromedriver.exe')

browser=driver.get("https://www.saucedemo.com/")
driver.maximize_window()

try:
    user_name= driver.find_element(by=By.ID,value="user-name")
    user_name.send_keys("standard_user")

    password= driver.find_element(By.NAME,"password")
    password.send_keys("secret_sauce")

except Exception as e:
    print(e)
finally:
    login= driver.find_element(By.XPATH, "//*[@id='login-button']")
    login.click()
    time.sleep(10)

def test_login():
    assert driver.title=="Swag Labs"


action = ActionChains(driver)
twitter_id= driver.find_element(By.CSS_SELECTOR, "a[]")
