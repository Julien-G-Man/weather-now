# WeatherNow

A simple, modern Django web app to get real-time weather updates for any city.

## Features

- Search for any city to get current weather data
- Displays country code, coordinates, temperature (°C), pressure, and humidity
- Clean, responsive UI with Bootstrap 5
- Weather icons from OpenWeatherMap

## Demo

<!-- Optionally add a screenshot here -->
<!-- ![Screenshot](screenshot.png) -->

## Getting Started

### 1. Clone the repository

```sh
git clone https://github.com/Julien-G-Man/weather-now.git
cd weather-now
```

### 2. Create and activate a virtual environment (recommended)

```sh
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Run migrations

```sh
python manage.py migrate
```

### 5. Run the development server

```sh
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Project Structure

```
weatherdetector/
  └── templates/
      └── index.html
  └── ... (other Django app files)
manage.py
requirements.txt
```

## Technologies Used

- Python (Django)
- Bootstrap 5
- OpenWeatherMap API

## .gitignore

Make sure your `.gitignore` includes:
```
__pycache__/
*.pyc
*.sqlite3
.env
venv/
```

## Credits

- Weather icons by [OpenWeatherMap](https://openweathermap.org/)
- UI inspired by Bootstrap examples

---

*Get real-time weather updates for any city!*