FROM python:3.11-slim
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    python3-dev

WORKDIR /PetAndOwners

COPY docker/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy django code to docker
COPY src/backend /PetAndOwners

COPY docker/backend/test_data.json /test_data/test_data.json

COPY docker/backend/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]