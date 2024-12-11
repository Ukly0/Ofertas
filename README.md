# UNIQLO Price Tracker Bot

## Description
UNIQLO Price Tracker Bot is a scalable application designed to track product prices on the UNIQLO online store. Its main goal is to notify users via a Telegram bot when a registered item's price drops below a specified value.

---

## Features
- **Price Tracking:** Extracts up-to-date product information from UNIQLO.
- **Variant Management:** Supports multiple colors and sizes.
- **Telegram Notifications:** Sends automatic alerts when a registered item hits the desired price.
- **Scalable:** Easy integration with databases and additional services.

---

## Technologies Used
- **Language:** Python
- **Web Scraping:** Playwright
- **Databases:** PostgreSQL (optional for long-term storage)
- **Automation:** Telegram Bot (using `python-telegram-bot` or similar)

---

## Installation

### Prerequisites
- **Python 3.9+**
- **Playwright Setup:**
  ```bash
  pip install playwright
  playwright install
  ```
- **Additional Libraries:**
  ```bash
  pip install python-telegram-bot
  ```

### Clone the Repository
```bash
git clone https://github.com/Ukly0/Ofertas.git
cd Ofertas
```

### Run the Price Tracker
```bash
python main.py
```

---

## Configuration

1. **Configuration File:**
   - Create a `.env` file with the following data:
     ```env
     TELEGRAM_API_KEY=your_telegram_bot_api_key
     DATABASE_URL=your_database_url (optional)
     ```

2. **Customization:**
   - Define the minimum price for receiving alerts.
   - Add products to the tracking list.

---

## Usage

1. **Start the Telegram Bot:**
   - Log in to your Telegram bot.
   - Send commands like `/add` to add products and `/track` to view the tracking list.

2. **Automation:**
   - Set up scheduled tasks using `cron` or `Task Scheduler` to run price tracking periodically.

---

## Project Structure
```
Ofertas/
├── main.py              # Main file
├── uniqlo_scraper.py    # UNIQLO scraping module
├── bot.py               # Telegram bot
├── database.py          # Database management (optional)
├── requirements.txt     # Project dependencies
└── README.md            # Reference document
```

---

## Contributions

Contributions are welcome. Fork the project, create a branch with your changes, and submit a pull request.

**Have an interesting idea or feature?** Feel free to collaborate and improve the project! 🚀

---

## License
This project is under the MIT license. See the `LICENSE` file for more information.

---

## Disclaimer
This project is for educational purposes only. Using bots and scrapers may violate the terms of service of certain websites. Use it at your own responsibility.

---

Thank you for using UNIQLO Price Tracker Bot! 🎉

