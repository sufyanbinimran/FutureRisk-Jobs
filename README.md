# 🚀 FutureRisk Jobs – Full-Stack Job Board Application

vimeo video link : https://vimeo.com/1093064966?share=copy 
listen on 2x for better experince 

FutureRisk Jobs is a full-stack MERN-style (MongoDB alternative: **MySQL** used here) job board web application. It allows users to view, post, edit, and delete actuarial job listings. The application consists of:

- 🌐 **Frontend** (React)
- 🔧 **Backend** (Flask - Python)
- 🤖 **Scraper** (Selenium-based bot that extracts jobs from [ActuaryList](https://www.actuarylist.com))

---

## 📁 Project Structure

```
FutureRisk-Jobs/
├── frontend/     # React app
├── backend/      # Flask API and MySQL DB (via SQLAlchemy)
├── scraper/      # Selenium bot that scrapes external job data
```

---

## ⚙️ Technologies Used

| Layer     | Tech Stack                         |
|-----------|------------------------------------|
| Frontend  | React, Axios, Bootstrap            |
| Backend   | Flask, SQLAlchemy, Flask-CORS      |
| Scraper   | Python, Selenium, BeautifulSoup    |
| Database  | MySQL                              |

---

## 🚀 Setup Instructions

### 🔹 1. Backend (Flask + MySQL)

#### Prerequisites:
- Python 3.9+
- MySQL server running
- Create a database: `joblisting`

#### Install dependencies:

```bash
cd backend
python -m venv venv
# Activate virtualenv
# Windows:
venv\Scripts\activate
# macOS/Linux:
# source venv/bin/activate

pip install -r requirements.txt
```

#### Configure `.env`:

Create a `.env` file in `/backend`:

```env
DATABASE_URL=mysql+mysqlconnector://root:yourpassword@localhost:3306/joblisting
JWT_SECRET_KEY=your_jwt_secret
JWT_ACCESS_TOKEN_EXPIRES=3600
```

#### Run the backend:

```bash
python app.py
```

---

### 🔹 2. Frontend (React)

#### Prerequisites:
- Node.js (v16+ recommended)

#### Install dependencies:

```bash
cd frontend
npm install
```

#### Start the frontend:

```bash
npm start
```

> Runs at `http://localhost:3000` and connects to backend at `http://localhost:5000`

---

### 🔹 3. Scraper (Selenium + BeautifulSoup)

#### Install dependencies:

```bash
cd scraper
pip install -r requirements.txt
```

> Make sure ChromeDriver is installed or use `webdriver-manager`.

#### Run the scraper:

```bash
python scrape_actuary.py
```

> Scrapes up to 50 job listings from ActuaryList and stores them in your MySQL DB using SQLAlchemy.

---

## 🌐 REST API Endpoints

| Method | Route           | Description         |
|--------|------------------|---------------------|
| GET    | `/api/jobs`      | List all jobs       |
| POST   | `/api/jobs`      | Create new job      |
| PUT    | `/api/jobs/<id>` | Update job by ID    |
| DELETE | `/api/jobs/<id>` | Delete job by ID    |

Supports filtering by `job_type`, `location`, `tags`, and sorting by `posting_date`.

---

## 🧪 Validation & Error Handling

- Server-side & client-side form validation
- Required fields: `title`, `company`, `location`, `posting_date`, `job_type`
- Graceful error handling and success messages

---

## 📌 Notes

- Use `.gitignore` to exclude:
  - `node_modules/`
  - `venv/`
  - `.env`
  - `__pycache__/`

- React + Flask are run concurrently on ports `3000` and `5000` during development.

---

## 👥 Author

- **Muhammad Sufyan Malik**

