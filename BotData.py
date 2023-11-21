import requests
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup 
import re
import time


def scraapy(content):

    page = BeautifulSoup(content, "html.parser")
    db_all = page.find_all("div" , class_="photo-disk-inner-font")

    # volt = page.find.recompile("div" , class_="photo-disk-inner-left>\d{3}\.\d{1}/")
    # amp = page.find.recompile("div" , class_="photo-disk-inner-left>\s\d{2}\.\d{1}/")

    print(len(db_all))
    volt = re.search('\d{3}\.\d{1}'  , str(db_all[3])).group()
    amp = re.search('\d{2}\.\d{1}'  , str(db_all[4])).group()

    # volt = re.search('class="photo-disk-inner-left">\d{3}\.\d{1}' , str(content))
    # amp = re.search('class="photo-disk-inner-left">\s\d{2}\.\d{1}' , content)
    # print(content)
    print(volt , amp)

#bot abre o site e navegar ate ter as informaçoes do inversor
with sync_playwright() as p:

    navegator = p.chromium.launch(headless=False) #headless mostra ou n o navegador
    page = navegator.new_page()
    page.goto("https://www.ingeconsunmonitor.com/login")
    
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
    time.sleep(2)
    # page.locator('xpath=//*[@id="primeNgOverride"]/div/div/table/tbody/tr/td[2]/app-deviceboardweb/button/img').click()

    validacao = page.locator('xpath=//*[@id="primeNgOverride"]/div/div/table/tbody/tr/td[2]/app-deviceboardweb/button/img')

    print(validacao.is_visible())
    
    if validacao == True:
        validacao.click()

        time.sleep(20)

        page.goto("https://device.ingeconsunmonitor.com/?board=1DM172B04A31&ptk=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJQbGFudElkIjoiMTk3OSIsIlVzZXJJZCI6IjEyMzAiLCJuYmYiOjE2OTk5ODc2OTYsImV4cCI6MTY5OTk5MTI5NiwiaWF0IjoxNjk5OTg3Njk2LCJpc3MiOiJpbmdlY29uc3VubW9uaXRvci5jb20ifQ.erIqOQHGDZ9m_94sV01jZ1QpKlcqp08SULlGffYFv-0#/embeddedinverter/main/local/1/-1")
        time.sleep(20)

        scraapy(page.content())
    
    else:
        print("not working frequency inverter")
