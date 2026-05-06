########################
AnatomicalTargetPosition
########################

:Semantic name: https://openminds.ebrains.eu/sands/AnatomicalTargetPosition

:Display as: Anatomical target position


------------

------------

Properties
##########

:Required: `anatomicalTarget <anatomicalTarget_heading_>`_, `targetIdentificationType <targetIdentificationType_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `spatialLocation <spatialLocation_heading_>`_

------------

.. _additionalRemarks_heading:

*****************
additionalRemarks
*****************

Mention of what deserves additional attention or notice.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/additionalRemarks
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter any additional remarks concerning this anatomical target position.

`BACK TO TOP <AnatomicalTargetPosition_>`_

------------

.. _anatomicalTarget_heading:

****************
anatomicalTarget
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anatomicalTarget
   :value type: | linked object array \(1-N\) of type
                | `CellType <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/controlledTerms/cellType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/controlledTerms/organ.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/controlledTerms/organismSubstance.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/controlledTerms/subcellularEntity.html>`_, `UBERONParcellation <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/controlledTerms/UBERONParcellation.html>`_, `CustomAnatomicalEntity <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/SANDS/non-atlas/customAnatomicalEntity.html>`_, `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/SANDS/atlas/parcellationEntity.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add all anatomical entities that describe the target position(s).

`BACK TO TOP <AnatomicalTargetPosition_>`_

------------

.. _spatialLocation_heading:

***************
spatialLocation
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/spatialLocation
   :value type: | embedded object array \(1-N\) of type
                | `CoordinatePoint <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/SANDS/miscellaneous/coordinatePoint.html>`_
   :instructions: Add all coordinate points that describe the spatial location of the anatomical target structure(s).

`BACK TO TOP <AnatomicalTargetPosition_>`_

------------

.. _targetIdentificationType_heading:

************************
targetIdentificationType
************************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/targetIdentificationType
   :value type: | linked object of type
                | `AnatomicalIdentificationType <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/controlledTerms/anatomicalIdentificationType.html>`_
   :instructions: Add the target identification type that best describes how the this anatomical target position was identified.

`BACK TO TOP <AnatomicalTargetPosition_>`_

------------

