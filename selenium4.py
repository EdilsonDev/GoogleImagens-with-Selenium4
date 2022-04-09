from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import a

driver = webdriver.Chrome()

driver.get("https://www.google.com/")  # url

chrome_service = Service(
    executable_path="chromedriver.exe"
)

driver.find_element(By.XPATH, a.gimagem).click()  # google img
sleep(1)
driver.find_element(By.NAME, "q").send_keys(a.texto)  # digita python
driver.find_element(By.XPATH, a.confirmar).click()
driver.find_element(By.XPATH, a.clica_imagem).click()
sleep(1.5)
driver.find_element(By.XPATH, a.proximo).click()
sleep(1.5)
driver.find_element(By.XPATH, a.proximo1).click()
sleep(1.5)
driver.find_element(By.XPATH, a.voltar).click()
sleep(1.5)
driver.execute_script(a.abregit)  # abre github
sleep(4.5)
driver.close()   # fecha primeira pagina
sleep(6)
driver.quit()

print(f"\n{'':20}Obrigado por utilizar python selenium\n")
