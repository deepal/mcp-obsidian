# Use Python 3.12 slim image as base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml .
COPY src/ ./src/
COPY README.md .

# Install dependencies
RUN pip install --no-cache-dir .

# Run the application
CMD ["python", "-m", "src.mcp_obsidian"]
