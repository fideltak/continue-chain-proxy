FROM python:3.11.2-alpine
COPY src /src
WORKDIR /src
RUN pip install -r requirements.txt
CMD ["fastapi", "run", "proxy.py"]