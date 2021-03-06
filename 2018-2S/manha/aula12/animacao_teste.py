import pygame
from pygame import QUIT

pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
sprite_sheet = pygame.image.load("EpicArmor.png").convert_alpha()

sergio = {  "state": "images_state_up_stop",
            "images_state_up_run":[1, 2, 3, 4, 5, 6, 7, 8],
            "images_state_up_stop":[0],
            "images_state_down_run": [19, 20, 21, 22, 23, 24, 25, 26],
            "images_state_down_stop": [18],
            "frame_index": 0
        }

def get_frame( gId ):
    global sprite_sheet
    top = 0
    margin = 0
    space_h = 0
    space_v = 0
    width = 64
    height = 64
    columns = 9
    coluna = gId % columns
    linha = int(gId / columns)
    x = margin + (coluna * (width + space_h))
    y = top + (linha * (height + space_v))
    img = sprite_sheet.subsurface(x, y, width, height)
    return img

def anima( obj ):
    chave = obj["state"]
    frames = obj[chave]
    obj["frame_index"] += 1
    if obj["frame_index"] > len(frames):
        obj["frame_index"] = 0
    gId = frames[obj["frame_index"]]
    sur_frame = get_frame(gId)
    tela.blit(sur_frame, (400, 300))

frame_index = 19
clk = pygame.time.Clock()

while True:
    # Calcular Regras
    frame_index += 1
    if frame_index > 26:
        frame_index = 19

    # Pintar
    tela.fill((0, 0, 0))
    frame = get_frame( frame_index )
    tela.blit(frame, (400, 300))
    pygame.display.update()
    clk.tick(10)

    # Captura eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()