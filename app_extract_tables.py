# app_extract_tables.py
import streamlit as st
import camelot
import json
import pandas as pd
import tempfile
import os

def extract_tables(pdf_path):
    tables = camelot.read_pdf(pdf_path, pages='all')
    all_data = [table.df.to_dict(orient='records') for table in tables]
    return all_data

st.set_page_config(page_title="PDF Table Extractor", layout="centered")
st.title("📄 Extract Tables from PDF")

uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_pdf:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_pdf.read())
        tmp_path = tmp.name

    with st.spinner("Extracting tables..."):
        try:
            result = extract_tables(tmp_path)
            st.success(f"✅ Extracted {len(result)} tables successfully.")
            
            for i, table in enumerate(result):
                df = pd.DataFrame(table)
                st.write(f"**Table {i+1}**")
                st.dataframe(df)

            json_str = json.dumps(result, indent=2, ensure_ascii=False)
            st.download_button("📥 Download JSON", data=json_str, file_name="extracted_tables.json", mime="application/json")
        except Exception as e:
            st.error(f"❌ Error: {e}")
