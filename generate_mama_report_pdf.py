import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class MamaReportPDF(FPDF):
    def header(self):
        # Top banner: Gold accent
        self.set_fill_color(184, 138, 23) # Gold 600
        self.rect(0, 0, 210, 6, 'F')
        
        self.set_y(12)
        self.set_font('Helvetica', 'B', 15)
        self.set_text_color(20, 20, 20)
        self.cell(130, 8, 'LAPORAN SISTEM WEB MANAGEMENT ARTIS', new_x=XPos.RIGHT, new_y=YPos.TOP)
        
        self.set_font('Helvetica', 'B', 9.5)
        self.set_text_color(184, 138, 23)
        self.cell(60, 8, 'STATUS: SELESAI & ONLINE (100%)', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='R')
        
        self.set_font('Helvetica', '', 8.5)
        self.set_text_color(100, 100, 100)
        self.cell(130, 4, 'Dokumentasi Sistem Agensi & Manajemen Artis Mega Bintang Indonesia', new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.cell(60, 4, '2 November 2026', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='R')
        
        self.set_draw_color(210, 210, 210)
        self.set_line_width(0.3)
        self.line(10, 28, 200, 28)
        self.ln(5)

    def footer(self):
        self.set_y(-18)
        self.set_draw_color(220, 220, 220)
        self.set_line_width(0.3)
        self.line(10, 280, 200, 280)
        
        self.set_font('Helvetica', '', 8)
        self.set_text_color(140, 140, 140)
        self.cell(0, 5, 'Mega Bintang Artist Management - Official Agency System Report', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

pdf = MamaReportPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False)

# ==================== PAGE 1 ===================
pdf.add_page()
pdf.set_y(32)

# Item 1: Branding, Header Kontak, & Jalur Satu Pintu
pdf.set_fill_color(250, 248, 242)
pdf.set_draw_color(225, 215, 190)
pdf.rect(10, 32, 190, 115, 'DF')

pdf.set_xy(14, 35)
pdf.set_font('Helvetica', 'B', 10.5)
pdf.set_text_color(160, 115, 15)
pdf.cell(180, 6, '1. Standar Branding Agensi Resmi, Kontak Hotline, & Jalur 1 Pintu', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Image 1 (Left)
img1 = "/home/hermesagent/obsidian-vault/projects/report_assets_mama/annotated_hero.jpg"
pdf.image(img1, x=14, y=43, w=62)

# Details (Right)
pdf.set_xy(80, 43)
pdf.set_font('Helvetica', 'B', 8.5)
pdf.set_text_color(40, 40, 40)
pdf.cell(115, 5, 'Kebutuhan Agensi & Standar Representasi:', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(80)
pdf.set_font('Helvetica', 'I', 8)
pdf.set_text_color(80, 80, 80)
pdf.multi_cell(115, 4.2, 'Website harus tampil elegan, berwibawa, dan profesional untuk meyakinkan klien korporat, BUMN, dan penyelenggara festival.')

pdf.ln(1.5)
pdf.set_x(80)
pdf.set_font('Helvetica', 'B', 8.5)
pdf.set_text_color(40, 40, 40)
pdf.cell(115, 5, 'Penyempurnaan Visual & Identitas:', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(80)
pdf.set_font('Helvetica', '', 8)
pdf.set_text_color(70, 70, 70)
pdf.multi_cell(115, 4, 'Desain menggunakan konsep "Dark Luxury & Gold" khas agensi hiburan internasional. Seluruh identitas non-korporat dibersihkan, nomor hotline resmi (+62 882-1241-4791) diposisikan di header utama (kotak merah).')

pdf.ln(1.5)
pdf.set_x(80)
pdf.set_font('Helvetica', 'B', 8.5)
pdf.set_text_color(160, 115, 15)
pdf.cell(115, 5, 'Fitur Utama yang Diterapkan:', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(80)
pdf.set_font('Helvetica', '', 8)
pdf.set_text_color(40, 40, 40)
pdf.multi_cell(115, 3.8, 
    '[v] Top Announcement Bar resmi terhubung langsung ke Hotline WhatsApp 0882-1241-4791.\\n'\
    '[v] Indikator Kredibilitas: 50+ Roster Artis, 300+ Event, 100% SPK Legalitas Resmi.\\n'\
    '[v] Jalur Satu Pintu (Direct Booking): Bebas calo berantai, jaminan kontrak transparan.')


# Item 2: Roster Artis & Filter Kategori
pdf.set_fill_color(250, 248, 242)
pdf.set_draw_color(225, 215, 190)
pdf.rect(10, 152, 190, 115, 'DF')

pdf.set_xy(14, 155)
pdf.set_font('Helvetica', 'B', 10.5)
pdf.set_text_color(160, 115, 15)
pdf.cell(180, 6, '2. Roster Artis Multi-Genre (Dangdut, Pop, MC TV, Religi, Komedian)', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Image 2 (Left)
img2 = "/home/hermesagent/obsidian-vault/projects/report_assets_mama/annotated_roster.jpg"
pdf.image(img2, x=14, y=163, w=62)

# Details (Right)
pdf.set_xy(80, 163)
pdf.set_font('Helvetica', 'B', 8.5)
pdf.set_text_color(40, 40, 40)
pdf.cell(115, 5, 'Katalog Pengisi Acara Lengkap:', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(80)
pdf.set_font('Helvetica', 'I', 8)
pdf.set_text_color(80, 80, 80)
pdf.multi_cell(115, 4.2, 'Menyediakan pilihan talenta lengkap agar pihak Event Organizer (EO) dapat langsung memilih artis yang relevan dengan tema acara.')

pdf.ln(1.5)
pdf.set_x(80)
pdf.set_font('Helvetica', 'B', 8.5)
pdf.set_text_color(40, 40, 40)
pdf.cell(115, 5, 'Kategori & Kartu Interaktif:', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(80)
pdf.set_font('Helvetica', '', 8)
pdf.set_text_color(70, 70, 70)
pdf.multi_cell(115, 4, 'Tab filter kategori (kotak merah) membagi talenta menjadi Dangdut Koplo, Pop & Band, MC Presenter TV, Religi, serta Komedian dengan spacing kartu yang rapi dan terstruktur.')

pdf.ln(1.5)
pdf.set_x(80)
pdf.set_font('Helvetica', 'B', 8.5)
pdf.set_text_color(160, 115, 15)
pdf.cell(115, 5, 'Direct Booking Action:', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(80)
pdf.set_font('Helvetica', '', 8)
pdf.set_text_color(40, 40, 40)
pdf.multi_cell(115, 3.8, 
    '[v] Profil Bintang: Fahmi Shahab (Kopi Dangdut), Rani Pop Lawas, All Stars Pantura, MC TV.\\n'\
    '[v] Tombol "Booking Artis Ini": Membuka chat WhatsApp dengan draf pesan otomatis menyebutkan nama artis yang dipilih.\\n'\
    '[v] Label Ketersediaan: Setiap kartu dilengkapi indikator status "Siap Booking".')


# ==================== PAGE 2 ===================
pdf.add_page()
pdf.set_y(32)

# Item 3: Tampilan Mobile di HP & Spacing Lega
pdf.set_fill_color(250, 248, 242)
pdf.set_draw_color(225, 215, 190)
pdf.rect(10, 32, 190, 105, 'DF')

pdf.set_xy(14, 35)
pdf.set_font('Helvetica', 'B', 10.5)
pdf.set_text_color(160, 115, 15)
pdf.cell(180, 6, '3. Tata Letak Responsif & Spacing Lega (Optimal di Layar Smartphone)', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Image 3 (Left)
img3 = "/home/hermesagent/obsidian-vault/projects/report_assets_mama/annotated_mobile.jpg"
pdf.image(img3, x=22, y=43, w=46)

# Details (Right)
pdf.set_xy(80, 43)
pdf.set_font('Helvetica', 'B', 8.5)
pdf.set_text_color(40, 40, 40)
pdf.cell(115, 5, 'Kenyamanan Akses Pengguna:', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(80)
pdf.set_font('Helvetica', 'I', 8)
pdf.set_text_color(80, 80, 80)
pdf.multi_cell(115, 4.2, 'Mayoritas calon klien mengakses website melalui link WhatsApp langsung di smartphone mereka.')

pdf.ln(1.5)
pdf.set_x(80)
pdf.set_font('Helvetica', 'B', 8.5)
pdf.set_text_color(40, 40, 40)
pdf.cell(115, 5, 'Perbaikan Jarak & Kerapian Visual:', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(80)
pdf.set_font('Helvetica', '', 8)
pdf.set_text_color(70, 70, 70)
pdf.multi_cell(115, 4, 'Seluruh elemen yang sebelumnya terlalu mepet telah diperbaiki dengan padding dan margin yang lebih lega dan proporsional (kotak merah). Teks tidak bertumpuk dan tombol aksi mudah dijangkau.')

pdf.ln(1.5)
pdf.set_x(80)
pdf.set_font('Helvetica', 'B', 8.5)
pdf.set_text_color(160, 115, 15)
pdf.cell(115, 5, 'Keunggulan Penggunaan:', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(80)
pdf.set_font('Helvetica', '', 8)
pdf.set_text_color(40, 40, 40)
pdf.multi_cell(115, 3.8, 
    '[v] Navigasi ringkas dengan tombol aksi cepat Hubungi WhatsApp di sudut kanan atas.\\n'\
    '[v] Waktu muat halaman sangat instan (<1 detik) tanpa script berat atau pop-up mengganggu.\\n'\
    '[v] Tampilan profesional di semua resolusi: Android, iPhone, tablet, hingga desktop.')


# Item 4: Form Request Jadwal
pdf.set_fill_color(250, 248, 242)
pdf.set_draw_color(225, 215, 190)
pdf.rect(10, 142, 190, 85, 'DF')

pdf.set_xy(14, 145)
pdf.set_font('Helvetica', 'B', 10.5)
pdf.set_text_color(160, 115, 15)
pdf.cell(180, 6, '4. Formulir Permintaan Jadwal & Reservasi Terintegrasi WhatsApp', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Image 4 (Left)
img4 = "/home/hermesagent/obsidian-vault/projects/report_assets_mama/annotated_form.jpg"
pdf.image(img4, x=22, y=153, w=46)

# Details (Right)
pdf.set_xy(80, 153)
pdf.set_font('Helvetica', 'B', 8.5)
pdf.set_text_color(40, 40, 40)
pdf.cell(115, 5, 'Efisiensi Penerimaan Data Klien:', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(80)
pdf.set_font('Helvetica', 'I', 8)
pdf.set_text_color(80, 80, 80)
pdf.multi_cell(115, 4.2, 'Panitia acara dapat langsung menyusun draft kebutuhan event secara teratur tanpa harus mengetik format dari nol.')

pdf.ln(1.5)
pdf.set_x(80)
pdf.set_font('Helvetica', 'B', 8.5)
pdf.set_text_color(160, 115, 15)
pdf.cell(115, 5, 'Fitur Form Terintegrasi:', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(80)
pdf.set_font('Helvetica', '', 8)
pdf.set_text_color(70, 70, 70)
pdf.multi_cell(115, 4, 'Formulir mencakup: Nama Pemesan/Instansi, Nomor WhatsApp, Pilihan Artis, Jenis Acara, Tanggal, dan Lokasi Kota (kotak merah).')

pdf.ln(1.5)
pdf.set_x(80)
pdf.set_font('Helvetica', 'B', 8.5)
pdf.set_text_color(160, 115, 15)
pdf.cell(115, 5, 'Output Otomatis:', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(80)
pdf.set_font('Helvetica', '', 8)
pdf.set_text_color(40, 40, 40)
pdf.multi_cell(115, 3.8, 
    '[v] Tombol submit merangkai pesan reservasi resmi dan membuka aplikasi WhatsApp.\\n'\
    '[v] Admin manajemen langsung menerima rincian acara lengkap untuk dicek ketersediaannya.\\n'\
    '[v] Mempercepat proses negosiasi dan pembuatan Surat Perjanjian Kerja (SPK).')


# Link Web Box (Bottom)
pdf.set_fill_color(254, 252, 240)
pdf.set_draw_color(217, 160, 24)
pdf.rect(10, 232, 190, 42, 'DF')

pdf.set_xy(14, 235)
pdf.set_font('Helvetica', 'B', 10.5)
pdf.set_text_color(160, 115, 15)
pdf.cell(180, 5, 'Tautan Resmi Website Management Artis (Sudah Aktif & Online):', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.set_x(14)
pdf.set_font('Helvetica', '', 8.5)
pdf.set_text_color(40, 40, 40)
pdf.multi_cell(180, 4.2, 
    'Website resmi telah aktif dan dipublikasikan secara langsung pada jaringan CDN publik:\\n\\n'\
    'Link Website: https://afridho-ikhsan.github.io/bintang-management-artis/\\n'\
    'Kode Sumber: https://github.com/afridho-ikhsan/bintang-management-artis\\n'\
    'Mega Bintang Artist Management | Official Booking Hotline: +62 882-1241-4791')

out_pdf = "/home/hermesagent/obsidian-vault/projects/Laporan_Website_Management_Artis_Mama.pdf"
pdf.output(out_pdf)
print("Updated Mama PDF report successfully created at:", out_pdf)
print("File size:", os.path.getsize(out_pdf), "bytes")
