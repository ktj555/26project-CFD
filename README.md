# Project 목표 및 계획

### 목표
주제 : 열전발전 시스템의 유동 및 열해석 가능한 수치해석 라이브러리 만들기
  
이전에 만들어보았던 라이브러리의 경우 속도가 매우 느리고 정확성과 확장성에 문제가 있었기 때문에  
이를 개선하여 빠른 수행속도와 정확성을 보장하고 확장성이 높게 하기  
추가적으로 가능하다면 더 복잡한 물리 현상을 반영할 수 있는 모델로 확장해보기  

### 프로그램 기능
1. 사용자로부터 형상 정보(시스템 전체 크기 및 배열 형태, 유동 입구와 출구) 입력 받기
2. 사용자로부터 물질 정보(흐르는 유체의 물성치, 시스템 구성 물질) 입력 받기
3. 2차원 형상 정보를 연결하여 1차원 해석이 가능하도록 정렬하기
4. <details>
    <summary>해석하기</summary>
    <div markdown="1">
      
      기존의 경우 Python만을 이용하여 해석을 수행하였지만 (편의성을 위해)
      이번 목표가 계산 속도의 향상인 만큼 보조적으로 C를 통해서 이 부분을 진행하고자 합니다.
      Python을 포기하지 않는 이유는 데이터 핸들링에서 C보다 유용하며  
      데이터의 전처리 및 후처리 과정의 소요시간은 해석 소요시간에 비해 굉장히 짧기 때문에  
      Python의 장점과 C의 장점을 모두 활용하기 위함입니다.
      
    </div>
  </details>
5. 데이터 시각화 or 데이터 저장

### 진행 계획
|Week|Plan|
|--|--|
|1|구현할 내용을 최소 단위로 분리하고 구현할 객체 선정 체계화|
|2|계산의 수행 속도 향상을 위한 C언어와 Python의 연동 구성|
|3|Python class 정의 및 구현|
|4|C solve function 구현|
|5|Python & C 연동|
|6|Test data 생성|
|7|Test 및 결과 비교|

*****

## 진행 상황
### 18-24, July
계획 수립  
핵심적인 부분은?  
* Module : 해석에 있어서 가장 작은 단위, 입출구 조건 4개에 의해서 결과(전력 및 열량)를 출력하는 것을 구현해야 함
  * hot & cold side 유체의 물성 및 입구 유량, inlet 형상, 소자 물성, 소자 형상에 대한 접근 가능
  * inlet 형상 유체의 물성 및 입구 유량을 통해 열전달 및 유동 특성 계산
  * 입력으로 입출구 4개의 온도를 받음
  * 전기적 특성 계산
  * 피드백 받은 열전달 특성 계산 후 결과(Q_h_H,Q_h_E,Q_c_H,Q_c_E) return
* solver : Module에서 처리하는 결과들을 받아서 피드백 해주는 기능을 가짐, 혹은 각각의 클래스들을 연결시키는 기능을 함
  * Module에서 전달받은 전압과 저항을 통해 회로 해석 후 전류 도출 및 Module에 전달
  * Module에서 전달받은 결과를 통해 온도 조정 
  
각각을 위해 필요한 구조들
* material : 물성치를 정의하는 모듈, 유체 및 고체의 특성을 담고 있어야 하며 유체의 경우 입력받은 값에 의해서 유동 특성을 도출 할 수 있게 설계
* Shape : 단면 형상을 정의하는 모듈, 옵션을 통해서 heatsink 혹은 clearance 등의 상황을 사용자가 입력할 수 있도록 하고 그에 맞는 계산을 수행할 수 있도록 설계
* Path : 유동 및 전기적 연결을 정의하는 모듈, 연결되어 있는 입구와 출구를 지정하여 유향그래프로 저장, 입력받은 경로에 따라서 계산 순서를 반환할 수 있어야 함

가장 많은 계산이 소요되는 구간은 식에 값을 대입하여 결과를 도출해야하는 과정인 전압 및 저항 계산, 열유속 계산 과정  
이는 단순히 순차적 계산만이 요구되는 구간으로 속도의 향상을 위해서 C를 통해 처리하는 것이 효과적  
  
### 25-31, July
* material 모듈 개선
  이전의 모델의 경우 새로운 물성치를 정의하고 사용하는 과정에서 사용자에게 모든 입력값을 받아야 했기 때문에 굉장히 번거로운 과정이 있었음  
  그래서 이러한 불편 사항을 개선하기 위해 기본적으로 자주 사용하는 물질(ex. air, water, steel, aluminum)등을 미리 정의해두고 수정할 수 있는 기능을 추가  
* Path 모듈 구현
  회로를 입력받으면 전류를 계산할 수 있는 solve 기능 구현  
  유향그래프를 이용하며 너비우선탐색을 이용하여 회로를 해석  
    * 시작점에서 가까운 부분부터 정의해가는 것이 유용하기때문에 DFS보다 BFS가 적절
  각 노드는 전압 및 저항을 가지고 있으며 자신에게 들어오고 나가는 전압과 전류 정보를 가지고 있어야 함  
  전압 정보는 각 노드의 경로에 의존하며 시작점에서부터의 경로를 저장함, 전류는 부모노드와 자식노드에 의존하며 이들의 인덱스 정보를 저장  
  입력 전류와 출력 전류의 정보가 다른 노드를 탐색하고 둘이 동일하다는 것을 이용하여 해석 가능
  동일한 노드의 서로 다른 인덱스의 입력 전압 정보가 주어진 경우 서로 동일하다는 것을 이용하여 해석 가능  
  Load Resistence를 알아내기 위해 모든 노드의 전압이 0인 동일한 회로를 복사하여 해석할 필요가 있음
  <details>
    <summary>이 방식으로 다 하지 않는 이유</summary>
      <div markdown="1">
        
        Load Resistence 를 구하기 위한 Thevenin's theorem의 활용은 등가 저항을 구하는 아이디어만 착안하는데 이는 등가 전압을 해석하는 비용이 많이 듦  
        한 노드의 전류를 정확히 구하기 위해서는 등가전압까지 구해내야 하며 이는 회로의 크기가 커질 경우 계산복잡도가 크게 증가  
          
        Load Resistence 를 구하기 위한 방법은 회로의 등가저항을 구하는 것이므로 필수적으로 필요한 과정  
        하지만 이후 각 노드의 전류를 구하는 과정은 각각을 독립적으로 해석하여 계산 비용을 증가시킬 필요가 없음
  
      </div>
    </details>
