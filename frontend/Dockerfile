# ベースイメージの作成
FROM node:18.0.0
# コンテナ内で作業するディレクトリを指定
WORKDIR /frontend
# package.jsonとyarn.lockを/usr/src/appにコピー
COPY ["package.json", "yarn.lock", "./"]
# パッケージをインストール
RUN yarn install
# ファイルを全部作業用ディレクトリにコピー
COPY . /frontend
# コンテナを起動する際に実行されるコマンド
ENTRYPOINT [ "yarn", "start" ]