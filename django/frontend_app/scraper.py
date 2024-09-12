import requests
from bs4 import BeautifulSoup
import hashlib
import datetime
import sys
import os
import django

# 確保 Django 專案路徑在 sys.path 中
sys.path.append('/Users/user/Github/112_Wistron_Cooperation/django')  # 替換為你的 Django 專案路徑

# 設定 Django 環境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')  # 替換為正確的專案名稱
django.setup()

from frontend_app.models import SecurityNews

# 生成唯一的新聞 ID
def generate_id(text):
    return hashlib.sha1(text.encode()).hexdigest()[:50]

# 抓取網頁 HTML 內容
def fetch_html(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch data from {url}")
        return None
    return response.text

# 從區塊中提取新聞連結
def fetch_news_from_block(base_url, page_num):
    if page_num == 0:
        html = fetch_html(base_url)
    else:
        html = fetch_html(f'{base_url}?page={page_num}')
    
    if not html:
        return []
    
    soup = BeautifulSoup(html, 'html.parser')
    news_links = []

    # 尋找重要新聞
    headline_news = soup.find('div', class_='featured-channle-headline-first')
    if headline_news:
        links = headline_news.find_all('a')
        for link in links:
            full_link = f"https://www.ithome.com.tw{link['href']}"
            news_links.append(full_link)

    # 尋找其他新聞
    news_items = soup.find_all('div', class_='span4 channel-item')
    for item in news_items:
        links = item.find_all('p', class_='title')
        for links_tmp in links:
            link = links_tmp.find('a')
            full_link = f"https://www.ithome.com.tw{link['href']}"
            news_links.append(full_link)

    return news_links

# 抓取新聞的詳細內容
def fetch_news_details(news_url):
    html = fetch_html(news_url)
    if not html:
        return None

    soup = BeautifulSoup(html, 'html.parser')

    # 抓取標題
    title_element = soup.find('h1')
    if not title_element:
        print(f"Title not found for {news_url}")
        return None
    title = title_element.text.strip()

    # 抓取摘要
    content_summary_find = soup.find("div", class_="content-summary")
    if not content_summary_find:
        print(f"Content summary not found for {news_url}")
        return None
    content_summary_store = content_summary_find.text.strip()

    # 抓取發佈日期
    publish_date_element = soup.find('span', class_="created")
    if not publish_date_element:
        print(f"Publish date not found for {news_url}")
        return None
    publish_date_store = publish_date_element.text.strip().split()[0]
    publish_datetime = datetime.datetime.strptime(publish_date_store, '%Y-%m-%d')

    # 抓取文章內容
    content_element = soup.find('div', class_='field-item even')
    if not content_element:
        print(f"Content not found for {news_url}")
        return None
    content_store = content_element.text.strip()

    news_id = generate_id(news_url)

    return {
        'news_id': news_id,
        'content_summary': content_summary_store,
        'title': title,
        'publish_date': publish_datetime,
        'url': news_url,
        'content': content_store
    }

# 儲存新聞資料到資料庫
def store_news(news_data):
    SecurityNews.objects.update_or_create(
        url=news_data['url'],
        defaults={
            'title': news_data['title'],
            'publish_date': news_data['publish_date'],
            'content': news_data['content']
        }
    )

# 爬取新聞並儲存
def crawl_news(base_url, page_num):
    for cnt_num in range(page_num + 1):
        news_links = fetch_news_from_block(base_url, cnt_num)
        for link in news_links:
            print(f"Fetching details for {link}")
            news_details = fetch_news_details(link)
            if news_details:
                store_news(news_details)
    print('News scraping and storing completed.')

# 主程式
def main():
    base_url = "https://www.ithome.com.tw/security"
    try:
        page_num = int(input('Enter number of pages to scrape: '))
        crawl_news(base_url, page_num)
    except ValueError:
        print("Invalid input, please enter a number.")

if __name__ == '__main__':
    main()