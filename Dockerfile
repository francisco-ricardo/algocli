FROM python:latest

RUN apt update -y && apt install -y \
    build-essential \
    git \    
    vim \
    vim-fugitive \
    vim-scripts \
    && rm -Rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip && \ 
    pip install ipython pylint pep8 flake8 sly

RUN git config --global user.name "francisco" && \
    git config --global user.email "franciscoricardo.dev@gmail.com." && \
    git config --global core.editor "vim"

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod 0755 /usr/local/bin/docker-entrypoint.sh

COPY docker-cmd-script.sh /usr/local/bin/docker-cmd-script.sh
RUN chmod 0755 /usr/local/bin/docker-cmd-script.sh

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD ["/usr/local/bin/docker-cmd-script.sh"]

# EOF



