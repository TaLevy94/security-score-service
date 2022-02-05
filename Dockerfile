FROM python:3.7-alpine3.15

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apk add gcc libffi-dev libstdc++ build-base linux-headers git npm
RUN /usr/bin/npm install depcheck -g

RUN adduser -D worker
USER worker
WORKDIR /home/worker
ENV PATH="/home/worker/.local/bin:${PATH}"

COPY requirements.txt ./

RUN /usr/local/bin/python -m pip install --no-cache-dir -r requirements.txt
COPY ./src/ ./
EXPOSE 5000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]