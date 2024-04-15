# app.py

from flask import Flask, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GOOGLE_SHEETS_CONFIG

app = Flask(__name__)

# Google Sheets API credentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_dict(GOOGLE_SHEETS_CONFIG, scope)
client = gspread.authorize(creds)

# Fetch Google Form responses
def fetch_responses():
    sheet = client.open_by_url(GOOGLE_SHEETS_CONFIG['https://forms.gle/zxWJz7HwgWza9LoK9']).sheet1
    responses = sheet.get_all_records()
    return responses

@app.route('/')
def index():
    responses = fetch_responses()
    return render_template('index.html', responses=responses)

if __name__ == '__main__':
    app.run(debug=True)
