# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AllowedAudiencesValidation
from ._models_py3 import AllowedPrincipals
from ._models_py3 import AppLogsConfiguration
from ._models_py3 import AppRegistration
from ._models_py3 import Apple
from ._models_py3 import AppleRegistration
from ._models_py3 import AuthConfig
from ._models_py3 import AuthConfigCollection
from ._models_py3 import AuthPlatform
from ._models_py3 import AvailableOperations
from ._models_py3 import AvailableWorkloadProfile
from ._models_py3 import AvailableWorkloadProfileProperties
from ._models_py3 import AvailableWorkloadProfilesCollection
from ._models_py3 import AzureActiveDirectory
from ._models_py3 import AzureActiveDirectoryLogin
from ._models_py3 import AzureActiveDirectoryRegistration
from ._models_py3 import AzureActiveDirectoryValidation
from ._models_py3 import AzureCredentials
from ._models_py3 import AzureFileProperties
from ._models_py3 import AzureStaticWebApps
from ._models_py3 import AzureStaticWebAppsRegistration
from ._models_py3 import BaseContainer
from ._models_py3 import BillingMeter
from ._models_py3 import BillingMeterCollection
from ._models_py3 import BillingMeterProperties
from ._models_py3 import Certificate
from ._models_py3 import CertificateCollection
from ._models_py3 import CertificatePatch
from ._models_py3 import CertificateProperties
from ._models_py3 import CheckNameAvailabilityRequest
from ._models_py3 import CheckNameAvailabilityResponse
from ._models_py3 import ClientRegistration
from ._models_py3 import Configuration
from ._models_py3 import ConnectedEnvironment
from ._models_py3 import ConnectedEnvironmentCollection
from ._models_py3 import ConnectedEnvironmentStorage
from ._models_py3 import ConnectedEnvironmentStorageProperties
from ._models_py3 import ConnectedEnvironmentStoragesCollection
from ._models_py3 import Container
from ._models_py3 import ContainerApp
from ._models_py3 import ContainerAppAuthToken
from ._models_py3 import ContainerAppCollection
from ._models_py3 import ContainerAppProbe
from ._models_py3 import ContainerAppProbeHttpGet
from ._models_py3 import ContainerAppProbeHttpGetHttpHeadersItem
from ._models_py3 import ContainerAppProbeTcpSocket
from ._models_py3 import ContainerAppSecret
from ._models_py3 import ContainerResources
from ._models_py3 import CookieExpiration
from ._models_py3 import CustomDomain
from ._models_py3 import CustomDomainConfiguration
from ._models_py3 import CustomHostnameAnalysisResult
from ._models_py3 import CustomHostnameAnalysisResultCustomDomainVerificationFailureInfo
from ._models_py3 import CustomHostnameAnalysisResultCustomDomainVerificationFailureInfoDetailsItem
from ._models_py3 import CustomOpenIdConnectProvider
from ._models_py3 import CustomScaleRule
from ._models_py3 import Dapr
from ._models_py3 import DaprComponent
from ._models_py3 import DaprComponentsCollection
from ._models_py3 import DaprMetadata
from ._models_py3 import DaprSecret
from ._models_py3 import DaprSecretsCollection
from ._models_py3 import DefaultAuthorizationPolicy
from ._models_py3 import DefaultErrorResponse
from ._models_py3 import DefaultErrorResponseError
from ._models_py3 import DefaultErrorResponseErrorDetailsItem
from ._models_py3 import DiagnosticDataProviderMetadata
from ._models_py3 import DiagnosticDataProviderMetadataPropertyBagItem
from ._models_py3 import DiagnosticDataTableResponseColumn
from ._models_py3 import DiagnosticDataTableResponseObject
from ._models_py3 import DiagnosticRendering
from ._models_py3 import DiagnosticSupportTopic
from ._models_py3 import Diagnostics
from ._models_py3 import DiagnosticsCollection
from ._models_py3 import DiagnosticsDataApiResponse
from ._models_py3 import DiagnosticsDefinition
from ._models_py3 import DiagnosticsProperties
from ._models_py3 import DiagnosticsStatus
from ._models_py3 import EnvironmentAuthToken
from ._models_py3 import EnvironmentSkuProperties
from ._models_py3 import EnvironmentVar
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import ExtendedLocation
from ._models_py3 import Facebook
from ._models_py3 import ForwardProxy
from ._models_py3 import GitHub
from ._models_py3 import GithubActionConfiguration
from ._models_py3 import GlobalValidation
from ._models_py3 import Google
from ._models_py3 import HttpScaleRule
from ._models_py3 import HttpSettings
from ._models_py3 import HttpSettingsRoutes
from ._models_py3 import IdentityProviders
from ._models_py3 import Ingress
from ._models_py3 import InitContainer
from ._models_py3 import IpSecurityRestrictionRule
from ._models_py3 import JwtClaimChecks
from ._models_py3 import LogAnalyticsConfiguration
from ._models_py3 import Login
from ._models_py3 import LoginRoutes
from ._models_py3 import LoginScopes
from ._models_py3 import ManagedEnvironment
from ._models_py3 import ManagedEnvironmentOutboundSettings
from ._models_py3 import ManagedEnvironmentStorage
from ._models_py3 import ManagedEnvironmentStorageProperties
from ._models_py3 import ManagedEnvironmentStoragesCollection
from ._models_py3 import ManagedEnvironmentsCollection
from ._models_py3 import ManagedServiceIdentity
from ._models_py3 import Nonce
from ._models_py3 import OpenIdConnectClientCredential
from ._models_py3 import OpenIdConnectConfig
from ._models_py3 import OpenIdConnectLogin
from ._models_py3 import OpenIdConnectRegistration
from ._models_py3 import OperationDetail
from ._models_py3 import OperationDisplay
from ._models_py3 import ProxyResource
from ._models_py3 import QueueScaleRule
from ._models_py3 import RegistryCredentials
from ._models_py3 import RegistryInfo
from ._models_py3 import Replica
from ._models_py3 import ReplicaCollection
from ._models_py3 import ReplicaContainer
from ._models_py3 import Resource
from ._models_py3 import Revision
from ._models_py3 import RevisionCollection
from ._models_py3 import Scale
from ._models_py3 import ScaleRule
from ._models_py3 import ScaleRuleAuth
from ._models_py3 import Secret
from ._models_py3 import SecretsCollection
from ._models_py3 import SourceControl
from ._models_py3 import SourceControlCollection
from ._models_py3 import SystemData
from ._models_py3 import TcpScaleRule
from ._models_py3 import Template
from ._models_py3 import TrackedResource
from ._models_py3 import TrafficWeight
from ._models_py3 import Twitter
from ._models_py3 import TwitterRegistration
from ._models_py3 import UserAssignedIdentity
from ._models_py3 import VnetConfiguration
from ._models_py3 import Volume
from ._models_py3 import VolumeMount
from ._models_py3 import WorkloadProfile
from ._models_py3 import WorkloadProfileStates
from ._models_py3 import WorkloadProfileStatesCollection
from ._models_py3 import WorkloadProfileStatesProperties

