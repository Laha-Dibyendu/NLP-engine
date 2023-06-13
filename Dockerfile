FROM python:3.9-slim

# Install & use pipenv
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy
RUN python -m spacy download en_core_web_lg
RUN python -m spacy download en_core_web_md
RUN python -m spacy download en_core_web_sm

WORKDIR /app
COPY . /app

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "api.py"]