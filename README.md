# 🛠️ Work Order Tracker

A REST API built with **FastAPI** and **MySQL** for managing work orders. It supports creating, listing, fetching, and updating work orders, and includes an AI-powered summarization endpoint using **Google Gemini** via LangChain.

---

## 🚀 Features

- Create new work orders
- List all work orders
- Get a single work order by ID
- Update a work order's status
- AI-powered work order summarization (Gemini)

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-----------|
| API Framework | FastAPI |
| Database | MySQL |
| AI / LLM | Google Gemini (via LangChain) |
| Python Version | 3.14+ |
| Package Manager | [uv](https://docs.astral.sh/uv/) |

---

## ⚙️ Prerequisites

Make sure the following are installed on your machine:

- [Python 3.14+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) — fast Python package manager
- [MySQL](https://dev.mysql.com/downloads/) — running locally or on a remote server

---

## 📦 Installation

**1. Clone the repository**
```bash
git clone https://github.com/jabbarnawaz/work-order-tracker.git
cd work-order-tracker
```

**2. Install dependencies using `uv`**
```bash
uv sync
```

---

## 🗄️ Database Setup

**1. Open your MySQL client and create the database and table:**
```sql
CREATE DATABASE operations;

USE operations;

CREATE TABLE work_orders (
    id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    detail TEXT,
    priority VARCHAR(50),
    order_status VARCHAR(50)
);
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root (it is already git-ignored for safety):

```env
DB_HOST=127.0.0.1
DB_NAME=operations
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_mysql_password

GOOGLE_API_KEY=your_google_gemini_api_key
```

> **Never commit your `.env` file to GitHub.** It is already listed in `.gitignore`.

---

## ▶️ Running the Server

```bash
uvicorn app:app --reload
```

The API will be available at: **`http://127.0.0.1:8000`**

---

## 📖 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/work_orders` | Create a new work order |
| `GET` | `/work_orders` | List all work orders |
| `GET` | `/work_orders/{order_id}` | Get a work order by ID |
| `PUT` | `/work_orders/{order_id}` | Update a work order's status |
| `POST` | `/work_orders/{order_id}/sammurize` | Summarize a work order using AI |

### Example — Create a Work Order

```bash
curl -X POST http://127.0.0.1:8000/work_orders \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "title": "Fix leaking pipe",
    "detail": "The pipe in room 3B is leaking and needs immediate repair.",
    "priority": "High",
    "order_status": "pending"
  }'
```

### Example — Update Status

```bash
curl -X PUT "http://127.0.0.1:8000/work_orders/1?status=completed"
```

---

## 🌐 Interactive API Docs

FastAPI provides built-in interactive documentation. After starting the server, open:

- **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📁 Project Structure

```
work-order-tracker/
├── app.py            # Main FastAPI application
├── pyproject.toml    # Project dependencies
├── uv.lock           # Locked dependency versions
├── .env              # Environment variables (git-ignored)
├── .gitignore        # Git ignore rules
└── README.md         # This file
```

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
