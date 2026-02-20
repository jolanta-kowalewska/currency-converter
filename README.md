💱 Currency Converter

Python-based currency converter with real-time exchange rates and conversion history tracking.
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

📸 Demo


=== KALKULATOR WALUT ===
1. Przelicz kwotę na dowolną walutę
2. Zapisz historię do pliku
3. Zamknij
============================

Wybierz opcję: 1

--- KONWERSJA WALUT ---
Z jakiej waluty? (np. USD): USD
Na jaką walutę? (np. PLN): PLN
Podaj kwotę: 100

✅ 100 USD = 395.50 PLN
   Kurs: 1 USD = 3.9550 PLN

✨ Features

 💰 **Real-time conversion** - Live exchange rates for 160+ currencies
 📊 **History tracking** - Save all conversions to JSON file
 🛡️ **Error handling** - Robust API error management with timeouts
 🎨 **Clean interface** - User-friendly CLI with clear formatting
 🔄 **OOP design** - Dictionary dispatch pattern for menu handling

🚀 Tech Stack

 **Python 3.8+**
 **requests** - HTTP library for API calls
 **json** - Data serialization
 **OOP principles** - Class-based architecture

📦 Installation

bash
# Clone repository
git clone https://github.com/jolanta-kowalewska/currency-converter.git
cd currency-converter

# Install dependencies
pip install requests

# Run
python currency_converter.py


💡 Usage


1. Convert currency
Choose option: 1
From: USD
To: EUR
Amount: 100
Result: 100 USD = 92.50 EUR

2. Save history
Choose option: 2
✅ History saved to history.json

3. Exit
Choose option: 0
👋 Goodbye!


📂 Project Structure

currency-converter/
│
├── currency_converter.py    # Main application
├── history.json             # Conversion history (auto-generated)
└── README.md               # Documentation


🔧 Code Highlights

Dictionary Dispatch Pattern

self.menu = {
    1: ("Convert currency", self.convert_currency),
    2: ("Save history", self.save_history),
    3: ("Exit", self.exit)
}

Easy to extend - just add one line!


API Integration with Error Handling

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"API Error: {e}")


🎯 Learning Outcomes

This project demonstrates:
 ✅ RESTful API integration
 ✅ JSON data handling
 ✅ File I/O operations
 ✅ Exception handling
 ✅ OOP design patterns
 ✅ Clean code principles

 🛣️ Future Enhancements

- [ ] Historical rate tracking (date-based conversions)
- [ ] Multiple file history with timestamps
- [ ] Currency rate charts
- [ ] Web interface with Flask
- [ ] Unit tests

 📝 API

Uses free **ExchangeRate-API**: https://api.exchangerate-api.com/v4/latest
 👩‍💻 About

Built as part of my learning journey transitioning from VMware Administration to Cloud Engineering.

**Skills focus:** Python • API Integration • Cloud Technologies

 📄 License

MIT License - feel free to use for learning!



⭐ **Star this repo if you found it helpful!**

💼 **Connect with me on [LinkedIn] https://pl.linkedin.com/in/jolanta-kowalewska-b1281799 **

