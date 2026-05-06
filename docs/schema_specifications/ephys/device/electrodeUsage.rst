##############
ElectrodeUsage
##############

:Semantic name: https://openminds.om-i.org/types/ElectrodeUsage

:Display as: Electrode usage


------------

------------

Properties
##########

:Required: `device <device_heading_>`_
:Optional: `anatomicalLocation <anatomicalLocation_heading_>`_, `contactResistance <contactResistance_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `metadataLocation <metadataLocation_heading_>`_, `spatialLocation <spatialLocation_heading_>`_, `usedSpecimen <usedSpecimen_heading_>`_

------------

.. _anatomicalLocation_heading:

******************
anatomicalLocation
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/anatomicalLocation
   :value type: | linked object of type
                | `CellType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/cellType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/organ.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/organismSubstance.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/subcellularEntity.html>`_, `UBERONParcellation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/UBERONParcellation.html>`_, `CustomAnatomicalEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/non-atlas/customAnatomicalEntity.html>`_, `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntity.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add the anatomical entity that semantically best describes the anatomical location of the electrode contact.

`BACK TO TOP <ElectrodeUsage_>`_

------------

.. _contactResistance_heading:

*****************
contactResistance
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/contactResistance
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the contact resistance of this electrode during its use.

`BACK TO TOP <ElectrodeUsage_>`_

------------

.. _device_heading:

******
device
******

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/device
   :value type: | linked object of type
                | `Electrode <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/electrode.html>`_
   :instructions: Add the electrode used.

`BACK TO TOP <ElectrodeUsage_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this device usage that may help you to find this instance more easily.

`BACK TO TOP <ElectrodeUsage_>`_

------------

.. _metadataLocation_heading:

****************
metadataLocation
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/metadataLocation
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/file.html>`_ or `FileBundle <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/fileBundle.html>`_
   :instructions: Add all files or file bundles containing additional information about the usage of this device.

`BACK TO TOP <ElectrodeUsage_>`_

------------

.. _spatialLocation_heading:

***************
spatialLocation
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/spatialLocation
   :value type: | embedded object of type
                | `CoordinatePoint <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/miscellaneous/coordinatePoint.html>`_
   :instructions: Add the coordinate point that best describes the spatial location of the electrode contact during its use.

`BACK TO TOP <ElectrodeUsage_>`_

------------

.. _usedSpecimen_heading:

************
usedSpecimen
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/usedSpecimen
   :value type: | linked object of type
                | `SubjectState <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/subjectState.html>`_ or `TissueSampleState <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/tissueSampleState.html>`_
   :instructions: Add the state of the tissue sample or subject that this device was used on.

`BACK TO TOP <ElectrodeUsage_>`_

------------

