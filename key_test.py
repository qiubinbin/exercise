import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
screen_color = (255, 255, 255)


def show_text(surface_handle, pos, text, color, font_bold=False, font_size=13, font_italic=False):
    '''''
    Function:文字处理函数
    Input：surface_handle：surface句柄
           pos：文字显示位置
           color:文字颜色
           font_bold:是否加粗
           font_size:字体大小
           font_italic:是否斜体
    Output: NONE
    author: socrates
    blog:http://blog.csdn.net/dyx1024
    date:2012-04-15
    '''
    # 获取系统字体，并设置文字大小
    cur_font = pygame.font.SysFont("宋体", 100)

    # 设置是否加粗属性
    cur_font.set_bold(font_bold)

    # 设置是否斜体属性
    cur_font.set_italic(font_italic)

    # 设置文字内容
    text_fmt = cur_font.render(text, 1, color)

    # 绘制文字
    surface_handle.blit(text_fmt, pos)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print(event.key)
    screen.fill(screen_color)
    show_text(screen, (960, 540), "A", (255, 0, 0))
    pygame.display.flip()
