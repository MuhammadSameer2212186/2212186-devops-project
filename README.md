# 2212186-devops-project

**Student:** Muhammad Sameer  
**Registration Number:** 2212186  
**Supervisor:** Sir Afaq Ahmed  

## Live URL
http://100.26.137.51:8000

## Architecture
- **Web Service:** FastAPI running on port 8000
- **Database:** PostgreSQL 15 on port 5432
- **Containers:** Docker + Docker Compose
- **CI Pipeline:** GitHub Actions (flake8 + pytest)
- **CD Pipeline:** GitHub Actions (auto deploy to EC2 on push)
- **Cloud Server:** AWS EC2 t2.micro (Ubuntu)

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check with student reg number |
| POST | /students | Add a new student record |
| GET | /students | Get all student records |
| GET | /students/{reg_no} | Get one student by reg number |

## Setup Instructions

### Run Locally
1. Clone the repo:
   git clone https://github.com/MuhammadSameer2212186/2212186-devops-project.git
2. Start containers:
   docker-compose up --build
3. Open browser:
   http://localhost:8000/health

### Run on EC2
1. SSH into server
2. Run: docker-compose -f docker-compose.prod.yml up --build -d
3. Open: http://100.26.137.51:8000/health
