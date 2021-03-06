# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, Optional, Union

import msrest.serialization

from ._cpim_configuration_client_enums import *


class AsyncOperationStatus(msrest.serialization.Model):
    """The async operation status.

    :param subscription_id: Subscription ID that the resource belongs to.
    :type subscription_id: str
    :param id: The GET resource path for the operation.
    :type id: str
    :param name: The operation ID.
    :type name: str
    :param status: The status of the operation. Possible values include: "Succeeded", "Pending",
     "Failed".
    :type status: str or ~$(python-base-namespace).v2019_01_01_preview.models.StatusType
    :param start_time: Start time of the async operation.
    :type start_time: str
    :param end_time: End time of the async operation.
    :type end_time: str
    :param error: Error response if async operation failed.
    :type error: ~$(python-base-namespace).v2019_01_01_preview.models.AsyncOperationStatusError
    :param billing_config: The billing configuration for the tenant.
    :type billing_config: ~$(python-base-
     namespace).v2019_01_01_preview.models.B2CTenantResourcePropertiesBillingConfig
    :param tenant_id: An identifier of the B2C tenant.
    :type tenant_id: str
    """

    _attribute_map = {
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'str'},
        'end_time': {'key': 'endTime', 'type': 'str'},
        'error': {'key': 'error', 'type': 'AsyncOperationStatusError'},
        'billing_config': {'key': 'properties.billingConfig', 'type': 'B2CTenantResourcePropertiesBillingConfig'},
        'tenant_id': {'key': 'properties.tenantId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        subscription_id: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        status: Optional[Union[str, "StatusType"]] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        error: Optional["AsyncOperationStatusError"] = None,
        billing_config: Optional["B2CTenantResourcePropertiesBillingConfig"] = None,
        tenant_id: Optional[str] = None,
        **kwargs
    ):
        super(AsyncOperationStatus, self).__init__(**kwargs)
        self.subscription_id = subscription_id
        self.id = id
        self.name = name
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.error = error
        self.billing_config = billing_config
        self.tenant_id = tenant_id


class AsyncOperationStatusError(msrest.serialization.Model):
    """Error response if async operation failed.

    :param code: Error code.
    :type code: str
    :param message: Error message.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(AsyncOperationStatusError, self).__init__(**kwargs)
        self.code = code
        self.message = message


class B2CResourceSKU(msrest.serialization.Model):
    """SKU properties of the Azure AD B2C tenant. Learn more about Azure AD B2C billing at `aka.ms/b2cBilling <https://aka.ms/b2cBilling>`_.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param name: The name of the SKU for the tenant. Possible values include: "Standard",
     "PremiumP1", "PremiumP2".
    :type name: str or ~$(python-base-namespace).v2019_01_01_preview.models.B2CResourceSKUName
    :ivar tier: The tier of the tenant. Default value: "A0".
    :vartype tier: str
    """

    _validation = {
        'tier': {'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    tier = "A0"

    def __init__(
        self,
        *,
        name: Optional[Union[str, "B2CResourceSKUName"]] = None,
        **kwargs
    ):
        super(B2CResourceSKU, self).__init__(**kwargs)
        self.name = name


class B2CTenantResource(msrest.serialization.Model):
    """B2CTenantResource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar type: The type of the B2C tenant resource. Default value:
     "Microsoft.AzureActiveDirectory/b2cDirectories".
    :vartype type: str
    :param sku: Required. SKU properties of the Azure AD B2C tenant. Learn more about Azure AD B2C
     billing at `aka.ms/b2cBilling <https://aka.ms/b2cBilling>`_.
    :type sku: ~$(python-base-namespace).v2019_01_01_preview.models.B2CResourceSKU
    :ivar id: An identifier that represents the B2C tenant resource.
    :vartype id: str
    :ivar name: The name of the B2C tenant resource.
    :vartype name: str
    :param location: Required. The location in which the resource is hosted and data resides. Refer
     to `this documentation <https://aka.ms/B2CDataResidency>`_ to see valid data residency
     locations. Please choose one of 'United States', 'Europe', and 'Asia Pacific'.
    :type location: str
    :param tags: A set of tags. Resource Tags.
    :type tags: dict[str, str]
    :param billing_config: The billing configuration for the tenant.
    :type billing_config: ~$(python-base-
     namespace).v2019_01_01_preview.models.B2CTenantResourcePropertiesBillingConfig
    :param tenant_id: An identifier of the B2C tenant.
    :type tenant_id: str
    """

    _validation = {
        'type': {'readonly': True, 'constant': True},
        'sku': {'required': True},
        'id': {'readonly': True},
        'name': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'B2CResourceSKU'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'billing_config': {'key': 'properties.billingConfig', 'type': 'B2CTenantResourcePropertiesBillingConfig'},
        'tenant_id': {'key': 'properties.tenantId', 'type': 'str'},
    }

    type = "Microsoft.AzureActiveDirectory/b2cDirectories"

    def __init__(
        self,
        *,
        sku: "B2CResourceSKU",
        location: str,
        tags: Optional[Dict[str, str]] = None,
        billing_config: Optional["B2CTenantResourcePropertiesBillingConfig"] = None,
        tenant_id: Optional[str] = None,
        **kwargs
    ):
        super(B2CTenantResource, self).__init__(**kwargs)
        self.type = None
        self.sku = sku
        self.id = None
        self.name = None
        self.location = location
        self.tags = tags
        self.billing_config = billing_config
        self.tenant_id = tenant_id


class B2CTenantResourceList(msrest.serialization.Model):
    """The collection of Azure AD B2C tenant resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of guest usages resources.
    :vartype value: list[~$(python-base-namespace).v2019_01_01_preview.models.B2CTenantResource]
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[B2CTenantResource]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(B2CTenantResourceList, self).__init__(**kwargs)
        self.value = None


