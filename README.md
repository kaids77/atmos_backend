# Atmos Backend: AI & Weather Services API

A high-performance FastAPI server powering the Atmos mobile experience.

## The "Why"
**What is it?** The robust backend infrastructure for the Atmos mobile app.
**Who is it for?** Developers and maintainers running the Atmos server environment.
**What are the core features?** 
- Serves AI chat endpoints via advanced AI integration.
- Retrieves and formats weather data from OpenWeather API.
- Manages Firebase Firestore synchronization for user chat histories.

## Visuals
*(Terminal screenshot of Uvicorn running or Swagger UI goes here)*

## Getting Started
### Prerequisites
- Python 3.9+

### Installation
```bash
cd atmos_backend
python -m venv .venv

# On Windows:
.\.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

## Usage
Start the development server using Uvicorn. The API documentation will be available at `http://127.0.0.1:8000/docs`.

```bash
uvicorn app.main:app --reload
```

## Folder Structure
```text
atmos_backend/
├── app/
│   ├── api/        # API route definitions and endpoints
│   ├── core/       # Configurations and security
│   ├── models/     # Database models
│   ├── schemas/    # Pydantic validation schemas
│   └── services/   # Core logic (e.g., ai_service.py)
├── .env            # Environment variables
└── requirements.txt# Python dependencies
```

## Configuration
You must create a `.env` file in the `atmos_backend` directory.

| Variable | Description | Default |
| -------- | ----------- | ------- |
| `OPENWEATHER_API_KEY` | OpenWeatherMap API Key | None |
| `apiKey` | Firebase API Key | None |
| `authDomain` | Firebase Auth Domain | None |
| `projectId` | Firebase Project ID | None |
| `storageBucket` | Firebase Storage Bucket | None |
| `messagingSenderId` | Firebase Sender ID | None |
| `appId` | Firebase App ID | None |
| `measurementId` | Firebase Measurement ID | None |
| `MAKE_WEBHOOK_URL` | Integration webhook URL | None |
| `GOOGLE_APPLICATION_CREDENTIALS` | Path to Firebase Admin SDK JSON | None |
| `SECRET_KEY` | FastAPI Secret Key | None |

## Roadmap & Contributing
**Roadmap:**
- Implement Redis caching for weather data to reduce API calls.
- Add user authentication endpoints.

**Contributing:**
We welcome contributions! Please refer to our main repository guidelines before opening a Pull Request.

## License & Contact
- **License:** MIT License
- **Contact:** Reach out at charliemangyao@gmail.com.com or find us on Facebook *santino.cc7*.
