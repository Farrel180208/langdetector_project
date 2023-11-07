import tkinter as tk
from langdetect import detect
from googletrans import Translator, constants
import spacy

# Muat model bahasa spaCy yang sesuai (misalnya, bahasa Inggris)
nlp = spacy.load('en_core_web_sm')

def get_language_name(language_code):
    language_names = {
        'id': 'Bahasa Indonesia',
        'en': 'Bahasa Inggris',
        'de': 'Bahasa Jerman',
        'es': 'Bahasa Spanyol',
        'fr': 'Bahasa Perancis',
        'zh-cn': 'Bahasa Mandarin',
    }
    return language_names.get(language_code, 'Bahasa lain')

def get_welcome_message(language_code):
    welcome_messages = {
        'id': 'Selamat datang! Anda berbicara dalam Bahasa Indonesia 🇮🇩',
        'en': 'Welcome! You are speaking in English 🇺🇸',
        'de': 'Willkommen! Sie sprechen Deutsch 🇩🇪',
        'es': '¡Bienvenido! Estás hablando en español 🇪🇸',
        'fr': 'Bienvenue! Vous parlez en français 🇫🷪',
        'zh-cn': '欢迎！您正在使用中文 🇨🇳',
    }
    return welcome_messages.get(language_code, 'Welcome! You are speaking in an unknown language 🌐')

def detect_language():
    text = entry.get()
    detected_language = detect(text)
    language_name = get_language_name(detected_language)
    welcome_message = get_welcome_message(detected_language)
    result_label.config(text=f"Detected language: {language_name}")
    welcome_label.config(text=welcome_message)

    # Tambahkan bahasa yang terdeteksi ke dalam daftar riwayat
    detected_languages_list.insert(0, f"{text} -> {language_name}")

    # Terjemahkan teks ke bahasa Inggris (contoh)
    translator = Translator()
    translation = translator.translate(text, src=detected_language, dest='en')
    translation_text = translation.text

    # Periksa dan berikan saran perbaikan pada tata bahasa dan kosakata menggunakan spaCy
    doc = nlp(translation_text)
    corrected_text = ' '.join(token.text_with_ws if token.text != token.text_with_ws else token.text for token in doc)

    translation_result_label.config(text=f"Translation (to English with corrections): {corrected_text}")

app = tk.Tk()
app.title("Language Detector App")

# Gaya font besar
font_style = ('Arial', 18)

entry_label = tk.Label(app, text="Enter text:", font=font_style)
entry_label.pack()

entry = tk.Entry(app, font=font_style)
entry.pack()

detect_button = tk.Button(app, text="Detect Language", command=detect_language, font=font_style)
detect_button.pack()

result_label = tk.Label(app, text="", font=font_style)
result_label.pack()

welcome_label = tk.Label(app, text="", font=font_style)
welcome_label.pack()

# Tambahkan Listbox untuk menampilkan riwayat bahasa
detected_languages_list = tk.Listbox(app, font=font_style, width=70)
detected_languages_list.pack()

# Tambahkan label untuk hasil terjemahan
translation_result_label = tk.Label(app, text="", font=font_style, wraplength=600)
translation_result_label.pack()

app.mainloop()
