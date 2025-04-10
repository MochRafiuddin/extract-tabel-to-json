# 🧾 PDF Table Extractor

A simple web-based tool to extract tables from PDF files using Camelot. Built with Python and Streamlit, this app provides two main features:

1. **Extract all tables** from a PDF and export as JSON.
2. **Merge tables with matching headers** and save as a single JSON file.

---

## 🚀 Features

✅ Upload PDF file  
✅ View and preview extracted tables  
✅ Download output as JSON  
✅ Merge logic for repeated headers (Page break handling)

---

## 🧰 Requirements

- Python 3.7+
- [Ghostscript](https://www.ghostscript.com/) (required for Camelot to read PDFs)

---

## 📦 Installation

1. Clone this repository or download the ZIP:
   ```bash
   git clone https://github.com/yourusername/pdf-table-extractor.git
   cd pdf-table-extractor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   - Extract tables only:
     ```bash
     streamlit run app_extract_tables.py
     ```
   - Merge tables with same headers:
     ```bash
     streamlit run app_merge_tables.py
     ```

---

## 📁 Output

- All output will be downloadable directly from the UI as `.json` files.
- You can open them in any JSON viewer or convert them to Excel if needed.

---

## 📸 Screenshots

Here is an example of the app in action:

![Table Extractor UI](images/screenshot1.png)

---

## 📃 License

MIT License – Free to use, modify, and distribute.

---

## ✨ Created By

Made with ❤️ using Python, Camelot, and Streamlit.
