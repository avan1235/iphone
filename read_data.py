from lxml import html
import requests
from edit_text import delete_spaces

SFERIS_PRICE_SPAN_ID = 12
MEDIAEXPERT_PRICE_POSITION_ID = 0


def get_sferis_price():
    page = requests.get(
        'https://www.sferis.pl/smartfon-apple-iphone-8-mq6j2zd-a-bluetooth-wifi-gps-lte-64gb-ios-11-zloty-p594270')
    tree = html.fromstring(page.content)
    specials = tree.xpath('//span/text()')
    price = specials[SFERIS_PRICE_SPAN_ID]
    where_ends = price.find(",")
    price = price[0:where_ends]
    return_price = float(delete_spaces(price))
    return  return_price


def get_mediamarkt_price():
    page = requests.get("https://mediamarkt.pl/telefony-i-smartfony/smartfony.apple?sort=name_desc&limit=20&page=1&filter%5B8380%5D%5B%5D=56011302&filter%5B8380%5D%5B%5D=56011302&filter%5B18692%5D%5B%5D=712221&filter%5B22823%5D%5B%5D=819561&filter%5B22823%5D%5B%5D=819561&filter%5B22823%5D%5B%5D=819561&filter%5B22823%5D%5B%5D=819561&filter%5B18790%5D%5B%5D=711609&filter%5B18790%5D%5B%5D=34341042&filter%5B22825%5D%5B%5D=790003&filter%5B28%5D%5B%5D=5828651")
    tree = html.fromstring(page.content)
    specialst = tree.xpath('/html/body/section/main/div[6]/div[5]/div[1]/div/div[2]/div/div[1]/div[2]/span[1]/text()')
    specialss = tree.xpath('/html/body/section/main/div[6]/div[5]/div[1]/div/div[2]/div/div[1]/div[2]/span[2]/text()')
    specialsd = tree.xpath('/html/body/section/main/div[6]/div[5]/div[1]/div/div[2]/div/div[1]/div[2]/span[3]/text()')
    specialsj = tree.xpath('/html/body/section/main/div[6]/div[5]/div[1]/div/div[2]/div/div[1]/div[2]/span[4]/text()')
    return (1000*float(specialst[0]))+(100*float(specialss[0]))+(10*float(specialsd[0]))+float(specialsj[0])



def get_mediaexpert_price():
    page = requests.get("https://www.mediaexpert.pl/smartfony/smartfon-apple-iphone-8-64gb-zloty,id-986796")
    tree = html.fromstring(page.content)
    specials = tree.xpath('//p[@class="price" and @data-atat="price"]/text()')
    return_price = float(specials[MEDIAEXPERT_PRICE_POSITION_ID])
    return return_price


def get_xkom_price():
    page = requests.get("https://www.x-kom.pl/g-4/c/1590-smartfony-i-telefony.html?f[manufacturers][357]=1&f[201][95640]=1&f[193][62726]=1&f[195][62729]=1&f[202][4913]=1&f[4588][73155]=1")
    tree = html.fromstring(page.content)
    specials = tree.xpath('//span[@class="price text-nowrap"]/text()')
    price = specials.pop()
    where_ends = price.find(",")
    return_price = float(delete_spaces(price[:where_ends]))
    return return_price


def get_euroagd_price():
    page = requests.get("https://www.euro.com.pl/telefony-komorkowe/apple-iphone-8-64gb-zloty.bhtml")
    tree = html.fromstring(page.content)
    specials = tree.xpath('//div[@class="price-normal selenium-price-normal"]/text()')
    price = "".join(specials[0].split())
    where_end = price.find("zł")
    return_price = float(price[:where_end])
    return return_price


def get_vobis_price():
    page = requests.get("https://vobis.pl/mobile/smartfony/iphone-8-64gb-gold")
    tree = html.fromstring(page.content)
    specials = tree.xpath('//span[@class="is-regular"]/text()')
    price = "".join(specials[0].split())
    where_ends = price.find(",")
    return_price = float(price[:where_ends])
    return return_price


def get_morele_price():
    page = requests.get("https://www.morele.net/smartfon-apple-iphone-8-64gb-zloty-mq6j2zd-a-1605878/")
    tree = html.fromstring(page.content)
    specials = tree.xpath('//*[@id="product_price_brutto"]/text()')
    price = specials[0]
    price = delete_spaces(price)
    where_ends = price.find("z")
    price = price[:where_ends]
    comma = price.find(",")
    price = price[:comma]+"."+price[comma+1:]
    return_price = float(price)
    return return_price


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