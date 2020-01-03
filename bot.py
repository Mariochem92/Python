from selenium import webdriver
import os
import click
import time
import numpy as np
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
import random


#tags= np.array(['selfie','backhome','love','friends','style','food','instagood','photooftheday','fashion','happy','beautiful','cute','christmas','nature'])
tags= np.array(['dance','holyday','family','starwars','ubuntu'])

wtime=30
us=input('insert username: ')
ps=getpass('insert password: ')
driver = webdriver.Firefox()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(2)
driver.find_element_by_name('username').send_keys(us)
driver.find_element_by_name('password').send_keys(ps,Keys.ENTER)
time.sleep(3)
#Not Now button
driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']").click()
time.sleep(5+8*random.uniform(0.2, 1))
count=0
maxlike=250
while count<maxlike:
    random.shuffle(tags)
    print(tags)
    for tag in tags:
        #define how many pics to like per hashtag
        npic=random.randint(8,15)
        driver.get("https://www.instagram.com/explore/tags/"+tag+'/')
        #find 1st pic
        like=WebDriverWait(driver, wtime).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div/div[2]/div[1]/a')))
        #open pic and like
        driver.execute_script("arguments[0].click();", like)
        time.sleep(2+8*random.uniform(0.01, 1))
        WebDriverWait(driver, wtime).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button'))).click()
        count=count+1
        print(count)
        print(tag)
        time.sleep(5+8*random.uniform(0, 1))
        stop= random.randint(21,26)
        if count>stop:
            count=0
            time.sleep(27+20*random.uniform(-1,1))
        for _ in  range(npic): 
            #move to next pic
            WebDriverWait(driver, wtime).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div/div/a[2]'))).click()
            time.sleep(2+8*random.uniform(0.01, 1))
            WebDriverWait(driver, wtime).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button'))).click()
            count=count+1
            print(count)
            time.sleep(15+8*random.uniform(0.2, 1))
