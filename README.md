# Student Management System 🎓

A responsive full-stack web application featuring a robust **FastAPI backend API** paired with a sleek **Tailwind CSS frontend dashboard**. This system tracks student records, manages profile updates, applies validations, and dynamically searches data records.

---

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI, Pydantic (Data Validation), Uvicorn (ASGI Server)
- **Frontend:** HTML5, JavaScript (Fetch API), Tailwind CSS (UI Styling)

---

## 🚀 Features

- **Full CRUD operations:** Create, Read, Update, and Delete student profiles seamlessly.
- **Advanced Validation:** - Restricts marks to a strict range between `0` and `100`.
  - Enforces a clean 10-digit format regular expression check for contact numbers.
- **Dynamic Search Engine:** Live filtering across fields like `Course` and `City` using case-insensitive checks.
- **Asynchronous Communications:** Built-in CORS handler allows cross-origin browser interactions seamlessly.

---

## 📂 Project Structure

```text
student-management-api/
│
├── main.py          # FastAPI application server & routes
├── index.html       # Single-page Tailwind CSS dashboard
└── README.md        # Documentation
