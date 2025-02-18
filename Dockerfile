FROM python:3.12.9-bullseye

ARG ENV_TYPE=development

ENV APP_HOME /backend

WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y --allow-unauthenticated vim cron

COPY requirements.txt $APP_HOME

RUN pip install --root-user-action=ignore --upgrade pip
RUN pip3 install --root-user-action=ignore -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
