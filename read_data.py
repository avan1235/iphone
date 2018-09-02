from lxml import html
import requests
import json

def get_sferis_price():
    page = requests.get(
        'https://www.sferis.pl/smartfon-apple-iphone-8-mq6j2zd-a-bluetooth-wifi-gps-lte-64gb-ios-11-zloty-p594270')
    tree = html.fromstring(page.content)
    data = tree.xpath('//meta[@itemprop="price"]/@content')
    if len(data):
        data = [float(i) for i in data]
        return min(data)
    return 0


def get_mediamarkt_price():
    page = requests.get("https://mediamarkt.pl/telefony-i-smartfony/smartfony.apple?sort=name_desc&limit=20&page=1&filter%5B8380%5D%5B%5D=56011302&filter%5B8380%5D%5B%5D=56011302&filter%5B18692%5D%5B%5D=712221&filter%5B22823%5D%5B%5D=819561&filter%5B22823%5D%5B%5D=819561&filter%5B22823%5D%5B%5D=819561&filter%5B22823%5D%5B%5D=819561&filter%5B18790%5D%5B%5D=711609&filter%5B18790%5D%5B%5D=34341042&filter%5B22825%5D%5B%5D=790003&filter%5B28%5D%5B%5D=5828651")
    tree = html.fromstring(page.content)
    data = tree.xpath('//div[@itemprop="price"]/@content')
    if len(data):
        data = [float(i) for i in data]
        return min(data)
    return 0


def get_mediaexpert_price():
    page = requests.get("https://www.mediaexpert.pl/smartfony/smartfon-apple-iphone-8-64gb-zloty,id-986796")
    tree = html.fromstring(page.content)
    data = tree.xpath('//meta[@itemprop="price"]/@content')
    if len(data):
        data = [float(i) for i in data]
        return min(data)
    return 0


def get_xkom_price():
    page = requests.get("https://www.x-kom.pl/p/382277-smartfon-telefon-apple-iphone-8-64gb-gold.html")
    tree = html.fromstring(page.content)
    data = tree.xpath('//meta[@itemprop="price"]/@content')
    if len(data):
        data = [float(i) for i in data]
        return min(data)
    return 0


def get_euroagd_price():
    page = requests.get("https://www.euro.com.pl/telefony-komorkowe/apple-iphone-8-64gb-zloty.bhtml")
    tree = html.fromstring(page.content)
    for text in tree.xpath('//script[@type="application/ld+json"]//text()'):
        data = json.loads(text)
        if 'offers' in data:
            if 'price' in data['offers']:
                return float(data['offers']['price'])
    return 0


def get_vobis_price():
    page = requests.get("https://vobis.pl/mobile/smartfony/iphone-8-64gb-gold")
    tree = html.fromstring(page.content)
    data = tree.xpath('//span[@itemprop="price"]//text()')
    if len(data):
        data = [float(i) for i in data]
        return min(data)
    return 0


def get_morele_price():
    page = requests.get("https://www.morele.net/smartfon-apple-iphone-8-64gb-zloty-mq6j2zd-a-1605878/")
    tree = html.fromstring(page.content)
    data = tree.xpath('//div[@itemprop="price"]/@content')
    if len(data):
        data = [float(i) for i in data]
        return min(data)
    return 0


def get_price(shop_name):
    if shop_name == "MediaExpert":
        return get_mediaexpert_price()
    elif shop_name == "MediaMarkt":
        return get_mediamarkt_price()
    elif shop_name == "morele":
        return get_morele_price()
    elif shop_name == "RTVEuroAGD":
        return get_euroagd_price()
    elif shop_name == "Sferis":
        return get_sferis_price()
    elif shop_name == "Vobis":
        return get_vobis_price()
    elif shop_name == "XKOM":
        return get_xkom_price()
    else:
        return 0