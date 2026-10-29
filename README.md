# Real-Time Indonesia Economic Statistics Dashboard with Grafana API Integration-

Visit realtime dashboard : https://indostats.grafana.net/public-dashboards/b10df2e20cf5421b8dc73d4986935b42

Dashboard publik di Grafana Cloud yang memantau kurs rupiah, utang pemerintah, defisit APBN, indikator makroekonomi, harga minyak, IHSG, dan BI-Rate. 
Semua data berasal dari API gratis dan disambungkan melalui plugin Infinity, sehingga tidak diperlukan database atau server sendiri.

> **Status:** live and public (akan ada update dalam beberapa hari kedepan)

## Contents
## 1. Gambaran Dashboard

| Dashboard | Status | Isi |
|---|---|---|
| **Kurs-dashboard** ("Indonesia Statistics Update") | Live, publik | Kurs rupiah, utang pemerintah, defisit APBN, inflasi, pertumbuhan PDB, pengangguran, harga minyak, BI-Rate |
| **IHSG dan foreign flow** | Live, publik | Harga dan pergerakan IHSG serta aliran dana asing di BEI |
| **Commodities and Geopolitics** | Coming soon | Coming soon |

## 2. Data sources

Semua data menggunakan API gratis dan disambungkan melalui infinity plugin grafana
Setiap data source hanya mengizinkan hostnya sendiri, dan kredensial disimpan di pengaturan data source, bukan di URL panel.

| Data source | Allowed host | Autentikasi | Refresh data | Keterangan |
|---|---|---|---|---|
| `infinity-Kurs-idr-USD-SGD` | `openexchangerates.org` | App ID (tersimpan di data source) | Cache panjang | Paket gratis: pembaruan per jam, basis USD, 1.000 permintaan per bulan |
| `infinity-frankfurter` | `api.frankfurter.dev` | Tidak ada | 12 jam | Kurs referensi ECB, terbit sekali per hari kerja |
| `infinity-imf` | `www.imf.org` | Tidak ada | 24 jam | Diperbarui IMF 2 kali setahun; tahun terbaru berupa estimasi |
| `infinity-worldbank` | `api.worldbank.org` | Tidak ada | 24 jam | Data tahunan dengan jeda satu sampai dua tahun |
| `infinity-oilprice` | `api.oilpriceapi.com` | Header `Authorization: Token <key>` | 24 jam | Harga front-month futures (bukan harga spot harian) |
| `APBN-Deficit-Gauge` | Tidak ada API | Tidak ada | Manual | Diolah manual dari PDF APBN KiTa terbaru (data inline) https://www.kemenkeu.go.id/apbnkita |
| `IHSG-Metrics` | `api.zapi.ink` | Api-key (ada) | Harian | Layanan pihak ketiga, bukan feed resmi BEI |
| `BI-Rate` | `www.bi.go.id` | Tidak ada | - | [Halaman indikator BI-Rate](https://www.bi.go.id/id/statistik/indikator/bi-rate.aspx) |

### APBN deficit 

- Data defisit APBN diolah secara manual berdasarkan PDF APBN KiTa dari Kementerian Keuangan, karena tidak tersedia API gratis.
- Skala pengukur: **Min `-3`**, **Maks `0`**, sehingga pengisian bertambah dari 0 menuju batas maksimal yang diizinkan di angka -3%.
- Angka yang ditampilkan adalah akumulasi tahun berjalan (**year to date**). Batas defisit 3% terhadap PDB (UU No. 17 Tahun 2003 tentang Keuangan Negara) berlaku untuk satu tahun penuh.
- Angka terbaru bersifat sementara dan dapat direvisi.

### IHSG-Metrics
- Data IHSG menggunakan API dari zapi
- Update data IHSG adalah harian (daily) max jam 17.00 wib
- **Foreign flow** adalah aliran dana investor asing di Bursa Saham BEI
- **Foreign buy** adalah total nilai transaksi pembelian saham yang dilakukan oleh investor asing (baik perorangan maupun institusi dari luar negeri) di BEI dalam 1 hari bursa kerja.
- **Foreign sell** adalah total nilai transaksi penjualan saham yang dilakukan oleh investor asing (baik perorangan maupun institusi dari luar negeri) di BEI dalam 1 hari bursa kerja.
- **Net foreign flow** adalah selisih dari total transaksi asing untuk pembelian (foreign buy) dan penjualan (foreign sell) yang dilakukan oleh investor asing di BEI dalam periode 1 hari ini/sebelumnya. Apabila negatif (-) artinya dihari yang sama lebih dominan transaksi asing jual dari pada beli begitupun sebaliknya.

## 3. Security notes

- API dan token hanya disimpan dalam pengaturan sumber data Infinity. Data tersebut tidak disertakan dalam URL panel, tangkapan layar, maupun file JSON yang diekspor.
- Sebelum menyimpan (commit) dasbor yang telah diekspor (melalui menu *Share*, lalu *Export*), periksa file JSON tersebut untuk memastikan tidak ada `apikey`, `app_id`, `Token`, atau alamat email Anda di dalamnya.
- Dasbor publik akan memicu request setiap kali ada pengunjung, sehingga durasi *cache* diatur cukup lama untuk menjaga kuota permintaan (*request quotas*).

## 4. How to reproduce

1. Buat akun Grafana Cloud .
2. Install Infinity plugin, lalu tambahkan data source API per row. Sesuaikan dengan **Security, Allowed hosts, key-api**.
3. Set Query TTL pada **Cache** tab.
4. Buat panel panel visualisasi dan isi query, tes setiap query di **Explore**.
5. Add Visualisasi panel dan text panel bisa dengan footnotes and sumber baru open new tab.
6. Publish public dashboard, dan buka publik link untuk diuji di private browser/browser lainnya.

## 5. Limitation
- Semua data diambil dari API dengan paket gratis, sehingga ada batas jumlah permintaan, frekuensi pembaruan, dan waktu muat panel (loading) bisa lebih lama.
- Beberapa panel dashboard sedang dalam proses pembaruan, sehingga panel hanya menampilkan 'No Data' untuk sementara waktu.

## Screenshots

for example :

<img width="1911" height="817" alt="image" src="https://github.com/user-attachments/assets/4d15e3ad-548f-46fa-a5f0-27d6b5de336b" />
</p>
<br>
<img width="1910" height="865" alt="image" src="https://github.com/user-attachments/assets/68d439fa-66bb-4f6b-9fab-e04c619e7f96" />
</p>
<br>
<img width="1911" height="937" alt="image" src="https://github.com/user-attachments/assets/34cddf8f-4f36-4ed2-bbf3-cc742961b95b" />


