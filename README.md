# Evalution Criteria

This project provides a Django-based application for integrating with the SUMSUB API to manage applicant data and document uploads for verification.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Features

- Upload a csv file that contains software requirements and its corresponding evaluation criteria
- The program aim to output the minimum combination of both that could lead to an effective system development
- It can output this as pure json or as a new csv file

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.8 or later
- pip (Python package installer)
- Git (optional, for cloning the repository)

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/OkayJosh/evaluate_requirements
   cd evaluate_requirements
   
2. **Create and activate a virtual environment:**

##### You can use venv (Python's built-in virtual environment module) to create a virtual environment.

   ```bash
    python -m venv .venv
   ```

For Windows:

```bash
  .venv\Scripts\activate
```

For macOS/Linux:
```bash
source .venv/bin/activate
```

3. **install the requirements packages for the project:**

```bash
    pip install -r requirements.txt
```

4. **There is no .env file in the root directory of this project**

5. **No need to run database migrations:**

Apply the migrations to set up your database:

```bash
python manage.py migrate
```
6. **Start the application**

```bash

python manage.py runserver
```

#### You should see output indicating that the server is running, usually at http://127.0.0.1:8000/.

### API Endpoints
```
You can access the following API endpoints (replace <base_url> with your local server URL):

Upload Document: POST <base_url>/api/evaluate/
```

### License
This project is licensed under the MIT License. See the LICENSE file for more details.