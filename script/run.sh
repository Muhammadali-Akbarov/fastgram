#!/bin/sh
if [ "$IS_DEBUG_MODE" = "true" ]; then
  uvicorn main:app --reload --port ${SERVICE_PORT} --host 0.0.0.0
else
  uvicorn main:app --port ${SERVICE_PORT} --host 0.0.0.0
fi
