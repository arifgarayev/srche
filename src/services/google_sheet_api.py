from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import os


class GoogleSheet:
    # default

    scopes = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    service_account_file = os.path.dirname(os.getcwd()) + '/config/ServiceAccountToken.json'

    def __init__(self, sheet_id, worksheet_name):
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.service_account_file, GoogleSheet.scopes)

        self.service_sheets = build('sheets', 'v4', credentials=self.credentials)

        self.sheet_id = sheet_id
        self.worksheet_name = worksheet_name
        self.cell_range_insert = 'A4'


    def add_data(self, date, time, name,):
        ...
