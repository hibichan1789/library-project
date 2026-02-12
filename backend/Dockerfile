#/backend/Dockerfile
FROM python:3.11-slim

# 環境変数の設定
# .pycファイルを作らない/標準出力をバッファリング(一時的な記憶)をしないで出す
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#バックエンドコンテナ内の作業ディレクトリ
WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir  --upgrade -r requirements.txt

# 先にディレクトリを作って所有権を myuser に変える
RUN useradd -m myuser && \
    mkdir -p /code/app /code/data && \
    chown -R myuser:myuser /code

# COPYの際も所有者を指定する
COPY --chown=myuser:myuser ./app ./app

#Dockerfileから見てのappをコンテナ内の作業ディレクトcode/appにコピー
COPY ./app ./app

USER myuser

# app.main:app appフォルダのapp.mainモジュールを示す
CMD [ "uvicorn", "app.main:app" , "--host", "0.0.0.0", "--port", "8000", "--reload"]