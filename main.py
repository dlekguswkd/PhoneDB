# 전화번호 관리 프로그램

import phone_dao

print("*******************************************")
print("*         전화번호 관리 프로그램          *")
print("*******************************************")


while True:
    print("")
    print("1.리스트   2.등록   3.삭제   4.검색   5.종료")
    print("--------------------------------------------")

    no = int(input(">메뉴번호: "))

    if no == 1:
        print("<1.리스트>")
        phone_dao.get_person_list()

    elif no == 2:
        print("<2.등록>")
        phone_dao.add_person()

    elif no == 3:
        print("<3.삭제>")
        phone_dao.delete_person()

    elif no == 4:
        print("<4.검색>")   
        phone_dao.search_person()

    elif no == 5:
        print("*******************************************")
        print("*               감사합니다                *")
        print("*******************************************")
        break
    else:
        print("[다시 입력해 주세요.]")


