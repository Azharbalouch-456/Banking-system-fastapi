Banking System FastAPI

A simple banking backend built with FastAPI.
It includes basic features like authentication, deposit, bank transfer, and balance updates.

Features

User login

Deposit money

Bank transfer

Check balance

FastAPI documentation at /docs

How to Run
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn
uvicorn main:app --reload

Endpoints

GET / – API check

POST /authenticate – User login

POST /deposit – Add money

POST /bank-transfer – Transfer money
