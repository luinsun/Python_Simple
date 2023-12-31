# DAO: Database Access Object
#    - 데이터 작업(CRUD)을 하는 객체

# 예시)
# 회원 -> member_dao
#         ㄴ 회원가입, 회원수정, 회원조회, 회원검색, 회원삭제

# 로그인 -> login_dao
#         ㄴ 로그인, 로그아웃, ID찾기, PW찾기

from db.common.connection import conn_mongodb

def add_news(data):
    conn = conn_mongodb()  # 1.Connection
    conn.insert_one(data)  # 2.DB에 저장