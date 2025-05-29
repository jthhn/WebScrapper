# 🌐 WebScrapper - Django Web Link Scraper

A simple Django web application that scrapes all hyperlinks from a given URL and displays them with pagination. You can also clear saved links with a single click.

## 📌 Features

- Input any URL to scrape all anchor (`<a>`) tags
- Stores and displays the link text and address
- Pagination support (10 links per page)
- Option to clear all stored links
- Built using Django, Requests, and BeautifulSoup

## 🛠 Tech Stack

- Python 3.x
- Django
- BeautifulSoup (bs4)
- Requests

## 🚀 How to Run Locally

### ✅ Prerequisites

- Python installed
- pip installed
- Virtualenv (optional but recommended)

### 📦 Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/webscrapper.git
   cd webscrapper
2. **Create and activate a virtual environment (optional but recommended)**
  - Linux/macOS
    ```bash
    python -m venv env
    source env/bin/activate
  - Windows
    ```cmd
    python -m venv env
    env\Scripts\activate
3. **Install the dependencies**
    ```bash
    pip install -r requirements.txt

4. **Apply migrations**
  ```bash
  python manage.py migrate
  ```
5. **Run the development server**
  ```bash
  python manage.py runserver
  ```
6. **open the your broweser and go to**
  ```bash
  http://127.0.0.1:8000/
  ```

### 💡 How to Use
- Enter a full website URL (including http:// or https://) into the input field.
- Click Scrape to extract all links from the page.
- Scroll through the paginated results (10 links per page).
- Click Clear to delete all saved links.

### 🧹 Clear Data
  - To clear all scraped links, just go to:

    ```arduino
      http://127.0.0.1:8000/clear
### 📁 Project Structure
  ```bash
    webscrapper/
├── scrapper/
│   ├── templates/scrapper/index.html
│   ├── models.py
│   ├── views.py
│   └── ...
├── WebScrapper/
│   ├── urls.py
│   └── settings.py
├── db.sqlite3
├── manage.py
└── requirements.txt






