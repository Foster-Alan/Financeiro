import streamlit as st
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def authenticate():
    service_account_info = st.secrets["google_service_account"]
    creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
    return gspread.authorize(creds)

def get_sheet():
    gc = authenticate()
    sh = gc.open_by_key('1MC2iJ-04NHLs2SfVl0A3qy7qMbH0FiIPPjSKR1Al25E')
    return sh.worksheet("RendasFixas")

def read_rendas():
    sheet = get_sheet()
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    if 'Valor' in df.columns:
        df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce').fillna(0)
    return df

def append_renda(row):
    sheet = get_sheet()
    sheet.append_row(row)

def delete_renda(index):
    sheet = get_sheet()
    sheet.delete_rows(index + 2)  # +2: para considerar cabeçalho e index 0

def update_pago(index, novo_valor):
    sheet = get_sheet()
    cell = f"E{index + 2}"  # Coluna E = "Pago"
    sheet.update_acell(cell, novo_valor)
