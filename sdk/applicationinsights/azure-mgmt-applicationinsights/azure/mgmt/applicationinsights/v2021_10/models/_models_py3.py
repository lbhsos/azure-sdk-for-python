# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ErrorResponseLinkedStorage(msrest.serialization.Model):
    """ErrorResponseLinkedStorage.

    :ivar error: Error response indicates Insights service is not able to process the incoming
     request. The reason is provided in the error message.
    :vartype error: ~azure.mgmt.applicationinsights.v2021_10.models.ErrorResponseLinkedStorageError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponseLinkedStorageError'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorResponseLinkedStorageError"] = None,
        **kwargs
    ):
        """
        :keyword error: Error response indicates Insights service is not able to process the incoming
         request. The reason is provided in the error message.
        :paramtype error:
         ~azure.mgmt.applicationinsights.v2021_10.models.ErrorResponseLinkedStorageError
        """
        super(ErrorResponseLinkedStorage, self).__init__(**kwargs)
        self.error = error


class ErrorResponseLinkedStorageError(msrest.serialization.Model):
    """Error response indicates Insights service is not able to process the incoming request. The reason is provided in the error message.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: Error code.
    :vartype code: str
    :ivar message: Error message indicating why the operation failed.
    :vartype message: str
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(ErrorResponseLinkedStorageError, self).__init__(**kwargs)
        self.code = None
        self.message = None


class LiveTokenResponse(msrest.serialization.Model):
    """The response to a live token query.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar live_token: JWT token for accessing live metrics stream data.
    :vartype live_token: str
    """

    _validation = {
        'live_token': {'readonly': True},
    }

    _attribute_map = {
        'live_token': {'key': 'liveToken', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(LiveTokenResponse, self).__init__(**kwargs)
        self.live_token = None


class OperationInfo(msrest.serialization.Model):
    """Information about an operation.

    :ivar provider: Name of the provider.
    :vartype provider: str
    :ivar resource: Name of the resource type.
    :vartype resource: str
    :ivar operation: Name of the operation.
    :vartype operation: str
    :ivar description: Description of the operation.
    :vartype description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword provider: Name of the provider.
        :paramtype provider: str
        :keyword resource: Name of the resource type.
        :paramtype resource: str
        :keyword operation: Name of the operation.
        :paramtype operation: str
        :keyword description: Description of the operation.
        :paramtype description: str
        """
        super(OperationInfo, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class OperationLive(msrest.serialization.Model):
    """Represents an operation returned by the GetOperations request.

    :ivar name: Name of the operation.
    :vartype name: str
    :ivar is_data_action: Indicates whether the operation is a data action.
    :vartype is_data_action: bool
    :ivar display: Display name of the operation.
    :vartype display: ~azure.mgmt.applicationinsights.v2021_10.models.OperationInfo
    :ivar origin: Origin of the operation.
    :vartype origin: str
    :ivar properties: Properties of the operation.
    :vartype properties: any
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
        'display': {'key': 'display', 'type': 'OperationInfo'},
        'origin': {'key': 'origin', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        is_data_action: Optional[bool] = None,
        display: Optional["OperationInfo"] = None,
        origin: Optional[str] = None,
        properties: Optional[Any] = None,
        **kwargs
    ):
        """
        :keyword name: Name of the operation.
        :paramtype name: str
        :keyword is_data_action: Indicates whether the operation is a data action.
        :paramtype is_data_action: bool
        :keyword display: Display name of the operation.
        :paramtype display: ~azure.mgmt.applicationinsights.v2021_10.models.OperationInfo
        :keyword origin: Origin of the operation.
        :paramtype origin: str
        :keyword properties: Properties of the operation.
        :paramtype properties: any
        """
        super(OperationLive, self).__init__(**kwargs)
        self.name = name
        self.is_data_action = is_data_action
        self.display = display
        self.origin = origin
        self.properties = properties


class OperationsListResult(msrest.serialization.Model):
    """Result of the List Operations operation.

    :ivar value: A collection of operations.
    :vartype value: list[~azure.mgmt.applicationinsights.v2021_10.models.OperationLive]
    :ivar next_link: URL to get the next set of operation list results if there are any.
    :vartype next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[OperationLive]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["OperationLive"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword value: A collection of operations.
        :paramtype value: list[~azure.mgmt.applicationinsights.v2021_10.models.OperationLive]
        :keyword next_link: URL to get the next set of operation list results if there are any.
        :paramtype next_link: str
        """
        super(OperationsListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link