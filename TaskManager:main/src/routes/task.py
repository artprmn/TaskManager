from fastapi import APIRouter, Header, HTTPException, Depends
from fastapi.openapi.models import Response
from starlette import status
from fastapi.middleware.cors import CORSMiddleware

from database.actions.with_token import valid_token, valid_cache
from src.models import Task_py
from database.models import Task
from src.Token import Token
from database.connect_to_db import async_session
from database.actions.with_task import select_task_id, select_task, create_task, update_task, owner

task_router = APIRouter(prefix='/task', tags=['Task'])


class CustomException(HTTPException):
    def __init__(self, detail: str, status_code: int = 401):
        super().__init__(status_code=status_code, detail=detail)




@task_router.get("/{id}")
async def get_by_id(id: int, Authorization: str = Header(None)):
    if Authorization is None:
        raise CustomException(status_code=401, detail="Where's your token?")

    async with async_session() as session:
        try:
            if Authorization.startswith("Bearer "):
                token = Authorization[7:]
            payload = Token.decode_token(token)
            owner1 = payload.get("user")

            if await owner(id, owner1, session):
                if await valid_token(owner1, token, session):
                    success = await select_task(id, session)
                    if success:
                        return {
                            "id": f"{success.id}",
                            "name": f"{success.name}",
                            "description": f"{success.description}"
                        }
                    else:
                        return {"message": f"Task with id '{id}' not found."}
                else:
                    return {"message": "Your token is old"}
            else:
                raise HTTPException(
                    status_code=403,
                    detail=f"Permission denied"
                )
        except Exception as e:
            raise HTTPException(
                status_code=401,
                detail=f"{e}"
            )


@task_router.get("/")
async def get_task(limit: int = 10):
    return {"message": "Welcome to task creation page"}


@task_router.post("/")
async def post_task(task: Task_py, authorization: str = Header(...)):
    async with async_session() as session:
        try:
            if authorization.startswith("Bearer "):
                token = authorization[7:]
            payload = Token.decode_token(token)
            owner = payload.get("user")
            print(payload)

            # if await valid_token(owner, token, session):
            #     task1 = Task(name=task.name, description=task.description, owner=owner)
            #     await create_task(task1, session)
            #     return {"message": "success"}
            if await valid_cache(owner, token):
                task1 = Task(name=task.name, description=task.description, owner=owner)
                await create_task(task1, session)
                return {"message": "success"}
            return {"message": "Your token is old"}
        except HTTPException as e:
            raise e
        except Exception as e:
            return {"message": f"error: {e}"}


@task_router.put("/")
async def put_task(task: Task_py):
    async with async_session() as session:
        try:
            success = await update_task(task.name, task.description, session)
            if success:
                return {"message": "success"}
            else:
                return {"message": f"Task with name '{task.name}' not found."}
        except Exception as e:
            return {"message": f"error: {e}"}


@task_router.delete("/")
async def delete_task(id: int, authorization: str = Header(...)):
    async with async_session() as session:
        try:
            if authorization.startswith("Bearer "):
                token = authorization[7:]
            else:
                return {"message": "Authorization header is invalid."}

            payload = Token.decode_token(token)
            owner = payload.get("user")

            if await valid_token(owner, token, session):
                success = await select_task_id(id, session)
                if not success:
                    return {"message": f"Task with ID '{id}' not found."}

                deleted = await delete_task(id, session)
                await session.commit()
                if deleted:
                    return {"message": f"Task with ID '{id}' deleted successfully."}
                else:
                    return {"message": f"Task with ID '{id}' could not be deleted."}
            else:
                return {"message": "Your token is invalid or expired."}
        except Exception as e:
            return {"message": f"error: {e}"}
