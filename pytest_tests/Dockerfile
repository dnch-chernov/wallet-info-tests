FROM python:3.10-slim-bullseye

WORKDIR /tests

COPY . /tests

RUN pip install -r requirements.txt

ENV BACKEND_URL "http://localhost"
ENV USDC_CONTRACT_ADDRESS "0x07865c6e87b9f70255377e024ace6630c1eaa37f"

CMD ["pytest", "-v"]