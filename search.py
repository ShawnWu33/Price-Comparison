import requests
from lxml import html


class SearchEngine:
    def __init__(self):
        self.davidJonesAddress = 'https://search.www.davidjones.com/search'
        self.myerAddress = 'https://www.myer.com.au/shop/mystore/SearchDisplay'
        self.bigwAddress = 'https://www.bigw.com.au/search/'

    def searchDavidJones(self,itemName):
        result=[];
        page = requests.get(self.davidJonesAddress, {'w': itemName})
        tree = html.fromstring(page.content)
        tdElems = tree.cssselect("[data-tb-sid=\"st_result-container-content\"]")  # list of all td elems
        if len(tdElems) > 10:
            tdElems = tdElems[:10]

        for item in tdElems:
            # text = item.text_content()  # text inside each td elem
            # splitText = text.split("\n")  # returns list of text in between "\n" chars
            # information = {'brand':splitText[6],'name':splitText[8]}
            brand = item.cssselect('.item-brand')[0].text_content().strip()
            print(brand)
            name = item.cssselect("a")[0].text_content().strip()
            print(name)
            link = item.cssselect("a")[0].get('href')
            print(link)
            itemPage = requests.get(link)
            tree = html.fromstring(itemPage.content)
            if tree.cssselect("p.price.now") != []:
                price = tree.cssselect("p.price.now")[0].text_content()
            else:
                price = tree.cssselect("p.price")[0].text_content()
            print(price)
            result.append({'title':brand+' '+name,'price':price,'link':link, 'store':'DavidJones'})
        # soup = BeautifulSoup(page.content,features="lxml")
        # for script in soup(["script", "style"]):
        #     script.extract()
        return result

    def searchMyer(self,itemName):
        page = requests.get(self.myerAddress, {'storeId':10251,
                                                     'beginIndex':0,
                                                     'sType':'SimpleSearch',
                                                     'searchTerm':itemName})
        root = html.fromstring(page.content)
        #print(page.content)
        print(len(root.cssselect(".item-containner")))
        print('No this item in myer')
        return []
        items=tree.cssselect('div.item-container')[0].cssselect('div.item')
        for item in items:
            info = item.cssselect('a')[0]
            print(info.text_content())
        return 0

    def searchBigW(self,itemName):
        result=[]
        page = requests.get(self.bigwAddress,{'text':itemName})
        root = html.fromstring(page.content)
        items = root.cssselect(".productGridItem")
        for item in items:
            title = item.cssselect("a")[0].get('title').strip()
            link = 'www.bigw.com.au'+item.cssselect("a")[0].get('href').strip()
            price = item.cssselect("strong")[0].text_content().strip()
            #print(title+'\n'+link+'\n'+price)
            result.append({'title':title, 'price':price,'link':link,'store':'BigW'})
        return result


