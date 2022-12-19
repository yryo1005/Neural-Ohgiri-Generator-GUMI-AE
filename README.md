# Neural_Oh!giri_Generator_v1

![generate_smaple](http://i.imgur.com/Jjwsc.jpghttps://github.com/yryo1005/Neural_Oh-giri_Generator_v1/blob/main/image.png?raw=true)

Pix2SeqとAutoEncoderを用いて画像から大喜利を生成するAIを作成しました.

本研究の特徴的な点は, Pix2Seqの画像のエンコーダとして, 事前学習済みの大規模画像認識モデルを用いる代わりに, AutoEncoderのエンコーダを用いているところです.

- [X] 推論
- [X] データのスクレイピング
- [ ] 学習

## 必要ライブラリ

tensorflow==2.11.0 (モデルが大容量なので, 学習を行わない場合, GPUは使わない方がいいかもしれません)

numpy==1.23.5

matplotlib==3.6.2

tqdm==4.64.1

ipykernel==6.15.2

### 学習を行う場合

scikit-learn==1.2.0

### ボケてのデータをスクレイピングする場合

scrapy関連はversionがうるさいので注意

scrapy==1.5.0

Twisted==21.7.0

pyopenssl==22.0.0 

## モデル, データのダウンロード

[画像のエンコーダ](https://drive.google.com/file/d/1VL3Gyr91_LSSVPyHknY4RnZMfy6Z8PZu/view?usp=share_link)
(新たにモデルを訓練する場合不要)

[大喜利の生成器](https://drive.google.com/file/d/1zxl9RC8dZFF4hYltz4V5AkHqgQTDZ8tf/view?usp=share_link)
(新たにモデルを訓練する場合不要)

[語彙データ](https://drive.google.com/file/d/1TelxXPss39oHVkOlEpGvmbCgQrsQMMib/view?usp=share_link)
(新たにモデルを訓練する場合不要)

[Boketeの画像データ](https://drive.google.com/file/d/1JJxKH7oYjtbjDebvMCyq15WWmklSHSvE/view?usp=share_link)
(ダウンロード後解凍してください. データをスクレイピングする場合不要)

[Boketeの大喜利データ](https://drive.google.com/file/d/1_cKPz-zfRphi9oa7wTMV_ilyaBbkqCs5/view?usp=share_link)
(データをスクレイピングする場合不要)

[学習に使用したデータ](https://drive.google.com/file/d/1G6HkNVT-OX7mhvutLt7HYuIU_k0a9JWm/view?usp=share_link)
(新たにモデルを訓練する場合不要)

上記のデータをダウンロードして次のように配置してください

Neural_Oh-giri_Generator_v1

├ generate_boke.ipynb

├ dist_encoder.h5

├ dist_generator.h5

├ dist_accepted_numbers.json

├ dist_word_to_index.json

├ dist_bokete_data.json

├ bokete_image

&emsp;├ 4.jpg

&emsp;├ 5.jpg

&emsp;&emsp;...

## 大喜利を生成する

[generate_boke.ipynb](https://github.com/yryo1005/Neural_Oh-giri_Generator_v1/blob/main/generate_boke.ipynb)を開き, 上から順に実行してください.

新たにAIを学習した場合, 適時モデル等のパスを変更してください.

generate_boke関数は, 学習に使用したboketeの画像からランダムに選んで大喜利を生成します(引数にボケ番号を与えた場合, その番号の画像に対し大喜利を生成します).

generate_boke_from_image関数は, 引数に指定したパスの画像に対し大喜利を生成します.

## データのスクレイピング

100000件以上データを必要としない場合, 配布しているファイルを使用する方が早いです.

m1チップのMacはScrapyが非対応のため, GoogleColab等で実行してください.

### 1. ボケてからデータを取得

以下のコマンドを実行

```
cd scraping_project/bokete_scrape/spiders

scrapy crawl bokete_basic -o test.json
```

実行しているうちに403エラーで蹴られるので, その際は時間を空けて再度コマンドを実行してください

途中で止まった場合も続きから再開するようにプログラムされています

スクレイピングするお題の数を指定する場合, 

[scraping_project/bokete_scrape/spiders/bokete_basic.py](https://github.com/yryo1005/Neural_Oh-giri_Generator_v1/blob/main/scraping_project/bokete_scrape/spiders/bokete_basic.py)

の, END_NUMの値を変更してください(デフォルトでは100000になっています)

### 2. データ整形

規定数スクレイピングが出来たら, 以下のコマンドを実行

```
python reshape_bokete_data.py
```

## モデルを学習する

配布モデルはRTX3090Ti(24GB)を限界ギリギリまで使って学習しています.

そのため, これより性能が低いPCで実行する場合, 適時パラメータやネットワーク構造を編集してください.

### 1. AutoEncoderの学習
AutoEncoderの学習の際, 学習データにアニメ画像やイラストなど単調な画像が含まれると, 学習が上手くいきません.

そのため, これらの画像を取り除いて学習します.

目視でアニメ画像やイラストなど単調な画像でないと確認したもののリストがあるのでダウンロードして, train_autoencoder.ipynbと同じ階層のディレクトリに配置してください.

[リスト](https://drive.google.com/file/d/1_HwAgnqpuY8jdTqpNvVr6wa34xlHUEtb/view?usp=share_link)

[train_autoencoder.ipynb](https://github.com/yryo1005/Neural_Oh-giri_Generator_v1/blob/main/train_autoencoder.ipynb)を開き, 上から順に実行してください.

### 2. 2値分類AIの学習

### 3. 画像の特徴を抽出

### 4. 大喜利生成器の学習
