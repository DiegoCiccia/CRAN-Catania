import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def click(text, driver, t):
    WebDriverWait(driver, t).until(EC.presence_of_element_located((By.XPATH, text))).click()

def set_text(text, keys, driver, t):
    WebDriverWait(driver, t).until(EC.presence_of_element_located((By.XPATH, text))).send_keys(keys)

def get_attribute(text, attribute, driver, t):
    a = WebDriverWait(driver, t).until(EC.presence_of_element_located((By.XPATH, text))).get_attribute(attribute)
    return(a)

def check_text(text, driver, t):
    try:   
        a = WebDriverWait(driver, t).until(EC.presence_of_element_located((By.XPATH, text))).text
    except:
        a = ""
    return(a)    

data = pd.read_csv("mirrors.csv")

t = 5
cwd = os.getcwd()
options = webdriver.ChromeOptions()
#options.headless = True
driver = webdriver.Chrome(cwd + "\\chromedriver\\chromedriver", options = options)

# Manual adjustments
data.loc[data["description"] == "School of Mathematics and Statistics, University of Melbourne", "description"] = "Melbourne"
data.loc[data["description"] == "Patrick Wessa", "description"] = "Basel"
data.loc[data["description"] == "Belnet, the Belgian research and education network", "description"] = "Brussels"
data.loc[data["description"] == "Oswaldo Cruz Foundation, Rio de Janeiro", "description"] = "Rio de Janeiro"
data.loc[data["description"] == "University of Sao Paulo, Sao Paulo", "description"] = "Sao Paulo"
data.loc[data["description"] == "University of Sao Paulo, Piracicaba", "description"] = "Piracicaba"
data.loc[data["description"] == "Sofia University", "description"] = "Sofia City"
data.loc[data["description"] == "Manitoba Unix User Group", "description"] = "Manitoba"
data.loc[data["description"] == "Departamento de Ciencias de la Computación, Universidad de Chile", "description"] = "Universidad de Chile"
data.loc[data["description"] == "TUNA Team, Tsinghua University", "description"] = "Tsinghua University"
data.loc[data["description"] == "Beijing Foreign Studies University", "description"] = "Beijing City"
data.loc[data["description"] == "KoDDoS in Hong Kong", "description"] = "Hong Kong"
data.loc[data["description"] == "Lanzhou University Open Source Society", "description"] = "Lanzhou University"
data.loc[data["description"] == "eScience Center, Nanjing University", "description"] = "Nanjing University"
data.loc[data["description"] == "Distance State University (UNED)", "description"] = "San José City"
data.loc[data["description"] == "Dept. of Biometry & Evol. Biology, University of Lyon", "description"] = "University of Lyon"
data.loc[data["description"] == "CNRS IBCP, Lyon", "description"] = "Centre National de la Recherche Scientifique Lyon"
data.loc[data["description"] == "French Nuclear Safety Institute, Paris", "description"] = "Paris"
data.loc[data["description"] == "dogado GmbH", "description"] = "Dortmund"
data.loc[data["description"] == "ClientVPS", "description"] = "Berlin"
data.loc[data["description"] == "National Institute of Science Education and Research (NISER)", "description"] = "Ibadan"
data.loc[data["description"] == "Garr Mirror, Milano", "description"] = "Milano"
data.loc[data["description"] == "Evoluso.com", "description"] = "Amsterdam"
data.loc[data["description"] == "Lyra Hosting", "description"] = "Amsterdam"
data.loc[data["description"] == "MI2.ai, Warsaw University of Technology", "description"] = "Warsaw"
data.loc[data["description"] == "RadicalDevelop, Lda", "description"] = "Faro Portugal"
data.loc[data["description"] == "Truenetwork", "description"] = "Moscow"
data.loc[data["description"] == "TENET, Johannesburg", "description"] = "Johannesburg"
data.loc[data["description"] == "Oficina de software libre (CIXUG)", "description"] = "Vigo"
data.loc[data["description"] == "Spanish National Research Network, Madrid", "description"] = "Madrid"
data.loc[data["description"] == "Academic Computer Club, Umeå University", "description"] = "Umeå University"
data.loc[data["description"] == "Prince of Songkla University, Hatyai", "description"] = "Prince of Songkla University"
data.loc[data["description"] == "MBNI, University of Michigan, Ann Arbor, MI", "description"] = "University of Michigan"
data.loc[data["description"] == "Washington University, St. Louis, MO", "description"] = "Washington City"
data.loc[data["description"] == "Statlib, Carnegie Mellon University, Pittsburgh, PA", "description"] = "Carnegie Mellon University"
data.loc[data["description"] == "Hoobly Classifieds, Pittsburgh, PA", "description"] = "Pittsburgh"
data.loc[data["description"] == "National Institute for Computational Sciences, Oak Ridge, TN", "description"] = "Oak Ridge"
data.loc[data["description"] == "New York University in Abu Dhabi", "description"] = "Abu Dhabi"
data.loc[data["description"] == "Facultad de Derecho, Universidad de la República", "description"] = "Montevideo"
data.loc[data["description"] == "MARWAN", "description"] = "Rabat City"

x = []
y = []
mirrors = data["description"].tolist()
del mirrors[0]
del mirrors[len(mirrors)-1]

for i in range(len(mirrors)):
    driver.get("https://www.openstreetmap.org/#map=19/-34.91240/-57.95622")
    driver.maximize_window()
    set_text("/html/body/div/div[1]/div[1]/form[1]/div/div[1]/div/input[1]", mirrors[i], driver, t)
    click("/html/body/div/div[1]/div[1]/form[1]/div/div[1]/div/input[2]", driver, t)
    if len(check_text("/html/body/div/div[1]/div[5]/div[2]/ul/li/a", driver, t)) > 0:
        x.append(get_attribute("/html/body/div/div[1]/div[5]/div[2]/ul/li/a", "data-lon", driver, t))
        y.append(get_attribute("/html/body/div/div[1]/div[5]/div[2]/ul/li/a", "data-lat", driver, t))
        print(mirrors[i], ":", x[i], y[i])
    else:
        x.append(0)
        y.append(0)
        print(mirrors[i], "not found")
driver.quit()

out = {}
out["mirror"] = mirrors
out["nation"] = data["nation"].tolist()[1:-1]
out["x"] = x
out["y"] = y
Frame = pd.DataFrame.from_dict(out)
Frame.to_csv("mirrors_coord.csv", encoding = "utf-8-sig", index = False)  
