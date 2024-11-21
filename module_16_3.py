from fastapi import FastAPI


users = {'1': 'Имя: Example, возраст: 18'}
app = FastAPI()


@app.get("/users")
async def get_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def post_user(username: str, age: int) -> str:
    new_user =  f"Имя: {username}, возраст: {age}"
    users[str(len(users) + 1)] = new_user
    user_id = len(users)
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f"User № {user_id} has been deleted"



