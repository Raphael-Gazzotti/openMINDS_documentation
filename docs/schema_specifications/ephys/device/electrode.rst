#########
Electrode
#########

:Semantic name: https://openminds.om-i.org/types/Electrode

:Display as: Electrode

Structured information on an electrode.


------------

------------

Properties
##########

:Required: `deviceType <deviceType_heading_>`_, `name <name_heading_>`_
:Optional: `conductorMaterial <conductorMaterial_heading_>`_, `description <description_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `insulatorMaterial <insulatorMaterial_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `intrinsicResistance <intrinsicResistance_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `manufacturer <manufacturer_heading_>`_, `owner <owner_heading_>`_, `serialNumber <serialNumber_heading_>`_

------------

.. _conductorMaterial_heading:

*****************
conductorMaterial
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/conductorMaterial
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/chemicals/chemicalMixture.html>`_, `ChemicalSubstance <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/chemicals/chemicalSubstance.html>`_ or `MolecularEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/molecularEntity.html>`_
   :instructions: Add the conductor material of this electrode.

`BACK TO TOP <Electrode_>`_

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

`BACK TO TOP <Electrode_>`_

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

`BACK TO TOP <Electrode_>`_

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

`BACK TO TOP <Electrode_>`_

------------

.. _insulatorMaterial_heading:

*****************
insulatorMaterial
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/insulatorMaterial
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/chemicals/chemicalMixture.html>`_, `ChemicalSubstance <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/chemicals/chemicalSubstance.html>`_ or `MolecularEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/molecularEntity.html>`_
   :instructions: Add the insulator material of this electrode.

`BACK TO TOP <Electrode_>`_

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
   :instructions: Enter the identifier (or label) of this electrode that is used within the corresponding data files to identify this electrode.

`BACK TO TOP <Electrode_>`_

------------

.. _intrinsicResistance_heading:

*******************
intrinsicResistance
*******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/intrinsicResistance
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the intrinsic resistance of this electrode.

`BACK TO TOP <Electrode_>`_

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

`BACK TO TOP <Electrode_>`_

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

`BACK TO TOP <Electrode_>`_

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

`BACK TO TOP <Electrode_>`_

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

`BACK TO TOP <Electrode_>`_

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

`BACK TO TOP <Electrode_>`_

------------

