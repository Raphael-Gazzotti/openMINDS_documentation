############
PipetteUsage
############

:Semantic name: https://openminds.om-i.org/types/PipetteUsage

:Display as: Pipette usage


------------

------------

Properties
##########

:Required: `device <device_heading_>`_, `pipetteSolution <pipetteSolution_heading_>`_
:Optional: `anatomicalLocation <anatomicalLocation_heading_>`_, `chlorideReversalPotential <chlorideReversalPotential_heading_>`_, `compensationCurrent <compensationCurrent_heading_>`_, `endMembranePotential <endMembranePotential_heading_>`_, `holdingPotential <holdingPotential_heading_>`_, `inputResistance <inputResistance_heading_>`_, `labelingCompound <labelingCompound_heading_>`_, `liquidJunctionPotential <liquidJunctionPotential_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `metadataLocation <metadataLocation_heading_>`_, `pipetteResistance <pipetteResistance_heading_>`_, `sealResistance <sealResistance_heading_>`_, `seriesResistance <seriesResistance_heading_>`_, `spatialLocation <spatialLocation_heading_>`_, `startMembranePotential <startMembranePotential_heading_>`_, `usedSpecimen <usedSpecimen_heading_>`_

------------

.. _anatomicalLocation_heading:

******************
anatomicalLocation
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/anatomicalLocation
   :value type: | linked object of type
                | `CellType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/cellType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/organ.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/organismSubstance.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/subcellularEntity.html>`_, `UBERONParcellation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/UBERONParcellation.html>`_, `CustomAnatomicalEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/non-atlas/customAnatomicalEntity.html>`_, `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntity.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add the anatomical entity that semantically best describes the anatomical location of the pipette tip.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _chlorideReversalPotential_heading:

*************************
chlorideReversalPotential
*************************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/chlorideReversalPotential
   :value type: | embedded object array \(1-N\) of type
                | `Measurement <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/measurement.html>`_
   :instructions: Enter all chloride reversal potentials for the intracellular solution(s) of the pipette measured during its use.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _compensationCurrent_heading:

*******************
compensationCurrent
*******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/compensationCurrent
   :value type: | embedded object of type
                | `Measurement <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/measurement.html>`_
   :instructions: Enter the compensation current for the series resistance of the pipette measured during its use.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _device_heading:

******
device
******

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/device
   :value type: | linked object of type
                | `Pipette <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/pipette.html>`_
   :instructions: Add the pipette used.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _endMembranePotential_heading:

********************
endMembranePotential
********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/endMembranePotential
   :value type: | embedded object of type
                | `Measurement <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/measurement.html>`_
   :instructions: Enter the membrane potential of e.g., a patched cell at the end of a recording measured during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _holdingPotential_heading:

****************
holdingPotential
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/holdingPotential
   :value type: | embedded object of type
                | `Measurement <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/measurement.html>`_
   :instructions: Enter the holding membrane potential of e.g., a patched cell measured during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _inputResistance_heading:

***************
inputResistance
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/inputResistance
   :value type: | embedded object of type
                | `Measurement <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/measurement.html>`_
   :instructions: Enter the input resistance of e.g., a patched cell measured during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _labelingCompound_heading:

****************
labelingCompound
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/labelingCompound
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/chemicals/chemicalMixture.html>`_, `ChemicalSubstance <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/chemicals/chemicalSubstance.html>`_ or `MolecularEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/molecularEntity.html>`_
   :instructions: Add the used compound for labelling e.g., a patched cell during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _liquidJunctionPotential_heading:

***********************
liquidJunctionPotential
***********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/liquidJunctionPotential
   :value type: | embedded object of type
                | `Measurement <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/measurement.html>`_
   :instructions: Enter the liquid junction potential of e.g., a patched cell measured during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

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

`BACK TO TOP <PipetteUsage_>`_

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

`BACK TO TOP <PipetteUsage_>`_

------------

.. _pipetteResistance_heading:

*****************
pipetteResistance
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/pipetteResistance
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the resistance of the pipette during its use.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _pipetteSolution_heading:

***************
pipetteSolution
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/pipetteSolution
   :value type: | linked object of type
                | `ChemicalMixture <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/chemicals/chemicalMixture.html>`_
   :instructions: Enter the solution with which the pipette was filled during its use.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _sealResistance_heading:

**************
sealResistance
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/sealResistance
   :value type: | embedded object of type
                | `Measurement <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/measurement.html>`_
   :instructions: Enter the seal resistance of e.g., a patched cell measured during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _seriesResistance_heading:

****************
seriesResistance
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/seriesResistance
   :value type: | embedded object of type
                | `Measurement <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/measurement.html>`_
   :instructions: Enter the series resistance of the pipette measured during its use.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _spatialLocation_heading:

***************
spatialLocation
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/spatialLocation
   :value type: | embedded object of type
                | `CoordinatePoint <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/miscellaneous/coordinatePoint.html>`_
   :instructions: Add the coordinate point that best describes the spatial location of the pipette tip during its use.

`BACK TO TOP <PipetteUsage_>`_

------------

.. _startMembranePotential_heading:

**********************
startMembranePotential
**********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/startMembranePotential
   :value type: | embedded object of type
                | `Measurement <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/measurement.html>`_
   :instructions: Enter the membrane potential of e.g., a patched cell at the beginning of a recording measured during the use of this pipette.

`BACK TO TOP <PipetteUsage_>`_

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

`BACK TO TOP <PipetteUsage_>`_

------------

