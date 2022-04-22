class Television:
    """
    A class representing details for a television object
    """
    MIN_CHANNEL: int = 0  # Minimum TV channel
    MAX_CHANNEL: int = 3  # Maximum TV channel

    MIN_VOLUME: int = 0  # Minimum TV volume
    MAX_VOLUME: int = 2  # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create initial state of a television object
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False

    def power(self) -> None:
        """
        Method to toggle power from on to off and off to on
        """
        self.__status = not self.__status

    def channel_up(self) -> None:
        """
        Method to increment the variable channel if power is on
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrement the variable channel if power is on
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increment the variable volume if power is on
        """
        if self.__status and self.__volume < Television.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrement the variable channel if power is on
        """
        if self.__status and self.__volume > Television.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to return television status for channel, volume, and power
        """
        return f'TV status: is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'



