# 📚 Library Management System (Django)

A full-featured **Library Management System** built using Django.
This project allows users to register, log in, browse books, issue/return them, and track activity with fine calculation.

---

## 🚀 Features

* 🔐 User Authentication (Register, Login, Logout)
* 📚 Book Management System
* 🔄 Issue and Return Books
* 👤 Student Dashboard
* 💰 Automatic Fine Calculation
* 👑 Admin Panel (Full Control)

---

## 🧰 Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Database:** SQLite
* **Tools:** VS Code, Git, GitHub

---

## 📦 Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/PARZIVAL283/Library-Management-System.git
cd Library-Management-System
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install django
```

---

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

---

### 6. Run the Server

```bash
python manage.py runserver
```

Open your browser:

👉 http://127.0.0.1:8000/

---

## 🧭 Project Structure

```
Library_system/
│
├── library/              # Main Django app
│   ├── models.py         # Database models
│   ├── views.py          # Application logic
│   ├── urls.py           # App routing
│   ├── forms.py          # User forms
│   └── templates/        # HTML templates
│
├── Library_system/       # Project settings
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
└── db.sqlite3
```

---

## 🔑 Key Functionalities

### 📚 Book Management

* Add books via admin panel
* Display books to users
* Track availability

### 🔄 Issue & Return System

* Users can issue available books
* Return books updates availability
* Tracks issue and return dates

### 💰 Fine Calculation

* First 7 days: Free
* After 7 days: 10 BDT per day

### 👤 User Dashboard

* View issued books
* Check return status
* See calculated fine

---

## 👑 Admin Panel

Access:

👉 http://127.0.0.1:8000/admin/

Admin can:

* Add/Edit/Delete books
* Monitor issued books
* Manage users

---

## 📸 Screenshots (Add Later)

* Home Page
* Login/Register Page
* Book List
* Dashboard
* Admin Panel

---

## 💡 Future Improvements

* 🔍 Search and filter books
* 📄 Pagination
* 📧 Email notifications
* 🌐 Deployment (Render / Railway / Heroku)
* 📱 Mobile app version

---

## 👨‍💻 Author

**Parzival**
CSE Student | Developer | Content Creator (XENON GAMING)

---

## 📜 License

This project is developed for educational purposes only.
