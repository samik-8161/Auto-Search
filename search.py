from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import sys

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"       #{normal , eager, none} 
service = Service('C:\Setup\chromedriver.exe')
service.start()

browser = webdriver.Remote(service.service_url,desired_capabilities=caps)
filename = "set"+sys.argv[1]+".txt"
file = open(filename,'r')

search_list = file.readlines()
n = len(search_list)
for i in range(n):
    search_list[i] = " ".join(search_list[i].split())
print(len(search_list))
file.close()

for i in range(len(search_list)):
    tabname = "tab"+str(i+1)
    search_query = "mcq " + search_list[i]
    browser.get("https://google.com")
    search_box = browser.find_element_by_name('q')
    search_box.send_keys(search_query)
    search_box.submit()
    scr = "window.open('about:blank','" + tabname + "');"
    browser.execute_script(scr)
    browser.switch_to.window(tabname)
    
end = input()
browser.quit()
