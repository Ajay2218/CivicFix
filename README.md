# 🚀 CivicFix – Community Issue Reporting System

CivicFix is a full-stack web application built using Django that enables users to report, track, and manage community issues efficiently. It integrates real-time status tracking with location-based mapping to improve communication between citizens and administrators.

---

## 🌟 Features

- 🔐 User Authentication (Register/Login)
- 📝 Issue Reporting with detailed input
- 📍 Location-based mapping using Leaflet.js
- 🔄 Real-time status tracking (Pending, In Progress, Resolved)
- 🗂️ Category-based issue management
- 🛠️ Admin dashboard for managing complaints
- 📱 Responsive user interface

---

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite  
- **Tools:** Git, GitHub  
- **Map Integration:** Leaflet.js  

---

## ⚙️ Installation & Setup  

Follow these steps to run the project locally:

### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/civicfix.git
cd civicfix
```

### 2. Create Virtual Environment  
```bash
python -m venv venv
```

### 3. Activate Virtual Environment  
**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 5. Configuration  
- Ensure `settings.py` is properly configured  
- Set `DEBUG = True` for development  
- Configure `ALLOWED_HOSTS` if required  

### 6. Database Setup  
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser  
```bash
python manage.py createsuperuser
```

### 8. Run the Server  
```bash
python manage.py runserver
```

### 9. Access the Application  
- 🌐 Home: http://127.0.0.1:8000/  
- 🔐 Admin Panel: http://127.0.0.1:8000/admin/  

### 💡 Note  
Replace `your-username` with your actual GitHub username.
