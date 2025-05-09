# NoteNest 📝🛡️

**A secure place to nest your thoughts.**

---

## 📦 Project Overview

**NoteNest** is a simple yet secure notes application where users can register, log in, and create private notes. Each note is associated with a specific user and can only be accessed by that user. The application is built using **Flask** and **SQLite** for a lightweight, easy-to-deploy solution.

---

## ✅ Features

- User Registration & Login  
- Secure User Authentication  
- Create, View, and Delete Notes  
- Protected Routes  
- Logout Functionality  
- Basic Styling with CSS  

---

## 🛠️ Tech Stack

- **Python**  
- **Flask**  
- **SQLite**  
- **HTML/CSS**  
- **Bootstrap** (for basic styling)  

---

## 🚀 Getting Started

### 1. Clone the Repository:

```bash
git clone https://github.com/Kirankumarvel/NoteNest.git
cd NoteNest
```

### 2. Create a Virtual Environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\Activate
```

### 3. Install Dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables:

- Create a `.env` file in the project root and add:

```env
SECRET_KEY=your_secret_key_here
```

### 5. Initialize the Database:

```bash
python app.py
```

### 6. Run the Application:

```bash
flask run
```

Access the application at: **`http://127.0.0.1:5000`**

---

## 📝 Usage

- Register a new account or log in with an existing account.  
- Create new notes from the dashboard.  
- View, edit, and delete your notes.  
- Log out to end the session.  

---

## 📂 Project Structure

```
NoteNest/
│── app.py
│── config.py
│── requirements.txt
│── .env
│── database.db
├── static/
│   └── styles.css
│   └── dashboard.css
│   └── login.css
│   └── signup.css
├── templates/
│   └── base.html
│   └── home.html
│   └── login.html
│   └── signup.html
│   └── dashboard.html
```

---

## ⚡ Future Enhancements

- Implement search and filter functionality.  
- Add password reset feature.  
- Improve user interface with advanced styling.  

---

## 🤝 Contributions

Feel free to fork the repository and create a pull request for any feature you would like to add.

---

## 📧 Contact

For any queries, reach out to **[Kiran Kumar](https://github.com/Kirankumarvel)**.

---

**Happy Nesting!** 📝🛡️
