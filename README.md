# **2022 Tools Project 발표**
## **Index**
1. 프로젝트 소개
2. 개발 과정
3. 결과 및 차후 개발 계획

## **프로젝트 소개**
### **What is _CFD_?**  
CFD(Computational Fluid Dynamics) = **컴퓨터를 통한 유동 시뮬레이션**  
CFD ~ 물리엔진  
![172ad833dc96da6d282f930534a293e4](https://user-images.githubusercontent.com/97779416/188765074-ad3edbdf-9c97-4d3c-b633-24c012787413.gif)
![20180916_155215_-1960973110](https://user-images.githubusercontent.com/97779416/188765076-685fc50c-43b7-4c50-b4a7-183606a3fb78.gif)
<p align="center">Example</p>  
<a href="url"><img src="https://user-images.githubusercontent.com/97779416/188304788-2883f4b0-c4da-41f1-be60-e100270023df.png" width="400" height="260"><img src="https://user-images.githubusercontent.com/97779416/188305226-a736a695-0a32-427e-862a-89638e69b472.PNG" width="400" height="260"></a> 
  
### **CFD의 고질적 문제점**
1. 낮은 신뢰도
2. 엄청난 계산 비용
3. 높은 진입장벽

### **목표**
Python을 통한 사용하기 쉬운 CFD 라이브러리 만들기
<p align="center"><a href="url"><img src="https://user-images.githubusercontent.com/97779416/188045873-8481adb2-3656-49a1-9578-517262de2f48.jpg" width="400" height="240"></a></p>
<p align="center">전기 + 열 + 유동</p>

## **게발 환경 및 언어**
<p align="center"><a href="url"><img src="https://user-images.githubusercontent.com/97779416/188306109-81e655a6-344e-4bc5-ab17-ed4d25b7fe64.png" width="400" height="240"><img src="https://user-images.githubusercontent.com/97779416/188306189-fbfa893b-b3d8-4e9b-a593-06185bd7ba0c.png" width="400" height="240"></a></p>


## **개발과정**
<p align="center"><a href="url"><img src="https://user-images.githubusercontent.com/97779416/188415468-1a2fa1ba-4a93-48cd-aa0e-9f75a7048e3f.PNG" width="800" height="440"></a></p> 


## **해석 절차**
1. 고온부, 저온부, 발전장치의 모양 및 물성 지정 &rarr; Module
2. Module들을 만들어 배치 &rarr; System
3. System에 경계조건 부여
4. 해석
  * 초기값 부여
  * 유동 해석 &rarr; 열 해석을 위한 경계조건 결정
  * 열 해석 part.1 &rarr; 각각의 Module 전압 및 저항 계산
  * 전기회로 해석 &rarr; 전류 계산
  * 열 해석 part.2 &rarr; 최종 계산 결과 도출 및 error 계산
  * 반복


## **Modules**
총 6개 모듈
* config.py
* material.py
* part.py
* **module.py**
* **path.py**
* **system.py**

## **Code**
<p align="center"><a href="url"><img src="https://user-images.githubusercontent.com/97779416/188553875-e97276ac-26a2-4b1f-998a-ac1593710f1f.PNG"><img src="https://user-images.githubusercontent.com/97779416/188553872-c490b86d-f637-45a6-a724-65083c28e0f8.PNG"><img src="https://user-images.githubusercontent.com/97779416/188553877-7707fc27-7c17-4733-a97a-59260ef3a25a.PNG"><img src="https://user-images.githubusercontent.com/97779416/188553878-0ccce11b-0511-4ecd-94cd-7e1a8f90047d.PNG"><img src="https://user-images.githubusercontent.com/97779416/188553881-4661072e-a2d8-4b5b-98db-b97d88332ff0.PNG"></a></p>

## **Concept**
<p align="center"><a href="url"><img src="https://user-images.githubusercontent.com/97779416/188427001-bbf25d48-2f29-4a99-9e4e-9e8a2d58fa26.PNG" width="800" height="300"></a></p>

전기 회로 : 노드와 노드의 연결로 구성된 폐회로 &rarr; Graph

## **Circuit**
<p align="center"><a href="url"><img src="https://user-images.githubusercontent.com/97779416/188554456-80f0b0aa-0500-4278-89fa-ad45cb5d2640.PNG"><img src="https://user-images.githubusercontent.com/97779416/188554457-d246af4f-fa6f-4142-98a9-9c13ca5e2759.PNG"></a></p>

## **System**
<p align="center"><a href="url"><img src="https://user-images.githubusercontent.com/97779416/188554487-9add47d5-93c9-4697-af76-fdccfd4bfc06.PNG"><img src="https://user-images.githubusercontent.com/97779416/188554489-90268b8c-374b-491a-b331-11ff1eab7666.PNG"><img src="https://user-images.githubusercontent.com/97779416/188554490-2df0f02c-e391-416d-83b5-e4ed1e02fb55.PNG"><img src="https://user-images.githubusercontent.com/97779416/188554492-5b23bd59-5bda-46fd-b612-7bfcefa64376.PNG"><img src="https://user-images.githubusercontent.com/97779416/188554496-c7e0e882-b319-4c59-aa63-fe1566ebc9d4.PNG"></a></p>

## **TEST**
<p align="center"><img src="https://user-images.githubusercontent.com/97779416/188593667-5ed93599-656d-4911-a8c7-be6d1c560b67.PNG"><a href="url"><img src="https://user-images.githubusercontent.com/97779416/188591819-53a15f12-7b78-4e83-a57d-489d5f0bb609.PNG"></a></p>

## **차후 계획**
