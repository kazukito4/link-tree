FROM python:3

ADD https://astral.sh/uv/install.sh /uv-installer.sh

RUN sh /uv-installer.sh && rm /uv-installer.sh

ENV PATH="/root/.local/bin/:$PATH"

WORKDIR /src

COPY . . 

RUN pip install uv

CMD [ "uv","run", "src/main.py"]