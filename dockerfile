FROM python:3.10-slim
ENV TOKEN='7217776780:AAFqrt1vVVfqv6R8q0l4U5NwbFKrnBMwIWs'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "bot.py"]