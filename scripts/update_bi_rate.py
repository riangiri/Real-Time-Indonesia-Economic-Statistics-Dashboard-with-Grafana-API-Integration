import json
import re
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

URL = "https://www.bi.go.id/id/statistik/indikator/bi-rate.aspx"
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "bi_rate.json"

MONTHS_ID = {
    "januari": 1,
    "februari": 2,
    "maret": 3,
    "april": 4,
    "mei": 5,
    "juni": 6,
    "juli": 7,
    "agustus": 8,
    "september": 9,
    "oktober": 10,
    "november": 11,
    "desember": 12,
}


def parse_indonesian_date(value):
    parts = value.strip().lower().split()
    if len(parts) != 3:
        raise ValueError(f"Format tanggal tidak dikenali: {value!r}")

    day = int(parts[0])
    month = MONTHS_ID.get(parts[1])
    year = int(parts[2])

    if month is None:
        raise ValueError(f"Nama bulan tidak dikenali: {parts[1]!r}")

    return f"{year:04d}-{month:02d}-{day:02d}"


def main():
    response = requests.get(
        URL,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/131.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        },
        timeout=30,
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    target_table = None

    for table in soup.find_all("table"):
        headers = " ".join(
            cell.get_text(" ", strip=True).lower()
            for cell in table.find_all(["th", "td"])[:12]
        )
        if "tanggal" in headers and "bi-rate" in headers:
            target_table = table
            break

    if target_table is None:
        raise RuntimeError(
            "Tabel BI Rate tidak ditemukan di HTML. "
            "Situs mungkin mengubah struktur halaman."
        )

    records = []
    for row in target_table.find_all("tr"):
        cells = row.find_all(["td", "th"], recursive=False)
        if len(cells) < 3:
            continue

        values = [cell.get_text(" ", strip=True) for cell in cells]
        if values[0].strip().lower() in {"no", "nomor"}:
            continue

        # Struktur tabel BI: No | Tanggal | BI-Rate | Pranala Siaran Pers
        date_text = values[1] if len(values) > 1 else ""
        rate_text = values[2] if len(values) > 2 else ""

        if not date_text or not rate_text:
            continue

        match = re.search(r"(\d+(?:[.,]\d+)?)", rate_text.replace(" ", ""))
        if not match:
            continue

        try:
            iso_date = parse_indonesian_date(date_text)
            rate = float(match.group(1).replace(",", "."))
        except (ValueError, TypeError):
            continue

        records.append({
            "date": iso_date,
            "rate": rate,
        })

    if not records:
        raise RuntimeError(
            "Tabel ditemukan tetapi tidak ada baris BI Rate yang bisa dibaca. "
            "JSON lama tidak diubah."
        )

    # Hilangkan duplikat berdasarkan tanggal, lalu urutkan dari tanggal terbaru.
    unique_records = {item["date"]: item for item in records}
    records = sorted(
        unique_records.values(),
        key=lambda item: item["date"],
        reverse=True,
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "source": "Bank Indonesia",
        "source_url": URL,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "note": (
            "Data yang diambil adalah baris yang tersedia pada tabel halaman "
            "BI Rate saat ini; halaman dapat menampilkan data per halaman."
        ),
        "data": records,
    }

    OUTPUT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Berhasil menyimpan {len(records)} baris BI Rate ke {OUTPUT}")
    print("Contoh data terbaru:", records[0])


if __name__ == "__main__":
    main()
