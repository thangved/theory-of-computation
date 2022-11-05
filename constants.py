from classes.nfa import EPSILON

COLOR_PRIMARY = '#3d7eff'
COLOR_SECONDARY = '#ff8b17'
COLOR_WHITE = '#ffffff'
COLOR_BLACK = '#000000'

FORMAT_FILE_MESSAGE = """File văn bản gồm các dòng sau:
1. Tập các trạng thái, mỗi trạng thái cách nhau 1 dấu cách
2. Tập các ký tự, mỗi ký tự cách nhau 1 dấu cách
3. Trạng thái bắt đầu
4. Tập các trạng thái kết thúc, mỗi trạng thái cách nhau 1 dấu cách
5. Các dòng còn lại là danh sách các hàm sinh
    Với mỗi dòng:
        - Ký tự đầu là trạng thái
        - Ký tự thứ 2 là nhãn
        - Các ký tự còn lại là tập các trạng thái khi đọc vào nhãn

Ghi chú: Ký hiệu """ + EPSILON + """thay thế cho epsilon
"""

WIN_TITLE = "NFAε Program - Dev by Minh Thang & Truc Mai"
