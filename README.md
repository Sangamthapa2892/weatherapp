# 🌤️ Weather Dashboard

A dynamic weather dashboard built with Django, OpenWeatherMap, and Unsplash APIs. It displays real-time weather data, forecasts, and city-specific imagery with robust error handling and a polished UI.

## 🚀 Features

- 🌍 Search weather by city (default: Kathmandu)
- 📸 Dynamic background images from Unsplash
- 🌡️ Real-time temperature, humidity, pressure, wind speed, visibility
- 📅 5-day forecast with min/max temperatures and icons
- 🌆 Popular cities section with snapshots
- 🛡️ Graceful fallback for missing data or API errors
- 🎨 Responsive design with Bootstrap styling

## 🛠️ Tech Stack

- **Backend**: Django, REST API integration
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **APIs**: OpenWeatherMap, Unsplash
- **Deployment**: Railway / PythonAnywhere (optional)
- **Security**: `.env` for API keys, `.gitignore` for secrets

## 📦 Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/weatherapp.git
   cd weatherapp
2. Create a virtual environment: 
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install dependencies: 
    pip install -r requirements.txt

4. Add your .env file: 
    -view .env.example file for reference
    OPENWEATHER_API_KEY=your_openweather_api_key
    UNSPLASH_API_KEY=your_unsplash_api_key
5. Run the server: 
    python manage.py runserver

6. Visit: 
    http://127.0.0.1:8000/

📁 Project Structure
weatherapp/
├── app/
│   ├── templates/
│   ├── static/
│   └── views.py
├── weatherapp/
│   └── settings.py
├── manage.py
├── requirements.txt
└── .env


📸 Screenshots
Add screenshots here once deployed or locally hosted.
🧠 Author

Sangam Thapa
Backend Developer | Django Enthusiast | DevOps Learner
📍 Kathmandu, Nepal





