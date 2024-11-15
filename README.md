# **Custom PC Build Management System**

A web-based application to simplify custom PC building by providing a platform to select, manage, and save configurations with real-time price calculations.

---

## **Features**
- 🔐 **User Authentication**: Secure login and registration.
- 🖥️ **Component Selection**: Choose CPUs, GPUs, RAM, and more from an integrated database.
- 💰 **Real-Time Price Calculation**: Dynamic updates based on selected components.
- 🛠️ **Build Management**: Create, view, and manage multiple PC builds.
- 🌟 **User-Friendly Design**: Intuitive interface with a responsive layout.

---

## **Technologies Used**
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL
- **Libraries**:
  - Flask
  - Jinja2 (templating engine)
  - MySQL Connector

---

## **Getting Started**

### **Prerequisites**
Ensure you have the following installed on your system:
- Python 3.8 or higher
- MySQL Server
- Pip package manager

### **Setup Instructions**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/Custom-PC-Build-Management.git
   cd Custom-PC-Build-Management
   
2. **Install dependencies:**

```pip install -r requirements.txt```

3. **Set up the database:**

Import the database.sql file into your MySQL server:

```mysql -u root -p < database.sql```

4. **Update the database connection settings in DCDSL_Project.py:**
    
    conn = mysql.connector.connect(
    host='your_host',
    user='your_user',
    password='your_password',
    database='custom_pc_builder')
    
5. **Run the application:**

```python DCDSL_Project.py```

Open http://127.0.0.1:5000 in your browser.

## How to Use

Register for an account or log in with your credentials.
Navigate to the homepage to view saved builds.
Create a new PC build by selecting components from dropdown menus.
View real-time total price updates.
Save your build or manage existing builds.

## Project Structure

```
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
```

## Future Enhancements

🔍 Component filtering by price, brand, and specifications.

🌟 User reviews and ratings for components.

💳 Payment gateway integration for purchasing builds.

🔧 Admin panel for managing users and builds.

🌎 Price conversion for international users.

## Screenshots
**Homepage**

![Screenshot 2024-11-10 210725](https://github.com/user-attachments/assets/8bc1bcd7-3bd5-4ec2-a68f-038a5de68044)

**Create Build**

![Screenshot 2024-11-10 210819](https://github.com/user-attachments/assets/efb4ebd9-ab8c-4765-943b-2ed25bab0776)


## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

