# ==========================================
# STAGE 1: Build React Frontend
# ==========================================
FROM node:20-alpine AS frontend-builder
WORKDIR /build

COPY frontend/package*.json ./
RUN npm install

COPY frontend/ ./
ENV VITE_API_BASE_URL=/api/v1
RUN npm run build

# ==========================================
# STAGE 2: Python Backend & Production Serving
# ==========================================
FROM python:3.11-slim

WORKDIR /app

# Install system utilities needed for building packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r ./backend/requirements.txt

# Copy Knowledge Base and Sample Logs
COPY knowledge_base/ ./knowledge_base/
COPY sample_logs/ ./sample_logs/

# Also link to root / for path-resolution tolerance
RUN ln -s /app/knowledge_base /knowledge_base 2>/dev/null || true && \
    ln -s /app/sample_logs /sample_logs 2>/dev/null || true

# Copy compiled Frontend static build from Stage 1
COPY --from=frontend-builder /build/dist ./frontend/dist
RUN mkdir -p /frontend && ln -s /app/frontend/dist /frontend/dist 2>/dev/null || true

# Copy Backend application code
COPY backend/ ./backend/

# Pre-cache the ChromaDB ONNX embedding model during build so startup is instant
RUN python -c "import chromadb; c = chromadb.Client(); col = c.create_collection('init'); col.add(documents=['init'], ids=['1'])"

WORKDIR /app/backend

EXPOSE 8000

# Render dynamically passes $PORT. Shell form ensures $PORT is expanded at runtime.
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
