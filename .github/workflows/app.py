from flask import Flask, request, render_template_string
from attendance import calculate_attendance, check_attendance

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Attendance System</title>
</head>
<body>
    <h1>Student Attendance Management System</h1>

    <form method="POST">
        <label>Student Name:</label>
        <input type="text" name="name" required>

        <br><br>

        <label>Classes Attended:</label>
        <input type="number" name="present"
               min="0" required>

        <br><br>

        <label>Total Classes:</label>
        <input type="number" name="total"
               min="1" required>

        <br><br>

        <button type="submit">Calculate Attendance</button>
    </form>

    {% if result %}
        <h2>Attendance Result</h2>
        <p>Student: {{ result.name }}</p>
        <p>Attendance: {{ result.percentage }}%</p>
        <p>Status: {{ result.status }}</p>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        name = request.form["name"].strip()
        present = int(request.form["present"])
        total = int(request.form["total"])

        if not name or total <= 0 or present < 0 or present > total:
            return "Invalid student or attendance details", 400

        percentage = calculate_attendance(present, total)

        status = check_attendance(percentage)

        result = {
            "name": name,
            "percentage": round(percentage, 2),
            "status": status
        }

    return render_template_string(HTML, result=result)


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(debug=True)
