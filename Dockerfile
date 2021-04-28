FROM debian:buster-slim
ENV PYTHONBUFFERED 1

RUN mkdir -p /code/requirements
WORKDIR /code

COPY ./requirements/base.txt \
	./requirements/mysql.txt \
	./requirements/gunicorn.txt \
	/code/requirements/

RUN apt-get update && apt-get install --no-install-recommends --yes \
	python3-pip python3-setuptools python3-venv \
	libmariadbclient-dev libmariadb-dev-compat libmariadb3 mariadb-client \
	python3-wheel libpython3.7-dev \
	gcc-7 gcc git \
	build-essential libxml2-dev libxslt-dev zlib1g-dev \
	pandoc texlive texlive-xetex lmodern librsvg2-bin

RUN python3 -m venv venv
ENV PATH="/code/venv/bin:$PATH"
RUN pip3 install --upgrade pip
RUN pip3 install -r /code/requirements/base.txt \
	-r /code/requirements/mysql.txt \
	-r /code/requirements/gunicorn.txt

RUN apt-get purge -y libmariadbclient-dev libmariadb-dev-compat \
	gcc-7 gcc libpython3.7-dev && \
    apt-get autoremove -y && \
    apt-get clean

COPY entrypoint.sh /code
COPY ./config /code/config/
COPY ./manage.py /code/
COPY ./tools/wait-for-mysql.sh /code/

ENTRYPOINT ["/code/entrypoint.sh"]
