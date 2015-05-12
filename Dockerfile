FROM ipython/scipyserver

RUN pip install requests

WORKDIR /notebooks
