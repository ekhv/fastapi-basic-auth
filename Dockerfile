FROM python:slim
ENV PYTHONUNBUFFERED=1
WORKDIR	/home
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN adduser --disabled-password --no-create-home user
COPY main.py .


USER user
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
