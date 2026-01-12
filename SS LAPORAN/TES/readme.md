## 🚀 Tools Kuliah (`autoss.py`)
Script ini dapat mengubah screenshot praktikum menjadi kode LaTeX secara instan.

**Persiapan:**
1. Pastikan script `autoss.py` ada di folder kerja.
2. Atur **ShareX** agar nama file otomatis menjadi `step-%i` (Contoh hasil: `step-1.png`, `step-2.png`).

**Cara Pakai:**
1. Lakukan screenshot langkah praktikum (file akan tersimpan otomatis).
2. Buat file `langkah.txt` dan tulis deskripsi dengan format pemisah `|`:
   ```text
   Judul Gambar | Penjelasan panjang langkah tersebut...
   Input Data | Klik menu File > Import Data...
3. Buka terminal dan jalankan:
   ```text
   python autoss.py
5. Salin output terminal ke editor LaTeX Anda.

Repo ini dibuat untuk mempercepat pengerjaan laporan.
