import scrapy

# スクレイピングを始める初めのボケ番号
START_NUM = 1

# スクレイピングを終える終わりのボケ番号
END_NUM = 5

class BoketeBasicSpider(scrapy.Spider):
    name = 'bokete_basic'
    allowed_domains = ['bokete.jp']

    # スクレイピングを開始するURL
    start_urls = [f"https://bokete.jp/odai/{START_NUM}?page=1"]

    def parse(self, response):

        #　存在しないページにアクセスしているか確認
        tmp = response.xpath("//div[@class='en-message']")
        tmp = tmp.xpath("./text()").get()

        if tmp is not None:
            # 存在しないページにアクセスしている場合、次のお題に移動
            pass
            # https://bokete.jp/odai/Y?page=X
            # Y = Y + 1
            now_url = response.request.url
            tmp = now_url.split("/")
            tmp = tmp[-1].split("?")
            if int(tmp[0]) == 100:
                pass
            else:
                next_url = f"https://bokete.jp/odai/{int(tmp[0])+1}?page=1"

                # 次のページに移動
                yield response.follow(url = next_url, callback = self.parse)
        
        else:
            # imgタグにタグを限定, すべてのimgタグをリスト化
            # 一番初めのボケクラスはお題の画像とカテゴリ・ラベル等の情報を含む
            tmp = response.xpath('k')[0]
            
            # 画像のソースを取得
            img_src = "https:" + tmp.xpath("./div/div/a/img/@src").get()

            # お題のカテゴリを取得
            category = tmp.xpath("./div/div/div[2]/a[3]/text()").get()

            # お題のラベルを取得
            labels = []
            tmp_label = tmp.xpath("./div/div/div[3]/a")
            for T in tmp_label:
                # ラベル
                l = T.xpath("./text()").get()
                # 投票率
                p = T.xpath("./small/text()").get()
                labels.append([l, p])

            # 全てのボケを取得
            bokes = []
            tmp_boke = response.xpath('//div[@id="content"]/div[@class="boke"]')
            for T in tmp_boke:
                # ボケの文章を取得
                b = T.xpath("./a[@class='boke-text']/div/text()").get()
                # ボケの評価を取得したい！
                e = T.xpath("./div[2]/div/div/div[@class='boke-stars']/a/text()").get()
                bokes.append([b, e])

            # ページのボケ数が０の時、そのお題のボケは全てスクレイプできているので次のお題に移動
            if len(bokes) == 0:
                # https://bokete.jp/odai/Y?page=X
                # Y = Y + 1
                now_url = response.request.url
                tmp = now_url.split("/")
                tmp = tmp[-1].split("?")

                # お題番号が以下の数字になったら終了
                if int(tmp[0]) == END_NUM:
                    pass
                else:
                    next_url = f"https://bokete.jp/odai/{int(tmp[0])+1}?page=1"

                    # 次のページに移動
                    yield response.follow(url = next_url, callback = self.parse)

            # 同じお題の次のページに移動
            else:
                yield{
                    "page_url" : response.request.url, 
                    "img_src" : img_src,
                    "category" : category,
                    "labels[ラベル, 投票率]" : labels,
                    "bokes[ボケ, ボケの評価（現状不可）]" : bokes,
                }
                
                # https://bokete.jp/odai/Y?page=X
                # X = X + 1
                now_url = response.request.url
                tmp = now_url.split("=")
                next_url = tmp[0] + "=" + str(int(tmp[1]) + 1)
                    
                # 次のページに移動
                yield response.follow(url = next_url, callback = self.parse)