sudo lsof -t -i tcp:${SERVICE_PORT} | xargs kill -9
