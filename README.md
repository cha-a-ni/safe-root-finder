# safe-root-finder

가로등·CCTV 등 안전 시설물 데이터를 활용해 단순 최단 경로가 아닌 **안전 경로(Safe Path)**를 탐색하는 알고리즘 프로젝트입니다.  
지도 기반 그래프를 구성하고, 안전 가중치를 반영해 더 안전한 경로를 계산합니다.

---

## 📌 프로젝트 개요

- 목표: 시설물 안전 요소(가로등·CCTV)를 반영한 안전 경로 탐색
- 핵심 개념:
  - 교차로·도로 지점을 노드(Node)
  - 도로 연결을 엣지(Edge)
  - 링크·시설물 데이터를 이용한 가중치(weight) 기반 경로 계산
- 개발 환경: Python, Jupyter Notebook
- 활용 API: Kakao Local API(주소 → 좌표 변환)

---

## 🔧 기술 요소

- NetworkX 기반 그래프 생성 및 최단 경로 탐색
- JSON 기반 노드/엣지/시설물 데이터 로딩
- 주소 좌표 변환(Kakao Local API)
- 안전 가중치 적용(CCTV/가로등 수 반영)
- 최단 경로 vs 안전 경로 비교 시각화

---

## 📁 프로젝트 구조

safe-route-planner/  
├── README.md  
├── src/  
│   └── map_algorithm_r1.ipynb
└── data/  
    ├── link.json  
    └── node.json (필요한 경우)  


---

## 🧠 알고리즘 구성 과정

### 1) 주소 → 좌표 변환 (Kakao Local API)
Kakao Local API를 활용하여 입력 주소를 좌표(x, y)로 변환합니다.  
주소가 인식되지 않으면 documents가 빈 리스트로 반환되므로 예외 처리 적용.

### 2) 노드·엣지 데이터 로딩
node.json: 각 노드의 ID와 좌표  
link.json: 노드 간 연결 정보  

### 3) 그래프 구성 (NetworkX)
노드를 좌표 기반으로 추가하고, 링크 데이터를 이용해 엣지를 생성합니다.

### 4) 안전 가중치 적용
- 가로등이 많은 구간 → weight 감소  
- CCTV 있는 구간 → weight 감소  
- 어두운 구간 → weight 증가  
- 거리(distance) 또한 기본 weight로 포함  

### 5) 경로 탐색
- Shortest Path: 거리 기반 가중치  
- Safe Path: 안전 가중치(safe_weight) 기반  

---


## 🧪 실험 결과

- 최단 경로는 가장 빠르지만 어두운 구간을 포함할 수 있음  
- 안전 경로는 거리가 약간 길어지지만 가로등과 CCTV가 많은 구간을 선택  
- 안전 가중치 조절에 따라 경로가 크게 변화함  
→ 경로 의사결정에서 **가중치 설계의 중요성** 확인

---

## 🎯 배운 점

- 그래프 이론(Node/Edge/Weight)을 실제 지도 문제에 적용
- JSON 데이터 처리 및 Kakao API 활용 능력 향상
- 데이터 기반 의사결정 및 경로 최적화 경험
- 리스크 기반 안전 경로 모델 설계의 의미 체감

---
