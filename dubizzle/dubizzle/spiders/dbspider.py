import scrapy
import pandas as pd


class QuotesSpider(scrapy.Spider):
    name = "villa_listings"
    start_urls = [
        'https://dubai.dubizzle.com/en/property-for-sale/residential/villahouse/?filters=(bedrooms%3E%3D3%20AND%20bedrooms%3C%3D3)%20AND%20(amenities_v2.value%3A%22maids_room%22)'
    ]

    # df1 = pd.DataFrame(columns=['titles','community','price','sqfootage'])

    def parse(self, response):
        titles = response.css('.irHTOV::text').getall()
        community = response.css('.jkEDAl::text').getall()
        price = response.css('.eAldjT::text').getall()
        sqfootage = response.css('.jPhJFM~.jPhJFM+.jPhJFM::text').getall()
        sqfootage = [x for x in sqfootage if x != ' ' and x != 'SqFt']

        data = zip(titles,community,price,sqfootage)

        for item in data:
            info = {
                'titles': item[0],
                'community': item[1],
                'price': item[2],
                'sqfootage':item[3],
            }
            yield info

        next_page = response.css('.ePpunG::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


    #     df2 = pd.DataFrame(list_df).T
    #     df2.columns = ['titles','community','price','sqfootage']
    #     yield df2

    # df1.append(df2, ignore_index=True, inplace=True)    
    # df1.to_csv('villa_listings.csv')



        # dict_for_df = {'titles':titles, 'community':community, 'price':price, 'sqfootage':sqfootage}
        # df = pd.DataFrame(columns=['titles','community','price','sqfootage'])
        # df = pd.concat([df,dict_for_df],ignore_index=True)
        # df.to_csv('villa_listings.csv')
        # print(dict_for_df)


