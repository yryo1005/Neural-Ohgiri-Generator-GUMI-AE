# Neural_Oh!giri_Generator_v1

Pix2SeqとAutoEncoderを用いて画像から大喜利を生成するAIを作成しました

## 必要ライブラリ

tensorflow==2.11.0

numpy==1.23.5

matplotlib==3.6.2

scikit-learn==1.2.0

tqdm==4.64.1

ipykernel==6.15.2
 

## モデル, データのダウンロード

[画像のエンコーダ](https://drive.google.com/file/d/1VL3Gyr91_LSSVPyHknY4RnZMfy6Z8PZu/view?usp=share_link)

[大喜利の生成器](https://drive.google.com/file/d/1zxl9RC8dZFF4hYltz4V5AkHqgQTDZ8tf/view?usp=share_link)

[語彙データ](https://drive.google.com/file/d/1TelxXPss39oHVkOlEpGvmbCgQrsQMMib/view?usp=share_link)

[Boketeの画像データ](https://drive.google.com/file/d/1JJxKH7oYjtbjDebvMCyq15WWmklSHSvE/view?usp=share_link)
(ダウンロード後解凍してください)

[Boketeの大喜利データ](https://drive.google.com/file/d/1_cKPz-zfRphi9oa7wTMV_ilyaBbkqCs5/view?usp=share_link)

[学習に使用したデータ](https://drive.google.com/file/d/1G6HkNVT-OX7mhvutLt7HYuIU_k0a9JWm/view?usp=share_link)

上記のデータをダウンロードして次のように配置してください

Neural_Oh-giri_Generator_v1

├ generate_boke.ipynb

├ dist_encoder.h5

├ dist_generator.h5

├ accepted_numbers.json

├ word_to_index.json

bokete_data.json

bokete_image

├ 4.jpg

├ 5.jpg

...

## 大喜利を生成する

generate_boke.ipynbを開き, 上から順に実行してください.
