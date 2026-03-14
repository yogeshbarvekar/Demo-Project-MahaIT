# Python Microservice

A simple, production-ready Python microservice built with Flask, containerized for Docker.

## Features

- RESTful API endpoints with JSON responses
- Health check endpoint for monitoring
- Comprehensive logging
- Docker containerization with multi-worker setup
- Docker Compose for easy deployment
- Error handling and validation
- CORS-ready structure

## Project Structure

```
.
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker image configuration
├── docker-compose.yml    # Docker Compose configuration
├── .dockerignore         # Files to exclude from Docker build
└── README.md            # This file
```

## Available Endpoints

### Health Check
- **GET** `/health` - Returns health status
  ```bash
  curl http://localhost:5000/health
  ```

### Greet API
- **POST** `/api/greet` - Returns a greeting message
  ```bash
  curl -X POST http://localhost:5000/api/greet \
    -H "Content-Type: application/json" \
    -d '{"name": "John"}'
  ```

### Get Data
- **GET** `/api/data` - Returns sample data
  ```bash
  curl http://localhost:5000/api/data
  ```

### Echo API
- **POST** `/api/echo` - Echoes back the request payload
  ```bash
  curl -X POST http://localhost:5000/api/echo \
    -H "Content-Type: application/json" \
    -d '{"message": "Hello, World!"}'
  ```

## Local Development Setup

### Prerequisites
- Python 3.11 or higher
- pip package manager

### Installation

1. Clone/navigate to the project directory:
   ```bash
   cd /path/to/microservice
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

Run the Flask development server:
```bash
python app.py
```

The microservice will be available at `http://localhost:5000`

## Docker Setup

### Build the Docker Image

```bash
docker build -t python-microservice:latest .
```

### Run with Docker

```bash
docker run -p 5000:5000 python-microservice:latest
```

### Run with Docker Compose

```bash
docker-compose up
```

To run in the background:
```bash
docker-compose up -d
```

To stop the service:
```bash
docker-compose down
```

## Environment Variables

- `FLASK_ENV` - Set to `production` in Docker (default: `development`)

## Production Deployment

The Dockerfile uses **Gunicorn** as a production WSGI server with 4 workers for better performance and reliability:

```dockerfile
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120", "app:app"]
```

For scaling, adjust the `--workers` parameter based on the number of CPU cores available.

## Health Checks

The Docker image includes a built-in health check that monitors the `/health` endpoint every 30 seconds.

## Logging

Application logs are written to stdout and include:
- Timestamp
- Logger name
- Log level
- Message

Logs are automatically captured by Docker and available via:
```bash
docker logs <container-id>
```

## Development Tips

1. **Hot Reload**: During development, use Flask's debug mode by setting `debug=True` in `app.run()` in app.py

2. **Virtual Environment**: Always use a virtual environment for development to avoid dependency conflicts

3. **Dependencies**: When adding new packages, update `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```

4. **Testing**: You can test the API using:
   - `curl` (command line)
   - Postman (GUI)
   - Python `requests` library

## Common Commands

```bash
# Build Docker image
docker build -t python-microservice:latest .

# Run container
docker run -p 5000:5000 python-microservice:latest

# View logs
docker logs <container-id>

# Stop container
docker stop <container-id>

# Remove image
docker rmi python-microservice:latest

# Docker Compose
docker-compose up -d      # Start
docker-compose down       # Stop
docker-compose logs -f    # View logs
docker-compose ps         # List running services
```

## License

MIT License - Feel free to use this microservice as a template for your projects.
