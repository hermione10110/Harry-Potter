import streamlit as st

# ---------------- 기본 설정 ----------------
st.set_page_config(
    page_title="Hogwarts Sorting Hat",
    page_icon="🪄",
    layout="centered"
)
# ---------------- CSS ----------------
st.markdown("""
<style>

/* 전체 앱 배경 */
.stApp {
    background-color: #0e1117;
    color: #f5f5f5;
    font-family: 'Georgia', serif;
}

/* 제목 */
h1, h2, h3 {
    text-align: center;
    color: #d4af37;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.7);
}

/* 버튼 (Streamlit 최신 selector) */
button[kind="primary"],
button[kind="secondary"],
div[data-testid="stButton"] > button {
    background-color: #3b2f2f !important;
    color: #f5f5f5 !important;
    border-radius: 12px;
    border: 2px solid #d4af37;
    padding: 0.6em 1.2em;
    font-size: 16px;
    transition: all 0.3s ease;
}

/* 버튼 hover */
div[data-testid="stButton"] > button:hover {
    background-color: #d4af37 !important;
    color: #1a1a1a !important;
    transform: scale(1.05);
}

/* 이미지 */
img {
    cursor: pointer;
    transition: transform 0.3s ease;
}

img:hover {
    transform: scale(1.03);
}

</style>
""", unsafe_allow_html=True)


# ---------------- 배경 음악 (숨김) ----------------
st.audio(
    r"Harry_Potter_-_Theme_Song_Hedwig_s_Theme_(mp3.pm).mp3",
    format="audio/mp3"
)

# ---------------- 세션 상태 ----------------
if "page" not in st.session_state:
    st.session_state.page = "select"
if "house" not in st.session_state:
    st.session_state.house = None

# ---------------- PAGE 1 : 기숙사 선택 ----------------
if st.session_state.page == "select":

    st.title("🪄 Welcome to Hogwarts")

    st.image(
        "https://media.giphy.com/media/26BRzozg4TCBXv6QU/giphy.gif",
        use_column_width=True
    )

    st.header("✨ Choose your dormitory")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        if st.button("🦁:red[Gryffindor]"):
            st.session_state.house = "Gryffindor"
            st.session_state.page = "image"

    with col2:
        if st.button("🐍 :green[Slytherin]"):
            st.session_state.house = "Slytherin"
            st.session_state.page = "image"

    with col3:
        if st.button("🦅:blue[Ravenclaw]"):
            st.session_state.house = "Ravenclaw"
            st.session_state.page = "image"

    with col4:
        if st.button("🦡 :yellow[Hufflepuff]"):
            st.session_state.house = "Hufflepuff"
            st.session_state.page = "image"

# ---------------- PAGE 2 : 이미지 클릭 ----------------
elif st.session_state.page == "image":

    st.title(f"🏰 {st.session_state.house}")

    house_images = {
        "Gryffindor": "https://i.pinimg.com/474x/c4/53/a0/c453a00f4ddc4de3853830fd373788c8.jpg",
        "Slytherin": "https://upload.wikimedia.org/wikipedia/commons/3/34/Slytherin.png",
        "Ravenclaw": "https://img.fruugo.com/product/2/50/46790502_0340_0340.jpg",
        "Hufflepuff": "https://dh.aks.ac.kr/Edu/wiki/images/2/2b/57235fc71095f77d755aa73e47126d65.jpg"
    }

    st.image(house_images[st.session_state.house], use_column_width=True)

    if st.button("➡️ Enter the dorm"):
        st.session_state.page = "final"

    if st.button("⬅️ Back"):
        st.session_state.page = "select"
        st.session_state.house = None

# ---------------- PAGE 3 : 다음 페이지 ----------------
elif st.session_state.page == "final":

    st.title("🎉 Welcome to your new dorm!")

    st.write(f"""
    **{st.session_state.house}** has chosen you.  
    Your magical journey begins now ✨
    """)

    # 기본 비디오
    st.video("https://www.youtube.com/watch?v=NWoQz0HtQGU")

    # Start over 버튼
    if st.button("🔄 Start over"):
        st.session_state.page = "select"
        st.session_state.house = None

    # 추가 비디오 버튼
    more_videos = [
        "https://www.youtube.com/watch?v=q6tsk1LhVVM",
        "https://www.youtube.com/watch?v=n1IrlvvQwzMM",
        "https://www.youtube.com/watch?v=g3xqNANJP2o",
        "https://www.youtube.com/watch?v=hemydBAVaA4",
        "https://www.youtube.com/watch?v=nZrAR73zVxU",
        "https://www.youtube.com/watch?v=e2TUpDlYMRk",
        "https://www.youtube.com/watch?v=TJhj6H5NTvM",
    ]

    for i, url in enumerate(more_videos):
        if st.button("👍more❤️", key=f"more_{i}"):
            st.video(url)