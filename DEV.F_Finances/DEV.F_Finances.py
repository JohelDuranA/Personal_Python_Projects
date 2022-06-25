#!/usr/bin/env python3

#Importar librerias
import streamlit as st
import yfinance as yf
from datetime import datetime


def local_css(file_name):
	with open(file_name) as f:
		st.sidebar.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
		
#Hoja de estilos
local_css("style.css")

#bucador
st.sidebar.title("""DEV.F Finances 📉""")

st.sidebar.text(""" TSLA: Tesla \n AAPL: Apple \n BTC-USD: Bitcoin \n ETH-USD: Ethereum""")

selected_stock = st.sidebar.text_input("Por favor ingrese un símbolo bursátil valido...", "TSLA")


button_clicked = st.sidebar.button("Buscar")
if button_clicked == "Buscar":
	main()
	
expander_bar = st.expander("About")
expander_bar.markdown("""
* **Librerias Python:** pandas, streamlit, yfinance, time.
* **Fuente de datos:** [Yahoo Finance](https://finance.yahoo.com/).
* **Creditos:** [Download Financial Dataset Using Yahoo Finance in Python | A Complete Guide](https://www.analyticsvidhya.com/blog/2021/06/download-financial-dataset-using-yahoo-finance-in-python-a-complete-guide/)  escrito por Arnab Mondal.
""")
	

def main():
	st.subheader("""Valor de cierre diario para """ + selected_stock)
	
	
	stock_data = yf.Ticker(selected_stock)
	
	stock_df = stock_data.history(period='1d', start='2021-10-31', end=None)

	st.line_chart(stock_df.Close)
	
	st.subheader("""Ultimo valor de cierre para """ + selected_stock)
	
	today = datetime.today().strftime('%Y-%m-%d')
	
	stock_lastprice = stock_data.history(period='1d', start=today, end=today)
	
	last_price = (stock_lastprice.Close)

	if last_price.empty == True:
		st.write("No hay información de momento 😢")
	else:
		st.write(last_price)
		
	
	
	st.sidebar.subheader("""¿Desea ver información adicional? 🧐""")
	
	
	
	
	actions = st.sidebar.checkbox("Acciones bursátiles")
	if actions:
		st.subheader("""Acciones bursátiles para """ + selected_stock)
		display_action = (stock_data.actions)
		if display_action.empty == True:
			st.write("No hay información de momento 😢")
		else:
			st.write(display_action)
			
	
	financials = st.sidebar.checkbox("Finanzas trimestrales")
	if financials:
		st.subheader("""**Finanzas trimestrales** para """ + selected_stock)
		display_financials = (stock_data.quarterly_financials)
		if display_financials.empty == True:
			st.write("No hay información de momento 😢")
		else:
			st.write(display_financials)
			
	
	major_shareholders = st.sidebar.checkbox("Accionistas institucionales")
	if major_shareholders:
		st.subheader("""**Accionistas institucionales** para """ + selected_stock)
		display_shareholders = (stock_data.institutional_holders)
		if display_shareholders.empty == True:
			st.write("No hay información de momento 😢")
		else:
			st.write(display_shareholders)
			
	
	balance_sheet = st.sidebar.checkbox("Hoja de balance trimestral")
	if balance_sheet:
		st.subheader("""**Hoja de balance trimestral** para """ + selected_stock)
		display_balancesheet = (stock_data.quarterly_balance_sheet)
		if display_balancesheet.empty == True:
			st.write("No hay información de momento 😢")
		else:
			st.write(display_balancesheet)
			
	
	cashflow = st.sidebar.checkbox("Flujo de caja trimestral")
	if cashflow:
		st.subheader("""**Flujo de caja trimestral** para """ + selected_stock)
		display_cashflow = (stock_data.quarterly_cashflow)
		if display_cashflow.empty == True:
			st.write("No hay información de momento 😢")
		else:
			st.write(display_cashflow)
			
	
	earnings = st.sidebar.checkbox("Resultados trimestrales")
	if earnings:
		st.subheader("""**Resultados trimestrales** para """ + selected_stock)
		display_earnings = (stock_data.quarterly_earnings)
		if display_earnings.empty == True:
			st.write("No hay información de momento 😢")
		else:
			st.write(display_earnings)
			
	
	analyst_recommendation = st.sidebar.checkbox("Recomendación de los analistas")
	if analyst_recommendation:
		st.subheader("""**Recomendación de los analistas** para """ + selected_stock)
		display_analyst_rec = (stock_data.recommendations)
		if display_analyst_rec.empty == True:
			st.write("No hay información de momento 😢")
		else:
			st.write(display_analyst_rec)
			
if __name__ == "__main__":
	main()