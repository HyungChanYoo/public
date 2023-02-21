Registry
========

마이크로소프트 윈도우 32/64비트 버전과 윈도우 모바일 운영체제의 설정과 선택 항목을 담고 있는 데이터베이스로, 모든 하드웨어, 운영 체제 소프트웨어, 대부분의 비운영 체제 소프트웨어, 사용자 PC 선호도 등에 대한 정보와 설정이 들어 있음.
사용자가 제어판 설정, 파일 연결, 시스템 정책, 또는 설치된 소프트웨어를 변경하면, 이에 따른 변경 사항들이 레지스트리에 반영되어 저장됨.

## 구조

`키`와 `값`으로 구성되어 있음

레지스트리 `키`는 폴더와 비슷. -값과 더불어, 각 키는 서브키를 가질 수 있음.
백슬래시를 사용하여 키 계급 수준을 지시

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows는 
"HKEY_LOCAL_MACHINE" 키의 "Software" 서브키의 "Microsoft" 서브키의 "Windows"라는 서브키를 가리킴/

레제스트리 `값`은 키 안에 들어 있는 이름/자료.
값은 여러 키로부터 따로 참조할 수  있음.
값 이름은 백슬래시를 포함할 수 있어서 키 경로와 구별하는 것이 어려울 수 있음.

<table>
  <tr>
    <td colspan="3" align="center">레지스트 값 종류 목록</td>    
  </tr>
  <tr>
    <td>0</td>
    <td>REG_NONE</td>
    <td>종류 없음</td>    
  </tr>
  <tr>
    <td>1</td>
    <td>REG_SZ</td>
    <td>문자열 값</td>    
  </tr>
  <tr>
    <td>2</td>
    <td>REG_EXPAND_SZ</td>
    <td>확장할 수 있는 문자열 값, 환경 변수를 포함할 수 있음.</td>    
  </tr>
  <tr>
    <td>3</td>
    <td>REG_BINARY</td>
    <td>이진값(임의의 데이터, 00~FF)</td>    
  </tr>
  <tr>
    <td>4</td>
    <td>REG_DWORD/REG_DWORD_LITTLE_ENDIAN</td>
    <td>DWORD 값 (32 비트) 정수 (0 ~ 4,294,967,295 [2^32 – 1]) (리틀 엔디언)</td>    
  </tr>
  <tr>
    <td>5</td>
    <td>REG_DWORD_BIG_ENDIAN</td>
    <td>WORD 값 (32 비트) 정수 (0 ~ 4,294,967,295 [232 – 1]) (빅 엔디언)</td>    
  </tr>
  <tr>
    <td>6</td>
    <td>REG_LINK</td>
    <td>심볼 링크 (유니코드)</td>    
  </tr>
  <tr>
    <td>7</td>
    <td>REG_MULTI_SZ</td>
    <td>다중 문자열 값 (고유한 문자열의 배열)</td>    
  </tr>
  <tr>
    <td>8</td>
    <td>REG_RESOURCE_LIST</td>
    <td>리소스 목록 (플러그 앤 플레이 하드웨어 열거 및 구성에 쓰임)</td>    
  </tr>
  <tr>
    <td>9</td>
    <td>REG_FULL_RESOURCE_DESCRIPTOR</td>
    <td>리소스 서술자 (플러그 앤 플레이 하드웨어 열거 및 구성에 쓰임)</td>    
  </tr>
  <tr>
    <td>10</td>
    <td>REG_RESOURCE_REQUIREMENTS_LIST</td>
    <td>리소스 요구 목록 (플러그 앤 플레이 하드웨어 열거 및 구성에 쓰임)</td>    
  </tr>
  <tr>
    <td>11</td>
    <td>REG_QWORD/REG_QWORD_LITTLE_ENDIAN	</td>
    <td>QWORD 값 (64 비트 정수), 빅/리틀 엔디언 또는 정의되지 않음 (윈도우 2000에 도입)</td>    
  </tr>  
</table>

## 하이브

레지스트리는 수많은 논리를 구분하는 `하이브`로 나눌 수 있음. 모든 하이브는 `HKEY`로 시작.

HKEY_LOCAL_MACHINE과 HKEY_CURRENT_USER 노드는 서로 비슷한 구조를 가지고 있음.
응용 프로그램은 보통 "HKEY_CURRENT_USER\Software\제조업체 이름\응용 프로그램 이름\버전 번호\설정 이름"의 설정 항목을 검색하고 설정값을 찾지 못할 경우 HKEY_LOCAL_MACHINE 키의 같은 위치에서 다시 한 번 검색.
또, HKEY_LOCAL_MACHINE을 먼저 기록하지만 (로그온한 사용자가 관리자가 아닌 경우 등에 따라) 기록하지 못하는 경우, 설정값은 HKEY_CURRENT_USER에 대신 저장.

종류
* HKEY_CLASSES_ROOT(HKCR): 파일 연결, 확장자 설정, OLE 객체 클래스 ID와 같은 등록된 응용 프로그램 정보를 담고 있음.
* HKEY_CURRENT_USER(HKCU): 현재 로그인한 사용자의 설정을 담고 있음.
* HKEY_LOCAL_MACHINE(HKLM): 컴퓨터의 모든 사용자의 설정을 담고 있음.
* HKEY_USERS(HKU): 컴퓨터에서 사용 중인 각 사용자 프로파일에 대한 HKEY_CURRENNT_USER 키에 일치하는 서브키를 담고 있음.
* HKEY_CURRENT_CONFIG: 실행 시간에 수집한 자룔르 담고 있음. 이 키에 저장된 정보는 디스크에 영구적으로 저장되지 않고 시동 시간에 생성됨.
* HKEY_PERFORMANCE_DATA: 런타임 성능 데이트 정보를 제공. 이 키는 레지스트리 편집기에 보이지 않지만 윈도우 API의 레지스트리 명령어를 통해 볼 수 있음.
* HKEY_DYN_DATA: 이 키는 윈도우 95, 윈도우 98, 윈도우 Me에만 쓰임. 플러그 앤 플레이를 비롯한 하드웨어 장치, 네트워크 성능 통계에 대한 정보를 포함. 이 하이브의 정보는 하드 드라이브에 저장되지 않는다. 플러그 앤 플레이 정보는 컴퓨터가 시작할 때 구성되면 메모리에 저장됨.

위키백과/나무위키
