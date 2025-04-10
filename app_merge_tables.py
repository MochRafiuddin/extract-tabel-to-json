# app_merge_tables.py
import streamlit as st
import camelot
import json
import pandas as pd
import tempfile
import os

def merge_tables_by_header(pdf_path):
    tables = camelot.read_pdf(pdf_path, pages='all')
    merged_data = []

    for table in tables:
        df = table.df
        current_data = df.to_dict(orient='records')

        if not current_data:
            continue

        if not merged_data:
            merged_data.append(current_data)
        else:
            last_data = merged_data[-1]
            if (len(last_data) >= 2 and len(current_data) >= 2 and
                last_data[0] == current_data[0] and last_data[1] == current_data[1]):
                merged_data[-1].extend(current_data[2:])
            else:
                merged_data.append(current_data)

    return merged_data

st.set_page_config(page_title="Merge PDF Tables", layout="centered")
st.title("🧩 Merge PDF Tables with Matching Headers")

uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_pdf:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_pdf.read())
        tmp_path = tmp.name

    with st.spinner("Processing..."):
        try:
            result = merge_tables_by_header(tmp_path)
            st.success(f"✅ Merged into {len(result)} tables successfully.")
            
            for i, table in enumerate(result):
                df = pd.DataFrame(table)
                st.write(f"**Table {i+1}**")
                st.dataframe(df)

            json_str = json.dumps(result, indent=2, ensure_ascii=False)
            st.download_button("📥 Download JSON", data=json_str, file_name="merged_tables.json", mime="application/json")
        except Exception as e:
            st.error(f"❌ Error: {e}")
