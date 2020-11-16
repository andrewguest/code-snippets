### What docker-compose.yml does:

1. Starts a database container based on the MongoDB image, without exposing the MongoDB port (27017) outside the Docker network for security reasons.
2. Builds the API image, if needed.
3. Uses gunicorn to start 1 uvicorn worker process to server the FastAPI application.
4. Forwards the host port 5050 to port 5000 on the container.



### Expected project structure:

```
microservices/
  |- this_microservice/
    |- app/
      |- this_microservice_api.py
    |- database/
    |- routes/
    |- tests/
    |- Dockerfile
    |- requirements.txt
    |- docker-compose.yml
```