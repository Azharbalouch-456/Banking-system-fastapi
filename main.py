from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_balances = {
    "Alice": 1000.00, # Example initial balance
    "Bob": 500.00     # Example initial balance
}

class User(BaseModel):
    name: str

class Deposit(BaseModel):
    name: str
    amount: float

class BankTransfer(BaseModel):
    sender: str
    receiver: str
    amount: float

# @app.get("/")
# def home():
#     return {"message": "Hello World"}

@app.post("/authenticate")
def authenticate(user: User):
    if user.name not in user_balances:
        user_balances[user.name] = 0.00 # Initialize new user with 0 balance
    return {"message": f"Hello {user.name}, you are authenticated", "current_balance": user_balances[user.name]}

@app.post("/deposit")
def deposit(deposit: Deposit):
    global user_balances

    if deposit.amount <= 0:
        return {"message": "Deposit amount must be positive.", "current_balance": user_balances.get(deposit.name, 0.00)}

    if deposit.name not in user_balances:
        user_balances[deposit.name] = 0.00 # Initialize new user with 0 balance if they don't exist
    
    user_balances[deposit.name] += deposit.amount
    return {"message": f"Deposit of {deposit.amount} to {deposit.name} successful.", "current_balance": user_balances[deposit.name]}

@app.post("/bank-transfer")
def bank_transfer(transfer: BankTransfer):
    global user_balances

    if transfer.amount <= 0:
        return {"message": "Transfer amount must be positive.", "sender_balance": user_balances.get(transfer.sender, 0.00)}

    if transfer.sender not in user_balances:
        return {"message": f"Sender {transfer.sender} not found.", "sender_balance": user_balances.get(transfer.sender, 0.00)}

    if user_balances[transfer.sender] < transfer.amount:
        return {"message": "Insufficient funds.", "sender_balance": user_balances[transfer.sender]}

    user_balances[transfer.sender] -= transfer.amount

    if transfer.receiver not in user_balances:
        user_balances[transfer.receiver] = 0.00 # Initialize receiver if they don't exist
    user_balances[transfer.receiver] += transfer.amount

    auth_user_receiver = User(name=transfer.receiver)
    auth_message_receiver = authenticate(auth_user_receiver)

    return {
        "message": f"Transfer of {transfer.amount} from {transfer.sender} to {transfer.receiver} successful.",
        "sender_balance": user_balances[transfer.sender],
        "receiver_authentication_status": auth_message_receiver
    }