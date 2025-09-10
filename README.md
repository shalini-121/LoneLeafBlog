# 📝 LoneLeaf Blog

A simple blog application built with **Flask**, **SQLite**, and **Flask-Login**.  
Users can register, log in, create posts, edit posts, delete posts and view posts.  

## 🚀 Features
- 🔐 User authentication (Register/Login/Logout)  
- ✍️ Create, edit, and view blog posts  
- 🎨 Pink–Orange gradient theme (custom `style.css`)  
- 🗄️ SQLite database integration  
- 📱 Responsive UI  

## 📂 Project Structure
```
flask_blog/
│── venv/ # Virtual environment
│── app.py # Main Flask app
│── models.py # Database models
│── forms.py # Flask-WTF forms
│── templates/ # HTML templates
│ ├── base.html
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── new_post.html
│ ├── post.html
│── static/ # Static files
│ ├── style.css
```
## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/flask_blog.git
   cd flask_blog
   ```
2. Create virtual environment
   ```
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```
3.Install dependencies
   ```
   pip install -r requirements.txt

   ```
4. Initialize the database
   ```
   python
   >>> from app import app
   >>> from models import db
   >>> with app.app_context():
   ...     db.create_all()

   ```
 5. Run the app
   ```
   python app.py

   ```
6. Open in browser
   ```
   http://127.0.0.1:5000
   ```
## 📦 Requirements

Make sure your requirements.txt contains:
   ```
   Flask
   Flask-Login
   Flask-WTF
   Flask-SQLAlchemy
   Werkzeug
   ```
## 🎨 Theme

This app uses a pink–orange gradient theme for UI.
You can customize it in static/style.css.

## 📸 Screenshots

<img width="1906" height="829" alt="Screenshot (24)" src="https://github.com/user-attachments/assets/b6c03f01-5a81-4086-994b-e5fe9499c2fd" />


## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## 📜 License

This project is licensed under the MIT License.

