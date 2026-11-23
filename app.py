from flask import Flask, jsonify, request
from database import get_connection, initialize_database
from validation import validate_student

app = Flask(__name__)

initialize_database()


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Student Management Application"
    })


@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON data is required"}), 400

    name = data.get("name")
    age = data.get("age")
    department = data.get("department")

    valid, message = validate_student(name, age, department)

    if not valid:
        return jsonify({"error": message}), 400

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO students (name, age, department) VALUES (?, ?, ?)",
        (name.strip(), age, department.strip())
    )

    connection.commit()
    student_id = cursor.lastrowid
    connection.close()

    return jsonify({
        "message": "Student added successfully",
        "student_id": student_id
    }), 201


@app.route("/students", methods=["GET"])
def get_students():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    connection.close()

    return jsonify([
        {
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "department": row[3]
        }
        for row in students
    ])


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON data is required"}), 400

    name = data.get("name")
    age = data.get("age")
    department = data.get("department")

    valid, message = validate_student(name, age, department)

    if not valid:
        return jsonify({"error": message}), 400

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE students SET name=?, age=?, department=? WHERE id=?",
        (name.strip(), age, department.strip(), student_id)
    )

    connection.commit()
    updated = cursor.rowcount
    connection.close()

    if updated == 0:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({"message": "Student updated successfully"})


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    connection.commit()
    deleted = cursor.rowcount
    connection.close()

    if deleted == 0:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({"message": "Student deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)