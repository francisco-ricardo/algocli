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

ENTRYPOINT ["/algorithms/scripts/docker-entrypoint.sh"]
CMD ["/algorithms/scripts/docker-cmd-script.sh"]

# EOF



