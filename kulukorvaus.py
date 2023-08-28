from selenium import webdriver
from selenium.webdriver.common.by import By
import getpass
import glob
import os
import time
import csv

# Add your own file paths here
login_file_path = r"D:/KB/kulukorvausBot/login"
downloads_path = r"C:/Users/joona/Downloads/*"  # DONT REMOVE THE *
kulukorvaukset_path = r"F:/Hallitus/kulukorvaukset"


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

    email_input = browser.find_element(By.NAME, "user_email")
    email_input.send_keys(getEmail())
    password_input = browser.find_element(By.NAME, "user_password")
    password_input.send_keys(getPassword())

    login_btn = browser.find_element(By.NAME, "login")
    login_btn.click()
    browser.implicitly_wait(2)

    summary_page = browser.find_element(By.LINK_TEXT, "Tulosteet ja koosteet")
    summary_page.click()
    browser.implicitly_wait(2)

    file_type_select = browser.find_element(By.XPATH, '//*[@id="print_modes"]/label[3]/div/ins')
    file_type_select.click()

    select_date = browser.find_element(By.XPATH, '//*[@id="daterange-btn"]')
    select_date.click()

    select_week = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[3]')
    select_week.click()

    select_date.click()

    select_month = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[4]')
    select_month.click()

    download_csv = browser.find_element(By.XPATH, '//*[@id="new_print"]/div/div/div[3]/input')
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
            data = f"- {line[3]}; {line[10]}; {float(line[9]):.2f} €"
            relevant_data.append(data)

            if type == "Kulukorvaus":
                line = "; ".join(relevant_data)
                reimbursements.append(line)

            elif type == "Korttiosto killan kortilla":
                line = "; ".join(relevant_data)
                card_payments.append(line)

            elif type == "Haalaritiimin kulukorvaus":
                line = "; ".join(relevant_data)
                hati_reimbursements.append(line)

            elif type == "Killan yleinen kilometrikorvaus":
                line = "; ".join(relevant_data)
                mileages.append(line)

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

