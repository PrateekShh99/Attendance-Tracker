# Attendance Tracker

This project helps you track attendance using Python and Flask.

## How to Use

1. **Install Python**: Make sure you have Python installed on your computer.

2. **Clone the Repository**: Open your terminal or command prompt and run:
   ```bash
   git clone https://github.com/PratKing99/Attendance.git
   ```

3. **Install Dependencies**: Navigate to the project folder and install Flask and openpyxl:
   ```bash
   cd Attendance
   pip install Flask
   pip install openpyxl
   ```

4. **Run the App**: Start the Flask app by running:
   ```bash
   python main.py
   ```

5. **Access the App**: Open your web browser and go to `http://localhost:5000`.

6. **Mark Attendance**: On the web page, select the attendance status (Present, Absent, or Leave) for each person and click Submit.

7. **View Attendance**: Attendance data is saved in a file named `Attendance.xlsx`.

## Project Structure

- `main.py`: Contains the Flask application code.
- `templates/index.html`: HTML template for the web interface.
- `static/Style.css`: CSS file for styling the web interface.
- `static/JavaScript.js`: JavaScript file for client-side logic.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a new Pull Request.
