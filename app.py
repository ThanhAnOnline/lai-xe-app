import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Lái Xe Trường Vinh", layout="centered")

# Giao diện tiêu đề
st.markdown("<h1 style='text-align: center; color: white;'>HỆ THỐNG SÁT HẠCH</h1>", unsafe_allow_html=True)

# Khởi tạo điểm số trong bộ nhớ (nếu chưa có)
if 'diem' not in st.session_state:
    st.session_state.diem = 100

# Hiển thị điểm số rực rỡ
st.markdown(f"<h2 style='text-align: center; color: red; font-size: 60px;'>đ {st.session_state.diem}</h2>", unsafe_allow_html=True)

# Hàm để phát âm thanh (An thay link bằng link file mp3 của An nhé)
def play_audio(url):
    st.components.v1.html(f"""
        <audio autoplay>
            <source src="{url}" type="audio/mp3">
        </audio>
    """, height=0)

# Chia cột cho các nút Bài Thi
col1, col2 = st.columns(2)

with col1:
    if st.button("XUẤT PHÁT", use_container_width=True):
        play_audio("https://www.soundjay.com/buttons/sounds/button-3.mp3") # Ví dụ link âm thanh
        st.toast("Bắt đầu bài thi Xuất phát")

    if st.button("GIẢM SỐ", use_container_width=True):
        play_audio("https://www.soundjay.com/buttons/sounds/button-10.mp3")
        st.toast("Bắt đầu bài thi Giảm số")

with col2:
    if st.button("TĂNG SỐ", use_container_width=True):
        play_audio("https://www.soundjay.com/buttons/sounds/button-4.mp3")
        st.toast("Bắt đầu bài thi Tăng số")

    if st.button("KẾT THÚC", use_container_width=True):
        play_audio("https://www.soundjay.com/buttons/sounds/button-5.mp3")
        st.toast("Kết thúc bài thi")

# Nút trừ điểm (Lỗi chung)
st.markdown("---")
if st.button("LỖI CHOẠNG LÁI (-5 ĐIỂM)", use_container_width=True):
    st.session_state.diem -= 5