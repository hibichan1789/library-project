# fastAPIとviteの接続練習
fastAPIでの簡単なDBの作成とフロントエンドでの呼び出し練習

## 立ち上げ方法
docker compose up --buildで起動  
(url)[http://localhost:5173/]

## 学んだこと  
開発の流れ
dockerの環境を作る  
models.pyにデータベース型、DTO型を定義する  
database.pyにengine,dbを作る関数,session,を定義する  
SQLModelに定義したtable=Trueのものは自動でテーブルが作成される SQLModel.metadataに情報が入っているため  
main.pyでアプリ起動時(@asynccontextmanager)で起動時にテーブルを作成するようにする  
swaggerでdbの接続、動作確認  
corsにフロントエンドURLを定義して接続の設定を書く  
vite側でfetchして接続確認  

ApiRouterのprefixはエンドポイントのパスの接頭辞になり、tagsがswagger上の表示名になる  

## 所感
この前した時よりもスムーズにフロントエンドとバックエンドの接続ができた  
DBの型をそのまま使うとidまでpostできるのが危ないと気づき、DTO型の定義に至った  
→これはasp.net coreの経験があったからかも  
.envファイルにURLやポートを入れて環境変数から読み込む練習ができた  
とりあえずmain.pyに動作確認用のエンドポイントを置いて確認するのはありだと思った  