import streamlit as st
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1MC2iJ-04NHLs2SfVl0A3qy7qMbH0FiIPPjSKR1Al25E'

def authenticate():
    service_account_info = st.secrets["google_service_account"]
    creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
    return gspread.authorize(creds)

def read_data():
    gc = authenticate()
    sh = gc.open_by_key(SPREADSHEET_ID)
    worksheet = sh.worksheet("Gastos")  # Nome da aba no Google Sheets
    data = worksheet.get_all_records()
    return pd.DataFrame(data)

def append_data(row):   
    gc = authenticate()
    sh = gc.open_by_key(SPREADSHEET_ID)
    worksheet = sh.worksheet("Gastos")
    worksheet.append_row(row)

def update_pago_linha(index, novo_valor):
    gc = authenticate()
    sh = gc.open_by_key(SPREADSHEET_ID)
    worksheet = sh.worksheet("Gastos")  # Atualiza na aba correta
    col_pago = 5  # Supondo que a coluna "Pago" é a quinta (E)
    worksheet.update_cell(index + 2, col_pago, novo_valor)

def delete_linha(index):
    gc = authenticate()
    sh = gc.open_by_key(SPREADSHEET_ID)
    worksheet = sh.worksheet("Gastos")
    worksheet.delete_rows(index + 2)
