#!/bin/bash
# Startup script for Career Guidance Chatbot API
# Automatically kills any existing process on port 8000

cd "$(dirname "$0")"

# Kill any existing process on port 8000
echo "🔄 Checking for existing processes on port 8000..."
lsof -ti:8000 | xargs kill -9 2>/dev/null && echo "✅ Killed existing process" || echo "✅ Port 8000 is free"

# Activate virtual environment
source venv/bin/activate

# Start the server
echo "🚀 Starting Career Guidance API on http://localhost:8000"
uvicorn api.app:app --reload --host 0.0.0.0 --port 8000
