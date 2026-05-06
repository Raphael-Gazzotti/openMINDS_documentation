###################
ElectrodeArrayUsage
###################

:Semantic name: https://openminds.om-i.org/types/ElectrodeArrayUsage

:Display as: Electrode array usage


------------

------------

Properties
##########

:Required: `device <device_heading_>`_
:Optional: `anatomicalLocationOfArray <anatomicalLocationOfArray_heading_>`_, `anatomicalLocationOfElectrodes <anatomicalLocationOfElectrodes_heading_>`_, `contactResistances <contactResistances_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `metadataLocation <metadataLocation_heading_>`_, `spatialLocationOfElectrodes <spatialLocationOfElectrodes_heading_>`_, `usedElectrode <usedElectrode_heading_>`_, `usedSpecimen <usedSpecimen_heading_>`_

------------

.. _anatomicalLocationOfArray_heading:

*************************
anatomicalLocationOfArray
*************************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/anatomicalLocationOfArray
   :value type: | linked object array \(1-N\) of type
                | `CellType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/cellType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/organ.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/organismSubstance.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/subcellularEntity.html>`_, `UBERONParcellation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/UBERONParcellation.html>`_, `CustomAnatomicalEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/non-atlas/customAnatomicalEntity.html>`_, `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntity.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add all anatomical entities that semantically best describe the overall anatomical location of the electrode array.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _anatomicalLocationOfElectrodes_heading:

******************************
anatomicalLocationOfElectrodes
******************************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/anatomicalLocationOfElectrodes
   :value type: | linked object array \(2-N\) of type
                | `CellType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/cellType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/organ.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/organismSubstance.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/subcellularEntity.html>`_, `UBERONParcellation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/UBERONParcellation.html>`_, `CustomAnatomicalEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/non-atlas/customAnatomicalEntity.html>`_, `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntity.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add all anatomical entities that semantically best describe the anatomical location of each electrode contact of this array during its use, in the same order that the electrode identifiers for this electrode array have been specified.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _contactResistances_heading:

******************
contactResistances
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/contactResistances
   :value type: | embedded object array \(2-N\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the contact resistance for each electrode of this array during its use, in the same order that the electrode identifiers for this electrode array have been specified.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _device_heading:

******
device
******

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/device
   :value type: | linked object of type
                | `ElectrodeArray <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/electrodeArray.html>`_
   :instructions: Add the electrode array used.

`BACK TO TOP <ElectrodeArrayUsage_>`_

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

`BACK TO TOP <ElectrodeArrayUsage_>`_

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

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _spatialLocationOfElectrodes_heading:

***************************
spatialLocationOfElectrodes
***************************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/spatialLocationOfElectrodes
   :value type: | embedded object array \(2-N\) of type
                | `CoordinatePoint <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/miscellaneous/coordinatePoint.html>`_
   :instructions: Add all coordinate points that best describe the spatial location of each electrode contact of this array during its use, in the same order that the electrode identifiers for this electrode array have been specified.

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

.. _usedElectrode_heading:

*************
usedElectrode
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/usedElectrode
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter the identifiers of all electrodes that are actually in use for this array.

`BACK TO TOP <ElectrodeArrayUsage_>`_

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

`BACK TO TOP <ElectrodeArrayUsage_>`_

------------

