import requests
# 서버에 url요청
from bs4 import BeautifulSoup
# 크롤링할 뷰티풀솝깔기

#크롤링

weather_area = input('날씨를 알고 싶은 지역으로 입력하세요:(예:서울날씨)')
#인풋으로 지역을 받는다.
weather_html = requests.get(f"https://search.naver.com/search.naver?&query={weather_area}날씨")
#쿼리문에 입력될것을 찾는다.
# print(weather_html.text)
#weather_html = requests.get(f"https://search.naver.com/search.naver?&query=한남동날씨")
weather_soup = BeautifulSoup(weather_html.text, 'html.parser')

area_text=weather_soup.find('h2',{'class':'title'}).text #검색된 날씨 지역명
print(area_text)

today_temper=weather_soup.find('div',{'class':'temperature_text'}).text #현재 온도
print(today_temper[6:10])

today_temper = today_temper[6:11]
print(today_temper)

yesterday_weather=weather_soup.find('p',{'class':'summary'}).text #어제와의 날씨 비교
print(yesterday_weather)

yesterday_weather = yesterday_weather[0:13].strip()
# 공백삭제
print(yesterday_weather)


today_weather = weather_soup.find('span',{'class':'weather before_slash'}).text #검색된 날씨 지역명
print(today_weather)

sense_temper=weather_soup.select('dl.summary_list>dd') #체감온도
print(sense_temper[0].text)

sense_temper = sense_temper[0].text
print(sense_temper)

dust_info=weather_soup.select('ul.today_chart_list>li') #미세먼지
dust1_info = dust_info[0].find('span',{'class':'txt'}).text #미세먼지
dust2_info = dust_info[1].find('span',{'class':'txt'}).text #초미세먼지
print(dust2_info)

