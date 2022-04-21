from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

with open('messages.txt', 'r', encoding='utf-8') as messages:
    messagelist = list()
    text = messages.read()
    messagelist = text.split("\n")


def start():
    flag=False
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get("https://web.whatsapp.com/")
    print("1-Çevrimiçi Oluğunda Mesaj Gönder")
    print("2-İstenilen bir mesajı istenilen kez gönder")
    print("3-İstenilen bir mesajı sonsuz kere Gönder")

    istek = int(input("Seçiminiz: "))

    person_area = driver.find_element(By.XPATH, value='//*[@id="side"]/div[1]/div/label/div/div[2]')
    person_area.send_keys("The Batman")
    finded_person_area = driver.find_element(By.XPATH,value='//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span/span')
    finded_person_area.click()
    message_area = driver.find_element(By.XPATH,value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')



    if istek==1:
        while True:
            message_area.click()
            wp_source = driver.page_source
            soup = bs(wp_source, "lxml")
            # class="zzgSd _3e6xi"
            search = soup.findAll("div", {"class": ["zzgSd ", "_3e6xi"]})

            try:
                online = search[0].span.text
                print(online)
                if (online in ["çevrimiçi", "online"]) and flag == False:
                    print("Online")
                    msgToSend = messagelist[0]
                    message_area.send_keys(msgToSend)
                    message_area.send_keys(Keys.ENTER)
                    flag = True
                elif online not in ["çevrimiçi", "online"]:
                    print("Online Değil")
                    flag = False

            except:
                print("Şu anda Çevrimdışı")
                flag = False

            time.sleep(3)
    elif istek==2:
        mesaj=str(input("Gönderilecek Mesaj: "))
        tekrar=int(input("Kaç Kere Gönderilsin: "))

        while tekrar>0:
            message_area.click()
            try:
                    msgToSend = mesaj
                    message_area.send_keys(msgToSend)
                    message_area.send_keys(Keys.ENTER)

            except:
                print("Mesaj Gönderilemedi")

            tekrar=tekrar-1

            print("Mesaj başarılı bir şekilde gönderildi")
        time.sleep(3)

    elif istek==3:
        mesaj=str(input("Sonsuz Kez Gönderilecek Mesaj : "))
        while True:
            message_area.click()


            try:

                    msgToSend = mesaj
                    message_area.send_keys(msgToSend)
                    message_area.send_keys(Keys.ENTER)


            except:
                print("Şu anda Çevrimdışı")

        print("Sonsuz Mesaj Gönderiliyor")
        time.sleep(3)

    else:
        print("Yanlış Seçim !!!!")

start()
# while True:
    #     message_area.click()
    #     wp_source=driver.page_source
    #     soup=bs(wp_source,"lxml")
    #     #class="zzgSd _3e6xi"
    #     search=soup.findAll("div",{"class":["zzgSd ","_3e6xi"]})
    #
    #     try:
    #         online =search[0].span.text
    #         print(online)
    #         if (online in ["çevrimiçi","online"]) and flag==False:
    #             print("Online")
    #             msgToSend=messagelist[0]
    #             message_area.send_keys(msgToSend)
    #             message_area.send_keys(Keys.ENTER)
    #             flag=True
    #         elif online not in ["çevrimiçi","online"]:
    #             print("Online Değil")
    #             flag=False
    #
    #     except:
    #         print("Şu anda Çevrimdışı")
    #         flag=False
    #
    #
    #     time.sleep(3)