from database import create_tables, delete_tables
from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Очищена")
    await create_tables()
    print("Создана")
    yield
    print("Выключения")

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
