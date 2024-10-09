FROM python:latest

RUN apt update -y && apt install -y \
    build-essential \
    vim \
    vim-scripts \
    && rm -Rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip && \
    pip install ipython pylint pep8 flake8 sly

ENTRYPOINT ["/algorithms/scripts/docker-entrypoint.sh"]
CMD ["/algorithms/scripts/docker-cmd-script.sh"]

# EOF



