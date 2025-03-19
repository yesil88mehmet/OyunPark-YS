
import csv

weekly_data = {
    "week": "2025-03-10 to 2025-03-16",
    "subscriptions": [
        {"name": "Ali", "type": "Gold", "price": 200},
        {"name": "Ay�e", "type": "Silver", "price": 150},
        {"name": "Mehmet", "type": "Bronze", "price": 100}
    ],
    "cancellations": [
        {"name": "Fatma", "type": "Gold", "refund": 180},
        {"name": "Hasan", "type": "Silver", "refund": 140}
    ],
    "events": [
        {"event_name": "Kukla G�sterisi", "date": "2025-03-12"},
        {"event_name": "�izgi Film G�n�", "date": "2025-03-15"}
    ],
    "group_visits": [
        {"group_name": "Anaokulu A", "date": "2025-03-13", "size": 30},
        {"group_name": "�lkokul B", "date": "2025-03-14", "size": 25}
    ]
}

total_sales = sum(sub["price"] for sub in weekly_data["subscriptions"])
total_refunds = sum(cancel["refund"] for cancel in weekly_data["cancellations"])
net_revenue = total_sales - total_refunds

def save_report_as_csv(data, filename="weekly_report.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["?? Haftal�k Rapor", data["week"]])
        writer.writerow([])
        writer.writerow(["?? Alinan Abonmanlar"])
        writer.writerow(["�sim", "T�r", "Fiyat"])
        writer.writerows([[sub["name"], sub["type"], sub["price"]] for sub in data["subscriptions"]])
        writer.writerow([])
        writer.writerow(["?? �ptal Edilen Abonmanlar"])
        writer.writerow(["�sim", "T�r", "�ade"])
        writer.writerows([[cancel["name"], cancel["type"], cancel["refund"]] for cancel in data["cancellations"]])
        writer.writerow([])
        writer.writerow(["?? Finansal Durum"])
        writer.writerow(["Toplam Sat��lar", total_sales])
        writer.writerow(["Toplam �adeler", total_refunds])
        writer.writerow(["Net Gelir", net_revenue])
        writer.writerow([])
        writer.writerow(["?? Etkinlikler"])
        writer.writerow(["Etkinlik Ad�", "Tarih"])
        writer.writerows([[event["event_name"], event["date"]] for event in data["events"]])
        writer.writerow([])
        writer.writerow(["?? Gelecek Gruplar"])
        writer.writerow(["Grup Ad�", "Tarih", "Ki�i Say�s�"])
        writer.writerows([[group["group_name"], group["date"], group["size"]] for group in data["group_visits"]])
    print(f"? Rapor '{filename}' olarak kaydedildi.")

save_report_as_csv(weekly_data)