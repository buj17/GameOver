import os.path

import pygame

pygame.init()
_size = _width, _height = 600, 300
_main_screen = pygame.display.set_mode(_size)


def load_image(filename: str | os.PathLike, colorkey=None) -> pygame.Surface:
    fullname = os.path.join('data', filename)
    if not os.path.isfile(fullname):
        pass
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class GameOver(pygame.sprite.Sprite):
    gameover_image = load_image('gameover.png')

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = GameOver.gameover_image
        self.rect = self.image.get_rect()
        self.x = self.rect.x = -_width
        self.velocity = 200

    def move(self, fps: int):
        displacement = self.velocity / fps

        if self.x < 0:
            self.x += displacement

        self.rect.x = self.x


class MainWindow:
    def __init__(self):
        self.fps = 100
        self.size = _size
        self.screen = _main_screen
        self.main_sprite_group = pygame.sprite.Group()
        self.gameover = GameOver(self.main_sprite_group)

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            self.screen.fill(pygame.Color('blue'))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.gameover.move(self.fps)

            self.main_sprite_group.draw(self.screen)
            self.main_sprite_group.update()

            pygame.display.flip()
            clock.tick(self.fps)
        pygame.quit()


if __name__ == '__main__':
    window = MainWindow()
    window.run()
