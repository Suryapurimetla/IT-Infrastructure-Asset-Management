# IT Infrastructure & Asset Management System

## 1. Project Overview

The **IT Infrastructure & Asset Management System** is a web-based application developed to help organizations efficiently manage and track their IT assets. It provides a centralized platform to maintain asset information, monitor allocation, manage maintenance activities, and track warranty details.

The system is developed using Python, Django, and MySQL as part of the Software Engineering Mini Project.

## 2. Project Objectives

- Maintain a centralized record of IT assets.
- Simplify asset allocation and return processes.
- Track asset maintenance activities.
- Monitor warranty expiry information.
- Reduce manual record-keeping and improve asset management efficiency.

## 3. Features

- **Asset Management:** Add, view, update, and delete IT asset records.
- **Dashboard:** View asset statistics and search for assets.
- **Asset Allocation:** Allocate available assets to employees.
- **Asset Return:** Record returned assets and update their availability.
- **Allocation History:** View previous asset allocation records.
- **Maintenance Management:** Record maintenance activities and update asset status.
- **Maintenance History:** View maintenance records for individual assets.
- **Warranty Tracking:** Identify active, expired, and soon-to-expire warranties.
- **Input Validation:** Validate required fields and prevent duplicate asset IDs.

## 4. Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | Django |
| Database | MySQL |
| Frontend | HTML, CSS |
| Development Environment | Visual Studio Code |
| Version Control | Git and GitHub |
| Testing | Django Unit Testing |
| Code Coverage | Coverage.py |

## 5. Project Structure

```text
IT-Infrastructure-Asset-Management/
│
├── assets/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
│   └── admin.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── docs/
│   ├── sad/
│   ├── srs/
│   ├── testplan/
│   └── reports/
│
├── manage.py
├── README.md
└── .gitignore
```

## 6. Installation and Setup

### Prerequisites

- Python 3.10 or later
- Django
- MySQL Server
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/Suryapurimetla/IT-Infrastructure-Asset-Management.git
```

### Step 2: Navigate to the Project Directory

```bash
cd IT-Infrastructure-Asset-Management
```

### Step 3: Create and Activate a Virtual Environment

```bash
python -m venv venv
```

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate
```

### Step 4: Install Dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the required packages individually.

### Step 5: Configure MySQL

Create the project database in MySQL:

```sql
CREATE DATABASE itam_db;
```

Update the database configuration in `config/settings.py` with your local MySQL database name, username, and password.

### Step 6: Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## 7. Testing

The project includes automated tests to verify application functionality.

Run all tests:

```bash
python manage.py test
```

Run tests for the assets application:

```bash
python manage.py test assets
```

Run tests with detailed output:

```bash
python manage.py test assets --verbosity 2
```

### Code Coverage

Run coverage analysis:

```bash
coverage run manage.py test assets
coverage report
coverage html
```

The generated HTML coverage report can be viewed from the `htmlcov` directory.

## 8. Documentation

The project documentation includes:

- Software Requirements Specification (SRS)
- Software Architecture Document (SAD)
- Software Test Plan (STP)
- Unit Testing Report
- System Validation Report
- Code Coverage Report
- Branch Coverage Report

## 9. Version Control and Collaboration

Git and GitHub are used for version control and team collaboration.

The project follows a branch-based development workflow:

1. Create a feature branch.
2. Implement the assigned functionality.
3. Test the changes.
4. Commit the changes with a meaningful commit message.
5. Push the branch to GitHub.
6. Review and merge changes.

## 10. Team Details

**Team Number: 08**

| Sl. No. | Team Member Name | SRN |
|---|---|---|
| 1 | P.JAYA SURYA | PES1UG24AM210 |
| 2 | SREYAESH PERURI | PES1UG24AM18 |
| 3 | AKASH RAMESH | PES1UG24AM212 |
| 4 | PURVIK V GOWDA | PES1UG24AM211 |

## 11. Future Enhancements

- Role-based access control.
- Advanced reporting and analytics.
- Automated maintenance reminders.
- Improved dashboard visualizations.
- Exporting asset reports.

## 12. Conclusion

The IT Infrastructure & Asset Management System provides a centralized solution for managing organizational IT assets. It simplifies asset tracking, allocation, returns, maintenance, and warranty monitoring.

The project demonstrates the application of software engineering principles, database management, web development, version control, and software testing in developing a practical system.
