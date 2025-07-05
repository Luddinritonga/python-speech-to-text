# 🎤 Aplikasi Pengenalan Suara (Speech-to-Text Bahasa Indonesia)

Aplikasi desktop berbasis Python yang memungkinkan pengguna merekam suara dan mengonversinya menjadi teks secara real-time. Hasil teks ditampilkan di layar dan otomatis disimpan ke dalam file Microsoft Word (`hasil_suara.docx`). Aplikasi ini menggunakan antarmuka Tkinter dan mendukung Bahasa Indonesia.

---

## 🧩 Fitur Utama

- 🎙️ Merekam suara dari microphone
- 📝 Mengubah suara menjadi teks dengan Google Speech Recognition
- 📄 Menyimpan hasil ke file Word (`.docx`)
- 🪟 Antarmuka GUI menggunakan Tkinter
- ✅ Tombol untuk mulai, stop, dan keluar

---

## 📁 Struktur Proyek

speech-to-text-app/
├── main.py # File utama aplikasi
├── main1.py # File utama aplikasi
├── main2.py # File utama aplikasi
├── README.md # Dokumentasi ini
├── requirements.txt # Dependensi Python

#menginstall library di terminal
pip install -r requirements.txt
pip install speechrecognition
pip install python-docx
pip install pyaudio

jika gagal
    pip install pipwin
    pipwin install pyaudio

#menjalankan proyek di terminal
python main.py
python main1.py
python main2.py

💻 Teknologi yang Digunakan
Python 3.x
Tkinter (GUI)
SpeechRecognition
PyAudio
python-docx
Threading (untuk menjaga UI tetap responsif saat merekam)

##Author##
**Luddin ritonga**  
GitHub: [github.com/luddinritonga](https://github.com/Luddinritonga)  
Email: Luddinritonga1@gmail.com