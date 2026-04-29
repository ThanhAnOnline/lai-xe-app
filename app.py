import streamlit as st
import base64

# Cấu hình giao diện
st.set_page_config(page_title="Lái Xe Trường Vinh", layout="centered")

# Hàm xử lý âm thanh ẩn để tự động phát khi bấm nút
def play_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

# Giao diện
st.markdown("<h1 style='text-align: center;'>HỆ THỐNG SÁT HẠCH</h1>", unsafe_allow_html=True)

if 'diem' not in st.session_state:
    st.session_state.diem = 100

st.markdown(f"<h2 style='text-align: center; color: red; font-size: 80px;'>đ {st.session_state.diem}</h2>", unsafe_allow_html=True)

# Chia hàng nút bấm
col1, col2 = st.columns(2)

with col1:
    if st.button("XUẤT PHÁT", use_container_width=True):
        play_audio("xuat_phat.mp3")
    if st.button("GIẢM SỐ", use_container_width=True):
        play_audio("giam_so.mp3")

with col2:
    if st.button("TĂNG SỐ", use_container_width=True):
        play_audio("tang_so.mp3")
    if st.button("KẾT THÚC", use_container_width=True):
        play_audio("ket_thuc.mp3")

st.markdown("---")
if st.button("LỖI CHOẠNG LÁI (-5 ĐIỂM)", use_container_width=True):
    st.session_state.diem -= 5
