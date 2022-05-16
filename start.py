import pygame
import pygame_menu
import pythongra 
def zmianaRozdzielczosci(nazwaPola,atrybut):
    pythongra.rozdzielczosc=atrybut
def zmienKolorWaz1(value):
    pythongra.zmienaKolorWaz1(value)
def zmienKolorWaz2(value):
    pythongra.zmienaKolorWaz2(value)
def main():
    pygame.init()
    OknoMenu=pygame.display.set_mode((400,400))
    pygame.display.set_caption("Menu Snake")
    menu = pygame_menu.Menu('Snake 3TI', 400, 400,theme=pygame_menu.themes.THEME_DARK)
    menu.add.button("Start Gry",pythongra.main,background_color=(0,0,0))
    menu.add.selector("Rozmiar ekranu",[('400x400',400),('600x600',600),('800x800',800)],onchange=zmianaRozdzielczosci)
    menu.add.color_input("Kolor wąż 1",'rgb', default=(25,25,100),onreturn=zmienKolorWaz1) 
    menu.add.color_input("Kolor wąż 2",'rgb', default=(25,25,16),onreturn=zmienKolorWaz2) 

    menu.mainloop(OknoMenu)

main()
