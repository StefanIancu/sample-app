FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Intentionally broken: this file does not exist in the repo, so Kaniko
# will fail with "failed to get fileinfo ... no such file or directory".
# Used to verify the cleaned error callout on dev.
COPY this_file_does_not_exist.py .

COPY . .

EXPOSE 8000
CMD ["python", "main.py"]
