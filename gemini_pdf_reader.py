import streamlit as st
import google.generativeai as genai
import PyPDF2

def create_team_prompt(text_content: str, role: str) -> str:
    if role == "sam":
        return f"""당신은 Sam입니다. AI PhD 출신으로 복잡한 AI 개념을 쉽게 설명하는 전문가입니다.
        다음 논문을 분석하여 주요 포인트, 방법론, 발견사항을 파악하고 간단한 용어로 설명해주세요:
        
        논문 내용: {text_content}
        
        다음 형식으로 작성해주세요:
        1. 주요 포인트
        2. 연구 방법론
        3. 주요 발견사항
        4. 간단한 설명"""
        
    elif role == "jenny":
        return f"""당신은 Jenny입니다. AI와 교육 분야의 PhD를 가진 전문가입니다.
        Sam의 초안을 검토하고 더 이해하기 쉽게 개선해주세요:
        
        Sam의 분석: {text_content}
        
        다음을 포함해주세요:
        1. 더 쉬운 설명
        2. 교육적 맥락
        3. 실제 응용 사례
        4. 추가 설명이 필요한 부분"""
        
    else:  # will
        return f"""당신은 팀 리더 Will입니다. 최종 보고서를 작성해주세요:
        
        이전 분석: {text_content}
        
        다음 구조로 작성해주세요:
        1. 핵심 요약
        2. 연구 주제 소개
        3. 주요 발견 및 방법론
        4. 복잡한 개념의 쉬운 설명
        5. 실제 응용 및 영향
        6. 결론 및 향후 연구 방향"""

def main():
    st.title("AI 논문 리뷰 팀 with Gemini")
    
    # 팀 소개
    st.header("📚 논문 리뷰 팀 소개")
    team_info = {
        "Sam (AI PhD)": "복잡한 AI 개념을 간단한 용어로 설명하는 전문가",
        "Jenny (AI & Education PhD)": "교육적 관점에서 내용을 더 이해하기 쉽게 개선하는 전문가",
        "Will (Team Leader)": "최종 보고서를 구조화하고 완성하는 팀 리더"
    }
    
    for name, role in team_info.items():
        with st.expander(name):
            st.write(role)
    
    # API 키 입력
    api_key = st.text_input("Gemini API 키를 입력하세요", type="password")
    
    # PDF 파일 업로더
    uploaded_file = st.file_uploader("PDF 논문을 업로드하세요", type=['pdf'])
    
    if uploaded_file and api_key:
        # Gemini API 설정
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-pro-002')
        
        # PDF 텍스트 추출
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text_content = ""
        for page in pdf_reader.pages:
            text_content += page.extract_text()
        
        # 리뷰 프로세스 시작
        if st.button("논문 리뷰 시작"):
            with st.spinner("Sam이 논문을 분석 중..."):
                sam_prompt = create_team_prompt(text_content, "sam")
                sam_response = model.generate_content(sam_prompt)
                
                with st.expander("Sam의 초기 분석"):
                    st.write(sam_response.text)
            
            with st.spinner("Jenny가 검토 중..."):
                jenny_prompt = create_team_prompt(sam_response.text, "jenny")
                jenny_response = model.generate_content(jenny_prompt)
                
                with st.expander("Jenny의 검토 및 개선"):
                    st.write(jenny_response.text)
            
            with st.spinner("Will이 최종 보고서 작성 중..."):
                will_prompt = create_team_prompt(jenny_response.text, "will")
                will_response = model.generate_content(will_prompt)
                
                with st.expander("Will의 최종 보고서", expanded=True):
                    st.write(will_response.text)

if __name__ == "__main__":
    main()