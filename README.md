# FastAPI + Nuxt.js + Docker + PostgreSQL Boilerplate

## Overview

This repository provides a **full-stack boilerplate** integrating **FastAPI (backend), Nuxt.js (frontend), Docker (containerization), PostgreSQL (database), and Alembic (migrations)**. The goal is to offer an easy-to-use template for developers starting new projects with modern technologies.

## Features

- **FastAPI**: High-performance Python web framework for building APIs.
- **Nuxt.js**: Vue.js framework for building SSR and static applications.
- **Docker**: Containerization for seamless deployment.
- **PostgreSQL**: Robust and scalable database with async support.
- **SQLAlchemy & Alembic**: ORM and database migration tool.
- **Asynchronous Support**: Uses async PostgreSQL for improved performance.

## Prerequisites

Ensure you have the following installed:
- **Docker & Docker Compose**
- **Python 3.8+**
- **Node.js & npm/yarn**

## Installation & Setup

### 1. Clone the repository
```sh
 git clone https://github.com/powerfist01/fastapi-nuxt-boilerplate.git
 cd fastapi-nuxt-boilerplate
```

### 2. Setup environment variables

Create a `.env` from `.env.example` file in the root directory and configure the required.

### 3. Run with Docker

```sh
docker-compose -f docker-compose.dev.yml up --build
```

## Database Migrations

To create and apply migrations inside the backend container:
```sh
alembic upgrade head
```

## Contributing
Feel free to fork this repo, submit issues, and contribute via pull requests!

