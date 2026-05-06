##############
ElectrodeArray
##############

:Semantic name: https://openminds.om-i.org/types/ElectrodeArray

:Display as: Electrode array

Structured information on an electrode array.


------------

------------

Properties
##########

:Required: `contribution <contribution_heading_>`_, `electrodeIdentifier <electrodeIdentifier_heading_>`_, `name <name_heading_>`_, `numberOfElectrodes <numberOfElectrodes_heading_>`_, `type <type_heading_>`_
:Optional: `conductorMaterial <conductorMaterial_heading_>`_, `description <description_heading_>`_, `insulatorMaterial <insulatorMaterial_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `intrinsicResistance <intrinsicResistance_heading_>`_, `serialNumber <serialNumber_heading_>`_

------------

.. _conductorMaterial_heading:

*****************
conductorMaterial
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/conductorMaterial
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/chemicals/chemicalMixture.html>`_, `ChemicalSubstance <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/chemicals/chemicalSubstance.html>`_ or `MolecularEntity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/molecularEntity.html>`_
   :instructions: Add the conductor material of this electrode array.

`BACK TO TOP <ElectrodeArray_>`_

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

`BACK TO TOP <ElectrodeArray_>`_

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

`BACK TO TOP <ElectrodeArray_>`_

------------

.. _electrodeIdentifier_heading:

*******************
electrodeIdentifier
*******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/electrodeIdentifier
   :value type: | string array \(2-N\)
                | formatting: text/plain; singleline
   :instructions: Enter the identifiers for each electrode of this electrode array. Note that the number of identifiers should match the number of electrodes of the array as stated under 'numberOfElectrodes'.

`BACK TO TOP <ElectrodeArray_>`_

------------

.. _insulatorMaterial_heading:

*****************
insulatorMaterial
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/insulatorMaterial
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/chemicals/chemicalMixture.html>`_, `ChemicalSubstance <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/chemicals/chemicalSubstance.html>`_ or `MolecularEntity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/molecularEntity.html>`_
   :instructions: Add the insulator material of this electrode array.

`BACK TO TOP <ElectrodeArray_>`_

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
   :instructions: Enter the identifier (or label) of this electrode array that is used within the corresponding data files to identify this electrode array.

`BACK TO TOP <ElectrodeArray_>`_

------------

.. _intrinsicResistance_heading:

*******************
intrinsicResistance
*******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/intrinsicResistance
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the intrinsic resistance of this electrode array.

`BACK TO TOP <ElectrodeArray_>`_

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

`BACK TO TOP <ElectrodeArray_>`_

------------

.. _numberOfElectrodes_heading:

******************
numberOfElectrodes
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/numberOfElectrodes
   :value type: integer
   :instructions: Enter the number of electrodes that belong to this electrode array.

`BACK TO TOP <ElectrodeArray_>`_

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

`BACK TO TOP <ElectrodeArray_>`_

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

`BACK TO TOP <ElectrodeArray_>`_

------------

