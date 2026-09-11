#!/usr/bin/env bash
# ==============================================================================
# CyberSentinel AI - Local Development Runner
# Launches FastAPI Backend (Port 8000) and React Vite Frontend (Port 5173)
# ==============================================================================

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="$PROJECT_ROOT/backend"
FRONTEND_DIR="$PROJECT_ROOT/frontend"

echo "=================================================================="
echo "🛡️  STARTING CYBERSENTINEL AI SECURITY OPERATIONS CENTER"
echo "=================================================================="

# Function to handle shutdown
cleanup() {
    echo ""
    echo "Shutting down CyberSentinel AI services..."
    kill $(jobs -p) 2>/dev/null || true
    echo "Services stopped cleanly."
    exit 0
}
trap cleanup SIGINT SIGTERM

# 1. Start Backend
echo "📡 Launching FastAPI SOC Backend on http://127.0.0.1:8000 ..."
cd "$BACKEND_DIR"
"$BACKEND_DIR/venv/bin/uvicorn" app.main:app --host 127.0.0.1 --port 8000 --reload &
BACKEND_PID=$!

# Wait for backend to wake up
sleep 2

# 2. Start Frontend
echo "💻 Launching React SOC Dashboard on http://127.0.0.1:5173 ..."
cd "$FRONTEND_DIR"
npm run dev &
FRONTEND_PID=$!

echo "=================================================================="
echo "✅ CyberSentinel AI SOC Platform is LIVE!"
echo "   • SOC Web Dashboard: http://127.0.0.1:5173"
echo "   • Interactive OpenAPI Docs: http://127.0.0.1:8000/docs"
echo "   • Default Analyst Login: analyst / analyst123"
echo "   • Default Admin Login:   admin / admin123"
echo "=================================================================="
echo "Press Ctrl+C to terminate all services."

wait
