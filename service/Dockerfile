FROM skoogi/base

WORKDIR /usr
RUN git pull git@git.dev.attackt.com:attackt/services.git
RUN pip install --no-cache-dir -r ./services/requirements.txt