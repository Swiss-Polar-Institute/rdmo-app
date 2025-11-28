FROM debian:buster-slim
ENV PYTHONBUFFERED 1

# --- Use only archive.debian.org main repo because Buster security repo is gone ---
RUN echo "deb http://archive.debian.org/debian buster main contrib non-free" > /etc/apt/sources.list && \
    echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99no-check-valid-until

RUN mkdir -p /code/requirements
WORKDIR /code

COPY ./requirements/base.txt \
     ./requirements/mysql.txt \
     ./requirements/gunicorn.txt \
     /code/requirements/

# --- Install system dependencies from archive ---
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3-pip python3-setuptools python3-venv python3-wheel libpython3-dev \
    gcc git build-essential \
    libmariadb-dev libmariadb-dev-compat libmariadb3 mariadb-client \
    libxml2-dev libxslt-dev zlib1g-dev \
    pandoc texlive texlive-xetex lmodern librsvg2-bin

# --- Setup Python virtual environment ---
RUN python3 -m venv venv
ENV PATH="/code/venv/bin:$PATH"
RUN pip3 install --upgrade pip
RUN pip3 install -r /code/requirements/base.txt \
    -r /code/requirements/mysql.txt \
    -r /code/requirements/gunicorn.txt

# --- Clean up unnecessary packages ---
RUN apt-get purge -y libmariadb-dev-compat gcc libpython3-dev && \
    apt-get autoremove -y && \
    apt-get clean

COPY entrypoint.sh /code
COPY ./config /code/config/
COPY ./manage.py /code/
COPY ./tools/wait-for-mysql.sh /code/

ENTRYPOINT ["/code/entrypoint.sh"]
