##################
AccountInformation
##################

:Semantic name: https://openminds.om-i.org/types/AccountInformation

:Display as: Account information

Structured information about a user account for a web service.


------------

------------

Properties
##########

:Required: `service <service_heading_>`_, `userName <userName_heading_>`_
:Optional:

------------

.. _service_heading:

*******
service
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/service
   :value type: | linked object of type
                | `WebService <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/webService.html>`_
   :instructions: Add the web service of this account.

`BACK TO TOP <AccountInformation_>`_

------------

.. _userName_heading:

********
userName
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/userName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the user name for this account.

`BACK TO TOP <AccountInformation_>`_

------------

