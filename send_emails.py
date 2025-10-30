import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
# === CONFIGURATION ===
GMAIL_USER = "*********@gmail.com"
GMAIL_PASSWORD = "**********"  # à remplacer par ton mot de passe d'application Gmail
SUBJECT = "Recherche de sujet pour le projet de fin d'études - Master Ingénierie Logicielle"

# === MESSAGE DE BASE ===
BASE_MESSAGE = """Bonjour,"""

# === LECTURE DU FICHIER emails.txt ===
with open("emails.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Trouver toutes les paires SUJET/EMAIL avec regex
pairs = re.findall(r"SUJET:\s*(.*?)\s*EMAIL:\s*([\w\.-]+@[\w\.-]+)", content, re.DOTALL)

if not pairs:
    print("❌ Aucun sujet/email trouvé dans le fichier.")
    exit()

# === CONNEXION À GMAIL ===
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(GMAIL_USER, GMAIL_PASSWORD)
    print("✅ Connexion réussie à Gmail.\n")
except Exception as e:
    print("❌ Erreur de connexion :", e)
    exit()

# === ENVOI DES MAILS ===
for i, (subject_text, email) in enumerate(pairs, start=1):
    try:
        subject = f"Intérêt pour le sujet de PFE : {subject_text.strip()}"
        message = BASE_MESSAGE.format(subject=subject_text.strip())

        msg = MIMEMultipart()
        msg["From"] = GMAIL_USER
        msg["To"] = email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        server.sendmail(GMAIL_USER, email, msg.as_string())
        print(f"[{i}/{len(pairs)}] ✅ Email envoyé à {email} (sujet : {subject_text.strip()})")
        time.sleep(5)

    except Exception as e:
        print(f"[{i}/{len(pairs)}] ⚠️ Erreur avec {email}: {e}")

server.quit()
print("\n🎉 Tous les e-mails ont été envoyés avec succès !")