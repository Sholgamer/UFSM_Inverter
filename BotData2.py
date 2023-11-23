import requests
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup 
import time
import re

def scraapy(content):
    
    page = BeautifulSoup(content, "html.parser")
    db = page.find_all("h3" , class_="ng-star-inserted")
    
    pot = re.search('\d{1,2}\,\d{2}' , str(db[0])).group()

    print(pot)
    

    
with sync_playwright() as p:

    navegator = p.chromium.launch(headless=True) #headless mostra ou n o navegador
    url = "https://www.ingeconsunmonitor.com/login"

    # headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"}

    page = navegator.new_page()
    page.goto(url)
    
    #localiza o campo de preenchimento e preenche
    page.fill("xpath=/html/body/app-main-login/div/div[1]/div[2]/div/app-login/div/div/form/div[1]/div/div[1]/div/input" , "marcostreter@gmail.com")
    page.fill("xpath=/html/body/app-main-login/div/div[1]/div[2]/div/app-login/div/div/form/div[1]/div/div[2]/div/input" , "7BPttCtkcuNH.7V8mYmimCTK")
    time.sleep(0)

    #localiza o elemento na pagina e clica
    page.locator('xpath=/html/body/app-main-login/div/div[1]/div[2]/div/app-login/div/div/form/div[3]/div/button/span').click()
    time.sleep(1)

    #navega na pag
    page.locator('xpath=/html/body/app-dashboard/div/main/div/ng-component/div/div[1]/div/div/div/app-plant-card/div').click()
    time.sleep(1)
    page.locator('xpath=/html/body/app-dashboard/div/div[1]/nav/ul/li[2]/a').click()
    time.sleep(5)

    while True:
        time.sleep(5)
        scraapy(page.content())