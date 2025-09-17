# 🏥 Task Manager API

Production-ready FastAPI application for medical task management with PostgreSQL database, Docker containerization, and automated CI/CD pipeline.

## 🚀 Live Demo

- **API Endpoint:** [https://your-railway-url.com](https://your-railway-url.com)
- **Interactive Docs:** [https://your-railway-url.com/docs](https://your-railway-url.com/docs)
- **Health Check:** [https://your-railway-url.com/health](https://your-railway-url.com/health)

## ⚡ Quick Start

```bash
# Clone repository
git clone https://github.com/JCROMO11/task-manager-api.git
cd task-manager-api

# Run with Docker
docker-compose up -d

# API available at http://localhost:8000
```

## 🛠 Tech Stack

- **Backend:** FastAPI, Python 3.11
- **Database:** PostgreSQL with SQLAlchemy ORM
- **Authentication:** Bcrypt password hashing
- **Infrastructure:** Docker, Docker Compose
- **Deployment:** Railway cloud platform
- **CI/CD:** GitHub Actions
- **Testing:** Pytest with coverage reporting
- **Validation:** Pydantic models with email validation

## 📊 API Features

### User Management
- **POST /users/** - Create new user account
- **GET /users/{id}** - Retrieve user profile
- **GET /users/** - List all users (admin)

### Task Operations
- **POST /users/{id}/tasks/** - Create new task
- **GET /users/{id}/tasks/** - Get user's tasks
- **GET /tasks/{id}** - Get specific task
- **PUT /tasks/{id}** - Update task
- **DELETE /tasks/{id}** - Remove task

### System Endpoints
- **GET /** - Welcome message
- **GET /health** - System health check

## 🏗 Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   FastAPI App   │────│   PostgreSQL    │────│   Railway       │
│   (Python)      │    │   Database       │    │   Deployment    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                        │                       │
    ┌────▼─────┐            ┌─────▼──────┐         ┌──────▼───────┐
    │  Docker  │            │ SQLAlchemy │         │   CI/CD      │
    │Container │            │    ORM     │         │ GitHub Actions│
    └──────────┘            └────────────┘         └──────────────┘
```

## 📁 Project Structure

```
task-manager-api/
├── main.py                 # FastAPI application entry point
├── models.py              # Pydantic request/response models
├── db_models.py           # SQLAlchemy database models
├── database.py            # Database connection configuration
├── crud.py                # Database operations (Create, Read, Update, Delete)
├── requirements.txt       # Python dependencies
├── Dockerfile             # Container configuration
├── docker-compose.yml     # Multi-container setup
├── .github/workflows/     # CI/CD pipeline configuration
└── .env.example          # Environment variables template
```

## 🔧 Environment Setup

Create `.env` file:

```env
# Database Configuration
DATABASE_URL_LOCAL=postgresql+psycopg2://task_user:password@localhost:5432/task_db
DATABASE_URL_DOCKER=postgresql+psycopg2://task_user:password@db:5432/task_db

# Application Environment
APP_ENV=local
```

## 🧪 Development

```bash
# Install dependencies
pip install -r requirements.txt

# Create database tables
python create_tables.py

# Run development server
uvicorn main:app --reload

# Run tests
pytest --cov=. --cov-report=html
```

## 🐳 Docker Deployment

```bash
# Build and run services
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f api

# Stop services
docker-compose down
```

## 📈 Production Features

### Security
- Password hashing with bcrypt
- SQL injection protection via SQLAlchemy
- Input validation with Pydantic
- Environment-based configuration

### Monitoring & Reliability
- Health check endpoints
- Structured logging
- Database connection pooling
- Graceful error handling

### DevOps
- Automated testing pipeline
- Docker containerization
- Zero-downtime deployments
- Environment-specific configurations

## 🔍 API Examples

### Create User
```bash
curl -X POST "https://your-api-url.com/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "doctor_smith",
    "email": "doctor@hospital.com",
    "password": "secure_password"
  }'
```

### Create Task
```bash
curl -X POST "https://your-api-url.com/users/1/tasks/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Patient consultation",
    "description": "Review patient charts for morning rounds",
    "completed": false,
    "due_date": "2024-01-15T10:00:00"
  }'
```

## 📊 Performance & Scale

- **Response Time:** < 200ms average
- **Database:** Optimized queries with indexing
- **Concurrency:** Async FastAPI for high throughput
- **Scalability:** Stateless design for horizontal scaling

## 🚀 Deployment Pipeline

1. **Development** → Code push to GitHub
2. **CI Pipeline** → Automated testing with GitHub Actions
3. **Build** → Docker image creation
4. **Deploy** → Railway automatic deployment
5. **Monitor** → Health checks and logging

## 📚 Documentation

- **API Docs:** Auto-generated with FastAPI (Swagger UI)
- **Database Schema:** SQLAlchemy models with relationships
- **Docker Setup:** Multi-container development environment
- **Deployment Guide:** Railway cloud deployment instructions

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Create Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Jose Romo** - Backend Developer specializing in FastAPI and medical applications
- GitHub: [@JCROMO11](https://github.com/JCROMO11)
- LinkedIn: [Your LinkedIn Profile](www.linkedin.com/in/jose-carlos-romo11)

---

⭐ **Star this repository if it helped you build better APIs!**

