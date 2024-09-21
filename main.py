from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
import bcrypt

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los origenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los encabezados
)

# MongoDB connection
client = MongoClient("mongodb+srv://dardo:Ds276846@cluster0.aycnp.gcp.mongodb.net/")
db = client['Chat']
users_collection = db['usuarios']
  
class User(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(user: User):
    print("Login")
    print(user)
    db_user = users_collection.find_one({"username": user.username})
    if db_user and bcrypt.checkpw(user.password.encode('utf-8'), db_user['password']):
        return {"Mensaje": "Usuario validado"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

@app.post("/register")
async def register(user: User):
    print("Register")
    print(user)
    existing_user = users_collection.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    users_collection.insert_one({"username": user.username, "password": hashed_password})
    return {"Mensaje": "Usuario registrado correctamente"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)