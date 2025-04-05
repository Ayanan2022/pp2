import pygame

def load_music(path):
    pygame.mixer.music.load(path)

def handle_music_keys(event, songs, current_song, music_playing):
    if event.key == pygame.K_SPACE:
        if music_playing:
            pygame.mixer.music.pause()
            music_playing = False
        else:
            pygame.mixer.music.unpause()
            music_playing = True

    elif event.key == pygame.K_RIGHT:
        current_song += 1
        if current_song >= len(songs):
            current_song = 0
        load_music(songs[current_song])
        pygame.mixer.music.play()
        music_playing = True

    elif event.key == pygame.K_LEFT:
        current_song -= 1
        if current_song < 0:
            current_song = len(songs) - 1
        load_music(songs[current_song])
        pygame.mixer.music.play()
        music_playing = True

    return current_song, music_playing
