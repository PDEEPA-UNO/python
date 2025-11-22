class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Initializing the television object.
        :param self.__status: Indicates whether the tv is turned on or off
        :param self.__muted: Indicates whether the tv is muted or unmuted
        :param self.__volume: The default volume is set to 0; this variable
        can be manipulated through the volume_up and volume_down functions
        ":param self.__channel: The default channel is set to 0; this variable
        can be manipulated through the channel_up and channel_down functions.
        '''

        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        '''
        Toggles power on or off
        '''

        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        '''
        Toggles the mute option for the tv
        '''

        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        '''
        Increases the channel up 1
        If channel reaches MAX_CHANNEL, then channel sets back to the MIN_CHANNEL
        '''

        if self.__status == True:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        '''
        Decreases the channel down 1
        If channel reaches MIN_CHANNEL, then channel sets back to the MAX_CHANNEL
        '''

        if self.__status == True:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        '''
        Increases the volume up 1
        Unlike channel, if volume reaches MAX_VOLUME, volume stays at MAX_VOLUME
        '''

        if self.__status == True:
            self.__volume += 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            self.__muted = False

    def volume_down(self) -> None:
        '''
        Decreases the volume down 1
        Unlike channel, if volume reaches MIN_VOLUME, volume stays at MIN_VOLUME
        '''

        if self.__status == True:
            self.__volume -= 1
            if self.__volume < Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            self.__muted = False

    def __str__(self) -> str:
        '''
        Displays final configurations  of the television object
        :return: string outlining the power status, channel number and volume level
        '''

        if self.__muted == True:
            display_volume = 0
        else:
            display_volume = self.__volume
        return f'Power = {self.__status} Channel = {self.__channel} Volume = {display_volume}'