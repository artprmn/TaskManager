from hashlib import md5

import aioredis
from fastapi import APIRouter, Depends
from src.models import User_login
from database.connect_to_db import async_session
from database.actions.with_token import add_token
from database.actions.with_user import select_user, login, get_role_by_login
from src.Token import Token

login_router = APIRouter(prefix='/login', tags=['Login'])

async def redis_client():
    return await aioredis.StrictRedis(host="localhost", port="6379", db=0)

async def cache_path(path: str, response_data: str):
    async with async_session() as session:
        r = await redis_client()
        path_hash = md5(path.encode()).hexdigest()
        await r.set(path_hash, response_data, ex=3600)  # ex=3600 устанавливает срок жизни кеша на 1 час


async def get_cached_path(path: str) -> str:
    async with async_session() as session:
        r = await redis_client()
        path_hash = md5(path.encode()).hexdigest()
        cached_data = await r.get(path_hash)
        return cached_data

@login_router.get("/")
async def get_login():
    async with async_session() as session:
        cached_data = await get_cached_path('/login')
        if cached_data:
            return {"path": '/login', "cached": True, "data": cached_data}

        # Если кеша нет, генерируем ответ
        response_data = "Welcome to login page!"

        # Сохраняем результат в кеш
        await cache_path('/login', response_data)

        return {"path": '/login', "cached": False, "data": response_data}


@login_router.post("/")
async def post_login(user: User_login, client = Depends(redis_client)):
    async with async_session() as session:
        try:
            user_exists = await select_user(user.login, session)
            if user_exists:
                valid_login = await login(user.login, user.password, session)
                if valid_login:
                    role = await get_role_by_login(user.login, session)
                    token_access = Token.create_access_token({"user": user.login, "role": role})
                    token_refresh = Token.create_refresh_token({"user": user.login, "role": role})
                    await add_token(user.login, token_access, session)
                    await client.set(f'access:user:{user.login}', token_access, ex=3600)
                    await client.set(f'refresh:user:{user.login}', token_refresh, ex=3600)

                    access = await client.get(f'access:user:{user.login}')
                    refresh = await client.get(f'refresh:user:{user.login}')
                    return {
                        "message": "success",
                        "access_token": access.decode('utf-8'),
                        "refresh_token": refresh.decode('utf-8'),
                    }
                else:
                    return {"message": "Password is incorrect"}
            else:
                return {"message": f"There's no user with login '{user.login}'. Try a different one"}
        except Exception as e:
            return {"message": f"An error occurred: {e}"}
