# USL ID Management

A Flask-based ID management application for USL (United Soccer League).

## Features

- User identification management
- RESTful API endpoints
- Environment configuration support

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your configuration

## Running the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## API Endpoints

- `GET /` - Main page
- `GET /api/health` - Health check endpoint

## License

MIT
