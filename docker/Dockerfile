# FROM python:3.10

# WORKDIR /app
# COPY . /app

# RUN pip install --upgrade pip
# RUN pip install -r requirements/requirements.txt

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Use the official Python base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . .
# COPY requirements.txt .
# COPY wait-for.sh /wait-for.sh

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements/requirements.txt

# Run FastAPI app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]