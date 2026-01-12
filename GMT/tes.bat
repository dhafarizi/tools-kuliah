REM Ini adalah Komentar
REM Format: gmt begin [NamaOutput] [Format]

gmt begin peta_indonesia png
    
    REM Menggambar Peta Dasar (Coast)
    REM -R: Region (Batas Koordinat Barat/Timur/Selatan/Utara) -> Indonesia
    REM -J: Projection (Jenis Proyeksi). M = Mercator. 20c = Lebar peta 20 cm.
    REM -B: Border (Bingkai). a = Auto update angka koordinat. f = Frame.
    REM -G: Ground (Warna Darat). Coklat tanah.
    REM -S: Sea (Warna Laut). Biru muda.
    REM -W: Pen (Garis Pantai). 0.5 point, warna hitam.
    
    gmt coast -R90/145/-15/10 -JM20c -Baf -Gsienna -Slightblue -W0.5p,black

gmt end show