# USL ID Management

A Flask-based ID management application for USL (United Soccer League).

## Features

- User identification management
- RESTful API endpoints
- Environment configuration support
- Production-ready error handling
- Health check endpoints

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/olliew172-cpu/USL-id-management.git
   cd USL-id-management
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file (copy from `.env.example`):
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and set your configuration values.

## Running the Application

### Development
```bash
python app.py
```

### Production
```bash
gunicorn wsgi:app --bind 0.0.0.0:5000 --workers 4
```

The application will be available at `http://localhost:5000`

## API Endpoints

- `GET /` - Main API endpoint
- `GET /api/health` - Health check endpoint
- `GET /api/version` - API version information

## Troubleshooting

### Internal Server Error
If you see an "Internal Server Error":

1. Check that all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure `.env` file exists and is properly configured

3. Check application logs for detailed error messages

4. Make sure you have the correct Python version (3.7+)

## Deployment

### Vercel
1. Push code to GitHub
2. Connect repository to Vercel
3. Set environment variables in Vercel dashboard
4. Deploy

### Heroku
```bash
heroku create your-app-name
git push heroku main
heroku config:set FLASK_ENV=production
```

### Docker
```bash
docker build -t usl-id-management .
docker run -p 5000:5000 usl-id-management
```

## License

MIT
