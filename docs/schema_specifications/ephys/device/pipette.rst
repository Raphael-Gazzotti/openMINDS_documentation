#######
Pipette
#######

:Semantic name: https://openminds.om-i.org/types/Pipette

:Display as: Pipette


------------

------------

Properties
##########

:Required: `deviceType <deviceType_heading_>`_, `name <name_heading_>`_
:Optional: `description <description_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `externalDiameter <externalDiameter_heading_>`_, `internalDiameter <internalDiameter_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `manufacturer <manufacturer_heading_>`_, `material <material_heading_>`_, `owner <owner_heading_>`_, `serialNumber <serialNumber_heading_>`_

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

`BACK TO TOP <Pipette_>`_

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

`BACK TO TOP <Pipette_>`_

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

`BACK TO TOP <Pipette_>`_

------------

.. _externalDiameter_heading:

****************
externalDiameter
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/externalDiameter
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the external diameter of the pipette.

`BACK TO TOP <Pipette_>`_

------------

.. _internalDiameter_heading:

****************
internalDiameter
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/internalDiameter
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the internal diameter of the pipette.

`BACK TO TOP <Pipette_>`_

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
   :instructions: Enter the identifier (or label) of this pipette that is used within the corresponding data files to identify this pipette.

`BACK TO TOP <Pipette_>`_

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

`BACK TO TOP <Pipette_>`_

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

`BACK TO TOP <Pipette_>`_

------------

.. _material_heading:

********
material
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/material
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/chemicals/chemicalMixture.html>`_, `ChemicalSubstance <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/chemicals/chemicalSubstance.html>`_ or `MolecularEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/molecularEntity.html>`_
   :instructions: Add the material that the pipette is made of.

`BACK TO TOP <Pipette_>`_

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

`BACK TO TOP <Pipette_>`_

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

`BACK TO TOP <Pipette_>`_

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

`BACK TO TOP <Pipette_>`_

------------

