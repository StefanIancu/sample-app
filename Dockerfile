FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# NOTE: deliberate break to test orkestr's consecutive-failure help banner.
# This file does not exist in the repo, so the build fails at this COPY.
COPY this-file-does-not-exist.txt ./

# Bring in the whole app, including job.py so orkestr Jobs can run it inside
# this same image.
COPY . .

# Run as non-root (orkestr also hardens the container at runtime).
RUN useradd -m appuser && chown -R appuser /app
USER appuser

EXPOSE 8000

# Default (web service) command. Jobs override this with their own command,
# e.g. `python job.py`.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]