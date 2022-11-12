from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import getpass
import glob
import os
import time


def fetchEmail():
    """
    Fetches the user's email from the login file
    :return: user email as a string
    """
    login_file = open(r"C:\...", "r")   # EDIT THIS
    email = login_file.readline().split(";")[1]
    login_file.close()
    return email


def fetchPassword():
    """
    Fetches the user's password from the login file.
    :return: user password as a string
    """
    login_file = open(r"C:\...", "r")   # EDIT THIS
    password = login_file.readline().split(";")[3]
    login_file.close()
    return password


def downloadCSV(browser):
    """
    Opens a website, logs into it and navigates it to download a CSV file with data
    about new unapproved reimbursements within a 30-day period.
    :param browser: webdriver Chrome window
    """
    browser.get('https://kululaskut.fi/')
    browser.maximize_window()

    home_login_btn = browser.find_element(By.ID, "menu-item-112")
    home_login_btn.click()

    email_input = browser.find_element(By.NAME, "user_email")
    email_input.send_keys(fetchEmail())
    password_input = browser.find_element(By.NAME, "user_password")
    password_input.send_keys(fetchPassword())

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

    time.sleep(2)
    browser.quit()


def filterData():
    """
    Opens the most recent downloaded (CSV) file that contains all data regarding
    new unapproved reimbursements. Relevant data is then parsed from the file and
    into an array of strings.
    :return: an array of strings that contain reimbursements' data
    """
    downloads = glob.glob("C:\\Users\\nameHere\\Downloads\\*".format(getpass.getuser()))    # EDIT THIS
    latest_download = max(downloads, key=os.path.getctime)
    temp_data = []
    final_data = []

    csv_file = open(latest_download, "r")
    next(csv_file)  # skip the header line
    for line in csv_file:
        relevant_data = []
        line = line.split(";")
        relevant_data.extend((line[3][1:-1], line[10][1:-1], line[9][1:-1] + " € "))
        temp_data.append(relevant_data)
    csv_file.close()

    for array in temp_data:
        line = "; ".join(array)
        final_data.append(line)

    return final_data


def displayResults(data):
    """
    Writes data about the new reimbursements onto a file and opens that file
    :param data: an array of strings that contain reimbursements' data
    """

    file = open(r"C:\...\Hallitus\kulukorvaukset.txt", "w")     # EDIT THIS

    for line in data:
        line = line.replace("Ã¤", "ä")
        file.write(line + "\n")

    file.close()

    os.startfile(r"C:\...\Hallitus\kulukorvaukset.txt")     # EDIT THIS


# Open browser
chrome = webdriver.Chrome(ChromeDriverManager().install())

# Download data file
downloadCSV(chrome)

# Get the correct information from the data
final_data = filterData()

# Data about new reimbursements ready to be copied and pasted into the meeting's agenda
displayResults(final_data)

