# Project Analysis: Bank API

## Overview

This project is a simple banking API built using the Python FastAPI framework. It provides basic banking functionalities through a set of API endpoints. The entire application logic is contained within the `main.py` file.

## Technologies Used

- **Backend:** Python
- **API Framework:** FastAPI
- **Data Validation:** Pydantic

## Core Functionality

The API exposes the following endpoints:

-   `/authenticate`: Handles user authentication.
-   `/deposit`: Allows users to deposit funds into their accounts.
-   `/bank-transfer`: Enables transferring funds between users.

## Data Storage

The application uses a simple in-memory Python dictionary (`user_balances`) to store user account balances.

**Important:** This means the data is not persistent. All balances will be reset if the application is restarted.

## Key Files

-   `main.py`: The single source file containing all the application code, including API routes, business logic, and data storage.

## How to Run

The project likely includes a startup script. To run the server, execute the following command in your terminal:

```powershell
./start_server.ps1
```
