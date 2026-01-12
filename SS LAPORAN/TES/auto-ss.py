import os

# --- KONFIGURASI LAPORAN ---
NAMA_FILE_TEKS = "langkah.txt"
PREFIX_GAMBAR  = "step"
EKSTENSI_IMG   = ".png"

# --- TEMPLATE LATEX ---
# {{GAMBAR}}  = akan diganti nama file (Step-1.png)
# {{CAPTION}} = akan diganti teks sebelah kiri tanda |
# {{LABEL}}   = akan diganti label otomatis
# {{TEKS}}    = akan diganti teks sebelah kanan tanda | (penjelasan)

template_latex = r"""
\item {{TEKS}}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\textwidth]{{{GAMBAR}}}
    \caption{{{CAPTION}}}
    \label{fig:{{LABEL}}}
\end{figure}
"""

def main():
    print("-" * 40)
    print("   GENERATOR LAPORAN PRAKTIKUM   ")
    print("-" * 40)

    try:
        # Buka file teks
        with open(NAMA_FILE_TEKS, "r", encoding="utf-8") as f:
            # Baca baris per baris, abaikan baris kosong
            lines = [line.strip() for line in f.readlines() if line.strip()]

        print(f"% Total Langkah: {len(lines)}")
        print("% Copy kode di bawah ini ke LaTeX editor Anda:\n")
        print("% ================= MULAI ================= \n")

        for i, line in enumerate(lines):
            nomor = i + 1
            nama_file_gambar = f"{PREFIX_GAMBAR}-{nomor}{EKSTENSI_IMG}"
            
            # Logika Pemisah "|"
            if "|" in line:
                parts = line.split("|")
                caption_singkat = parts[0].strip()
                penjelasan_full = parts[1].strip()
            else:
                # Fallback jika lupa pakai "|", caption & teks disamakan
                caption_singkat = line
                penjelasan_full = line

            # Isi Template
            kode = template_latex.replace("{{GAMBAR}}", nama_file_gambar)
            kode = kode.replace("{{CAPTION}}", caption_singkat)
            kode = kode.replace("{{TEKS}}", penjelasan_full)
            kode = kode.replace("{{LABEL}}", f"{PREFIX_GAMBAR}-{nomor}") # Label referensi
            
            print(kode)

        print("\n% ================= SELESAI =================")

    except FileNotFoundError:
        print(f"[ERROR] File '{NAMA_FILE_TEKS}' tidak ditemukan di folder ini!")
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()