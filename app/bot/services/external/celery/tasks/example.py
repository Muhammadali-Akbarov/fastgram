"""
the example task
"""
from app.bot.services.external.celery import celery_app


@celery_app.task
def example_task(name: str) -> None:
    """
    simple example task for celery app
    """
    print(f"Hello - {name}")
