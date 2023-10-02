from selenium import webdriver
from selenium.webdriver.common.by import By
import getpass
import glob
import os
import time
import csv

# Add your own file paths here
login_file_path =  r"C:/.../login.txt"
downloads_path = r"C:/Users/_nameHere_/Downloads/*"  # DONT REMOVE THE *
kulukorvaukset_path = r"C:/.../Hallitus/kulukorvaukset.txt"


def getEmail():
    with open(login_file_path, "r") as login_file:
        email = login_file.readline().split(";")[1]
    return email


def getPassword():
    with open(login_file_path, "r") as login_file:
        password = login_file.readline().split(";")[3]
    return password


def downloadCSV(browser):
    browser.get('https://kululaskut.fi/')
    browser.maximize_window()

    home_login_btn = browser.find_element(By.ID, "menu-item-112")
    home_login_btn.click()

    email_input = browser.find_element(By.ID, "email")
    email_input.send_keys(getEmail())
    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys(getPassword())

    login_btn = browser.find_element(By.ID, "submit")
    login_btn.click()
    browser.implicitly_wait(2)

    file_type_select = browser.find_element(By.XPATH, '//*[text() = "Työkalut"]')
    file_type_select.click()
    browser.implicitly_wait(1)

    file_type_select = browser.find_element(By.XPATH, '//*[text() = "Tulosteet ja koosteet"]')
    file_type_select.click()
    browser.implicitly_wait(1)

    # Opens the date selection panel
    select_span = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/form/div[2]/div[1]/div/div/div/div/div/div')
    select_span.click()
    browser.implicitly_wait(1)

    select_month = browser.find_element(By.XPATH, '//*[text() = "Edelliset 30 päivää"]')
    select_month.click()
    browser.implicitly_wait(1)

    close = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/form/div[1]/label[1]')
    close.click()
    browser.implicitly_wait(1)

    pick_csv = browser.find_element(By.XPATH, '//*[@id="format"]/label[3]')
    pick_csv.click()
    browser.implicitly_wait(1)

    accepted = browser.find_element(By.XPATH, '//*[@id="status"]/label[2]')
    accepted.click()

    locked = browser.find_element(By.XPATH, '//*[@id="status"]/label[3]')
    locked.click()

    download_csv = browser.find_element(By.XPATH, '//*[@id="submit"]')
    download_csv.click()

    time.sleep(5)
    browser.quit()


def filterData():
    downloads = glob.glob(downloads_path.format(getpass.getuser()))
    latest_download = max(downloads, key=os.path.getctime)

    reimbursements = []
    card_payments = []
    mileages = []
    hati_reimbursements = []
    final_lists = []

    with open(latest_download, newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        next(reader)
        
        for line in reader:
            relevant_data = []
            type = line[11]
            data = f"- {line[3]}; {line[10]}; {line[9]} €"
            relevant_data.append(data)

            if line[17] == "Killan yleinen kilometrikorvaus":
                line = "; ".join(relevant_data)
                mileages.append(line)

            else:
                if type == "Kulukorvaus":
                    line = "; ".join(relevant_data)
                    reimbursements.append(line)

                elif type == "Korttiosto killan kortilla":
                    line = "; ".join(relevant_data)
                    card_payments.append(line)

                elif type == "Haalaritiimin kulukorvaus":
                    line = "; ".join(relevant_data)
                    hati_reimbursements.append(line)

    final_lists.extend((reimbursements, card_payments, mileages, hati_reimbursements))

    return final_lists


def displayResults(data):
    hasResults = False
    with open(kulukorvaukset_path, "w") as file:
        if len(data[0]) > 0:
            hasResults = True
            file.write("Kulukorvaukset: \n")
            for line in data[0]:
                line = line.replace("Ã¤", "ä")
                line = line.replace("Ã¶", "ö")
                file.write(line + "\n")

        if len(data[1]) > 0:
            hasResults = True
            file.write("Korttiostot: \n")
            for line in data[1]:
                line = line.replace("Ã¤", "ä")
                line = line.replace("Ã¶", "ö")
                file.write(line + "\n")

        if len(data[2]) > 0:
            hasResults = True
            file.write("Kilometrikorvaukset: \n")
            for line in data[2]:
                line = line.replace("Ã¤", "ä")
                line = line.replace("Ã¶", "ö")
                file.write(line + "\n")

        if len(data[3]) > 0:
            hasResults = True
            file.write("Hatin kulukorvaukset: \n")
            for line in data[3]:
                line = line.replace("Ã¤", "ä")
                line = line.replace("Ã¶", "ö")
                file.write(line + "\n")

        if not hasResults:
            file.write("Ei uusia korvauksia")

    os.startfile(kulukorvaukset_path)


# Open browser
chrome = webdriver.Chrome()

# Download data file
downloadCSV(chrome)

# Get the correct information from the data
final_data = filterData()

# Data about new reimbursements ready to be copied and pasted into the meeting's agenda
displayResults(final_data)

