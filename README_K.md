# Project AI

### 목표
Window 환경에 있어서
* 3D cad 파일 및 해석 결과 파일을 처리하여 학습 데이터를 만들기 위한 자동화 프로세스 구현하기
* 딥러닝을 이용한 속도장 예측하기(첫 번째 목표 달성 시 진행 예정)
  * 다른 CFD 시뮬레이션보다 월등히 빠른 계산 속도
  * 상당한 정확도  
등을 만족해야함

<details>
  <summary>CFD?</summary>
  <div markdown="1">
    
    CFD는 Computational Fuild Dynamics의 약자입니다.
      
    유체역학에 있어서,  
    general equations으로 알려진 Navier-Stokes equations은 수학적으로 분석될 수 없는 비선형 방정식입니다.  
      
    그래서 우리는 수학적인 해가 아닌 수치적인(컴퓨터 계산을 통한) 근사해만을 간신히 구할 수 있습니다.  
    CFD는 ns-eqn을 수치적인 방법을 통해 계산합니다.
    
    이러한 고전적인 유동해석 방식을 위한 프로세스는 수많은 iteration이 필요하기 때문에 한 번의 해석에 굉장한 시간이 걸리게 됩니다.
    
  </div>
</details>

### 구현 사항
* 3d CAD 및 해석 결과 파일을 특정 간격의 평면(이미지)으로 분리하고
* 분리된 각각의 평면(이미지)을 작은 격자로 나누어(Meshing)
* 3d CAD 파일의 경우 각각의 격자들에 대한 형상 정보만을
* 해석 결과 파일의 경우 형상 정보 및 속도 벡터를 .csv 형식으로 저장한다.

### 추가 사항
* 언어 : Python, matlab
* 개발환경 : VScode & jupyter notebook
* 개발 기간 : 8 weeks

### 사용할(학습해야 할) 라이브러리
* library : win32com, openCV(필요시)

### 진행 계획
|index|note|
|--|--|
|1~5|win32com 라이브러리를 활용한 inventor(3d CAD App) 및 COMSOL(CFD 프로그램) 처리 자동화|
|1|3d CAD 파일 솔리드 분해(혹은 Meshing) 자동화|
|2|생성된 격자(Mesh)의 형상 정보 접근 및 저장 자동화|
|3~5|CFD 해석 결과 파일 Meshing 자동화|
|6|생성된 Mesh 형상 및 속도장 정보 접근 및 저장 자동화|
|7|training dataset 준비 및 모델 훈련|
|8|Test|
