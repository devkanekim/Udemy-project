# 터틀 라이브러리를 이용하여 스네이크 생성
from turtle import Turtle

# 스네이크 한 부위당 20x20 으로 설정
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# 하드코딩이 되지않게 상수나 변수는 따로 관리
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # 사각형의 스네이크를 리스트에 담음
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    # 처음 시작 스네이크 3덩어리
    def create_snake(self):
        for position in STARTING_POSITIONS:
             self.add_segment(position)

    def add_segment(self, position):
            # 사각형의 집합으로 스네이크 생성
            new_segment = Turtle("square")
            new_segment.color("white")
            # 터틀 라이브러리에 설정된 기본값인 선긋기 해제
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    # 추가되는 꼬리 설정
    def extend(self):
        #  마지막 꼬리 추가시 현재 마지막 꼬리의 위치에 추가
         self.add_segment(self.segments[-1].position())
    # 앞에서부터 이동하면 다음 꼬리의 이동이 어려움
    # 뒤에서부터 이동. 단 머리는 제외  
    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # 머리는 고정된 이동량
        self.head.forward(MOVE_DISTANCE)

    # 상, 하, 좌, 우 이동 정의.
    # 게임 특성상 이동방향 반대는 허용되지 않음
    def up(self):
        if self.head.headging() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.headging() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.headging() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.headging() != LEFT:
            self.head.setheading(RIGHT)        
