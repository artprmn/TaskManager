
### 🌟 TaskManager 🌟

**TaskManager** is a modern task management application designed with a focus on secure authorization using **JWT (JSON Web Tokens)**. This project was created to explore and implement methodologies related to token-based authentication, with an emphasis on security and performance.

---

### 🚀 Features

#### 🔒 JWT Authorization
- Secure authorization using JWT.
- Complex secret key for signing tokens, making them resistant to brute-force attacks.
- Synchronous encryption ensures simplicity and security.

#### ⚡ Asynchronous Architecture
- The entire application stack supports asynchronous processing, enabling it to handle numerous requests simultaneously without blocking threads.
- Asynchronous SQLAlchemy is used for database operations.
- Asynchronous routes in FastAPI provide high performance and responsiveness.

#### ♻️ Refresh Tokens
- Implemented a refresh token system, with each token stored in the database.
- Old refresh tokens are invalidated upon use, preventing replay attacks and improving security.

#### 🔑 Role-based Access Control
- Includes a role-based system ('guest', 'user', 'admin').
- Access to various resources and actions is restricted based on roles.
- Seamless integration with JWT for access control verification.

#### 💾 Database Management
- SQLite is used for storing data, ensuring simplicity in deployment and usage.
- SQLAlchemy ORM is utilized for convenient database interactions.

#### 🧰 Session Caching with Redis
- User sessions are cached in Redis, enabling quick access to authorization data.
- JWT tokens are stored in the cache for faster reads and validation.
- Token expiration is controlled to ensure timely rotation.

---

### 🛠 Technical Details

- **Programming Language**: Python
- **Framework**: FastAPI
- **Database**: SQLite with SQLAlchemy ORM
- **Caching**: Redis for session and token caching
- **Token Signing Algorithm**: HMAC (synchronous), with plans to adopt asynchronous encryption (e.g., RSA)

#### Key Dependencies:
- **FastAPI**: Web framework
- **PyJWT**: For token management
- **SQLAlchemy**: For ORM
- **aioredis**: For asynchronous caching

---

### 💡 Project Goals

- Build a secure authorization system using JWT.
- Deep dive into refresh token mechanisms for rotation and access control.
- Implement role-based access control for restricted operations.
- Practice database management using SQLAlchemy.
- Leverage Redis for caching to enhance performance and scalability.

---

### 🔮 Future Plans

- 🚧 Transition from synchronous encryption to asynchronous encryption (e.g., RSA or ECDSA).
- 🛠 Expand TaskManager functionality to support:
  - Scalable databases
  - Integration with external APIs
  - Creation of a user-friendly interface
- 🌐 Enhance caching functionality:
  - Cache task data for quick access
  - Store temporary data for analytics

---

### 📦 Installation and Setup

#### 📥 Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/taskmanager.git
cd taskmanager
```

#### 🛠 Step 2: Install Dependencies
It is recommended to use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
```

#### ▶️ Step 3: Run the Application
```bash
python app.py
```
The application will be available at: `http://127.0.0.1:5000`.

---

### 🖥 Deployment

#### Hosted on TimeWeb
The application is deployed on a virtual hosting platform (TimeWeb) and is accessible at:  
`http://194.87.133.31:8000/docs`

#### 🐳 Docker Deployment
The application is containerized with Docker for easy and consistent deployment.

To deploy with Docker:
- Build the container:
  ```bash
  docker build -t taskmanager .
  ```
- Run the container:
  ```bash
  docker run -d -p 8000:8000 taskmanager
  ```
The application will be available on port `8000`.

---

### 🛡 Security

- A complex secret key is used for signing tokens, generated automatically.
- Each refresh token is stored in the database and invalidated upon reuse, preventing replay attacks.
- Tokens are time-bound with strict expiration.
- User sessions are cached in Redis for efficient token validation.
- Role-based access control restricts operations based on privileges.

---

### 📚 API Documentation

| Method | Path            | Description                                  |
|--------|-----------------|----------------------------------------------|
| POST   | `/login`        | User login and JWT issuance.                |
| POST   | `/refresh`      | Refresh token and obtain a new JWT.         |
| GET    | `/tasks`        | Retrieve a list of tasks.                   |
| POST   | `/tasks`        | Create a new task.                          |
| GET    | `/tasks/{id}`   | Retrieve a specific task by ID.             |
| DELETE | `/tasks/{id}`   | Delete a task by ID.                        |
| GET    | `/admin`        | Access admin-specific functions (admin only).|

