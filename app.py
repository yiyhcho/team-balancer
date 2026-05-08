import streamlit as st
import random

st.title("5:5 내전 팀 밸런스 생성기 📱")

# 세션 상태로 플레이어 리스트 저장 (새로고침 방지)
if 'players' not in st.session_state:
    st.session_state.players = []

# 입력 섹션
with st.form("add_player_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("이름")
    with col2:
        score = st.number_input("점수", min_value=0, step=1)
    
    submitted = st.form_submit_button("플레이어 추가")
    if submitted and name:
        st.session_state.players.append({"name": name, "score": score})

# 현재 명단 표시
st.write(f"현재 등록 인원: {len(st.session_state.players)}명")
if st.button("명단 초기화"):
    st.session_state.players = []
    st.rerun()

# 팀 구성 버튼
if st.button("팀 구성하기", type="primary"):
    if len(st.session_state.players) < 10:
        st.error("10명이 필요합니다!")
    else:
        players = st.session_state.players.copy()
        found = False
        for _ in range(2000):
            random.shuffle(players)
            team_a, team_b = players[:5], players[5:10]
            sum_a = sum(p['score'] for p in team_a)
            sum_b = sum(p['score'] for p in team_b)
            
            if abs(sum_a - sum_b) <= 15:
                found = True
                col_a, col_b = st.columns(2)
                with col_a:
                    st.success(f"A팀 (합계: {sum_a})")
                    for p in team_a: st.write(f"- {p['name']} ({p['score']})")
                with col_b:
                    st.info(f"B팀 (합계: {sum_b})")
                    for p in team_b: st.write(f"- {p['name']} ({p['score']})")
                st.balloons()
                break
        if not found:
            st.warning("밸런스를 찾지 못했습니다. 다시 시도하세요.")
