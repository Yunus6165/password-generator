import string
import random
import customtkinter as ctk
import pyperclip

# Design-Einstellungen festlegen
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Hauptfenster erstellen
app = ctk.CTk()
app.title("Passwort Generator")
app.geometry("400x550")
app.resizable(False, False)

# --- BACKEND LOGIK ---
def passwoerter_generieren():
    pool = {
        "lowercase": string.ascii_lowercase,
        "uppercase": string.ascii_uppercase,
        "sonderzeichen": string.punctuation,
        "zahlen": string.digits
    }

    # Werte aus den Eingabefeldern auslesen (Standard: 0 falls leer)
    try:
        anz_gross = int(entry_gross.get() or 0)
        anz_klein = int(entry_klein.get() or 0)
        anz_zahlen = int(entry_zahlen.get() or 0)
        anz_sonder = int(entry_sonder.get() or 0)
        anz_vorschlaege = int(entry_vorschlaege.get() or 1)
    except ValueError:
        textbox_ergebnis.configure(state="normal")
        textbox_ergebnis.delete("1.0", ctk.END)
        textbox_ergebnis.insert("1.0", "Bitte nur Zahlen eingeben!")
        textbox_ergebnis.configure(state="disabled")
        return

    ergebnisse = []

    for j in range(anz_vorschlaege):
        zeichen_liste = []

        for _ in range(anz_gross):
            zeichen_liste.append(random.choice(pool["uppercase"]))
        for _ in range(anz_klein):
            zeichen_liste.append(random.choice(pool["lowercase"]))
        for _ in range(anz_zahlen):
            zeichen_liste.append(random.choice(pool["zahlen"]))
        for _ in range(anz_sonder):
            zeichen_liste.append(random.choice(pool["sonderzeichen"]))

        if not zeichen_liste:
            textbox_ergebnis.configure(state="normal")
            textbox_ergebnis.delete("1.0", ctk.END)
            textbox_ergebnis.insert("1.0", "Bitte mindestens 1 Zeichen wählen.")
            textbox_ergebnis.configure(state="disabled")
            return

        random.shuffle(zeichen_liste)
        ergebnisse.append("".join(zeichen_liste))

    # Ergebnis in der Textbox anzeigen
    textbox_ergebnis.configure(state="normal")
    textbox_ergebnis.delete("1.0", ctk.END)
    for i, pw in enumerate(ergebnisse, 1):
        textbox_ergebnis.insert(ctk.END, f"{i}. {pw}\n")
    textbox_ergebnis.configure(state="disabled")

def erstes_passwort_kopieren():
    inhalte = textbox_ergebnis.get("1.0", ctk.END).strip().split("\n")
    if inhalte and inhalte[0] and not inhalte[0].startswith("Bitte"):
        # Entfernt die Nummerierung (z. B. "1. ") vor dem Kopieren
        reines_passwort = inhalte[0].split(". ", 1)[-1]
        pyperclip.copy(reines_passwort)
        btn_copy.configure(text="Kopiert!")
        app.after(1500, lambda: btn_copy.configure(text="Erstes PW kopieren"))

# --- OBERFLÄCHE (GUI) BUILDEN ---
label_titel = ctk.CTkLabel(app, text="Passwort Generator", font=("Arial", 20, "bold"))
label_titel.pack(pady=15)

# Input-Felder
# Input-Felder
def erstelle_input_zeile(text_label, standard_wert):
    frame = ctk.CTkFrame(app, fg_color="transparent")
    frame.pack(fill="x", padx=20, pady=4)  # Hier padx statt px
    
    lbl = ctk.CTkLabel(frame, text=text_label, width=180, anchor="w")
    lbl.pack(side="left")
    
    entry = ctk.CTkEntry(frame, width=60)
    entry.insert(0, str(standard_wert))
    entry.pack(side="right")
    return entry

entry_gross = erstelle_input_zeile("Großbuchstaben:", 2)
entry_klein = erstelle_input_zeile("Kleinbuchstaben:", 6)
entry_zahlen = erstelle_input_zeile("Zahlen:", 2)
entry_sonder = erstelle_input_zeile("Sonderzeichen:", 2)
entry_vorschlaege = erstelle_input_zeile("Anzahl Vorschläge:", 3)

# Buttons
btn_generate = ctk.CTkButton(app, text="Passwörter Generieren", command=passwoerter_generieren, font=("Arial", 14, "bold"))
btn_generate.pack(pady=15)

# Ausgabefeld
textbox_ergebnis = ctk.CTkTextbox(app, width=340, height=120)
textbox_ergebnis.pack(pady=5)
textbox_ergebnis.configure(state="disabled")

btn_copy = ctk.CTkButton(app, text="Erstes PW kopieren", command=erstes_passwort_kopieren, fg_color="gray")
btn_copy.pack(pady=10)

# App starten
app.mainloop()