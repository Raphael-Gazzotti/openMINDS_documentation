#######
MRICoil
#######

:Semantic name: https://openminds.om-i.org/types/MRICoil

:Display as: Mricoil


------------

------------

Properties
##########

:Required: `contribution <contribution_heading_>`_, `elementCount <elementCount_heading_>`_, `mountingType <mountingType_heading_>`_, `name <name_heading_>`_, `type <type_heading_>`_
:Optional: `description <description_heading_>`_, `intendedMountingLocation <intendedMountingLocation_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `serialNumber <serialNumber_heading_>`_

------------

.. _contribution_heading:

************
contribution
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/contribution
   :value type: | linked object array \(1-N\) of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html>`_
   :instructions: Add all relevant contributions (e.g., ownership, maintenance) for this device.

`BACK TO TOP <MRICoil_>`_

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
   :instructions: Enter a short description of the device. Describe the device itself for a custom-built device or note device-specific peculiarities or deviations from the standard product for a manufacturer-defined device.

`BACK TO TOP <MRICoil_>`_

------------

.. _elementCount_heading:

************
elementCount
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/elementCount
   :value type: integer
   :instructions: Enter the total number of coil elements.

`BACK TO TOP <MRICoil_>`_

------------

.. _intendedMountingLocation_heading:

************************
intendedMountingLocation
************************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/intendedMountingLocation
   :value type: | linked object of type
                | `ExternalBodyRegion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/externalBodyRegion.html>`_
   :instructions: Add the mounting location intended by the manufacturer (e.g., head, neck, knee).

`BACK TO TOP <MRICoil_>`_

------------

.. _internalIdentifier_heading:

******************
internalIdentifier
******************

Term or code that identifies someone or something within a particular product.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/internalIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier (or label) of this device that is used by the owner to identify or reference this device.

`BACK TO TOP <MRICoil_>`_

------------

.. _mountingType_heading:

************
mountingType
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/mountingType
   :value type: | linked object of type
                | `DeviceMountingType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/deviceMountingType.html>`_
   :instructions: Add the coil mounting type (e.g., built-in, external, interventional, wearable).

`BACK TO TOP <MRICoil_>`_

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
   :instructions: Enter a descriptive name for this device, preferably defined by the owner.

`BACK TO TOP <MRICoil_>`_

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

`BACK TO TOP <MRICoil_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/type
   :value type: | linked object of type
                | `DeviceType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/deviceType.html>`_ or `HardwareProduct <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/hardwareProduct.html>`_
   :instructions: Add the device classification reference. Identify a device type for a custom-built device, or a hardware product for a device corresponding to a manufacturer-defined product model.

`BACK TO TOP <MRICoil_>`_

------------

