from classes.nfa import EPSILON

COLOR_PRIMARY = '#3d7eff'
COLOR_SECONDARY = '#ff8b17'
COLOR_WHITE = '#ffffff'
COLOR_BLACK = '#000000'

WIN_TITLE = "NFAε Program - Dev by Minh Thang & Truc Mai"

FILE_FORMAT = "Định dạng file"

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

READ_FILE_ERROR = "Lỗi đọc file"
FILE_NOT_MATCH_FORMAT = "File của bạn đã mở không đúng định dạng"

CANNOT_TEST = "Không thể thực hiện kiểm tra"
PLEASE_IMPORT_FA = "Vui lòng nhập văn phạm trước khi kiểm tra chuỗi"

ERROR = "Lỗi"

FA_ACCEPTED_STR = "Chuỗi được chấp nhận bởi NFAε"
FA_NOT_ACCEPT_STR = "Chuỗi không được chấp nhận bởi NFAε"
CHECK_STR = "Kiểm tra chuỗi"

STATES = "Các trạng thái"
ALPHABETS = "Các ký tự"
ACCEPT_STATES = "Các trạng thái kết thúc"
START_STATES = "Trạng thái bắt đầu"
TRANSITION_FUNCTIONS = "Hàm chuyển trạng thái"
STR_NEED_TEST = "Chuỗi cần kiểm tra"

CHECK = "Kiểm tra"
SELECT_FILE_TO_IMPORT_FA = "Chọn file để nhập văn phạm"

WINDOW_INIT_WIDTH = 800
WINDOW_INIT_HEIGHT = 600
WINDOW_RESOLUTION = str(WINDOW_INIT_WIDTH) + 'x' + str(WINDOW_INIT_HEIGHT)
