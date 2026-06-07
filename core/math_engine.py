import numpy as np

def solve_by_cramer(matrix_A, vector_B):
    """
    ฟังก์ชันสำหรับคำนวณหาค่าตัวแปรจากระบบสมการเชิงเส้น 3 ตัวแปรด้วยกฎของคราเมอร์
    :param matrix_A: สัมประสิทธิ์หน้าตัวแปรในรูปแบบ Numpy Array ขนาด 3x3
    :param vector_B: ผลลัพธ์หลังเครื่องหมายเท่ากับในรูปแบบ Numpy Array ขนาด 3x1
    """
    try:
        # 1. คำนวณหาค่า Determinant ของเมทริกซ์หลัก (det A)
        det_A = np.linalg.det(matrix_A)
        
        # ตรวจสอบตัวหาร: หากค่า det_A เป็น 0 หรือเข้าใกล้ 0 จะไม่มีคำตอบเดี่ยว
        if np.isclose(det_A, 0, atol=1e-9):
            return {
                "success": False,
                "message": "❌ ระบบสมการนี้ไม่มีคำตอบเดียว (เนื่องจากค่า Determinant ของเมทริกซ์สัมประสิทธิ์ตัวหลักมีค่าเป็น 0)"
            }
        
        n = len(vector_B)
        solutions = []
        
        # 2. วนลูปสร้างเมทริกซ์ย่อย Ai โดยเอาเวกเตอร์ B ไปแทนที่ในคอลัมน์ที่ i
        for i in range(n):
            Ai = matrix_A.copy()
            Ai[:, i] = vector_B
            det_Ai = np.linalg.det(Ai)
            
            # คำนวณหาคำตอบตามสูตร xi = det(Ai) / det(A)
            solutions.append(det_Ai / det_A)
            
        return {
            "success": True,
            "data": solutions, # คืนค่าคำตอบกลับไปในรูปแบบรายการ [x, y, z]
            "det_A": det_A
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"เกิดข้อผิดพลาดทางคณิตศาสตร์: {str(e)}"
        }