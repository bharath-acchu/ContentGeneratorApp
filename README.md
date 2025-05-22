# 🧠 Content Generator App

This project is a full-stack AI web prototype that:
- Accepts user input
- Generates casual and formal responses using Gemini API
- Saves interactions to a PostgreSQL database
- Displays history and responses via a Streamlit frontend

---

## Features

- ⚡️ FastAPI backend (REST API)
- 💬 Gemini-powered AI responses (casual + formal)
- 🗃️ PostgreSQL database integration
- 🖼 Streamlit frontend UI
- ✅ Fully tested with Pytest

---

## Getting Started

### Prerequisites

- Python 3.9+ (recommend using Anaconda or virtualenv)
- PostgreSQL installed and running
- A free Gemini API Key: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

---

## Clone the Repository

```bash
git https://github.com/bharath-acchu/ContentGeneratorApp.git
cd ContentGeneratorApp

````
----

## Project Structure

```
ContentGeneratorApp/
├── backend/            # FastAPI app
├── frontend/           # Streamlit UI
├── tests/              # Unit + integration tests
├── .env                # Secret keys (add your own keys, please create .env file if not present when you clone)
├── requirements.txt    # Python dependencies
├── create_table.py     # Script to initialize DB tables
├── README.md

```
---------
## How to run? 
### Follow the below steps :

## Step 1: Set Up Virtual Environment

-----
```bash
# Using Conda
conda create -n <env_name> python=3.10 -y
conda activate <env_name>

```
----

## Step 2: Install Dependencies

------
```bash
pip install -r requirements.txt

```
-----

## Step 3: Set Up Environment Variables
---------
Create a file named .env in the root folder:
```bash
GEMINI_API_KEY=your_actual_gemini_api_key
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/ai_prompts_db

```
---------
## Step 4: Create PostgreSQL Database
---------
```bash
psql -U postgres
CREATE DATABASE ai_prompts_db;
\q

```
--------

## Step 5: Create Database Tables
---------
```bash
python create_table.py

```
---------

## Step 6: Run Backend (FastAPI)
--------
```bash
uvicorn backend.main:app --reload

```
--------

## Step 7: Run Frontend (Streamlit)
---------
```bash
streamlit run frontend/app.py

```
---------

## Step 8: Run Tests
------
```bash
pytest tests/

```
------

## Few Screenshots from the app

### Screenshot 1: Login
![](img/login.png)

---------------------------------------
### Screenshot 2: Main app search and generate
![](img/screen1.png)


### Screenshot 3: Main app stored history and logout
![](img/screen2.png)


### Demo Link
[Click here](https://ai-frontend-8zo0.onrender.com/)






