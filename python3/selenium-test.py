from selenium import webdriver
browser=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
browser.get("http://www.baidu.com")
input_first = browser.find_element_by_id("q")

print(input_first)
