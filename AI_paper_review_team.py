import streamlit as st
from typing import List, Dict
import time

class ReviewTeamMember:
    def __init__(self, name: str, role: str, description: str):
        self.name = name
        self.role = role
        self.description = description

class PaperReviewTeam:
    def __init__(self):
        self.members = {
            'sam': ReviewTeamMember(
                'Sam', 
                'AI PhD', 
                '복잡한 AI 개념을 간단하게 설명하는 전문가'
            ),
            'jenny': ReviewTeamMember(
                'Jenny', 
                'AI & Education PhD', 
                'Sam의 초안을 검토하고 더 이해하기 쉽게 개선하는 전문가'
            ),
            'will': ReviewTeamMember(
                'Will', 
                'Team Leader', 
                '최종 보고서를 검토하고 완성하는 팀 리더'
            )
        }

    def review_paper(self, paper_text: str) -> Dict[str, str]:
        reviews = {}
        
        # Sam의 초기 분석
        reviews['sam'] = self._sam_analysis(paper_text)
        
        # Jenny의 검토 및 개선
        reviews['jenny'] = self._jenny_review(reviews['sam'])
        
        # Will의 최종 검토
        reviews['will'] = self._will_finalize(reviews['jenny'])
        
        return reviews

    def _sam_analysis(self, paper_text: str) -> str:
        # Sam의 분석 로직 구현
        time.sleep(2)  # 분석 시간 시뮬레이션
        return f"Sam의 초기 분석:\n{paper_text[:500]}..."

    def _jenny_review(self, sam_analysis: str) -> str:
        # Jenny의 검토 로직 구현
        time.sleep(2)
        return f"Jenny의 검토:\n{sam_analysis}"

    def _will_finalize(self, jenny_review: str) -> str:
        # Will의 최종화 로직 구현
        time.sleep(2)
        return f"Will의 최종 검토:\n{jenny_review}"

def main():
    st.title("AI 논문 리뷰 팀")
    
    # 팀 소개
    st.header("팀 구성")
    team = PaperReviewTeam()
    
    for member in team.members.values():
        with st.expander(f"{member.name} ({member.role})"):
            st.write(member.description)
    
    # 논문 입력
    st.header("논문 리뷰")
    paper_text = st.text_area("논문 내용을 입력하세요:", height=300)
    
    if st.button("리뷰 시작"):
        if paper_text:
            with st.spinner("논문 분석 중..."):
                reviews = team.review_paper(paper_text)
                
                # 각 팀원의 리뷰 결과 표시
                for member_name, review in reviews.items():
                    member = team.members[member_name]
                    with st.expander(f"{member.name}의 리뷰"):
                        st.write(review)
        else:
            st.warning("논문 내용을 입력해주세요.")

if __name__ == "__main__":
    main()
