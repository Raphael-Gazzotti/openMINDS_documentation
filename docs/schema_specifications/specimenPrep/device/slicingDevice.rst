#############
SlicingDevice
#############

:Semantic name: https://openminds.om-i.org/types/SlicingDevice

:Display as: Slicing device


------------

------------

Properties
##########

:Required: `deviceType <deviceType_heading_>`_, `name <name_heading_>`_
:Optional: `description <description_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `manufacturer <manufacturer_heading_>`_, `owner <owner_heading_>`_, `serialNumber <serialNumber_heading_>`_

------------

.. _description_heading:

***********
description
***********

Longer statement or account giving the characteristics of someone or something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/description
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a short text describing this device.

`BACK TO TOP <SlicingDevice_>`_

------------

.. _deviceType_heading:

**********
deviceType
**********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/deviceType
   :value type: | linked object of type
                | `DeviceType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/deviceType.html>`_
   :instructions: Add the type of this device.

`BACK TO TOP <SlicingDevice_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/digitalIdentifier
   :value type: | linked object of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/DOI.html>`_ or `RRID <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/RRID.html>`_
   :instructions: Add the globally unique and persistent digital identifier of this device.

`BACK TO TOP <SlicingDevice_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this device that may help you to find this instance more easily.

`BACK TO TOP <SlicingDevice_>`_

------------

.. _manufacturer_heading:

************
manufacturer
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/manufacturer
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add the manufacturer (private or industrial) that constructed this device.

`BACK TO TOP <SlicingDevice_>`_

------------

.. _name_heading:

****
name
****

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive name for this device, preferably including the model name as defined by the manufacturer.

`BACK TO TOP <SlicingDevice_>`_

------------

.. _owner_heading:

*****
owner
*****

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/owner
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add all parties that legally own this device.

`BACK TO TOP <SlicingDevice_>`_

------------

.. _serialNumber_heading:

************
serialNumber
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/serialNumber
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the serial number of this device.

`BACK TO TOP <SlicingDevice_>`_

------------

