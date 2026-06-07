import numpy as np

def solve_by_cramer(matrix_A, vector_B):
    """
    ฟังก์ชันอัจฉริยะคำนวณ Cramer's Rule รองรับทั้งมิติ 2x2 และ 3x3
    """
    try:
        # 1. หาค่า Determinant ของเมทริกซ์หลัก
        det_A = np.linalg.det(matrix_A)
        
        if np.isclose(det_A, 0, atol=1e-9):
            return {
                "success": False,
                "message": "❌ ไม่สามารถหาคำตอบเดี่ยวได้ เนื่องจากค่า det(A) = 0"
            }
        
        n = len(vector_B)
        solutions = []
        
        # 2. วนลูปคำนวณตามจำนวนตัวแปรจริง
        for i in range(n):
            Ai = matrix_A.copy()
            Ai[:, i] = vector_B
            det_Ai = np.linalg.det(Ai)
            solutions.append(det_Ai / det_A)
            
        return {
            "success": True,
            "data": solutions,
            "det_A": det_A
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"เกิดข้อผิดพลาดทางคณิตศาสตร์: {str(e)}"
        }