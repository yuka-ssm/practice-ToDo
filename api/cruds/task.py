from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model
import api.schemas.task as task_schema


async def create_task(
    db: AsyncSession, task_create: task_schema.TaskCreate
) -> task_model.Task:
    task = task_model.Task(title=task_create.title)
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task
