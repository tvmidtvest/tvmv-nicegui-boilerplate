FROM zauberzeug/nicegui

COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir
