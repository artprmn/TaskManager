

# 🌟 **TaskManager** 🌟

TaskManager is a modern task management application designed with a focus on **secure authorization** using **JWT (JSON Web Tokens)**. This project was created to explore and implement methodologies of interest in the areas of authorization and token management, emphasizing security and performance.

---

## 🚀 **Features**

### 🔒 **JWT Authorization**
- Supports **secure authorization** via JWT.
- Utilizes a **complex secret** for token signing, ensuring resistance to brute-force attacks.
- Implements synchronous encryption for simplicity and security.

### ⚡ **Asynchronous Architecture**
- The entire application stack supports asynchronous operations, enabling high concurrency without thread blocking.
- Uses the asynchronous version of SQLAlchemy for database interactions.
- Asynchronous FastAPI routes ensure high performance and responsiveness.

### ♻️ **Refresh Tokens**
- Implements a token refresh system with each refresh token stored in the database.
- Every refreshed token invalidates the previous one, even if the previous token hasn't expired. This prevents reuse and enhances security.

### 🔑 **Role-Based Access Control (RBAC)**
- Supports role-based access control ("guest", "user", "admin").
- Restricts access to resources and actions based on roles.
- Seamlessly integrates with JWT for access validation.

### 💾 **Database**
- Data is stored using **SQLite**, ensuring ease of deployment and usage.
- Database management is handled through **SQLAlchemy ORM** for convenient query handling.

### 🧰 **Session Caching with Redis**
- User sessions are cached using **Redis**, enabling quick access to authorization data.
- JWT tokens are stored in the cache for fast reading and verification.
- **Cache expiration** for tokens is managed, ensuring timely rotation.

---

## 🛠 **Technical Details**

- **Programming Language:** Python.
- **Framework:** FastAPI.
- **Database:** SQLite with SQLAlchemy ORM.
- **Cache:** Redis for session and token data caching.
- **Token Signing Algorithm:** HMAC (synchronous), with plans to migrate to **asynchronous encryption** (e.g., RSA).
- **Key Dependencies:**
  - `FastAPI`
  - `PyJWT` for token management.
  - `SQLAlchemy` for ORM.
  - `aioredis` for asynchronous caching.

---

## 💡 **Project Goals**

The main goals of this project are to **explore and implement methodologies** of interest, specifically:

1. Developing a **secure authorization system** using JWT.
2. Gaining in-depth knowledge of refresh token workflows, ensuring secure rotation and access control.
3. Implementing **role-based access control** for restricted access.
4. Practicing database management and ORM tools like SQLAlchemy.
5. Integrating caching with Redis to improve performance and scalability.

---

## 🔮 **Future Plans**

- 🚧 Migrating from synchronous encryption to **asynchronous encryption** (e.g., RSA or ECDSA).
- 🛠 Expanding TaskManager functionality to support:
  - Scalable databases.
  - External API integration.
  - A user-friendly interface.
- 🌐 Enhancing caching functionality:
  - Task caching for quick access.
  - Temporary data storage for analytics.

---

## 📦 **Installation and Launch**

### 📥 **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-username/taskmanager.git
cd taskmanager
```

### 🛠 **Step 2: Install Dependencies**
It is recommended to use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # for Linux/MacOS
venv\Scripts\activate     # for Windows
pip install -r requirements.txt
```

### ▶️ **Step 3: Run the Application**
```bash
python app.py
```
The application will be available at: `http://127.0.0.1:5000`.

---

### 🖥 Deployment on a Server
The application is deployed on a virtual host (TimeWeb) and accessible at: http://194.87.133.31:8000/docs

### 🐳 Docker Deployment
The application is containerized with Docker for easy and consistent deployment.

To deploy the application in Docker:

Build the container:
```bash
docker build -t taskmanager .
```
Run the container:
```bash
docker run -d -p 8000:8000 taskmanager
```
The application will be accessible on port 8000.

---

## 🛡 **Security**

- A complex secret is used for token signing and is automatically generated.
- Each refresh token is stored in the database and replaced upon refresh, preventing reuse.
- All tokens are time-limited.
- **Sessions are cached in Redis**, reducing token verification time.
- The role-based system ensures restricted access to actions and data based on privileges.

---

## 📚 **API Documentation**

| Method   | Path                | Description                                                     |
|----------|---------------------|-----------------------------------------------------------------|
| `POST`   | `/login`            | User login and JWT issuance.                                   |
| `POST`   | `/refresh`          | Refreshes the token using a refresh token.                     |
| `GET`    | `/tasks`            | Retrieves a list of tasks.                                     |
| `POST`   | `/tasks`            | Creates a new task.                                            |
| `GET`    | `/tasks/{id}`       | Updates an existing task.                                      |
| `DELETE` | `/tasks/{id}`       | Deletes a task.                                                |
| `GET`    | `/admin`            | Provides access to admin functions (admin-only).               |

---

## ❤️ **Acknowledgments**

This project is the result of my interest in modern authorization methodologies. I hope it proves helpful and inspires new ideas! 🙌



