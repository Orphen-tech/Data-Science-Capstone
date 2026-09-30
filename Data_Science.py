import fitz  # PyMuPDF
import sqlite3

# 1. Modifica del Database SQLite
db_path = "spacex.db"  # Sostituisci con il percorso del tuo file .db / .sqlite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Aggiornamento di tutti i record nella tabella SPACEXTABLE
cursor.execute("UPDATE SPACEXTABLE SET Customer = 'Fabio Della Porta';")
conn.commit()

print(f"Record aggiornati con successo nel DB SQLite: {cursor.rowcount}")

# (Opzionale) Verifica delle modifiche
cursor.execute("SELECT Date, Payload, Customer FROM SPACEXTABLE LIMIT 5;")
for row in cursor.fetchall():
    print(row)

conn.close()

# 2. Modifica del file PDF di presentazione (se presente)
pdf_path = "Capstone Presentation.pdf"
try:
    doc = fitz.open(pdf_path)
    for page in doc:
        text_instances = page.search_for("TREVOR WHITESIDE")
        for inst in text_instances:
            # Copre il vecchio nome e inserisce il nuovo
            page.add_redact_annot(inst, fill=(1, 1, 1))
            page.apply_redactions()
            page.insert_text(inst.tl, "FABIO DELLA PORTA", fontsize=12)

    doc.save("Capstone_Presentation_Fabio_Della_Porta.pdf")
    print("Presentazione PDF aggiornata con successo!")
except Exception as e:
    print(f"Nota sul PDF: {e}")
