FROM debian:buster-slim
ENV PYTHONBUFFERED 1

# --- Fix Debian archive repos because Buster is EOL ---
RUN sed -i 's|deb.debian.org/debian|archive.debian.org/debian|g; \
            s|security.debian.org/debian-security|archive.debian.org/debian-security|g; \
            s|buster/updates|buster|g' /etc/apt/sources.list

# Disable "valid-until" check (archive repos have expired signatures)
RUN apt-get -o Acquire::Check-Valid-Until=false update

RUN mkdir -p /code/requirements
WORKDIR /code

COPY ./requirements/base.txt \
     ./requirements/mysql.txt \
     ./requirements/gunicorn.txt \
     /code/requirements/

# --- Install packages, using available versions in Buster archive ---
RUN apt-get install --no-install-recommends -y \
    python3-pip python3-setuptools python3-venv python3-wheel libpython3-dev \
    gcc git build-essential \
    libmariadb-dev libmariadb-dev-compat libmariadb3 mariadb-client \
    libxml2-dev libxslt-dev zlib1g-dev \
    pandoc texlive texlive-xetex lmodern librsvg2-bin

# --- Setup Python virtualenv ---
RUN python3 -m venv venv
ENV PATH="/code/venv/bin:$PATH"
RUN pip3 install --upgrade pip
RUN pip3 install -r /code/requirements/base.txt \
    -r /code/requirements/mysql.txt \
    -r /code/requirements/gunicorn.txt

# --- Clean up unnecessary packages ---
RUN apt-get purge -y libmariadb-dev-compat libmariadb-dev gcc libpython3-dev && \
    apt-get autoremove -y && \
    apt-get clean

COPY entrypoint.sh /code
COPY ./config /code/config/
COPY ./manage.py /code/
COPY ./tools/wait-for-mysql.sh /code/

ENTRYPOINT ["/code/entrypoint.sh"]
