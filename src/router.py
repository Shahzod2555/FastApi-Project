from typing import Annotated, Dict
from repository import TaskRepository
from fastapi import APIRouter, Depends

from src.schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix='/task'
)


@router.post('')
async def add_task(task: Annotated[STaskAdd, Depends()]) -> dict[str, bool | int]:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get('')
async def get_task() -> list[STask]:
    return await TaskRepository.get_all()
