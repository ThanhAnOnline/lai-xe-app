import streamlit as st
import base64

# --- CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="Lái Xe Trường Vinh", layout="centered")

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
        st.error(f"Không tìm thấy file: {file_path}")

# --- KHỞI TẠO TRẠNG THÁI ---
if 'diem' not in st.session_state:
    st.session_state.diem = 100
if 'bai_dang_chon' not in st.session_state:
    st.session_state.bai_dang_chon = None

# --- GIAO DIỆN CHÍNH ---
st.markdown("<h1 style='text-align: center;'>HỆ THỐNG SÁT HẠCH</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: center; color: red; font-size: 80px;'>đ {st.session_state.diem}</h2>", unsafe_allow_html=True)

# --- KHU VỰC BÀI THI ---
st.markdown("### BÀI THI")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("XUẤT PHÁT", use_container_width=True):
        st.session_state.bai_dang_chon = "xuat_phat"
        play_audio("xuat_phat.mp3")
with col2:
    if st.button("TĂNG SỐ", use_container_width=True):
        st.session_state.bai_dang_chon = "tang_so"
        play_audio("Tang_so.mp3")
with col3:
    if st.button("GIẢM SỐ", use_container_width=True):
        st.session_state.bai_dang_chon = "giam_so"
        play_audio("Giam_so.mp3")
with col4:
    if st.button("KẾT THÚC", use_container_width=True):
        st.session_state.bai_dang_chon = "ket_thuc"
        play_audio("Ket_thuc.mp3")

st.markdown("---")

# --- HIỂN THỊ LỖI THEO BÀI THI ---
def nut_loi(ten_loi, diem_tru):
    if st.button(f"{ten_loi} (-{diem_tru})", use_container_width=True):
        st.session_state.diem -= diem_tru
        st.toast(f"Đã trừ {diem_tru} điểm!")
        st.rerun()

if st.session_state.bai_dang_chon == "xuat_phat":
    st.subheader("Lỗi bài Xuất Phát")
    nut_loi("Không thắt dây an toàn", 5)
    nut_loi("Không nhả phanh tay", 5)
    nut_loi("Không bật xi nhan trái", 5)
    nut_loi("Không đúng số, đúng tốc độ", 5)
    nut_loi("Không tắt đèn xi nhan trái", 5)

elif st.session_state.bai_dang_chon == "tang_so":
    st.subheader("Lỗi bài Tăng Số")
    nut_loi("Không tăng số đúng quy định", 5)

elif st.session_state.bai_dang_chon == "giam_so":
    st.subheader("Lỗi bài Giảm Số")
    nut_loi("Không giảm số đúng quy định", 5)

elif st.session_state.bai_dang_chon == "ket_thuc":
    st.subheader("Lỗi bài Kết Thúc")
    nut_loi("Không bật xi nhan phải", 5)
    nut_loi("Không tắt xi nhan phải", 5)
    nut_loi("Không về số 0", 5)
    nut_loi("Không về được số P", 5)
    nut_loi("Không kéo phanh tay", 5)

# --- LỖI CHUNG & RESET ---
st.markdown("---")
if st.button("LÀM MỚI BÀI THI (100đ)", type="primary", use_container_width=True):
    st.session_state.diem = 100
    st.session_state.bai_dang_chon = None
    st.rerun()

if st.button("XE CHOẠNG LÁI / CHẾT MÁY (-5 ĐIỂM)", use_container_width=True):
    st.session_state.diem -= 5
    st.rerun()
