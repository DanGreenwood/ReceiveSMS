r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Chat
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Optional
from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.chat.v3.channel import ChannelList


class V3(Version):
    def __init__(self, domain: Domain):
        """
        Initialize the V3 version of Chat

        :param domain: The Twilio.chat domain
        """
        super().__init__(domain, "v3")
        self._channels: Optional[ChannelList] = None

    @property
    def channels(self) -> ChannelList:
        if self._channels is None:
            self._channels = ChannelList(self)
        return self._channels

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        """
        return "<Twilio.Chat.V3>"
