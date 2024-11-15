Custom PC Build Management System
A web-based application to simplify custom PC building by providing a platform to select, manage, and save configurations with real-time price calculations.

Features
User Authentication: Secure login and registration.
Component Selection: Choose CPUs, GPUs, RAM, and more from an integrated database.
Real-Time Price Calculation: Dynamic updates based on selected components.
Build Management: Create, view, and manage multiple PC builds.
User-Friendly Design: Intuitive interface with a responsive layout.
Technologies Used
Backend: Flask
Frontend: HTML, CSS, JavaScript
Database: MySQL
Libraries:
Flask (Python)
Jinja2 for templating
MySQL Connector
Getting Started
Prerequisites
Python 3.8 or higher
MySQL installed and configured
Pip package manager
Setup Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/your_username/Custom-PC-Build-Management.git
cd Custom-PC-Build-Management
Install required dependencies:

bash
Copy code
pip install -r requirements.txt
Import the database.sql file into your MySQL server:

bash
Copy code
mysql -u root -p < database.sql
Update database credentials in DCDSL_Project.py:

python
Copy code
conn = mysql.connector.connect(
    host='your_host',
    user='your_user',
    password='your_password',
    database='custom_pc_builder'
)
Run the application:

bash
Copy code
python DCDSL_Project.py
Open http://127.0.0.1:5000 in your browser.

How to Use
Register for an account or log in with your credentials.
Navigate to the homepage to view saved builds.
Create a new PC build by selecting components from dropdown menus.
View real-time total price updates.
Save your build or manage existing builds.
Project Structure
php
Copy code
DCDSL_Project/
├── templates/              # HTML templates
│   ├── index.html          # Homepage
│   ├── create_build.html   # Build creation page
│   ├── login.html          # Login page
│   ├── register.html       # Registration page
├── static/                 # Static files
│   ├── style.css           # Styling for the application
├── DCDSL_Project.py        # Main Flask application
├── database.sql            # SQL file for database schema
├── requirements.txt        # Project dependencies
└── README.md               # Documentation
Future Enhancements
Filtering components by price, brand, and specifications.
Adding user reviews and ratings for components.
Payment gateway integration for purchasing builds.
Admin panel for managing users and builds.
Price conversion for international users.
Screenshots
Homepage

Create Build

Authors
Sahil Awatramani (23070126112)
Riddhim Kawdia (23070126106)
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Dr. Kalyani Kadam, Project Guide
