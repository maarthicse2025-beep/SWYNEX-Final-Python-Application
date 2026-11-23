# SWYNEX Final Python Application

## Project Description
A Student Management REST API developed using Python, Flask, and SQLite.

## Features
- Add student records
- View all student records
- Update student details
- Delete student records
- Input validation
- Error handling
- SQLite database integration
- REST API endpoints

## Technologies Used
- Python
- Flask
- SQLite
- Postman

## Installation

Install Python and run:

pip install -r requirements.txt

## Run the Application

python app.py

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /students | View students |
| POST | /students | Add student |
| PUT | /students/1 | Update student |
| DELETE | /students/1 | Delete student |

## Project Structure

- app.py – Main Flask application
- database.py – Database connection and initialization
- validation.py – Input validation
- requirements.txt – Project dependencies
- students.db – SQLite database (created automatically)

## Testing
All API endpoints were tested using Postman, including validation and error handling.