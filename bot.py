import requests
import json

def get_market_data():
    try:
        # دریافت قیمت لحظه‌ای بیت‌کوین از بایننس
        res = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
        data = res.json()
        
        market_stats = {
            "btc_price": float(data['price']),
            "update_time": "2026-04-01",
            "status": "Live Update"
        }
        
        with open("market_data.json", "w") as f:
            json.dump(market_stats, f)
        print("داده‌ها با موفقیت در فایل ذخیره شد.")
    except Exception as e:
        print(f"خطا در دریافت داده: {e}")

if __name__ == "__main__":
    get_market_data()
