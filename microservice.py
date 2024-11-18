from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)


# Database connection configuration
db_config = {
    'host': '127.0.0.1',  # Update if your database is hosted elsewhere
    'user': 'root',       # Replace with your MySQL username
    'password': 'Password',  # Replace with your MySQL password
    'database': 'student_db',  # Replace with your database name
}



@app.route('/get-student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)


        query = "SELECT * FROM students WHERE id = %s"
        cursor.execute(query, (student_id,))
        student = cursor.fetchone()


        cursor.close()
        conn.close()



        if student:
            return jsonify(student), 200
        else:
            return jsonify({'error': 'Student not found'}), 404
    except mysql.connector.Error as err:
        return jsonify({'error': f'Database error: {err}'}), 500


if __name__ == '__main__':
    app.run(debug=True)