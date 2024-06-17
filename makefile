run.image:
	docker-compose down
	docker-compose up --build

run.bot:
	uvicorn main:app --port ${SERVICE_PORT} --host 0.0.0.0

run.celery.worker:
	celery -A app.bot.services.external.celery.tasks worker --loglevel=info --concurrency=1 --queues=example_queue

run.celery.beat:
	celery -A app.bot.services.external.celery.tasks beat -l INFO

logs:
	docker-compose logs
