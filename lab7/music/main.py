import pygame
from core.music import handle_music_keys, load_music
from core.renderer import draw_background

pygame.init()
screen = pygame.display.set_mode((225, 225))
pygame.display.set_caption("Simple Music Player")

songs = [
    "/Users/ayananauryzbaeva/Desktop/pp2/labky/lab7/music/assets/21 Savage - all of me.mp3",
    "/Users/ayananauryzbaeva/Desktop/pp2/labky/lab7/music/assets/21 Savage - dangerous (Feat. Lil Durk & Metro Boomin).mp3",
    "/Users/ayananauryzbaeva/Desktop/pp2/labky/lab7/music/assets/21 Savage - redrum.mp3"
]

current_song = 0
music_playing = True

load_music(songs[current_song])
pygame.mixer.music.play()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            current_song, music_playing = handle_music_keys(event, songs, current_song, music_playing)

    draw_background(screen)
    pygame.display.flip()
