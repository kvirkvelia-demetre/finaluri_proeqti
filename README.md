# 📚 წიგნების ბიბლიოთეკა

Flask-ზე დაფუძნებული ვებ აპლიკაცია, სადაც შეგიძლია წიგნების დამატება, ნახვა, რედაქტირება და კომენტარების დატოვება.

---

## 🛠 ტექნოლოგიები

- Python / Flask
- Flask-SQLAlchemy (SQLite)
- Flask-Login
- Flask-WTF
- Bootstrap 5
- Werkzeug (პაროლის hash-ისთვის)

---

## ⚙️ გაშვება

### 1. დააინსტალირე dependencies

```bash
pip install flask flask-sqlalchemy flask-login flask-wtf werkzeug
```

### 2. ინიციალიზაცია (პირველად გაშვებისას)

```bash
python init_db.py
```

> ეს შექმნის database-ს და დაამატებს admin მომხმარებელს.
> **admin** / **adminpass**

### 3. სერვერის გაშვება

```bash
python app.py
```

გახსენი ბრაუზერში: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔑 ფუნქციონალი

| ფუნქცია | აღწერა |
|---|---|
| რეგისტრაცია / შესვლა | მომხმარებლის ავთენტიფიკაცია |
| წიგნების სია | მთავარ გვერდზე ყველა წიგნი |
| ძებნა | წიგნის სახელით ძებნა |
| წიგნის დამატება | სათაური, ავტორი, ჟანრი, წელი, სურათი, აღწერა |
| წიგნის რედაქტირება | არსებული წიგნის განახლება |
| წიგნის წაშლა | წიგნის წაშლა სიიიდან |
| წიგნის დეტალები | სრული ინფორმაცია წიგნზე |
| კომენტარები | ავტორიზებული მომხმარებელი ტოვებს კომენტარს |

---

## 📁 პროექტის სტრუქტურა

```
PythonProject/
├── app.py            # აპლიკაციის entry point
├── ext.py            # Flask, SQLAlchemy, LoginManager კონფიგურაცია
├── models.py         # User, Book, Comment მოდელები
├── routes.py         # URL route-ები
├── forms.py          # WTForms ფორმები
├── init_db.py        # Database-ის ინიციალიზაცია
├── static/
│   ├── style.css     # სტილი
│   └── images/       # წიგნების სურათები
└── templates/
    ├── base.html         # საბაზო თემფლეითი
    ├── index.html        # მთავარი გვერდი
    ├── register.html     # რეგისტრაცია
    ├── login.html        # შესვლა
    ├── add_book.html     # წიგნის დამატება/რედაქტირება
    └── book_details.html # წიგნის დეტალები + კომენტარები
```

---

## 👤 Admin

პირველადი admin მომხმარებელი იქმნება `init_db.py`-ით:

- **username:** admin
- **password:** adminpass

---

## ⚠️ შენიშვნა

- `init_db.py` გაშვება წაშლის ყველა არსებულ მონაცემს
- Flask სერვერის გაშვებისას DB Browser-ი უნდა იყოს Disconnect რეჟიმში
