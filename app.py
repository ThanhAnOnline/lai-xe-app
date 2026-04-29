import streamlit as st
import base64

# --- CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="Lái Xe Trường Vinh", layout="centered")

# Hàm mã hóa âm thanh sang Base64 để phát ngay lập tức không cần tải file từ server
def play_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio autoplay="true">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(md, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Lỗi: Không tìm thấy file {file_path}. An hãy kiểm tra lại tên file trên GitHub!")

# --- GIAO DIỆN CHÍNH ---
st.markdown("<h1 style='text-align: center; color: white;'>HỆ THỐNG SÁT HẠCH</h1>", unsafe_allow_html=True)

# Khởi tạo điểm số
if 'diem' not in st.session_state:
    st.session_state.diem = 100

# Hiển thị điểm số nổi bật
st.markdown(f"<h2 style='text-align: center; color: red; font-size: 80px; margin-bottom: 0px;'>đ {st.session_state.diem}</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Thi thử - Hạng B</p>", unsafe_allow_html=True)

st.write("") # Tạo khoảng cách

# --- KHU VỰC BÀI THI (Phát âm thanh) ---
st.markdown("<h3 style='color: #00CCFF;'>BÀI THI</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    if st.button("XUẤT PHÁT", use_container_width=True):
        play_audio("xuat_phat.mp3")
    
    if st.button("GIẢM SỐ", use_container_width=True):
        play_audio("Giam_so.mp3")

with col2:
    if st.button("TĂNG SỐ", use_container_width=True):
        play_audio("Tang_so.mp3")
        
    if st.button("KẾT THÚC", use_container_width=True):
        play_audio("Ket_thuc.mp3")

# --- KHU VỰC LỖI CHUNG (Trừ điểm) ---
st.markdown("---")
st.markdown("<h3 style='color: #FFCC00;'>LỖI CHUNG</h3>", unsafe_allow_html=True)

# Danh sách lỗi để An dễ dàng thêm bớt
if st.button("XE CHOẠNG LÁI (-5 ĐIỂM)", use_container_width=True):
    st.session_state.diem -= 5
    st.toast("Đã trừ 5 điểm: Xe choạng lái")

if st.button("XE CHẾT MÁY (-5 ĐIỂM)", use_container_width=True):
    st.session_state.diem -= 5
    st.toast("Đã trừ 5 điểm: Xe chết máy")

# Nút Reset điểm
st.write("")
if st.button("LÀM MỚI BÀI THI (100đ)"):
    st.session_state.diem = 100
    st.rerun()
