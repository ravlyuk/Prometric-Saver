import random
import urllib.request
import socket
import os
import sys
from PIL import Image
import subprocess as sp
from colorama import init
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from glob import glob

init()

directory = os.getcwd()

link = str(urllib.request.urlopen('https://twitter.com/vivex10').read())
if 'mcu-off' in link:
    pass
else:
    print('Вас приветствует Prometric Saver v1.0 by Evgeny Ravlyuk!\n')

    setting = open(directory + '\\data\\Настройки.txt', 'r', encoding='utf8')
    setting_lines = setting.readlines()
    visible = int(setting_lines[0].split(':')[1].replace("\n", ""))
    acc_email = setting_lines[1].split(':')[1].replace("\n", "")
    acc_pass = setting_lines[2].split(':')[1].replace("\n", "")
    len_questions = int(setting_lines[3].split(':')[1].replace("\n", ""))
    href = setting_lines[4].replace("\n", "")
    catalog = directory + "\\Screenshots"

    # Настройки драйвера
    opts = Options()
    if visible == 0:
        opts.set_headless()
        assert opts.headless  # operating in headless mode
    binary = FirefoxBinary(
        directory + '\\data\\Program Files\\FirefoxPortable64-60.0.1\\FirefoxPortable64\\App\\Firefox\\firefox.exe')
    driver = Firefox(executable_path=directory + '\\data\\Program Files\\driver\\geckodriver64.exe',
                     firefox_binary=binary,  options=opts, log_path=directory + '\\data\\Program Files\\driver\\log.log')
    driver.set_page_load_timeout(15)
    driver.set_window_size(1280, 1000)

    try:
        driver.get('http://www.prometricmcq.me/assessment/login.php')
    except:
        driver.stop_client()

    print(
        f'\nВхожу в аккаунт под учётной записью:\n{acc_email}\n{acc_pass}\n')

    # Login
    driver_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username')))
    driver_element.send_keys(acc_email)
    driver_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password')))
    driver_element.send_keys(acc_pass)
    driver_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'btnSubmit')))
    driver_element.click()

    driver.get(href)

    try:
        driver.get(href)
    except:
        driver.stop_client()

    print('Приступаю к сохранению скриншотов!\n')

    for i in range(0, len_questions):
        print(f'Обработано {i+1} из {len_questions}')
        sleep(1)

        # скрол в самый верх страницы
        driver.execute_script("window.scrollBy(1, -9999999)")

        elementcheck = False
        for j in range(7):
            try:
                elementcheck = driver.find_element_by_xpath(
                    f'/html/body/div[1]/div[1]/div/div/div/div[1]/form/div[1]/table/tbody/tr[3]/td[1]/div[2]/table/tbody/tr[5]/td/table/tbody/tr[{j}]/td[2]/font')
            except:
                pass

        if not elementcheck:
            # Выбрать опции
            try:
                driver_element = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="rdAns"]')))
                driver_element.click()
            except:
                pass
            sleep(1)

            # Нажать далее
            try:
                WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/form/div[1]/table/tbody/tr[3]/td[1]/div[2]/table/tbody/tr[7]/td/input[3]')))
            except:
                driver_element = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/form/div[1]/table/tbody/tr[3]/td[1]/div[2]/table/tbody/tr[7]/td/input[1]')))
                driver_element.click()
            else:
                driver_element = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/form/div[1]/table/tbody/tr[3]/td[1]/div[2]/table/tbody/tr[7]/td/input[2]')))
                driver_element.click()

            sleep(1)
            driver.save_screenshot(
                directory + f'\\Screenshots\\question-{i+1}.png')

            # Нажать далее
            try:
                WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/form/div[1]/table/tbody/tr[3]/td[1]/div[2]/table/tbody/tr[7]/td/input[3]')))
            except:
                driver_element = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/form/div[1]/table/tbody/tr[3]/td[1]/div[2]/table/tbody/tr[7]/td/input[1]')))
                driver_element.click()
            else:
                driver_element = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/form/div[1]/table/tbody/tr[3]/td[1]/div[2]/table/tbody/tr[7]/td/input[2]')))
                driver_element.click()

        else:
            sleep(1)
            driver.save_screenshot(
                directory + f'\\Screenshots\\question-{i+1}.png')

            # Нажать далее
            try:
                WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/form/div[1]/table/tbody/tr[3]/td[1]/div[2]/table/tbody/tr[7]/td/input[3]')))
            except:
                driver_element = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/form/div[1]/table/tbody/tr[3]/td[1]/div[2]/table/tbody/tr[7]/td/input[1]')))
                driver_element.click()
            else:
                driver_element = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/form/div[1]/table/tbody/tr[3]/td[1]/div[2]/table/tbody/tr[7]/td/input[2]')))
                driver_element.click()

    print(colored('\nПрограмма завершила свою работу, все скриншоты сохранены в папку \"Screenshots\"', 'green'))
