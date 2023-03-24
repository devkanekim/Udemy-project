# 터틀 라이브러리를 이용하여 스네이크 게임 만들기
# 1. 스네이크 몸 만들기
# 2. 스네이크 구동
# 3. 스네이크 조작
# 4. 음식 감지
# 5. 스코어 표기
# 6. 벽 감지
# 7. 꼬리 감지


from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
