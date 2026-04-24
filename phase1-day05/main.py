# 创建一个完整的 Todo API 原型，包含自动文档和 Pydantic 验证
# 本次虚拟安装了fastapi uvicorn pydantic
# 运行：uvicorn main:app --reload

# 简单fastapi实例
# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}


from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI, HTTPException, Path, Query

# 创建FastAPI应用
app = FastAPI(
    title="FastAPI",
    description="这是一个FastAPI示例",
    version="1.0.0",
)

# == pydantic模型定义 ==
from pydantic import BaseModel, Field, validators


class TodoCreate(BaseModel):
    """创建 TODO 时的请求体模型"""

    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="待办事项标题",
        json_schema_extra={"example": "学习 FastAPI"},
    )
    description: Optional[str] = Field(None, max_length=500)
    completed: bool = False
    priority: int = Field(1, ge=1, le=5, description="待办事项优先级1-5")
    tags: List[str] = []

    # 自定义验证器
    @validators.validate_field("title")
    def title_not_empty(cls, v):
        if not v.strip():
            raise ValueError("标题不能为空")
        return v.strip()


class TodoUpdate(BaseModel):
    """更新 TODO 时的请求体模型（所有字段可选）"""

    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    completed: Optional[bool] = None
    priority: Optional[int] = Field(None, ge=1, le=5, description="待办事项优先级1-5")
    tags: Optional[List[str]] = None


class TodoResponse(BaseModel):
    """返回 TODO 时的响应体模型"""

    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    priority: int
    tags: List[str]
    created_at: datetime
    updated_at: datetime


# == 模拟数据库 ==
todos_db = []
id_counter = 1


def find_todo_index(todo_id: int) -> int:
    """根据 TODO ID 查找 TODO 在数据库中的索引 找不到返回-1"""
    for i, todo in enumerate(todos_db):
        if todo.id == todo_id:
            return i
    return -1


# == api路由接口 ==
@app.get("/", tags=["Root"])
async def root():
    """根路径，返回欢迎信息"""
    return {
        "message": "欢迎来到FastAPI TODO API",
        "docs": "/docs",
        "redoc": "/redoc",
    }


@app.post("/todos", response_model=TodoResponse, status_code=201, tags=["Todos"])
async def create_todo(todo: TodoCreate):
    """创建 TODO TODO"""
    global id_counter
    now = datetime.now()
    new_todo = {
        "id": id_counter,
        **todo.model_dump(),
        "created_at": now,
        "updated_at": now,
    }
    todos_db.append(new_todo)
    id_counter += 1
    return new_todo


@app.get("/todos", response_model=List[TodoResponse], tags=["Todos"])
async def list_todos(
    completed: Optional[bool] = Query(None, description="是否已完成状态筛选"),
    priority: Optional[int] = Query(None, ge=1, le=5, description="按优先级筛选1-5"),
    skip: int = Query(0, ge=0, description="跳过数量"),
    limit: int = Query(10, ge=1, le=100, description="每页数量"),
):
    """获取 TODO TODO 列表,支持筛选和分页"""
    result = todos_db.copy()
    if completed is not None:
        result = [t for t in result if t["completed"] == completed]
    if priority is not None:
        result = [t for t in result if t["priority"] == priority]
    return result[skip : skip + limit]


@app.get("/todos/{todo_id}", response_model=TodoResponse, tags=["Todos"])
async def get_todo(todo_id: int = Path(..., ge=1, description="待办事项ID")):
    """获取 TODO TODO 详情"""
    index = find_todo_index(todo_id)
    if index == -1:
        raise HTTPException(status_code=404, detail="待办事项不存在")

    return todos_db[index]


@app.put("/todos/{todo_id}", response_model=TodoResponse, tags=["Todos"])
async def update_todo(
    todo_id: int = Path(..., ge=1, description="待办事项ID"),
    todo_update: TodoUpdate = Field(..., description="待办事项更新信息"),
):
    """更新 TODO TODO 详情"""
    index = find_todo_index(todo_id)
    if index == -1:
        raise HTTPException(status_code=404, detail="待办事项不存在")

    update_data = todos_db[index].update(todo_update.model_dump(exclude_unset=True))
    for key, value in update_data.items():
        todos_db[index][key] = value
    todos_db[index]["updated_at"] = datetime.now()
    return todos_db[index]


@app.delete("/todos/{todo_id}", tags=["Todos"])
async def delete_todo(todo_id: int):
    """删除 TODO TODO"""
    index = find_todo_index(todo_id)
    if index == -1:
        raise HTTPException(status_code=404, detail="待办事项不存在")
    deleted = todos_db.pop(index)
    return {"message": f"Todo {todo_id} 已删除", "deleted": deleted}


@app.get("/health", tags=["System"])
async def health_check():
    """健康检查接口"""
    return {"status": "healthy", "todo_count": len(todos_db)}
