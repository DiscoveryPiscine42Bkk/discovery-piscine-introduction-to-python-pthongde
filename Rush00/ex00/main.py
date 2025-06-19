from check import is_in_check  # นำเข้าฟังก์ชันจากไฟล์ check.py

# ทดสอบกรณี Queen รุก King
is_in_check(
    "....",
    "..K.",
    "....",
    ".Q.."
)
# Output: Success

# ทดสอบกรณีไม่มีตัวใดรุก King ได้
is_in_check(
    "....",
    "..K.",
    "....",
    "...."
)
# Output: Fail