import streamlit as st
from books_to_scrape import scrape_books
from cleaner import clean_data
from exporter import export_to_csv, export_to_excel
import pandas as pd

st.set_page_config(page_title="Data Harvester Pro", page_icon="icon.png", layout="wide")

st.title("Data Harvester Pro")
st.write("Scrape competitors data from website, cleans the data and download result instantly")

pages = st.number_input("Number of pages to scrape", min_value=1, max_value=10, value=2)

if st.button("run scrapper"):
    with st.spinner("scrapping in progress..."):
        raw_data = scrape_books(pages=pages)
        cleaned_df = clean_data(raw_data)

        st.success(f"scraped {len(cleaned_df)} products")
        st.dataframe(cleaned_df.head())

        export_to_csv(cleaned_df, "exports/books.csv")
        export_to_excel(cleaned_df, "exports/books.xlsx")

        st.metric("Total books", len(cleaned_df))
        st.metric("Average price", f"£{cleaned_df['price'].mean():.2f}")

        st.download_button("Download csv", data=cleaned_df.to_csv(index=False), file_name="books.csv")