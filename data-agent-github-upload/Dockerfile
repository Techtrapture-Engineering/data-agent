FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY backend /app/backend

WORKDIR /app/backend

ENV GOOGLE_GENAI_USE_VERTEXAI=true
ENV GOOGLE_CLOUD_PROJECT=tt-labs-001
ENV GOOGLE_CLOUD_LOCATION=us-central1

EXPOSE 8080

CMD ["adk", "web", "/app", "--host", "0.0.0.0", "--port", "8080"]