import pandas as pd
from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By



def scrapping():
    data_list = []
    page_url = "https://vinylcollector.store/collections/nouveautes"
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(page_url)


    for li in driver.find_elements(By.CLASS_NAME, "grid__item"):
        titre = li.find_element(By.TAG_NAME,"h2").text
        prix = li.find_element(By.CSS_SELECTOR,".product-price").text
        data_list.append((titre, prix))
        print(titre,prix)
    
    myCollection = pd.DataFrame(data_list, columns=["titre", "prix"])    
    myCollection.to_csv(f"test.csv")





mydf = scrapping()

