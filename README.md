# 📧 Email Sender Automation Script

A Python automation script that sends personalized emails to multiple recipients.
It reads subjects and email addresses from a structured text file and sends custom messages through Gmail SMTP.
Ideal for contacting professors, companies, or collaborators efficiently and securely.

---

## 🚀 Features

- 📄 Reads subjects and email addresses from a structured text file (`emails.txt`)
- 💬 Sends personalized messages for each subject
- 🔐 Uses environment variables to protect Gmail credentials
- ⏱ Adds a small delay between emails to avoid spam detection
- 🧩 Easily customizable message template

---
## 🛠️ Technologies Used

- Python 3.x

- smtplib for sending emails

- email.mime for email formatting

- dotenv for loading environment variables

  ---
## 🧠 Example of `emails.txt`

```text
SUJET: Quantification de l’incertitude et explicabilité des modèles multimodaux
EMAIL: mostafa.elhabo@univ-brest.fr

SUJET: Métaheuristiques pour les problèmes de tournées de véhicules
EMAIL: ala_eddine@utt.fr
