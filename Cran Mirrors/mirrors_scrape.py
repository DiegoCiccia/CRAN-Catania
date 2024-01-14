import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def click(text, driver, t):
    WebDriverWait(driver, t).until(EC.presence_of_element_located((By.XPATH, text))).click()

def get_text(text, driver, t):
    a = WebDriverWait(driver, t).until(EC.presence_of_element_located((By.XPATH, text))).text
    return(a)

def check_text(text, driver, t):
    try:   
        a = WebDriverWait(driver, t).until(EC.presence_of_element_located((By.XPATH, text))).text
    except:
        a = ""
    return(a)    

t = 0.2
cwd = os.getcwd()
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(cwd + "\\chromedriver\\chromedriver", options = options)
driver.get("https://cran.r-project.org/mirrors.html")
driver.maximize_window()

nation = []
link = []
desc = []
for i in range(45):
        j = 1
        while len(check_text("/html/body/dl/dd["+str(i+1)+"]/table/tbody/tr["+str(j)+"]/td[1]/a", driver, t)) > 0:
            nation.append(get_text("/html/body/dl/dt["+str(i+1)+"]", driver, t))
            link.append(get_text("/html/body/dl/dd["+str(i+1)+"]/table/tbody/tr["+str(j)+"]/td[1]/a", driver, t))
            desc.append(get_text("/html/body/dl/dd["+str(i+1)+"]/table/tbody/tr["+str(j)+"]/td[2]", driver, t))
            j += 1
            print("Retrieving", desc[len(desc)-1], "mirror in", nation[len(nation)-1])

mirrors = {}
mirrors["nation"] = nation
mirrors["link"] = link
mirrors["description"] = desc

Frame = pd.DataFrame.from_dict(mirrors)
Frame.to_csv("mirrors.csv", encoding = "utf-8-sig", index = False)  
print("mirrors.csv available in root directory")
driver.quit()