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
.stApp {
    background: radial-gradient(circle at top, #1b1f2a, #0e1117);
    color: #f5f5f5;
    font-family: 'Georgia', serif;
}

h1, h2, h3 {
    text-align: center;
    color: #d4af37;
    text-shadow: 0 0 15px rgba(212,175,55,0.6);
}

.house-card {
    background: rgba(255,255,255,0.05);
    border: 2px solid #d4af37;
    border-radius: 16px;
    padding: 16px;
    text-align: center;
    transition: all 0.3s ease;
}

.house-card:hover {
    transform: translateY(-6px) scale(1.03);
    box-shadow: 0 0 25px rgba(212,175,55,0.4);
}

button {
    border-radius: 14px !important;
    border: 2px solid #d4af37 !important;
    background: linear-gradient(145deg, #3b2f2f, #2a1f1f) !important;
    color: #f5f5f5 !important;
    font-size: 16px !important;
    transition: all 0.3s ease;
}

button:hover {
    background: #d4af37 !important;
    color: #1a1a1a !important;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# ---------------- 배경 음악 ----------------
st.audio(
    "Harry_Potter_-_Theme_Song_Hedwig_s_Theme_(mp3.pm).mp3",
    format="audio/mp3",
    loop=True
)

# ---------------- 세션 상태 ----------------
if "page" not in st.session_state:
    st.session_state.page = "select"

if "house" not in st.session_state:
    st.session_state.house = None

if "video_index" not in st.session_state:
    st.session_state.video_index = 0

# ---------------- 데이터 ----------------
house_images = {
    "Gryffindor": "https://i.pinimg.com/474x/c4/53/a0/c453a00f4ddc4de3853830fd373788c8.jpg",
    "Slytherin": "https://upload.wikimedia.org/wikipedia/commons/3/34/Slytherin.png",
    "Ravenclaw": "https://img.fruugo.com/product/2/50/46790502_0340_0340.jpg",
    "Hufflepuff": "https://dh.aks.ac.kr/Edu/wiki/images/2/2b/57235fc71095f77d755aa73e47126d65.jpg"
}

videos = [
    "https://www.youtube.com/watch?v=NWoQz0HtQGU",
    "https://www.youtube.com/watch?v=q6tsk1LhVVM",
    "https://www.youtube.com/watch?v=n1IrlvvQwzMM",
    "https://www.youtube.com/watch?v=g3xqNANJP2o",
    "https://www.youtube.com/watch?v=hemydBAVaA4",
    "https://www.youtube.com/watch?v=nZrAR73zVxU",
    "https://www.youtube.com/watch?v=e2TUpDlYMRk",
    "https://www.youtube.com/watch?v=TJhj6H5NTvM",
]

# ---------------- PAGE 1 : 선택 ----------------
if st.session_state.page == "select":
    st.title("🪄 Welcome to Hogwarts")
    st.image(
        "https://media.giphy.com/media/26BRzozg4TCBXv6QU/giphy.gif",
        use_column_width=True
    )

    st.header("✨ The Sorting Hat is ready")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        if st.button("🦁 Gryffindor"):
            st.session_state.house = "Gryffindor"
            st.session_state.page = "image"

    with col2:
        if st.button("🐍 Slytherin"):
            st.session_state.house = "Slytherin"
            st.session_state.page = "image"

    with col3:
        if st.button("🦅 Ravenclaw"):
            st.session_state.house = "Ravenclaw"
            st.session_state.page = "image"

    with col4:
        if st.button("🦡 Hufflepuff"):
            st.session_state.house = "Hufflepuff"
            st.session_state.page = "image"

# ---------------- PAGE 2 : 이미지 ----------------
elif st.session_state.page == "image":
    st.title(f"🏰 {st.session_state.house}")
    st.image(house_images[st.session_state.house], use_column_width=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("➡️ Enter the dormitory"):
            st.session_state.page = "final"
    with col2:
        if st.button("⬅️ Back"):
            st.session_state.page = "select"
            st.session_state.house = None

# ---------------- PAGE 3 : 결과 ----------------
elif st.session_state.page == "final":
    st.title("🎉 Welcome Home")
    st.write(f"""
    **{st.session_state.house}** has chosen you.  
    Your magical journey begins now ✨
    """)

    st.video(videos[st.session_state.video_index])

    col1, col2 = st.columns(2)

    with col1:
        if st.button("👍 more ❤️"):
            if st.session_state.video_index < len(videos) - 1:
                st.session_state.video_index += 1

    with col2:
        if st.button("🔄 Start over"):
            st.session_state.page = "select"
            st.session_state.house = None
            st.session_state.video_index = 0

