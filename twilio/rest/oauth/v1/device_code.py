r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Oauth
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, serialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class DeviceCodeInstance(InstanceResource):

    """
    :ivar device_code: The device verification code.
    :ivar user_code: The verification code which end user uses to verify authorization request.
    :ivar verification_uri: The URI that the end user visits to verify authorization request.
    :ivar verification_uri_complete: The URI with user_code that the end-user alternatively visits to verify authorization request.
    :ivar expires_in: The expiration time of the device_code and user_code in seconds.
    :ivar interval: The minimum amount of time in seconds that the client should wait between polling requests to the token endpoint.
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.device_code: Optional[str] = payload.get("device_code")
        self.user_code: Optional[str] = payload.get("user_code")
        self.verification_uri: Optional[str] = payload.get("verification_uri")
        self.verification_uri_complete: Optional[str] = payload.get(
            "verification_uri_complete"
        )
        self.expires_in: Optional[int] = payload.get("expires_in")
        self.interval: Optional[int] = deserialize.integer(payload.get("interval"))

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Oauth.V1.DeviceCodeInstance>"


class DeviceCodeList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the DeviceCodeList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/device/code"

    def create(
        self,
        client_sid: str,
        scopes: List[str],
        audiences: Union[List[str], object] = values.unset,
    ) -> DeviceCodeInstance:
        """
        Create the DeviceCodeInstance

        :param client_sid: A 34 character string that uniquely identifies this OAuth App.
        :param scopes: An Array of scopes for authorization request
        :param audiences: An array of intended audiences for token requests

        :returns: The created DeviceCodeInstance
        """
        data = values.of(
            {
                "ClientSid": client_sid,
                "Scopes": serialize.map(scopes, lambda e: e),
                "Audiences": serialize.map(audiences, lambda e: e),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return DeviceCodeInstance(self._version, payload)

    async def create_async(
        self,
        client_sid: str,
        scopes: List[str],
        audiences: Union[List[str], object] = values.unset,
    ) -> DeviceCodeInstance:
        """
        Asynchronously create the DeviceCodeInstance

        :param client_sid: A 34 character string that uniquely identifies this OAuth App.
        :param scopes: An Array of scopes for authorization request
        :param audiences: An array of intended audiences for token requests

        :returns: The created DeviceCodeInstance
        """
        data = values.of(
            {
                "ClientSid": client_sid,
                "Scopes": serialize.map(scopes, lambda e: e),
                "Audiences": serialize.map(audiences, lambda e: e),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return DeviceCodeInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Oauth.V1.DeviceCodeList>"
