# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class RemoteRenderingOperations:
    """RemoteRenderingOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mixedreality.remoterendering._generated.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def create_conversion(
        self,
        account_id: str,
        conversion_id: str,
        body: "models.CreateAssetConversionSettings",
        **kwargs
    ) -> "models.AssetConversion":
        """Creates a conversion using an asset stored in an Azure Blob Storage account.

        Creates a conversion using an asset stored in an Azure Blob Storage account.

        :param account_id: The Azure Remote Rendering account ID.
        :type account_id: str
        :param conversion_id: An ID uniquely identifying the conversion for the given account. The ID
         is case sensitive, can contain any combination of alphanumeric characters including hyphens and
         underscores, and cannot contain more than 256 characters.
        :type conversion_id: str
        :param body: Request body configuring the settings for an asset conversion.
        :type body: ~azure.mixedreality.remoterendering._generated.models.CreateAssetConversionSettings
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AssetConversion, or the result of cls(response)
        :rtype: ~azure.mixedreality.remoterendering._generated.models.AssetConversion
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AssetConversion"]
        error_map = {
            404: ResourceNotFoundError,
            400: lambda response: HttpResponseError(response=response, model=self._deserialize(models.ErrorResponse, response)),
            409: lambda response: ResourceExistsError(response=response, model=self._deserialize(models.ErrorResponse, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(models.ErrorResponse, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_conversion.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'account_id': self._serialize.url("account_id", account_id, 'str'),
            'conversion_id': self._serialize.url("conversion_id", conversion_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'CreateAssetConversionSettings')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        if response.status_code == 200:
            response_headers['MS-CV']=self._deserialize('str', response.headers.get('MS-CV'))
            deserialized = self._deserialize('AssetConversion', pipeline_response)

        if response.status_code == 201:
            response_headers['MS-CV']=self._deserialize('str', response.headers.get('MS-CV'))
            deserialized = self._deserialize('AssetConversion', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    create_conversion.metadata = {'url': '/accounts/{account_id}/conversions/{conversion_id}'}  # type: ignore

    async def get_conversion(
        self,
        account_id: str,
        conversion_id: str,
        **kwargs
    ) -> "models.AssetConversion":
        """Gets the status of a particular conversion.

        Gets the status of a particular conversion.

        :param account_id: The Azure Remote Rendering account ID.
        :type account_id: str
        :param conversion_id: An ID uniquely identifying the conversion for the given account. The ID
         is case sensitive, can contain any combination of alphanumeric characters including hyphens and
         underscores, and cannot contain more than 256 characters.
        :type conversion_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AssetConversion, or the result of cls(response)
        :rtype: ~azure.mixedreality.remoterendering._generated.models.AssetConversion
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AssetConversion"]
        error_map = {
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(models.ErrorResponse, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"

        # Construct URL
        url = self.get_conversion.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'account_id': self._serialize.url("account_id", account_id, 'str'),
            'conversion_id': self._serialize.url("conversion_id", conversion_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers['MS-CV']=self._deserialize('str', response.headers.get('MS-CV'))
        response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
        deserialized = self._deserialize('AssetConversion', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get_conversion.metadata = {'url': '/accounts/{account_id}/conversions/{conversion_id}'}  # type: ignore

    def list_conversions(
        self,
        account_id: str,
        **kwargs
    ) -> AsyncIterable["models.ConversionList"]:
        """Gets a list of all conversions.

        Gets a list of all conversions.

        :param account_id: The Azure Remote Rendering account ID.
        :type account_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ConversionList or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mixedreality.remoterendering._generated.models.ConversionList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ConversionList"]
        error_map = {
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(models.ErrorResponse, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_conversions.metadata['url']  # type: ignore
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                    'account_id': self._serialize.url("account_id", account_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                    'account_id': self._serialize.url("account_id", account_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ConversionList', pipeline_response)
            list_of_elem = deserialized.conversions
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_conversions.metadata = {'url': '/accounts/{account_id}/conversions'}  # type: ignore

    async def create_session(
        self,
        account_id: str,
        session_id: str,
        body: "models.CreateRenderingSessionSettings",
        **kwargs
    ) -> "models.RenderingSession":
        """Creates a new rendering session.

        Creates a new rendering session.

        :param account_id: The Azure Remote Rendering account ID.
        :type account_id: str
        :param session_id: An ID uniquely identifying the rendering session for the given account. The
         ID is case sensitive, can contain any combination of alphanumeric characters including hyphens
         and underscores, and cannot contain more than 256 characters.
        :type session_id: str
        :param body: Settings of the session to be created.
        :type body: ~azure.mixedreality.remoterendering._generated.models.CreateRenderingSessionSettings
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RenderingSession, or the result of cls(response)
        :rtype: ~azure.mixedreality.remoterendering._generated.models.RenderingSession
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.RenderingSession"]
        error_map = {
            404: ResourceNotFoundError,
            400: lambda response: HttpResponseError(response=response, model=self._deserialize(models.ErrorResponse, response)),
            409: lambda response: ResourceExistsError(response=response, model=self._deserialize(models.ErrorResponse, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(models.ErrorResponse, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_session.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'account_id': self._serialize.url("account_id", account_id, 'str'),
            'session_id': self._serialize.url("session_id", session_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'CreateRenderingSessionSettings')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize('RenderingSession', pipeline_response)

        if response.status_code == 201:
            response_headers['MS-CV']=self._deserialize('str', response.headers.get('MS-CV'))
            deserialized = self._deserialize('RenderingSession', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    create_session.metadata = {'url': '/accounts/{account_id}/sessions/{session_id}'}  # type: ignore

    async def get_session(
        self,
        account_id: str,
        session_id: str,
        **kwargs
    ) -> "models.RenderingSession":
        """Gets the properties of a particular rendering session.

        Gets the properties of a particular rendering session.

        :param account_id: The Azure Remote Rendering account ID.
        :type account_id: str
        :param session_id: An ID uniquely identifying the rendering session for the given account. The
         ID is case sensitive, can contain any combination of alphanumeric characters including hyphens
         and underscores, and cannot contain more than 256 characters.
        :type session_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RenderingSession, or the result of cls(response)
        :rtype: ~azure.mixedreality.remoterendering._generated.models.RenderingSession
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.RenderingSession"]
        error_map = {
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(models.ErrorResponse, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"

        # Construct URL
        url = self.get_session.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'account_id': self._serialize.url("account_id", account_id, 'str'),
            'session_id': self._serialize.url("session_id", session_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('RenderingSession', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_session.metadata = {'url': '/accounts/{account_id}/sessions/{session_id}'}  # type: ignore

    async def update_session(
        self,
        account_id: str,
        session_id: str,
        body: "models.UpdateSessionSettings",
        **kwargs
    ) -> "models.RenderingSession":
        """Updates the max lease time of a particular rendering session.

        Updates the max lease time of a particular rendering session.

        :param account_id: The Azure Remote Rendering account ID.
        :type account_id: str
        :param session_id: An ID uniquely identifying the rendering session for the given account. The
         ID is case sensitive, can contain any combination of alphanumeric characters including hyphens
         and underscores, and cannot contain more than 256 characters.
        :type session_id: str
        :param body: Settings used to update the session.
        :type body: ~azure.mixedreality.remoterendering._generated.models.UpdateSessionSettings
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RenderingSession, or the result of cls(response)
        :rtype: ~azure.mixedreality.remoterendering._generated.models.RenderingSession
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.RenderingSession"]
        error_map = {
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            422: lambda response: HttpResponseError(response=response, model=self._deserialize(models.ErrorResponse, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(models.ErrorResponse, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_session.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'account_id': self._serialize.url("account_id", account_id, 'str'),
            'session_id': self._serialize.url("session_id", session_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'UpdateSessionSettings')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('RenderingSession', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    update_session.metadata = {'url': '/accounts/{account_id}/sessions/{session_id}'}  # type: ignore

    async def stop_session(
        self,
        account_id: str,
        session_id: str,
        **kwargs
    ) -> None:
        """Stops a particular rendering session.

        Stops a particular rendering session.

        :param account_id: The Azure Remote Rendering account ID.
        :type account_id: str
        :param session_id: An ID uniquely identifying the rendering session for the given account. The
         ID is case sensitive, can contain any combination of alphanumeric characters including hyphens
         and underscores, and cannot contain more than 256 characters.
        :type session_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(models.ErrorResponse, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"

        # Construct URL
        url = self.stop_session.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'account_id': self._serialize.url("account_id", account_id, 'str'),
            'session_id': self._serialize.url("session_id", session_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers['MS-CV']=self._deserialize('str', response.headers.get('MS-CV'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    stop_session.metadata = {'url': '/accounts/{account_id}/sessions/{session_id}/:stop'}  # type: ignore

    def list_sessions(
        self,
        account_id: str,
        **kwargs
    ) -> AsyncIterable["models.SessionsList"]:
        """Gets a list of all rendering sessions.

        Gets a list of all rendering sessions.

        :param account_id: The Azure Remote Rendering account ID.
        :type account_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SessionsList or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mixedreality.remoterendering._generated.models.SessionsList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SessionsList"]
        error_map = {
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(models.ErrorResponse, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_sessions.metadata['url']  # type: ignore
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                    'account_id': self._serialize.url("account_id", account_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                    'account_id': self._serialize.url("account_id", account_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('SessionsList', pipeline_response)
            list_of_elem = deserialized.sessions
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_sessions.metadata = {'url': '/accounts/{account_id}/sessions'}  # type: ignore