#####
Setup
#####

:Semantic name: https://openminds.om-i.org/types/Setup

:Display as: Setup


------------

------------

Properties
##########

:Required: `description <description_heading_>`_, `hasPart <hasPart_heading_>`_, `name <name_heading_>`_
:Optional: `location <location_heading_>`_, `manufacturer <manufacturer_heading_>`_, `type <type_heading_>`_

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
   :instructions: Enter a short text describing this setup.

`BACK TO TOP <Setup_>`_

------------

.. _hasPart_heading:

*******
hasPart
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/hasPart
   :value type: | linked object array \(2-N\) of type
                | `Setup <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/setup.html>`_, `SoftwareVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/softwareVersion.html>`_, `Electrode <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/electrode.html>`_, `ElectrodeArray <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/electrodeArray.html>`_, `Pipette <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/pipette.html>`_ or `SlicingDevice <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/specimenPrep/device/slicingDevice.html>`_
   :instructions: Add all components, including other setups, that are part of this setup. Note that a setup should not be only composed of software.

`BACK TO TOP <Setup_>`_

------------

.. _location_heading:

********
location
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/location
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the geographic location of this setup. This may include room number, building, institution and/or city.

`BACK TO TOP <Setup_>`_

------------

.. _manufacturer_heading:

************
manufacturer
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/manufacturer
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add the manufacturer (private or industrial) that constructed this setup.

`BACK TO TOP <Setup_>`_

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
   :instructions: Enter a descriptive name for this setup.

`BACK TO TOP <Setup_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/type
   :value type: | linked object array \(1-N\) of type
                | `SetupType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/setupType.html>`_
   :instructions: Add all types that describe this setup.

`BACK TO TOP <Setup_>`_

------------

