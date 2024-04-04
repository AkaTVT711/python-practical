from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "xxxxxxxx"
    db_user = models.User(
        email=user.email, hash_password=fake_hashed_password, username=user.username,
        first_name=user.first_name, last_name=user.last_name, is_admin=user.is_admin, is_active=user.is_active
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()


def get_task_by_email(db: Session, email: str):
    # Subquery to fetch the owner_id directly
    subquery = db.query(models.User.id).filter(models.User.email == email).subquery()

    # Query tasks using the subquery to filter by owner_id
    task = db.query(models.Task).filter(models.Task.owner_id == subquery).first()

    return task


def get_task_by_id(db: Session, owner_id: int):
    return db.query(models.Task).filter(models.Task.owner_id == owner_id).first()


def create_user_task(db: Session, task: schemas.TaskCreate, user_id: int):
    db_task = models.Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
