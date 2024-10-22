#0.import
import mysql.connector
from mysql.connector import Error

host="localhost"        # 호스트
user="phonebook"        # 사용자명
password="phonebook"    # 비밀번호
database="phonebook_db" # 데이터베이스명

# connect()함수
def get_connect():
    #1.연결/컨넥션 얻기  (메소드)   순서 바껴도되지만 보통 이순서 
    conn = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )
    return conn


# close()함수
def close(conn,cursor):
    #5.자원정리
    if conn is not None:
        conn.close()

    if cursor is not None:
        cursor.close()                  # 두개를 다 닫아줘야함  


# 리스트 
def get_person_list():
    try:

        #1.연결/컨넥션 얻기
        conn = get_connect()

        #2.커서생성
        cursor = conn.cursor()

        #3.SQL문준비 / 바인딩 / 실행
        #--SQL문
        query = """
            select person_id,
                    name,
                    hp,
                    company
            from person
        """

        #--바인딩(튜플)
        # ?가 없으면 생략

        #--실행
        cursor.execute(query)
        resultset = cursor.fetchall()

        #4.결과처리  리스트 [(튜플), (튜플), (튜플)]  -> 리스트[{딕션어리},{딕션어리},{딕션어리}]
        person_list = []
        for row in resultset:
            person_vo = {       # 딕션어리 {키-값}
                "person_id": row[0],      # person_id
                "name": row[1],      # name
                "hp": row[2],      # hp
                "company": row[3]      # company
            }
            person_list.append(person_vo)       # 추가하기  포문안에 있는거임
            
        for person in person_list:
            print(f"{person['person_id']}\t{person['name']}\t{person['hp']}\t{person['company']}")

    except Error as e:
        print(f"데이터베이스 오류: {e}")

    finally:
        #5.자원정리
        close(conn, cursor)


# 등록
def add_person():
    try:
        conn = get_connect()

        #2.커서생성
        cursor = conn.cursor()

        name = input(">이름: ")
        hp = input(">휴대전화: ")
        company = input(">회사전화: ")

        #3.SQL문준비 / 바인딩 / 실행
        #--SQL문
        query = '''
            insert into person (name, hp, company)
            values(%s, %s, %s)
        '''

        #--바인딩(튜플)

        #--실행
        cursor.execute(query, (name, hp, company))     # 임시반영 (성공하면 커밋  임시 -> 반영)
        conn.commit()                   # 최종반영

        #4.결과처리
        print(f"{cursor.rowcount} 건 등록되었습니다")          # 결과갯수 알려줌

    except Error as e:
        print(f"데이터베이스 오류: {e}")

    finally:
        #5.자원정리
        close(conn, cursor)


# 삭제
def delete_person():
    try:
        conn = get_connect()
        cursor = conn.cursor()

        # 2. 삭제할 항목의 인덱스 입력
        delete_no = int(input(">번호: ")) 

        # SQL DELETE 쿼리 실행
        delete_query = """
            delete from person 
            where person_id = %s
        """
        cursor.execute(delete_query, (delete_no,))      # 튜플로 전달해야 함

        # 4. 변경사항 커밋
        conn.commit()

        print(f"{cursor.rowcount} 건 삭제되었습니다.")  # 삭제된 레코드 수 출력

    except Error as e:
        print(f"데이터베이스 오류: {e}")

    finally:
        # 5. 자원 정리
        close(conn, cursor)


# 검색
def search_person():
    try:
        conn = get_connect()
        cursor = conn.cursor()

        # 2. 검색할 이름 또는 전화번호 입력
        search_value = input(">이름: ")

        # SQL SELECT 쿼리 실행 (이름 또는 전화번호로 검색)
        search_query = """
            select person_id, name, hp, company
            from person
            where name like %s
        """

        # 실행할 때 %search_value%로 부분 문자열 검색 (LIKE 연산자 사용)
        cursor.execute(search_query, ('%' + search_value + '%',))

        # 3. 결과 처리
        resultset = cursor.fetchall()

        if resultset:  # 검색 결과가 있을 때
            print("검색 결과:")
            for row in resultset:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
        else:
            print("검색된 결과가 없습니다.")

    except Error as e:
        print(f"데이터베이스 오류: {e}")

    finally:
        # 4. 자원 정리
        close(conn, cursor)