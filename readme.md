# AI 논문 리뷰 팀 웹 애플리케이션

이 웹 애플리케이션은 AI 논문을 분석하고 요약하는 팀의 역할을 시뮬레이션합니다. Sam, Jenny, Will이라는 가상의 팀원이 각자의 역할에 따라 논문을 분석하고 최종 보고서를 작성합니다.

## 📋 목차
- [기능](#기능)
- [설치 방법](#설치-방법)
- [사용법](#사용법)
- [주의사항](#주의사항)
- [문의](#문의)

## ✨ 기능

### 팀 구성
- **Sam (AI PhD)**: 논문의 주요 포인트와 방법론을 간단히 설명
- **Jenny (AI & Education PhD)**: Sam의 초안을 검토하고 교육적 관점에서 개선
- **Will (Team Leader)**: 최종 보고서를 작성

### 주요 기능
- PDF 파일에서 텍스트 자동 추출
- 단계별 논문 분석 및 요약
- 교육적 관점의 내용 개선
- 구조화된 최종 보고서 생성

## 🚀 설치 방법

### 1. 가상환경 생성 및 활성화

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 2. 필요한 라이브러리 설치

```bash
pip install -r requirements.txt
```

requirements.txt가 없는 경우:
```bash
pip install streamlit google-generativeai PyPDF2
```

## 💻 사용법

1. **애플리케이션 실행**
   ```bash
   streamlit run gemini_pdf_reader.py
   ```

2. **웹 인터페이스 사용**
   - Gemini API 키 입력
   - PDF 파일 업로드
   - "논문 리뷰 시작" 버튼 클릭

3. **결과 확인**
   - Sam의 초기 분석
   - Jenny의 검토 및 개선사항
   - Will의 최종 보고서

## ⚠️ 주의사항

- Google Generative AI API 키가 필요합니다
  - [Google AI Studio](https://makersuite.google.com/app/apikey)에서 발급 가능
- PDF 텍스트 추출 품질은 PDF 파일의 형식에 따라 달라질 수 있습니다
- 대용량 PDF 파일의 경우 처리 시간이 길어질 수 있습니다

## 📞 문의

프로젝트에 대한 문의나 버그 리포트는 다음 방법으로 연락해 주세요:
- 이슈 등록: [GitHub Issues](링크)
- 이메일: [이메일 주소]

## 📄 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.