## 📌 Project Overview

**This is a Django-based FAQ Management System that allows users to:**

1. Store and manage FAQs with multi-language translation.

2. Use WYSIWYG editor (CKEditor) for formatting answers.

3. Access FAQs via a REST API.

4. Deploy using Render and Gunicorn.

5. Provide an intuitive interface for managing FAQs efficiently.

## 📌 Tech Stack Used

**Backend:** Django (Python)

**Frontend:** Bootstrap (HTML, CSS, JavaScript)

**Database:** SQLite (default), PostgreSQL (for deployment)

**API Integration:** Google Translate (googletrans package)

**Deployment:** Render (Gunicorn for production server)

**Testing:** Django's built-in test framework

## 📌 Deployment 

**Deployed URL:** https://bharatfdbackend.onrender.com/
### 1️⃣ Deploy to Render

**🔹 Steps to Deploy**

1. Push your code to GitHub.

2. Go to Render.

3. Create a new Web Service.

4. Connect it to your GitHub repository.

5. Set the Start Command:

6. gunicorn bharatFD_backend.wsgi:application --bind 0.0.0.0:8000

7. Deploy and monitor logs for issues.

📌 Output Explanation

## Below are the screenshots of the working application:

1️⃣ Home Page (FAQ List)
![Screenshot 2025-02-02 205624](https://github.com/user-attachments/assets/472a450e-49d4-4f9a-8df8-bce259a45a2b)
Displays all FAQs.
![Screenshot 2025-02-02 205823](https://github.com/user-attachments/assets/ac7ea2d6-f739-42bd-b20f-6b76a66a2434)

![Screenshot 2025-02-02 210442](https://github.com/user-attachments/assets/1c00fd28-497c-4f9a-88d4-b1733ea3df8b)
Supports language selection via a dropdown.

2️⃣ Add FAQ Page
![Screenshot 2025-02-02 210718](https://github.com/user-attachments/assets/e92087da-0b10-4884-a962-b43d985ffb2c)
Allows adding new FAQs using a form with a WYSIWYG editor.


##📌 How to Use This Git Repository

###If you have pulled this repository and want to set up the project locally, follow these steps:

**1️⃣ Clone the Repository**

`git clone https://github.com/sushmakurella/bharatFDBackend.git
 cd faq-management-system`

**2️⃣ Create and Activate Virtual Environment**

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows

**3️⃣ Install Dependencies**

pip install -r requirements.txt

**4️⃣ Run Migrations**

python manage.py makemigrations
python manage.py migrate

**5️⃣ Start the Server**

python manage.py runserver

🔗 Open: http://127.0.0.1:8000/

**6️⃣ Access Admin Panel**

python manage.py createsuperuser

Then visit: http://127.0.0.1:8000/admin/ and log in.

##📌 Testing

**Run unit tests using:**

`python manage.py test`


##📌 Contact & Support

For issues, open an issue on GitHub or contact your suahmakurella@gmail.com.
