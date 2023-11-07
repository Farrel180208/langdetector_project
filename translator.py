from googletrans import Translator

def main():
    translator = Translator()
    
    while True:
        text = input("Masukkan teks Bahasa Indonesia (atau ketik 'keluar' untuk keluar): ")
        
        if text.lower() == 'keluar':
            break
        
        translated_text_en = translator.translate(text, src='id', dest='en')
        translated_text_de = translator.translate(text, src='id', dest='de')
        translated_text_zh = translator.translate(text, src='id', dest='zh-CN')
        translated_text_es = translator.translate(text, src='id', dest='es')
        
        print(f"Terjemahan ke Bahasa Inggris: {translated_text_en.text}")
        print(f"Terjemahan ke Bahasa Jerman: {translated_text_de.text}")
        print(f"Terjemahan ke Bahasa Mandarin: {translated_text_zh.text}")
        print(f"Terjemahan ke Bahasa Spanyol: {translated_text_es.text}")

if __name__ == "__main__":
    main()
