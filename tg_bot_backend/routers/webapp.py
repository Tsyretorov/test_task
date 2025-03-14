from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from pydantic import BaseModel
import httpx
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BOT_TOKEN = ""

class UserDataRequest(BaseModel):
    selected_date: str

shared_data = {}

@app.post("/get-user-data")
async def get_user_data(request: UserDataRequest):
    try:
        selected_date = request.selected_date

        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
            )
            updates = response.json().get("result", [])

            if updates:
                last_update = updates[-1]
                user = last_update["message"]["from"]

                user_data = {
                    "first_name": user.get("first_name"),
                    "last_name": user.get("last_name"),
                    "username": user.get("username"),
                    "selected_date": selected_date,
                }

                share_id = str(uuid.uuid4())
                shared_data[share_id] = user_data

                return {
                    "success": True,
                    "user": user_data,
                    "share_link": f"http://localhost:8000/share/{share_id}",
                }
            else:
                return {"success": False, "message": "Нет новых обновлений"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")

@app.get("/share/{share_id}", response_class=HTMLResponse)
async def get_shared_data(share_id: str):
    if share_id in shared_data:
        user_data = shared_data[share_id]
        return f"""
        <html>
            <head>
                <title>Данные пользователя</title>
            </head>
            <body>
                <h1>Данные пользователя</h1>
                <p>Имя: {user_data['first_name']}</p>
                <p>Фамилия: {user_data['last_name']}</p>
                <p>Username: {user_data['username']}</p>
                <p>Дата: {user_data['selected_date']}</p>
            </body>
        </html>
        """
    else:
        raise HTTPException(status_code=404, detail="Данные не найдены")