**🩸 LifeSupport — Blood Bank App**

📖 Overview

The Blood Bank App (LifeSupport) is a web-based platform designed to bridge the gap between blood donors and recipients. It provides a centralized system for mapping donors to recipients based on blood type compatibility, urgency, and location. The platform also supports real-time updates on urgent blood requests and enables hospitals, NGOs, and individuals to coordinate life-saving donations seamlessly.

This project was built with Django (Python) as the backend framework and integrates modern web technologies for scalability and maintainability.

⸻

🚀 Features
	•	🔐 User Authentication — Secure sign-up and login for donors, recipients, and admins.
	•	🧬 Donor-Recipient Mapping — Automated compatibility matching based on blood group and Rh factor.
	•	📍 Location Tracking — Match donors and recipients based on proximity.
	•	⚡ Urgent Requests — Highlight and broadcast cases where immediate donations are required.
	•	📊 Dashboard & Analytics — Overview of registered users, donations made, and urgent needs.
	•	🏥 Hospital/Organization Support — Hospitals can register to post urgent cases and track responses.
	•	📱 Responsive UI — Mobile-friendly, clean, and intuitive design.

⸻

🏗️ Tech Stack
	•	Backend: Django (Python)
	•	Frontend: HTML, CSS (Bootstrap), JavaScript
	•	Database: SQLite (default, but easily swappable to PostgreSQL/MySQL)
	•	APIs: REST (JSON serialization)
	•	Version Control: Git/GitHub

⸻

📂 Project Structure

blood-bank-app/
│
├── core/                 # Main Django app (views, models, urls)
├── templates/            # HTML templates
├── static/               # CSS, JS, images
├── db.sqlite3            # Database (for dev mode)
├── manage.py             # Django project manager
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

⸻

⚙️ Installation & Setup

1. Clone the Repository

git clone https://github.com/yourusername/blood-bank-app.git
cd blood-bank-app

2. Create Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

pip install -r requirements.txt

3. Run Database Migrations

python manage.py migrate

4. Start the Development Server

python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser.

⸻

🔮 Future Improvements
	•	✅ SMS/Email Notifications for urgent cases.
	•	✅ Role-based access control (donor, recipient, hospital, admin).
	•	✅ Integration with Google Maps API for geolocation-based donor-recipient matching.
	•	✅ Mobile app (Flutter/React Native) for wider accessibility.

⸻

🤝 Contributing

We welcome contributions! Fork the repo, create a feature branch, and submit a pull request.

⸻

📜 License

This project is licensed under the MIT License — feel free to use and modify it for your own projects.

⸻
