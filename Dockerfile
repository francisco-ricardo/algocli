FROM python:latest

RUN apt update -y && apt install -y \
    build-essential \
    valgrind \
    vim \
    default-jdk \
    && rm -Rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip && \
    pip install ipython pylint pep8 flake8 sly

ENTRYPOINT ["/algocli/scripts/docker-entrypoint.sh"]
CMD ["/algocli/scripts/docker-cmd-script.sh"]

# EOF



