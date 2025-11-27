{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ea0af36a-8efc-4df6-a3f5-829d18204d1c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: pip in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (25.3)\n"
     ]
    }
   ],
   "source": [
    "!python -m pip install --upgrade pip"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "171898d2-6191-4348-93ad-59c4225d7ba3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: folium in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (0.20.0)\n",
      "Requirement already satisfied: branca>=0.6.0 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from folium) (0.8.2)\n",
      "Requirement already satisfied: jinja2>=2.9 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from folium) (3.1.6)\n",
      "Requirement already satisfied: numpy in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from folium) (2.3.5)\n",
      "Requirement already satisfied: requests in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from folium) (2.32.5)\n",
      "Requirement already satisfied: xyzservices in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from folium) (2025.11.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from jinja2>=2.9->folium) (3.0.3)\n",
      "Requirement already satisfied: charset_normalizer<4,>=2 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from requests->folium) (3.4.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from requests->folium) (3.11)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from requests->folium) (2.5.0)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from requests->folium) (2025.11.12)\n",
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: haversine in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (2.9.0)\n",
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: pandas in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (2.3.3)\n",
      "Requirement already satisfied: numpy>=1.26.0 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from pandas) (2.3.5)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install folium\n",
    "!pip install haversine\n",
    "!pip install pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9f08e37d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import requests\n",
    "import folium as g\n",
    "import heapq\n",
    "import collections\n",
    "import sys\n",
    "from haversine import haversine\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0a4e64da",
   "metadata": {},
   "outputs": [],
   "source": [
    "def addr_to_lat_lon(addr):\n",
    "    url = 'https://dapi.kakao.com/v2/local/search/address.json?query={address}'.format(address=addr)\n",
    "    headers = {\"Authorization\": \"KakaoAK \" + \"9eed97785c1b2068d8f5a391d896567e\"}\n",
    "    result = json.loads(str(requests.get(url, headers=headers).text))\n",
    "    match_first = result['documents'][0]['address']\n",
    "    return float(match_first['x']), float(match_first['y'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "6b302bcf",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'documents'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[7], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m a, b \u001b[38;5;241m=\u001b[39m \u001b[43maddr_to_lat_lon\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43m서울 노원구 월계동 447-1\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\n",
      "Cell \u001b[1;32mIn[4], line 5\u001b[0m, in \u001b[0;36maddr_to_lat_lon\u001b[1;34m(addr)\u001b[0m\n\u001b[0;32m      3\u001b[0m headers \u001b[38;5;241m=\u001b[39m {\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mAuthorization\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mKakaoAK \u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;241m+\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m9eed97785c1b2068d8f5a391d896567e\u001b[39m\u001b[38;5;124m\"\u001b[39m}\n\u001b[0;32m      4\u001b[0m result \u001b[38;5;241m=\u001b[39m json\u001b[38;5;241m.\u001b[39mloads(\u001b[38;5;28mstr\u001b[39m(requests\u001b[38;5;241m.\u001b[39mget(url, headers\u001b[38;5;241m=\u001b[39mheaders)\u001b[38;5;241m.\u001b[39mtext))\n\u001b[1;32m----> 5\u001b[0m match_first \u001b[38;5;241m=\u001b[39m \u001b[43mresult\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mdocuments\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m]\u001b[49m[\u001b[38;5;241m0\u001b[39m][\u001b[38;5;124m'\u001b[39m\u001b[38;5;124maddress\u001b[39m\u001b[38;5;124m'\u001b[39m]\n\u001b[0;32m      6\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mfloat\u001b[39m(match_first[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mx\u001b[39m\u001b[38;5;124m'\u001b[39m]), \u001b[38;5;28mfloat\u001b[39m(match_first[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124my\u001b[39m\u001b[38;5;124m'\u001b[39m])\n",
      "\u001b[1;31mKeyError\u001b[0m: 'documents'"
     ]
    }
   ],
   "source": [
    "a, b = addr_to_lat_lon('서울 노원구 월계동 447-1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2cf4d795-a5dc-42d3-9a7f-929aefcd8964",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "#노드들의 정보 불러오기\n",
    "with open(\"C:\\\\Users\\\\home\\\\Documents\\\\카카오톡 받은 파일\\\\node.json\",\"r\") as file1:\n",
    "    node_data = json.load(file1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8203c401-59e9-4de6-aa8f-ccd80f675f22",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'neighbor'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[9], line 6\u001b[0m\n\u001b[0;32m      4\u001b[0m n1 \u001b[38;5;241m=\u001b[39m node_data[i]\n\u001b[0;32m      5\u001b[0m n1_id \u001b[38;5;241m=\u001b[39m n1[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m'\u001b[39m]\n\u001b[1;32m----> 6\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m j \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mrange\u001b[39m(\u001b[38;5;28mlen\u001b[39m(\u001b[43mn1\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mneighbor\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m]\u001b[49m)):\n\u001b[0;32m      7\u001b[0m     n2_id \u001b[38;5;241m=\u001b[39m n1[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mneighbor\u001b[39m\u001b[38;5;124m'\u001b[39m][j]\n\u001b[0;32m      8\u001b[0m     l_id \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m_\u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;241m.\u001b[39mformat(n1_id, n2_id)\n",
      "\u001b[1;31mKeyError\u001b[0m: 'neighbor'"
     ]
    }
   ],
   "source": [
    "link_data = []\n",
    "#각 인접한 노드끼리의 거리를 딕셔너리 형태로 리스트에 넣기\n",
    "for i in range(len(node_data)):\n",
    "    n1 = node_data[i]\n",
    "    n1_id = n1['id']\n",
    "    for j in range(len(n1[\"neighbor\"])):\n",
    "        n2_id = n1['neighbor'][j]\n",
    "        l_id = \"{}_{}\".format(n1_id, n2_id)\n",
    "        dict = {}\n",
    "        dict[\"id\"] = l_id\n",
    "        dict[\"distance\"] = haversine((n1[\"lat\"],n1[\"lon\"]),(node_data[n2_id - 1][\"lat\"],node_data[n2_id - 1][\"lon\"]))\n",
    "        link_data.append(dict)\n",
    "#인접한 노드들의 link정보들을  link.json라는 이름의 json파일로 만들기\n",
    "with open(\"C:\\\\Users\\\\home\\\\Documents\\\\카카오톡 받은 파일\\\\node.json\", \"w\") as file:\n",
    "    json.dump(link_data, file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f859022f-3033-4167-b215-2b52d056c5fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "#링크된 노드들의 정보 불러오기\n",
    "with open(\"C:\\\\Users\\\\home\\\\Documents\\\\카카오톡 받은 파일\\\\node.json\",\"r\") as file2:\n",
    "    link_data = json.load(file2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "40bc6af2-6653-4cc3-928b-0387d1903d65",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'type'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[11], line 13\u001b[0m\n\u001b[0;32m     11\u001b[0m n1_strid \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;241m.\u001b[39mformat(n1_id)\n\u001b[0;32m     12\u001b[0m l_dict \u001b[38;5;241m=\u001b[39m {}\n\u001b[1;32m---> 13\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[43mn1\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mtype\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m]\u001b[49m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnode\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[0;32m     14\u001b[0m     len_node \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;241m1\u001b[39m\n\u001b[0;32m     15\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m j \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mrange\u001b[39m(\u001b[38;5;28mlen\u001b[39m(n1[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mneighbor\u001b[39m\u001b[38;5;124m'\u001b[39m])):\n",
      "\u001b[1;31mKeyError\u001b[0m: 'type'"
     ]
    }
   ],
   "source": [
    "graph1 = {} \n",
    "graph2 = {} \n",
    "node_dict = {} #노드와 노드끼리의 distance를 담은 딕셔너리와 노드들의 위치 정보를 담은 딕셔너리 만들기\n",
    "len_node = 0\n",
    "\n",
    "#가로등, cctv까지 포함한 graph\n",
    "\n",
    "for i in range(len(node_data)):\n",
    "    n1 = node_data[i]\n",
    "    n1_id = n1['id']\n",
    "    n1_strid = \"{}\".format(n1_id)\n",
    "    l_dict = {}\n",
    "    if n1['type'] == \"node\":\n",
    "        len_node += 1\n",
    "    for j in range(len(n1['neighbor'])):\n",
    "        n2_id = n1['neighbor'][j]\n",
    "        n2_strid = \"{}\".format(n2_id)\n",
    "        l_id = \"{}_{}\".format(n1_id, n2_id)\n",
    "        if node_data[n2_id - 1][\"type\"] == \"street\" or node_data[n2_id - 1][\"type\"] == \"cctv\":\n",
    "            for k in range(len(link_data)):\n",
    "                if l_id == link_data[k]['id']:\n",
    "                    l_dict[n2_strid] = link_data[k]['distance']\n",
    "        else:\n",
    "            for k in range(len(link_data)):\n",
    "                if l_id == link_data[k]['id']:\n",
    "                    l_dict[n2_strid] = link_data[k]['distance'] + 0.35 #기로응과 cctv가 아니면 가중치부여\n",
    "    graph1[n1_strid] = l_dict\n",
    "    if n1['type'] == \"node\":\n",
    "        node_dict[n1_strid] = [n1['lat'], n1['lon']]\n",
    "\n",
    "#노드들만 포함한 graph\n",
    "\n",
    "for i in range(len_node):\n",
    "    n1 = node_data[i]\n",
    "    n1_id = n1['id']\n",
    "    n1_strid = \"{}\".format(n1_id)\n",
    "    l_dict = {}\n",
    "    for j in range(len(n1['neighbor'])):\n",
    "        n2_id = n1['neighbor'][j]\n",
    "        if n2_id > len_node: pass\n",
    "        else:\n",
    "            n2_strid = \"{}\".format(n2_id)\n",
    "            l_id = \"{}_{}\".format(n1_id, n2_id)\n",
    "            for k in range(len(link_data)):\n",
    "                if l_id == link_data[k]['id']:\n",
    "                    l_dict[n2_strid] = link_data[k]['distance']\n",
    "    graph2[n1_strid] = l_dict\n",
    "\n",
    "#graph 예시 {'1': {'13': 1부터 13까지의 distance}}\n",
    "#node_dict 예시 {'1': [1번 노드의 위도, 1번노드의 경도]} but, 가로등과 cctv는 넣지 않음"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b46a6999-adf5-4e47-943b-73d6c737d8fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "#가로등, cctv 위치정보 불러오기\n",
    "file3 = r\"C:\\Users\\COMS02\\Downloads\\서울시 노원구 안심이 CCTV 연계 현황.csv\"\n",
    "file4 = r\"C:\\Users\\COMS02\\Downloads\\서울특별시_노원구_보안등정보_20230726.csv\"\n",
    "\n",
    "# 데이터프레임 NaN 값 대체\n",
    "cctv_csv = pd.read_csv(file3,encoding='cp949')\n",
    "cctv_csv = cctv_csv.fillna(0.0)\n",
    "street_csv = pd.read_csv(file4,encoding='cp949')\n",
    "street_csv = cctv_csv.fillna(0.0)\n",
    "# x좌표(위도),y좌표(경도) 리스트로 만들기\n",
    "x1 = []\n",
    "y1 = []\n",
    "x2 = []\n",
    "y2 = []\n",
    "for i in range(len(cctv_csv['위도'])):\n",
    "    if cctv_csv['위도'][i] == 0.0 or cctv_csv['경도'][i] == 0.0:\n",
    "        pass\n",
    "    else:\n",
    "        x1.append(cctv_csv['위도'][i])\n",
    "        y1.append(cctv_csv['경도'][i])\n",
    "        \n",
    "for i in range(len(street_csv['위도'])):\n",
    "    if street_csv['위도'][i] == 0.0 or street_csv['경도'][i] == 0.0:\n",
    "        pass\n",
    "    else:\n",
    "        x2.append(cctv_csv['위도'][i])\n",
    "        y2.append(cctv_csv['경도'][i])\n",
    "        \n",
    "g_map = g.Map(location=[b, a], zoom_start = 17)\n",
    "#for i in range(len(x1)):\n",
    "    #marker = g.Marker([x1[i],y1[i]], popup = 'cctv_%d'%i, icon = g.Icon(color = 'red')).add_to(g_map)\n",
    "#for i in range(len(x2)):\n",
    "    #marker = g.Marker([x2[i],y2[i]], popup = 'street_%d'%i, icon = g.Icon(color = 'green')).add_to(g_map)\n",
    "#g_map"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a8773079-8d6c-4f42-bd39-31b3a7fcc013",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'b' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[12], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m g_map \u001b[38;5;241m=\u001b[39m g\u001b[38;5;241m.\u001b[39mMap(location\u001b[38;5;241m=\u001b[39m[\u001b[43mb\u001b[49m, a], zoom_start \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m17\u001b[39m)\n\u001b[0;32m      2\u001b[0m \u001b[38;5;66;03m#각 노드갯수만큼 지도에 마커찍기\u001b[39;00m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mrange\u001b[39m(\u001b[38;5;28mlen\u001b[39m(node_data)):\n",
      "\u001b[1;31mNameError\u001b[0m: name 'b' is not defined"
     ]
    }
   ],
   "source": [
    "g_map = g.Map(location=[b, a], zoom_start = 17)\n",
    "#각 노드갯수만큼 지도에 마커찍기\n",
    "for i in range(len(node_data)):\n",
    "    if node_data[i][\"type\"] == \"node\":\n",
    "        marker = g.Circle([node_data[i][\"lat\"],node_data[i][\"lon\"]], radius = 4, fill = 'blue', fill_opacity = 100, \n",
    "                          popup = node_data[i][\"id\"], icon = g.Icon(color = 'blue')).add_to(g_map)\n",
    "    elif node_data[i][\"type\"] == \"street\":\n",
    "        marker = g.Marker([node_data[i][\"lat\"],node_data[i][\"lon\"]], popup = node_data[i][\"id\"], icon = g.Icon(color = 'green')).add_to(g_map)\n",
    "    elif node_data[i][\"type\"] == \"cctv\":\n",
    "        marker = g.Marker([node_data[i][\"lat\"],node_data[i][\"lon\"]], popup = node_data[i][\"id\"], icon = g.Icon(color = 'red')).add_to(g_map)\n",
    "\n",
    "g_map"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "d0dbdf9c-12a3-438e-8750-e8ab00af2850",
   "metadata": {},
   "outputs": [],
   "source": [
    "def dijkstra(start, graph):\n",
    "    # 초기 배열 설정\n",
    "    distances = {node: [sys.maxsize, -1] for node in graph}\n",
    "    # 시작 노드의 거리는 0으로 설정\n",
    "    distances[start][0] = 0\n",
    "    queue = []\n",
    "    heapq.heappush(queue, (distances[start][0], start))\n",
    "\n",
    "    # 우선 순위 큐에 데이터가 하나도 없을 때까지 반복\n",
    "    while queue:\n",
    "        # 가장 낮은 거리를 가진 노드와 거리를 추출\n",
    "        curr_dist, node = heapq.heappop(queue)\n",
    "        if distances[node][0] < curr_dist:\n",
    "            continue \n",
    "        # 대상인 노드에서 인접한 노드와 거리를 순회\n",
    "        for adjacency_node, distance in graph[node].items():\n",
    "            # 현재 노드에서 인접한 노드를 지나갈 때까지의 거리를 더함\n",
    "            weighted_distance = curr_dist + distance\n",
    "            # 배열의 저장된 거리보다 위의 가중치가 더 작으면 해당 노드의 거리 변경\n",
    "            if weighted_distance < distances[adjacency_node][0]:\n",
    "                # 배열에 저장된 거리보다 가중치가 더 작으므로 변경\n",
    "                distances[adjacency_node] = [weighted_distance, node]\n",
    "                # 다음 인접 거리를 계산 하기 위해 우선 순위 큐에 삽입 (노드가 동일해도 일단 다 저장함)\n",
    "                heapq.heappush(queue, (weighted_distance, adjacency_node))\n",
    "    return distances"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "13e2e661",
   "metadata": {},
   "outputs": [],
   "source": [
    "#각 노드들이 지나온 거리 구하기\n",
    "def path_finder(info, start, end):\n",
    "    path = [end]\n",
    "    parent = info[end][1]\n",
    "    while parent != -1:\n",
    "        path.append(parent)\n",
    "        parent = info[parent][1]\n",
    "    path.reverse()\n",
    "    return path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "6926e195-0877-456a-85ba-eee1b59564d1",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'b' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[15], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m g_map \u001b[38;5;241m=\u001b[39m g\u001b[38;5;241m.\u001b[39mMap(location\u001b[38;5;241m=\u001b[39m[\u001b[43mb\u001b[49m, a], zoom_start \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m17\u001b[39m)\n\u001b[0;32m      3\u001b[0m \u001b[38;5;66;03m#각 노드갯수만큼 지도에 마커찍기\u001b[39;00m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mrange\u001b[39m(\u001b[38;5;28mlen\u001b[39m(node_data)):\n",
      "\u001b[1;31mNameError\u001b[0m: name 'b' is not defined"
     ]
    }
   ],
   "source": [
    "g_map = g.Map(location=[b, a], zoom_start = 17)\n",
    "\n",
    "#각 노드갯수만큼 지도에 마커찍기\n",
    "for i in range(len(node_data)):\n",
    "    if node_data[i][\"type\"] == \"node\":\n",
    "        marker = g.Circle([node_data[i][\"lat\"],node_data[i][\"lon\"]], radius = 4, fill = 'blue', fill_opacity = 100, \n",
    "                          popup = node_data[i][\"id\"], icon = g.Icon(color = 'blue')).add_to(g_map)\n",
    "    elif node_data[i][\"type\"] == \"street\":\n",
    "        marker = g.Marker([node_data[i][\"lat\"],node_data[i][\"lon\"]], popup = node_data[i][\"id\"], icon = g.Icon(color = 'green')).add_to(g_map)\n",
    "    elif node_data[i][\"type\"] == \"cctv\":\n",
    "        marker = g.Marker([node_data[i][\"lat\"],node_data[i][\"lon\"]], popup = node_data[i][\"id\"], icon = g.Icon(color = 'red')).add_to(g_map)\n",
    "start = input(\"출발 지점:\")\n",
    "arrive = input(\"도착 지점:\")\n",
    "\n",
    "#기존 최단경로 알고리즘\n",
    "dist_info = dijkstra(start, graph2)\n",
    "#print(\"기존 거리: {:.3f}km\".format(dist_info.get(arrive, 0)[0]))\n",
    "\n",
    "curr_path = path_finder(dist_info, start, arrive)\n",
    "lation_list = []\n",
    "for n in curr_path:\n",
    "    if node_data[int(n)-1][\"type\"] == \"node\":\n",
    "        lation_list.append(node_dict[n])\n",
    "g.PolyLine(locations = lation_list, tooltip = 'Polyline').add_to(g_map)\n",
    "\n",
    "#가로등, cctv를 반영한 경로 알고리즘\n",
    "dist_info = dijkstra(start, graph1)\n",
    "#print(\"반영 거리: {:.3f}km\".format(dist_info.get(arrive, 0)[0]))\n",
    "\n",
    "curr_path = path_finder(dist_info, start, arrive)\n",
    "lation_list = []\n",
    "for n in curr_path:\n",
    "    if node_data[int(n)-1][\"type\"] == \"node\":\n",
    "        lation_list.append(node_dict[n])\n",
    "g.PolyLine(locations = lation_list, tooltip = 'Polyline', color = 'red').add_to(g_map)\n",
    "\n",
    "g_map"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
