# Assignment 1 - Build Your First API Endpoint

## Overview

This project is a simple FastAPI backend with two JSON endpoints.

It demonstrates:
- Creating a FastAPI server
- Creating GET endpoints
- Returning JSON responses
- Testing using a browser and curl

---

## Technologies Used

- Python 3.14
- FastAPI
- Uvicorn

---

## Project Structure

```text
assignment1-build-your-first-api-endpoint/
│
├── main.py
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Rnehasree19/assignment1-build-your-first-api-endpoint.git
```

Move into the project folder:

```bash
cd assignment1-build-your-first-api-endpoint
```

Install the required packages:

```bash
py -m pip install fastapi uvicorn
```

---

## Run the Server

```bash
py -m uvicorn main:app --reload
```

The server will start at:

```text
http://127.0.0.1:8000
```

---

## API Endpoints

### Greeting Endpoint

**Method:** `GET`

**URL**

```text
/greeting
```

**Response**

```json
{
    "greeting": "hello"
}
```

---

### Name Endpoint

**Method:** `GET`

**URL**

```text
/name
```

**Response**

```json
{
    "name": "Neha"
}
```

---

## Testing in Browser

Open the following URLs in your browser:

```text
http://127.0.0.1:8000/greeting
```

```text
http://127.0.0.1:8000/name
```

---

## Testing with curl

Greeting endpoint:

```bash
curl http://127.0.0.1:8000/greeting
```

Name endpoint:

```bash
curl http://127.0.0.1:8000/name
```

---

## Author

**Neha**
