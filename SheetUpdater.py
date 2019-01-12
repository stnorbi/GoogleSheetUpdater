import pandas as pd
import gspread_dataframe as gd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

keyFile=os.path.dirname(__file__)+"/Youtube Analyser-2920d371ed7e.json"

credentials=ServiceAccountCredentials.from_json_keyfile_name(keyFile,['https://spreadsheets.google.com/feeds'])
client=gspread.authorize(credentials)

url_for_google_sheet="https://docs.google.com/spreadsheets/d/18rLmAROIsUgQ1LcmdJLn65Gt9TLQtm8wCk5_xAPZmBk/edit?usp=sharing"
sheet = client.open_by_url(url_for_google_sheet)
worksheet = sheet.get_worksheet(0)

print(worksheet.update_cell(2,2,3))