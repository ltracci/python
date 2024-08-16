
class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__actual_volume = self.__volume

    def power(self):
        self.__status = not self.__status
        if not self.__status:
            self.__muted = False  # Automatically unmute when TV is turned off

    def mute(self):
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.__actual_volume = self.__volume
            self.__volume = 0 if self.__muted else self.__actual_volume

    def channel_up(self):
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self):
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self):
        if self.__status and not self.__muted:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            self.__actual_volume = self.__volume

    def volume_down(self):
        if self.__status and not self.__muted:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            self.__actual_volume = self.__volume

    def __str__(self):
        power_status = "True" if self.__status else "False"
        display_volume = 0 if self.__muted else self.__volume
        return f"Power = {power_status}, Channel = {self.__channel}, Volume = {display_volume}"
