SupplyIQ is a robust, database-driven operations platform designed to manage product inventory, track stock levels, and provide automated business intelligence. Built with a 3-tier architecture, this project bridges the gap between raw relational data and actionable operational insights.

Key Features
Full CRUD Functionality: Seamlessly Create, Read, Update, and Delete inventory items.

Database-Driven Logic: Utilizes PostgreSQL views for efficient filtering of operational data.

Automated Alert System: Implements an event-driven background service using Python’s schedule library to monitor stock levels.

Modular Architecture: Designed with a clean separation between database connection logic, data manipulation scripts, and the application controller.

System Architecture
Database Layer: PostgreSQL (Tables: Products, Inventory, Warehouses).

Logic Layer: Python (using psycopg2 for database connectivity).

Service Layer: Automated background monitoring for low-stock alerts.

Tech Stack
Language: Python 3.x

Database: PostgreSQL 18

Libraries: psycopg2, schedule

How to Run
Clone the repository: git clone [your-repo-link]

Install dependencies: pip install -r requirements.txt

Configure Database: Ensure your PostgreSQL server is running and update db_connector.py with your credentials.

Launch the system: python main.py
