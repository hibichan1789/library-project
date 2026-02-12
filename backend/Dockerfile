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

#Dockerfileから見てのappをコンテナ内の作業ディレクトcode/appにコピー
COPY ./app ./app

RUN useradd -m myuser
USER myuser

# app.main:app appフォルダのapp.mainモジュールを示す
CMD [ "uvicorn", "app.main:app" , "--host", "0.0.0.0", "--port", "8000"]