from ._container_apps_api_client_enums import AccessMode
from ._container_apps_api_client_enums import Action
from ._container_apps_api_client_enums import ActiveRevisionsMode
from ._container_apps_api_client_enums import AppProtocol
from ._container_apps_api_client_enums import Applicability
from ._container_apps_api_client_enums import BindingType
from ._container_apps_api_client_enums import Category
from ._container_apps_api_client_enums import CertificateProvisioningState
from ._container_apps_api_client_enums import CheckNameAvailabilityReason
from ._container_apps_api_client_enums import ConnectedEnvironmentProvisioningState
from ._container_apps_api_client_enums import ContainerAppProvisioningState
from ._container_apps_api_client_enums import CookieExpirationConvention
from ._container_apps_api_client_enums import CreatedByType
from ._container_apps_api_client_enums import DnsVerificationTestResult
from ._container_apps_api_client_enums import EnvironmentProvisioningState
from ._container_apps_api_client_enums import ExtendedLocationTypes
from ._container_apps_api_client_enums import ForwardProxyConvention
from ._container_apps_api_client_enums import IngressTransportMethod
from ._container_apps_api_client_enums import LogLevel
from ._container_apps_api_client_enums import ManagedEnvironmentOutBoundType
from ._container_apps_api_client_enums import ManagedServiceIdentityType
from ._container_apps_api_client_enums import RevisionHealthState
from ._container_apps_api_client_enums import RevisionProvisioningState
from ._container_apps_api_client_enums import Scheme
from ._container_apps_api_client_enums import SkuName
from ._container_apps_api_client_enums import SourceControlOperationState
from ._container_apps_api_client_enums import StorageType
from ._container_apps_api_client_enums import Type
from ._container_apps_api_client_enums import UnauthenticatedClientActionV2
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AllowedAudiencesValidation",
    "AllowedPrincipals",
    "AppLogsConfiguration",
    "AppRegistration",
    "Apple",
    "AppleRegistration",
    "AuthConfig",
    "AuthConfigCollection",
    "AuthPlatform",
    "AvailableOperations",
    "AvailableWorkloadProfile",
    "AvailableWorkloadProfileProperties",
    "AvailableWorkloadProfilesCollection",
    "AzureActiveDirectory",
    "AzureActiveDirectoryLogin",
    "AzureActiveDirectoryRegistration",
    "AzureActiveDirectoryValidation",
    "AzureCredentials",
    "AzureFileProperties",
    "AzureStaticWebApps",
    "AzureStaticWebAppsRegistration",
    "BaseContainer",
    "BillingMeter",
    "BillingMeterCollection",
    "BillingMeterProperties",
    "Certificate",
    "CertificateCollection",
    "CertificatePatch",
    "CertificateProperties",
    "CheckNameAvailabilityRequest",
    "CheckNameAvailabilityResponse",
    "ClientRegistration",
    "Configuration",
    "ConnectedEnvironment",
    "ConnectedEnvironmentCollection",
    "ConnectedEnvironmentStorage",
    "ConnectedEnvironmentStorageProperties",
    "ConnectedEnvironmentStoragesCollection",
    "Container",
    "ContainerApp",
    "ContainerAppAuthToken",
    "ContainerAppCollection",
    "ContainerAppProbe",
    "ContainerAppProbeHttpGet",
    "ContainerAppProbeHttpGetHttpHeadersItem",
    "ContainerAppProbeTcpSocket",
    "ContainerAppSecret",
    "ContainerResources",
    "CookieExpiration",
    "CustomDomain",
    "CustomDomainConfiguration",
    "CustomHostnameAnalysisResult",
    "CustomHostnameAnalysisResultCustomDomainVerificationFailureInfo",
    "CustomHostnameAnalysisResultCustomDomainVerificationFailureInfoDetailsItem",
    "CustomOpenIdConnectProvider",
    "CustomScaleRule",
    "Dapr",
    "DaprComponent",
    "DaprComponentsCollection",
    "DaprMetadata",
    "DaprSecret",
    "DaprSecretsCollection",
    "DefaultAuthorizationPolicy",
    "DefaultErrorResponse",
    "DefaultErrorResponseError",
    "DefaultErrorResponseErrorDetailsItem",
    "DiagnosticDataProviderMetadata",
    "DiagnosticDataProviderMetadataPropertyBagItem",
    "DiagnosticDataTableResponseColumn",
    "DiagnosticDataTableResponseObject",
    "DiagnosticRendering",
    "DiagnosticSupportTopic",
    "Diagnostics",
    "DiagnosticsCollection",
    "DiagnosticsDataApiResponse",
    "DiagnosticsDefinition",
    "DiagnosticsProperties",
    "DiagnosticsStatus",
    "EnvironmentAuthToken",
    "EnvironmentSkuProperties",
    "EnvironmentVar",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "ExtendedLocation",
    "Facebook",
    "ForwardProxy",
    "GitHub",
    "GithubActionConfiguration",
    "GlobalValidation",
    "Google",
    "HttpScaleRule",
    "HttpSettings",
    "HttpSettingsRoutes",
    "IdentityProviders",
    "Ingress",
    "InitContainer",
    "IpSecurityRestrictionRule",
    "JwtClaimChecks",
    "LogAnalyticsConfiguration",
    "Login",
    "LoginRoutes",
    "LoginScopes",
    "ManagedEnvironment",
    "ManagedEnvironmentOutboundSettings",
    "ManagedEnvironmentStorage",
    "ManagedEnvironmentStorageProperties",
    "ManagedEnvironmentStoragesCollection",
    "ManagedEnvironmentsCollection",
    "ManagedServiceIdentity",
    "Nonce",
    "OpenIdConnectClientCredential",
    "OpenIdConnectConfig",
    "OpenIdConnectLogin",
    "OpenIdConnectRegistration",
    "OperationDetail",
    "OperationDisplay",
    "ProxyResource",
    "QueueScaleRule",
    "RegistryCredentials",
    "RegistryInfo",
    "Replica",
    "ReplicaCollection",
    "ReplicaContainer",
    "Resource",
    "Revision",
    "RevisionCollection",
    "Scale",
    "ScaleRule",
    "ScaleRuleAuth",
    "Secret",
    "SecretsCollection",
    "SourceControl",
    "SourceControlCollection",
    "SystemData",
    "TcpScaleRule",
    "Template",
    "TrackedResource",
    "TrafficWeight",
    "Twitter",
    "TwitterRegistration",
    "UserAssignedIdentity",
    "VnetConfiguration",
    "Volume",
    "VolumeMount",
    "WorkloadProfile",
    "WorkloadProfileStates",
    "WorkloadProfileStatesCollection",
    "WorkloadProfileStatesProperties",
    "AccessMode",
    "Action",
    "ActiveRevisionsMode",
    "AppProtocol",
    "Applicability",
    "BindingType",
    "Category",
    "CertificateProvisioningState",
    "CheckNameAvailabilityReason",
    "ConnectedEnvironmentProvisioningState",
    "ContainerAppProvisioningState",
    "CookieExpirationConvention",
    "CreatedByType",
    "DnsVerificationTestResult",
    "EnvironmentProvisioningState",
    "ExtendedLocationTypes",
    "ForwardProxyConvention",
    "IngressTransportMethod",
    "LogLevel",
    "ManagedEnvironmentOutBoundType",
    "ManagedServiceIdentityType",
    "RevisionHealthState",
    "RevisionProvisioningState",
    "Scheme",
    "SkuName",
    "SourceControlOperationState",
    "StorageType",
    "Type",
    "UnauthenticatedClientActionV2",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
