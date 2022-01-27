
import pygame as pg


def f(x):
    return 1 / (1 + 2.71828**(-x))


pg.init()
window = pg.display.set_mode((600, 600))

weights = [0.5] * 3
traning_data = []
test_data = []
for i in range(100):
    for j in range(100):
        test_data.append((i/100, j/100))


game = True
while game:

    for te in test_data:
        ret = f(te[0] * weights[0] + te[1] * weights[1] + weights[2])
        pg.draw.rect(window, (ret * 255, 255 - ret * 255, 0), (te[1] * 601, te[0] * 601, 6, 6))

    for tr in traning_data:
        pg.draw.rect(window, (tr[2] * 255, 255 - tr[2] * 255, 0), (tr[1] * 600, tr[0] * 600, 6, 6))
        pg.draw.rect(window, (0, 0, 0), (tr[1] * 600, tr[0] * 600, 6, 6), 1)

    pg.display.flip()

    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False

        if e.type == pg.KEYUP and e.key == pg.K_ESCAPE:
            traning_data = []

        if e.type == pg.MOUSEBUTTONUP:
            weights = [0.5]*3
            y, x = pg.mouse.get_pos()
            y, x = y / 600, x / 600
            if e.button == 3:
                traning_data.append((x, y, 1))
            if e.button == 1:
                traning_data.append((x, y, 0))

            q = 0.01
            for i in range(10000):
                for tr in traning_data:
                    ret = f(tr[0] * weights[0] + tr[1] * weights[1] + weights[2])

                    err = ret - tr[2]
                    delta = err * (1 - ret) * ret

                    weights[0] -= q * delta * tr[0]
                    weights[1] -= q * delta * tr[1]
                    weights[2] -= q * delta
