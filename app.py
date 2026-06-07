import streamlit as st
import numpy as np
# ดึงฟังก์ชันคำนวณมาจากโฟลเดอร์ core ที่เราเขียนแยกส่วนไว้
from core.math_engine import solve_by_cramer

# ตั้งค่ารายละเอียดแท็บเบราว์เซอร์ของหน้าเว็บ
st.set_page_config(
    page_title="Cramer's Rule Web Application",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 เว็บไซต์คำนวณสมการเชิงเส้นด้วยวิธีของคราเมอร์")
st.write("โครงสร้างระบบแบบโมดูลาร์ขนาดใหญ่ (แยกสมองกลและหน้าเว็บ)")
st.markdown("---")

st.header("1. ระบุค่าสัมประสิทธิ์หน้าตัวแปร (Matrix A)")
st.caption("จัดเรียงสมการให้อยู่ในรูป: ax + by + cz = d")

# ออกแบบกล่องกรอกข้อมูลเป็นมิติตาราง 3x3 ด้วยระบบจัดคอลัมน์ของ Streamlit
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)

with row1[0]: a11 = st.number_input("a11", value=2.0, key="a11")
with row1[1]: a12 = st.number_input("a12", value=1.0, key="a12")
with row1[2]: a13 = st.number_input("a13", value=1.0, key="a13")

with row2[0]: a21 = st.number_input("a21", value=1.0, key="a21")
with row2[1]: a22 = st.number_input("a22", value=-1.0, key="a22")
with row2[2]: a23 = st.number_input("a23", value=-1.0, key="a23")

with row3[0]: a31 = st.number_input("a31", value=1.0, key="a31")
with row3[1]: a32 = st.number_input("a32", value=2.0, key="a32")
with row3[2]: a33 = st.number_input("a33", value=1.0, key="a33")

st.header("2. ระบุค่าตัวเลขหลังเครื่องหมายเท่ากับ (Vector B)")
cols_b = st.columns(3)
with cols_b[0]: b1 = st.number_input("คำตอบสมการที่ 1 (b1)", value=3.0, key="b1")
with cols_b[1]: b2 = st.number_input("คำตอบสมการที่ 2 (b2)", value=0.0, key="b2")
with cols_b[2]: b3 = st.number_input("คำตอบสมการที่ 3 (b3)", value=0.0, key="b3")

st.markdown("<br>", unsafe_allow_html=True)

# 3. ตรวจสอบการกดปุ่มสั่งคำนวณบนหน้าเว็บ
if st.button("เริ่มคำนวณระบบสมการ", type="primary", use_container_width=True):
    # มัดรวมค่าคงที่ให้กลายเป็นโครงสร้างอาเรย์ของ NumPy ตามที่ส่วนคำนวณต้องการ
    matrix_A = np.array([
        [a11, a12, a13],
        [a21, a22, a23],
        [a31, a32, a33]
    ], dtype=float)
    
    vector_B = np.array([b1, b2, b3], dtype=float)
    
    # ส่งค่าไปคำนวณที่โมดูลคณิตศาสตร์ที่เราแยกไว้
    result = solve_by_cramer(matrix_A, vector_B)
    
    st.markdown("---")
    st.subheader("📊 ผลลัพธ์จากการประมวลผล")
    
    # ถ้าคำนวณไม่สำเร็จเนื่องจาก det เป็น 0 ให้แสดงกล่องข้อความเตือนสีแดง
    if not result["success"]:
        st.error(result["message"])
    else:
        solutions = result["data"]
        
        # แสดงผลลัพธ์เป็นกล่องการ์ดตัวเลขแยกฝั่งกันอย่างสวยงาม ปัดทศนิยม 4 ตำแหน่ง
        res_cols = st.columns(3)
        res_cols[0].metric(label="ค่าตัวแปร X", value=f"{solutions[0]:.4f}")
        res_cols[1].metric(label="ค่าตัวแปร Y", value=f"{solutions[1]:.4f}")
        res_cols[2].metric(label="ค่าตัวแปร Z", value=f"{solutions[2]:.4f}")
        
        # แสดงข้อมูลดีเทอร์มิแนนต์ประกอบเพิ่มเติมเพื่อประโยชน์ทางการศึกษา
        st.info(f"💡 ค่า Determinant ของเมทริกซ์หลัก (det A) มีค่าเท่ากับ {result['det_A']:.4f}")
        st.success("✅ โปรแกรมคำนวณผลลัพธ์สำเร็จเรียบร้อยแล้ว!")