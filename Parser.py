from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

WALLET_NAME = "заглушка"

def getSite(url: str):
    driver.get(url)  # получение данных сайта
    time.sleep(2)

def getAllOperationsUrl(url: str):
    getSite(url)
    links = driver.find_elements(By.TAG_NAME, "a")
    filtered_links = [link.get_attribute("href") for link in links if  # фильтрование только нужных ссылок
                      "https://solscan.io/tx/" in link.get_attribute("href")]
    return filtered_links


def getLastOperationUrl(url: str):
    getSite(url)
    links = driver.find_elements(By.TAG_NAME, "a")
    filtered_links = [link.get_attribute("href") for link in links if  # фильтрование только нужных ссылок
                      "https://solscan.io/tx/" in link.get_attribute("href")]
    return filtered_links[0]

def getLastOperationInfo(url: str, WALLET_NAME):
    myUrl = getLastOperationUrl(url)
    getSite(myUrl)

    all_values = driver.find_elements(By.CLASS_NAME, "not-italic")
    SwapInteract = all_values[23].text
    if(SwapInteract == 'Swap'):
        message = ("""Имя кошелька: {}
        Signature: {}
        Operation type: Swap
        for {} {}
        for {} {}
        """.format(WALLET_NAME, str(all_values[9].text), all_values[33].text, all_values[34].text, all_values[38].text, all_values[39].text))
        if(all_values[9].text == '0' or all_values[34].text == '0'):
            return ' '
        message2 = ''
        links2 = driver.find_elements(By.TAG_NAME, "a")
        filtered_links = [link2.get_attribute("href") for link2 in links2 if  # фильтрование только нужных ссылок
                          "https://solscan.io/token/" in link2.get_attribute("href")]
        for link2 in filtered_links:
            link2 = link2.replace("https://solscan.io/token/", "")
            if link2 not in message2:
                message2 += "https://photon-sol.tinyastro.io/en/lp/" + link2 + "\n"
        message += '\n' + message2
        return message
    elif(SwapInteract == 'Interact with program'):
        message = ("""Имя кошелька: {}
        Signature: {}
        
        Operation type: Interact
        """.format(WALLET_NAME, str(all_values[9].text)))
        i = 27
        if(all_values[i].text == '0'):
            return ' '
        while i < 1000:
            message+="\nfor {} {}".format(all_values[i].text, all_values[i + 1].text)
            if all_values[i + 2].text == 'Interact with program':
                i += 6
            elif all_values[i + 2].text == 'Transfer from':
                i += 5
            else:
                break
        message2 = ''
        links2 = driver.find_elements(By.TAG_NAME, "a")
        filtered_links = [link2.get_attribute("href") for link2 in links2 if  # фильтрование только нужных ссылок
                          "https://solscan.io/token/" in link2.get_attribute("href")]
        for link2 in filtered_links:
            link2 = link2.replace("https://solscan.io/token/", "")
            if link2 not in message2:
                message2 += "https://photon-sol.tinyastro.io/en/lp/" + link2 + "\n"
        message += '\n' + message2
        return message
    else:
        print("end")
        return '.'


    #message = ("""Имя кошелька: {}
    #Signature: {}""".format(WALLET_NAME,str(all_values[9].text)))
    #print("Кошелёк: ", WALLET_NAME)
    #print("Signature: ", all_values[9].text)
    #print("Result: ", all_values[16].text)
    #print("Fee: ", all_values[20].text)
    #print(all_values[24].text)
    #print("________________________________________________________________")
    #return message
    #for value in all_values:
    #    print(value.text)


def testThisOperation(url: str):
    driver.get(url)
    time.sleep(5)

    message2 = ''
    links2 = driver.find_elements(By.TAG_NAME, "a")
    filtered_links = [link2.get_attribute("href") for link2 in links2 if  # фильтрование только нужных ссылок
                      "https://solscan.io/token/" in link2.get_attribute("href")]
    for link2 in filtered_links:
        link2 = link2.replace("https://solscan.io/token/", "")
        if link2 not in message2:
            message2 += "https://photon-sol.tinyastro.io/en/lp/" + link2 + "\n"
    #https://solscan.io/token/So11111111111111111111111111111111111111112