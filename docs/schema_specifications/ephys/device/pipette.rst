#######
Pipette
#######

:Semantic name: https://openminds.om-i.org/types/Pipette

:Display as: Pipette


------------

------------

Properties
##########

:Required: `contribution <contribution_heading_>`_, `name <name_heading_>`_, `type <type_heading_>`_
:Optional: `description <description_heading_>`_, `externalDiameter <externalDiameter_heading_>`_, `internalDiameter <internalDiameter_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `material <material_heading_>`_, `serialNumber <serialNumber_heading_>`_

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

`BACK TO TOP <Pipette_>`_

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

`BACK TO TOP <Pipette_>`_

------------

.. _externalDiameter_heading:

****************
externalDiameter
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/externalDiameter
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
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
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
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

.. _material_heading:

********
material
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/material
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/chemicals/chemicalMixture.html>`_, `ChemicalSubstance <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/chemicals/chemicalSubstance.html>`_ or `MolecularEntity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/molecularEntity.html>`_
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
   :instructions: Enter a descriptive name for this device, preferably defined by the owner.

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

`BACK TO TOP <Pipette_>`_

------------

