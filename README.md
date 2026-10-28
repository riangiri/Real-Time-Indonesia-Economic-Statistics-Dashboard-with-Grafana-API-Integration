# Real-Time Indonesia Economic Statistics Dashboard with Grafana API Integration-

Visit realtime dashboard : https://indostats.grafana.net/public-dashboards/b10df2e20cf5421b8dc73d4986935b42

Dashboard publik di Grafana Cloud yang memantau kurs rupiah, utang pemerintah, defisit APBN, indikator makroekonomi, harga minyak, IHSG, dan BI-Rate. Semua data berasal dari API gratis dan disambungkan melalui plugin Infinity, sehingga tidak diperlukan database atau server sendiri.

> **Status:** live and public (akan ada update beberapa hari kedepan)

## Contents
## 1. Dashboards at a glance

| Dashboard | Status | What it shows |
|---|---|---|
| **Kurs-dashboard** ("Indonesia Statistics Update") | Live, public | Rupiah exchange rates, government debt, APBN deficit, inflation, GDP growth, unemployment, oil prices
| **IHSG and foreign flow**

## 2. Data sources

Semua data menggunakan API gratis dan disambungkan melalui infinity plugin grafana

| Data source | Allowed host | Info|
|---|---|---|---|
| `infinity-Kurs-idr-USD-SGD` | `openexchangerates.org` | (free plan allows 1,000 requests a month) |
| `infinity-frankfurter` | `api.frankfurter.dev` | None | Update setiap 12 jam |
| `infinity-imf` | `www.imf.org` | None | Update setiap 24 jam |
| `infinity-worldbank` | `api.worldbank.org` | None | Update setiap 24 hours |
| `infinity-oilprice` | `api.oilpriceapi.com` | `Authorisasi: Token <key>` | Update setiap 24 hours |
| `APBN-Decifit-Gauge` | `Kemenkeu APBN-KITA` | No API hanya diolah manual berdasarkan pdf pemaparan paling update |
| `IHSG-Metrics` | `https://api.Zapi.ink` |
| `BI-rate` | `(https://www.bi.go.id/id/statistik/indikator/bi-rate.aspx)` | 

### APBN deficit 

- Untuk data APBN Deficit (Deficit APBN) Diolah secara manual berdasarkan pdf dari website APBN Kita.
- Skala pengukur: **Min `-3`**, **Maks `0`**, sehingga pengisian bertambah dari 0 menuju batas yang diizinkan di angka -3%.
- -3% Deficit ini adalah per tahun (**year to date**) -3% cap (Berdasarkan UU No. 17/2003) disebut sebagai legal limit untuk defisit APBN per tahun.

### IHSG-Metrics
- Untuk IHSG menggunakan API dari zapi
- Update data IHSG adalah harian (daily) max jam 17.00 wib
- Foreign flow adalah aliran dana asing
- Foreign buy adalah total nilai transaksi pembelian saham yang dilakukan oleh investor asing (baik perorangan maupun institusi dari luar negeri) di BEI dalam 1 hari bursa kerja.
- Foreign sell adalah total nilai transaksi penjualan saham yang dilakukan oleh investor asing (baik perorangan maupun institusi dari luar negeri) di BEI dalam 1 hari bursa kerja.
- Net foreign flow adalah selisih dari total transaksi asing untuk pembelian (foreign buy) dan penjualan (foreign sell) yang dilakukan oleh investor asing di BEI dalam periode 1 hari ini/sebelumnya. Apabila (-) artinya dihari yang sama lebih dominan tranksaksi asing jual dari pada beli begitupun sebaliknya.

## 3. Security notes

- API dan token hanya disimpan dalam pengaturan sumber data Infinity. Data tersebut tidak disertakan dalam URL panel, tangkapan layar, maupun file JSON yang diekspor.
- Sebelum menyimpan (commit) dasbor yang telah diekspor (melalui menu *Share*, lalu *Export*), periksa file JSON tersebut untuk memastikan tidak ada `apikey`, `app_id`, `Token`, atau alamat email Anda di dalamnya.
- Dasbor publik akan memicu request setiap kali ada pengunjung, sehingga durasi *cache* diatur cukup lama untuk menjaga kuota permintaan (*request quotas*).

## 4. How to reproduce

1. Buat akun Grafana Cloud .
2. Install Infinity plugin dan tambahkan data source API per row. Sesuaikan dengan **Security, Allowed hosts, key-api**.
3. Set Query TTL pada **Cache** tab.
4. Buat panel panel visualisasi dan isi query, tes setiap query di **Explore**.
5. Add Visualisasi panel dan text panel bisa dengan footnotes and sumber baru open new tab.
6. Publish public dashboard, dan siap tes link untuk dibuka di private browser.

## 5. Limitation
- Dikarenakan semua data diambil dari API dengan pricing free maka ada keterbatasan data yang diambil hingga waktu loading.
- Beberapa panel dashboard sedang dalam proses pembaruan, sehingga panel akan menampilkan 'No Data' untuk sementara waktu.

## Screenshots

for example :

<img width="1911" height="817" alt="image" src="https://github.com/user-attachments/assets/4d15e3ad-548f-46fa-a5f0-27d6b5de336b" />

<br>

<img width="1910" height="865" alt="image" src="https://github.com/user-attachments/assets/68d439fa-66bb-4f6b-9fab-e04c619e7f96" />

<br>

<img width="1911" height="937" alt="image" src="https://github.com/user-attachments/assets/34cddf8f-4f36-4ed2-bbf3-cc742961b95b" />


