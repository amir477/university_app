<div dir="rtl">

# University App

> سیستم مدیریت دانشگاه | پروژه تیمی با PyQt5 و دیتابیس قابل تغییر (SQLite / MySQL)

---

## 📁 ساختار پروژه

university_app/
├── main.py
├── settings.py
├── core/
│ ├── init.py
│ ├── config.py
│ └── database.py
├── ui_form/
│ ├── init.py
│ ├── login.py
│ ├── admin.py
│ ├── professor.py
│ └── student.py
├── resources/
│ ├── icons/
│ ├── images/
│ └── styles/
└── requirements.txt


---

## ⚙️ پیش‌نیازها

- Python 3.10+
- PyQt5
- MySQL Connector (برای MySQL)
- SQLite (به صورت پیش‌فرض)

```bash
pip install -r requirements.txt
🚀 اجرای برنامه

از ریشه پروژه اجرا کنید:
python -m university_app.main
❌ اجرای مستقیم python main.py از داخل پوشه university_app باعث خطای import می‌شود.

🛠️ تنظیمات

تمام تنظیمات در settings.py قرار دارند:

DB_ENGINE → تغییر بین sqlite و mysql

DEBUG → حالت توسعه

مسیر دیتابیس و تنظیمات MySQL

برای دسترسی امن، از core/config.py استفاده کنید:

from university_app.core.config import get_app_name, get_db_engine

هیچ فرم یا ماژول UI نباید مستقیم settings.py یا دیتابیس را ایمپورت کند.

👨‍💻 قوانین تیمی

تمام فرم‌ها در ui_form/ قرار می‌گیرند.

هر عضو فقط روی فرم خودش کار می‌کند.

دسترسی مستقیم به دیتابیس از UI ممنوع است.

تغییر زیرساخت فقط در core/ انجام شود.

تنظیمات ثابت پروژه فقط در settings.py قرار دارند.

📌 نکات توسعه

برای اضافه کردن فرم جدید، یک فایل جدید در ui_form/ بسازید و import آن را در main.py یا ui_form/__init__.py انجام دهید.

برای مهاجرت دیتابیس به MySQL، کافیست DB_ENGINE را تغییر دهید و مطمئن شوید MySQL server در دسترس است.

تمامی مسیرها، ثابت‌ها و configurationها از طریق core/config.py خوانده شود.
