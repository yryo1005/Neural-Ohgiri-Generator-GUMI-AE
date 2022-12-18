# Neural_Oh!giri_Generator_v1

Pix2SeqとAutoEncoderを用いて画像から大喜利を生成するAIを作成しました.

本研究の特徴的な点は, Pix2Seqの画像のエンコーダとして, 事前学習済みの大規模画像認識モデルを用いる代わりに, AutoEncoderのエンコーダを用いているところです.

- [X] 推論
- [ ] データのスクレイピング
- [ ] 学習

## 必要ライブラリ

tensorflow==2.11.0

(モデルが大容量なのでGPUは使わない方がいいかもしれません)

numpy==1.23.5

matplotlib==3.6.2

tqdm==4.64.1

ipykernel==6.15.2

# 学習を行う場合

scikit-learn==1.2.0

# ボケてのデータをスクレイピングする場合

pip install scrapy==1.5.0

pip install Twisted==20.3.0

pip install pyopenssl==22.0.0 

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

generate_boke.ipynbを開き, 上から順に実行してください.

新たにAIを学習する場合, 適時モデル等のパスを変更してください.

generate_boke関数は, 学習に使用したboketeの画像からランダムに選んで大喜利を生成します(引数にボケ番号を与えた場合, その番号の画像に対し大喜利を生成します).

generate_boke_from_image関数は, 引数に指定したパスの画像に対し大喜利を生成します.

## データのスクレイピング

m1チップのMacはScrapyが非対応のため, GoogleColab等で実行してください.

以下のコマンドを実行

'''
cd scraping_project/bokete_scrape/spiders

scrapy crawl bokete_basic -o test.json
'''
