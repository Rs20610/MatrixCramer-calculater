import streamlit as st
import numpy as np
from core.math_engine import solve_by_cramer

st.set_page_config(page_title="Cramer's Rule Studio", page_icon="🧮", layout="centered")

st.title("🧮 โปรแกรมคำนวณสมการเชิงเส้นด้วยวิธีของคราเมอร์")
st.write("เวอร์ชันอัปเกรด: รองรับทั้งมิติ 2x2 และ 3x3")
st.markdown("---")

# 🌟 เพิ่มแถบเลือกโหมดการทำงาน
mode = st.radio("เลือกขนาดระบบสมการของคุณ:", ("2 ตัวแปร (เมทริกซ์ 2x2)", "3 ตัวแปร (เมทริกซ์ 3x3)"), horizontal=True)

if mode == "2 ตัวแปร (เมทริกซ์ 2x2)":
    st.header("สัมประสิทธิ์หน้าตัวแปร (Matrix A 2x2)")
    st.caption("สมการรูปแบบ: ax + by = c")
    
    row1 = st.columns(2)
    row2 = st.columns(2)
    with row1[0]: a11 = st.number_input("a11", value=2.0, key="2x2_a11")
    with row1[1]: a12 = st.number_input("a12", value=1.0, key="2x2_a12")
    with row2[0]: a21 = st.number_input("a21", value=1.0, key="2x2_a21")
    with row2[1]: a22 = st.number_input("a22", value=-3.0, key="2x2_a22")
    
    st.header("ค่าคงตัวหลังเครื่องหมายเท่ากับ (Vector B)")
    cols_b = st.columns(2)
    with cols_b[0]: b1 = st.number_input("b1", value=5.0, key="2x2_b1")
    with cols_b[1]: b2 = st.number_input("b2", value=-1.0, key="2x2_b2")
    
    if st.button("เริ่มคำนวณระบบสมการ 2x2", type="primary", use_container_width=True):
        matrix_A = np.array([[a11, a12], [a21, a22]], dtype=float)
        vector_B = np.array([b1, b2], dtype=float)
        
        result = solve_by_cramer(matrix_A, vector_B)
        st.markdown("---")
        if not result["success"]:
            st.error(result["message"])
        else:
            solutions = result["data"]
            res_cols = st.columns(2)
            res_cols[0].metric(label="ค่าตัวแปร X", value=f"{solutions[0]:.4f}")
            res_cols[1].metric(label="ค่าตัวแปร Y", value=f"{solutions[1]:.4f}")
            st.info(f"💡 ค่า det(A) = {result['det_A']:.4f}")

else: # โหมด 3x3
    st.header("สัมประสิทธิ์หน้าตัวแปร (Matrix A 3x3)")
    row1 = st.columns(3)
    row2 = st.columns(3)
    row3 = st.columns(3)
    with row1[0]: a11 = st.number_input("a11", value=2.0, key="3x3_a11")
    with row1[1]: a12 = st.number_input("a12", value=1.0, key="3x3_a12")
    with row1[2]: a13 = st.number_input("a13", value=1.0, key="3x3_a13")
    with row2[0]: a21 = st.number_input("a21", value=1.0, key="3x3_a21")
    with row2[1]: a22 = st.number_input("a22", value=-1.0, key="3x3_a22")
    with row2[2]: a23 = st.number_input("a23", value=-1.0, key="3x3_a23")
    with row3[0]: a31 = st.number_input("a31", value=1.0, key="3x3_a31")
    with row3[1]: a32 = st.number_input("a32", value=2.0, key="3x3_a32")
    with row3[2]: a33 = st.number_input("a33", value=1.0, key="3x3_a33")
    
    st.header("ค่าคงตัวหลังเครื่องหมายเท่ากับ (Vector B)")
    cols_b = st.columns(3)
    with cols_b[0]: b1 = st.number_input("b1", value=3.0, key="3x3_b1")
    with cols_b[1]: b2 = st.number_input("b2", value=0.0, key="3x3_b2")
    with cols_b[2]: b3 = st.number_input("b3", value=0.0, key="3x3_b3")
    
    if st.button("เริ่มคำนวณระบบสมการ 3x3", type="primary", use_container_width=True):
        matrix_A = np.array([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]], dtype=float)
        vector_B = np.array([b1, b2, b3], dtype=float)
        
        result = solve_by_cramer(matrix_A, vector_B)
        st.markdown("---")
        if not result["success"]:
            st.error(result["message"])
        else:
            solutions = result["data"]
            res_cols = st.columns(3)
            res_cols[0].metric(label="ค่าตัวแปร X", value=f"{solutions[0]:.4f}")
            res_cols[1].metric(label="ค่าตัวแปร Y", value=f"{solutions[1]:.4f}")
            res_cols[2].metric(label="ค่าตัวแปร Z", value=f"{solutions[2]:.4f}")
            st.info(f"💡 ค่า det(A) = {result['det_A']:.4f}")