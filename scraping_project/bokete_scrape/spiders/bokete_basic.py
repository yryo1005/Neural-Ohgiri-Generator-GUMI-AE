import scrapy
import os
import json

# スクレイピングを始める初めのボケ番号
if os.path.exists("test.json"):
    with open("test.json", "r", encoding = "utf-8") as f:
        a = f.readlines()
    START_NUM = json.loads(a[-2].replace("\n", ""))["boke_number"] + 1
else:
    START_NUM = 1

# スクレイピングを終える終わりのボケ番号
END_NUM = 100000

class BoketeBasicSpider(scrapy.Spider):
    name = 'bokete_basic'
    allowed_domains = ['bokete.jp']

    # スクレイピングを開始するURL
    start_urls = [f"https://bokete.jp/odai/{START_NUM}?page=1"]

    def parse(self, response):

        #　存在しないページにアクセスしているか確認
        is_nopage = response.xpath("//div[@class='en-message']").xpath("./text()").get()

        if is_nopage is not None:
            now_url = response.request.url
            now_number = int(now_url.split("/")[-1].split("?")[0])
            if now_number == END_NUM:
                pass
            else:
                next_url = f"https://bokete.jp/odai/{now_number + 1}?page=1"
                # 次のページに移動
                yield response.follow(url = next_url, callback = self.parse)
        
        else:
            now_url = response.request.url
            now_number = int(now_url.split("/")[-1].split("?")[0])

            # 画像のソースを取得
            img_src = "https:" + response.xpath('//*[@id="content"]/div[1]/div[1]/div/div/a/img/@src').get()

            # お題のカテゴリを取得
            category = response.xpath('//*[@id="content"]/div[1]/div[1]/div/div/div[2]/a[3]/text()').get()

            # 全てのボケを取得
            bokes = []
            tmp_boke = response.xpath('//div[@id="content"]/div[@class="boke"]')
            for T in tmp_boke:
                # ボケの文章を取得
                b = T.xpath("./a[@class='boke-text']/div/text()").get()
                bokes.append(b)

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
                    "boke_number" : now_number,
                    "page_url" : response.request.url, 
                    "img_src" : img_src,
                    "category" : category,
                    "bokes[ボケ, ボケの評価（現状不可）]" : bokes,
                }
                
                # https://bokete.jp/odai/Y?page=X
                # X = X + 1
                now_url = response.request.url
                tmp = now_url.split("=")
                next_url = tmp[0] + "=" + str(int(tmp[1]) + 1)
                    
                # 次のページに移動
                yield response.follow(url = next_url, callback = self.parse)
