import sys
import threading

import requests
from bs4 import BeautifulSoup

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

form_class = uic.loadUiType("ui/weatherApp.ui")[0]


class WeatherAppWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("오늘의 날씨")
        self.setWindowIcon(QIcon("icon/ti.png"))
        self.statusBar().showMessage('WEATHER APP VER 1.0 by hyejin')
        print("1")
        # 날씨 조회 버튼
        self.weather_button.clicked.connect(self.crawling_weather)
        self.weather_button.clicked.connect(self.reflashTimer)
        print("2")
    def crawling_weather(self):
        weather_area = self.input_area.text()  # 유저가 입력한 지역텍스트 가져오기
        weather_html = requests.get(f"https://search.naver.com/search.naver?&query={weather_area}날씨")
        print("3")
        weather_soup = BeautifulSoup(weather_html.text, 'html.parser')
        print("4")
        try:
            area_text = weather_soup.find('h2', {'class': 'title'}).text  # 검색된 날씨 지역명
            print(area_text)

            today_temper = weather_soup.find('div', {'class': 'temperature_text'}).text  # 현재온도
            today_temper = today_temper[6:11]
            print(today_temper)

            yesterday_weather = weather_soup.find('p', {'class': 'summary'}).text  # 어제와의 날씨 비교
            yesterday_weather = yesterday_weather[0:13].strip()  # 13자 까지 가져온 후 공백제거 후 저장
            print(yesterday_weather)

            today_weather = weather_soup.find('span', {'class': 'weather before_slash'}).text  # 오늘날씨
            print(today_weather)

            sense_temper = weather_soup.select('dl.summary_list>dd')
            sense_temper_text = sense_temper[0].text  # 체감온도
            print(sense_temper_text)

            dust_info = weather_soup.select('ul.today_chart_list>li')
            # print(dust_info)
            dust1_info = dust_info[0].find('span', {'class': 'txt'}).text  # 미세먼지 정보
            dust2_info = dust_info[1].find('span', {'class': 'txt'}).text  # 초미세먼지 정보
            print(dust1_info)
            print(dust2_info)
            print("5")
            self.area_in.setText(f"{weather_area}")
            self.area_out.setText(f"{area_text}")
            self.todayTemper.setText(f"{today_temper}")
            self.yesterdayWeather.setText(f"{yesterday_weather}")
            self.todayWeather.setText(f"{today_weather}")
            self.senseTemper.setText(f"{sense_temper}")
            self.dustWeather1.setText(f"{dust1_info}")
            self.dustWeather2.setText(f"{dust2_info}")
            print("6")
        except:
            try:
                area_text = weather_soup.find('span', {'class': 'btn_select'}).text
                area_text = area_text.strip()  # 공백제거
                today_temper = weather_soup.find('span', {'class': 'todaytemp'}).text  # 현재온도
                today_weather = weather_soup.find('p', {'class': 'cast_txt'}).text  # 오늘날씨
                today_weather = today_weather[0:2]
                today_weather = today_weather.strip()
                print(today_weather)
                self.area_out.setText(area_text)
                self.setWeatherImage(today_weather)
                self.yesterdayWeather.setText(f"{today_temper} ℃")
                self.todayWeather.setText("-")
                self.senseTemper.setText("-")
                self.dustWeather1.setText("-")
                self.dustWeather2.setText("-")
                print("7")
            except:
                self.area_label.setText("입력된 지역의 날씨 없음")
                print("8")
    # 날씨 정보에 따라 해당 날씨 이미지 출력 함수
    def setWeatherImage(self, weatherInfo):
        if weatherInfo == "흐림":
            weatherImg = QPixmap("icon/gu1.png")
        elif weatherInfo == "맑음":
            weatherImg = QPixmap("icon/hae.png")
        elif weatherInfo == "눈":
            weatherImg = QPixmap("icon/bi2.png")
        elif weatherInfo == "비":
            weatherImg = QPixmap("icon/bi")
        elif weatherInfo == "소닉":
            weatherImg = QPixmap("icon/bi")
        elif weatherInfo == "구름많음":
            weatherImg = QPixmap("icon/gu1.png")
        else:
            self.todayWeather.setText(weatherInfo)
        print("9")
        self.todayWeather.setPixmap(QPixmap(weatherImg))
        print("10")
    def reflashTimer(self):
        self.crawling_weather()
        threading.Timer(60, self.reflashTimer).start()
        print("11")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WeatherAppWindow()
    ex.show()
    sys.exit(app.exec_())