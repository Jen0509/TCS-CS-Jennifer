import random

def dinner_list():
    # 저녁 메뉴 목록
    menu = [
        "치킨",
        "단백질 쉐이크",
        "파스타",
        "샐러드",
        "스시",
        "햄버거",
        "도넛",
        "팟타이",
        "불고기",
        "삼겹살",
        "돈까스"
        "떡볶이"
    ]
    
    # 랜덤으로 메뉴 선택
    recommended_dinner = random.choice(menu)
    
    return recommended_dinner

# 인터페이스
if __name__ == "__main__":
    user_response = input("저녁 메뉴를 추천해드릴까요? (네/아니요): ")

    if user_response.strip() == "네":
        print("오늘 저녁 메뉴 추천:", dinner_list())
    else:
        print("추천하지 않겠습니다. 좋은 저녁 되세요!")