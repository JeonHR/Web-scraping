import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyautogui



# 첫 번째 질문
title = "Url"
text = "URL을 입력하세요:"
url2 = pyautogui.prompt(text=text, title=title)
url2 = url2.split('=')[0]

title = "End page"
text = "검색 범위인 start page를 선택하세요:"
start_page = pyautogui.prompt(text=text, title=title)
start_page2 = int(start_page)

# 두 번째 질문
title = "End page"
text = "검색 범위인 end page를 선택하세요:"
end_page = pyautogui.prompt(text=text, title=title)
end_page2 = int(end_page)

# 리뷰를 담을 리스트 초기화
post_reviews = []
comment_reviews = []

# 페이지를 순회하면서 데이터 수집
for page in range(start_page2, end_page2 + 1):
    # 각 페이지의 URL 설정
    url = url2 +f'{page}'
    
    # 웹페이지 가져오기
    response = requests.get(url)
    html_content = response.content
    
    # BeautifulSoup으로 HTML 파싱
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 클래스가 'review'와 'content'인 태그 찾아서 리뷰 추출
    review_tags = soup.find_all('div', class_=['txt1', 'merit'])
    for review_tag in review_tags:
        review_text = review_tag.text.strip()  # 리뷰 텍스트 추출
        if 'txt1' in review_tag['class']:
            post_reviews.append(review_text)
        elif 'merit' in review_tag['class']:
            comment_reviews.append(review_text)

# 데이터프레임 생성
df = pd.DataFrame({
    'Post_Review': post_reviews,
    'Comment_Review': comment_reviews
})

# 엑셀 파일로 저장
df.to_excel('reviews.xlsx', index=False)
