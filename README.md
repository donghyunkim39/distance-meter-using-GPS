# distance-meter-using-GPS

For user who : 자율주행 자동차에서 pure pursuit 알고리즘등을 적용하기 위해 지정한 look ahead distance가 담긴 GPS data를 구축해야하는 user, GPS way points를 특정 거리마다 만 txt, csv 파일로 저장하고 싶은 user 
>준비: GPS 위도(latitude) , 경도(longitude) 정보다 담긴 rosbag 파일

#원리
> https://en.wikipedia.org/wiki/Haversine_formula 참고 => 우리는 위도,경도로 직접 거리를 계산해주는 라이브러리 사용하면 편함.

## haversine 라이브러리 설치

윈도우 터미널 혹은 vscode 터미널에 아래 명령어 입력
```bash
pip install haversine
```

## 적용시 코드 수정 사항
![image](https://github.com/donghyunkim39/distance-meter-using-GPS/assets/163104650/6058f97e-1b74-4c04-a3dd-3ee108679889)

> 변경 1) rospy.Subscriber("/gps/fix", NavSatFix, self.fix_callback)

  ![Screenshot from 2024-04-24 04-40-19](https://github.com/donghyunkim39/distance-meter-using-GPS/assets/163104650/4d2cc303-f1af-4cb6-b5b5-58618d7cd939)
 
 필자의 경우 위도, 경도가 담긴 topic의 경우 /gps/fix 이고, 이토픽의 Type은 NavSatFix 이므로 위 위같이 설정함

> 변경 2) self.file_path = "/home/donghyun/gps_point.txt"

 필자의 경우 위도, 경도를 /home/donghyun 경로에 gps_point라는 이름으로 txt파일로 저장하기에 위같이 설정함

> 변경 3) if distance_meter > 3: #3m마다 gps 포인트를 txt파일에 기록한다.

 필자의 경우 3m 마다만 GPS point가 저장된 txt파일을 따로 필요로 하므로 위와같이 3으로 설정함

 ## 정확도

 ![image](https://github.com/donghyunkim39/distance-meter-using-GPS/assets/163104650/9bf62d03-ea3f-4439-ab6d-fc679ec633a7)

 >1) haversine 에서 본 거리: 51.864m



![스크린샷 2024-04-24 045620](https://github.com/donghyunkim39/distance-meter-using-GPS/assets/163104650/3031e1a7-63c7-4351-ac04-fe45881230d4)

 >2) Google earth로 본 거리: 51.95m

즉, rosbag record당시 RTK(고정밀GNSS)의 오차까지 생각한다면 오차가 거의 없음을 알수있다.
