## 📦 Requirements
Sebelum menjalankan tools di repo ini, install library berikut:
```bash
pip install pandas numpy ppigrf
```

## 🧲 IGRF Calculator (`igrf.py`)
Script untuk melakukan perhitungan nilai medan magnet referensi (IGRF-13) secara otomatis (batch processing) berdasarkan data koordinat dan waktu. Berguna untuk tahap koreksi IGRF pada pengolahan data metode Geomagnetik.

**Fitur:**
- **Auto-Calculation**: Menghitung komponen medan utama (F, H, Z) serta Deklinasi dan Inklinasi.
- **Batch Processing**: Mampu membaca file input (CSV/Excel) berisi ratusan titik ukur sekaligus.
- **Custom Elevation**: Mendukung perhitungan pada elevasi yang berbeda-beda (topografi).

**Cara Pakai:**
1. Siapkan file data (CSV) yang memiliki kolom: `Latitude`, `Longitude`, `Elevation`, dan `Date`.
2. Sesuaikan nama file input di dalam script `igrf_calc.py`.
3. Jalankan script:
   ```bash
   python igrf_calc.py
4. Output akan disimpan sebagai file CSV baru dengan tambahan kolom nilai IGRF.
