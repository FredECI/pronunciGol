import pygame as pg
import time

from pygame._sdl2 import (
    get_audio_device_names,
    AudioDevice,
    AUDIO_F32,
    AUDIO_ALLOW_FORMAT_CHANGE,
)
from pygame._sdl2.mixer import set_post_mix

class VoiceCapture:
    def __init__(self):
        pg.mixer.pre_init(44100, 32, 2, 512)
        pg.init()

        # init_subsystem(INIT_AUDIO)
        self.names = get_audio_device_names(True)
        self.sound_chunks = []


    def _callback(self, audiodevice, audiomemoryview):
        """This is called in the sound thread.
        Note, that the frequency and such you request may not be what you get.
        """
        # print(type(audiomemoryview), len(audiomemoryview))
        # print(audiodevice)
        self.sound_chunks.append(bytes(audiomemoryview))


    def _postmix_callback(self, postmix, audiomemoryview):
        """This is called in the sound thread.
        At the end of mixing we get this data.
        """
        print(type(audiomemoryview), len(audiomemoryview))
        print(postmix)

    def _create_audio_device(self):
        set_post_mix(self._postmix_callback)
        audio_device = AudioDevice(
            devicename=self.names[0],
            iscapture=True,
            frequency=44100,
            audioformat=AUDIO_F32,
            numchannels=2,
            chunksize=512,
            allowed_changes=AUDIO_ALLOW_FORMAT_CHANGE,
            callback=self._callback,
        )
        return audio_device

    def record(self):
        audio_device = self._create_audio_device()
        # start recording.
        audio_device.pause(0)

        print(f"recording with '{self.names[0]}'")
        time.sleep(5)

        print("Turning data into a pg.mixer.Sound")
        sound = pg.mixer.Sound(buffer=b"".join(self.sound_chunks))

        return sound


# voice_client = VoiceCapture()
# sound = voice_client.record()
# print("playing back recorded sound")
# sound.play()
# time.sleep(5)
# pg.quit() 