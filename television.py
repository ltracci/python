class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initialize the Television with default settings."""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__actual_volume = self.__volume

    def power(self):
        """Turn the TV on or off."""
        self.__status = not self.__status
        if not self.__status:
            self.__muted = False

    def mute(self):
        """Mute or unmute the TV."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """Increase the channel, returning to the lowest channel if at maximum."""
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self):
        """Decrease the channel, returning to the highest channel if at minimum."""
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self):
        """Increase the volume if TV is not muted up to maximum volume."""
        if self.__status and not self.__muted:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            self.__actual_volume = self.__volume

    def volume_down(self):
        """Decrease the volume if TV is not muted, down to minimum volume."""
        if self.__status and not self.__muted:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            self.__actual_volume = self.__volume

    def __str__(self):
        """Return strings for current power status, volume, and channel."
        power_status = "True" if self.__status else "False"
        display_volume = 0 if self.__muted else self.__volume
        return f"Power = {power_status}, Channel = {self.__channel}, Volume = {display_volume}"