class B2CTenantResourcePropertiesBillingConfig(msrest.serialization.Model):
    """The billing configuration for the tenant.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param billing_type: The type of billing. Will be MAU for all new customers. If 'Auths', it can
     be updated to 'MAU'. Cannot be changed if value is 'MAU'. Learn more about Azure AD B2C billing
     at `aka.ms/b2cBilling <https://aka.ms/b2cbilling>`_. Possible values include: "MAU", "Auths".
    :type billing_type: str or ~$(python-base-namespace).v2019_01_01_preview.models.BillingType
    :ivar effective_start_date_utc: The data from which the billing type took effect.
    :vartype effective_start_date_utc: str
    """

    _validation = {
        'effective_start_date_utc': {'readonly': True},
    }

    _attribute_map = {
        'billing_type': {'key': 'billingType', 'type': 'str'},
        'effective_start_date_utc': {'key': 'effectiveStartDateUtc', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        billing_type: Optional[Union[str, "BillingType"]] = None,
        **kwargs
    ):
        super(B2CTenantResourcePropertiesBillingConfig, self).__init__(**kwargs)
        self.billing_type = billing_type
        self.effective_start_date_utc = None


class B2CTenantUpdateRequest(msrest.serialization.Model):
    """The request body to update the Azure AD B2C tenant resource.

    :param sku: SKU properties of the Azure AD B2C tenant. Learn more about Azure AD B2C billing at
     `aka.ms/b2cBilling <https://aka.ms/b2cBilling>`_.
    :type sku: ~$(python-base-namespace).v2019_01_01_preview.models.B2CResourceSKU
    :param tags: A set of tags. Resource Tags.
    :type tags: dict[str, str]
    :param billing_config: The billing configuration for the tenant.
    :type billing_config: ~$(python-base-
     namespace).v2019_01_01_preview.models.B2CTenantResourcePropertiesBillingConfig
    :param tenant_id: An identifier of the B2C tenant.
    :type tenant_id: str
    """

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'B2CResourceSKU'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'billing_config': {'key': 'properties.billingConfig', 'type': 'B2CTenantResourcePropertiesBillingConfig'},
        'tenant_id': {'key': 'properties.tenantId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        sku: Optional["B2CResourceSKU"] = None,
        tags: Optional[Dict[str, str]] = None,
        billing_config: Optional["B2CTenantResourcePropertiesBillingConfig"] = None,
        tenant_id: Optional[str] = None,
        **kwargs
    ):
        super(B2CTenantUpdateRequest, self).__init__(**kwargs)
        self.sku = sku
        self.tags = tags
        self.billing_config = billing_config
        self.tenant_id = tenant_id


class CheckNameAvailabilityRequestBody(msrest.serialization.Model):
    """The information required to check the availability of the name for the tenant.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The domain name to check for availability.
    :type name: str
    :param country_code: Required. Country code of Azure tenant (e.g. 'US'). Refer to
     `aka.ms/B2CDataResidency <https://aka.ms/B2CDataResidency>`_ to see valid country codes and
     corresponding data residency locations. If you do not see a country code in an valid data
     residency location, choose one from the list.
    :type country_code: str
    """

    _validation = {
        'name': {'required': True},
        'country_code': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        country_code: str,
        **kwargs
    ):
        super(CheckNameAvailabilityRequestBody, self).__init__(**kwargs)
        self.name = name
        self.country_code = country_code


class CreateTenantRequestBody(msrest.serialization.Model):
    """The information needed to create the Azure AD B2C tenant and corresponding Azure resource, which is used for billing purposes.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. The location in which the resource is hosted and data resides. Refer
     to `this documentation <https://aka.ms/B2CDataResidency>`_ to see valid data residency
     locations. Please choose one of 'United States', 'Europe', and 'Asia Pacific'.
    :type location: str
    :param properties: Required.
    :type properties: ~$(python-base-
     namespace).v2019_01_01_preview.models.CreateTenantRequestBodyProperties
    :param sku: Required. SKU properties of the Azure AD B2C tenant. Learn more about Azure AD B2C
     billing at `aka.ms/b2cBilling <https://aka.ms/b2cBilling>`_.
    :type sku: ~$(python-base-namespace).v2019_01_01_preview.models.B2CResourceSKU
    :param tags: A set of tags. Resource Tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'location': {'required': True},
        'properties': {'required': True},
        'sku': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'CreateTenantRequestBodyProperties'},
        'sku': {'key': 'sku', 'type': 'B2CResourceSKU'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        location: str,
        properties: "CreateTenantRequestBodyProperties",
        sku: "B2CResourceSKU",
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(CreateTenantRequestBody, self).__init__(**kwargs)
        self.location = location
        self.properties = properties
        self.sku = sku
        self.tags = tags


class CreateTenantRequestBodyProperties(msrest.serialization.Model):
    """CreateTenantRequestBodyProperties.

    :param display_name: The display name of the B2C tenant.
    :type display_name: str
    :param country_code: Country code of Azure tenant (e.g. 'US'). Refer to
     `aka.ms/B2CDataResidency <https://aka.ms/B2CDataResidency>`_ to see valid country codes and
     corresponding data residency locations. If you do not see a country code in an valid data
     residency location, choose one from the list.
    :type country_code: str
    """

    _attribute_map = {
        'display_name': {'key': 'createTenantProperties.displayName', 'type': 'str'},
        'country_code': {'key': 'createTenantProperties.countryCode', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        display_name: Optional[str] = None,
        country_code: Optional[str] = None,
        **kwargs
    ):
        super(CreateTenantRequestBodyProperties, self).__init__(**kwargs)
        self.display_name = display_name
        self.country_code = country_code


class ErrorAdditionalInfo(msrest.serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: object
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorResponse(msrest.serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~$(python-base-namespace).v2019_01_01_preview.models.ErrorResponse]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~$(python-base-
     namespace).v2019_01_01_preview.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorResponse]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class NameAvailabilityResponse(msrest.serialization.Model):
    """Response of the CheckNameAvailability operation.

    :param message: Description of the reason if name is not available.
    :type message: str
    :param name_available: True if the name is available and can be used to create a new tenant.
     Otherwise false.
    :type name_available: bool
    :param reason: Describes the reason for the 'nameAvailable' value. Possible values include:
     "AlreadyExists", "Invalid".
    :type reason: str or ~$(python-base-
     namespace).v2019_01_01_preview.models.NameAvailabilityReasonType
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        message: Optional[str] = None,
        name_available: Optional[bool] = None,
        reason: Optional[Union[str, "NameAvailabilityReasonType"]] = None,
        **kwargs
    ):
        super(NameAvailabilityResponse, self).__init__(**kwargs)
        self.message = message
        self.name_available = name_available
        self.reason = reason


class Operation(msrest.serialization.Model):
    """Microsoft.AzureActiveDirectory REST API operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Operation name: {provider}/{resource}/{operation}.
    :vartype name: str
    :param display: The object that represents the operation.
    :type display: ~$(python-base-namespace).v2019_01_01_preview.models.OperationDisplay
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(
        self,
        *,
        display: Optional["OperationDisplay"] = None,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = display


class OperationDisplay(msrest.serialization.Model):
    """The object that represents the operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provider: Service provider: Microsoft.AzureActiveDirectory.
    :vartype provider: str
    :ivar resource: Resource on which the operation is performed: GuestUsages, etc.
    :vartype resource: str
    :ivar operation: Operation type: Read, write, delete, etc.
    :vartype operation: str
    :param description: Friendly name of the operation.
    :type description: str
    """

    _validation = {
        'provider': {'readonly': True},
        'resource': {'readonly': True},
        'operation': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        description: Optional[str] = None,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None
        self.description = description


class OperationListResult(msrest.serialization.Model):
    """Result of listing operations for the resourceProvider.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of cpim service operations supported by the Microsoft.AzureActiveDirectory
     resource provider.
    :vartype value: list[~$(python-base-namespace).v2019_01_01_preview.models.Operation]
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = None
