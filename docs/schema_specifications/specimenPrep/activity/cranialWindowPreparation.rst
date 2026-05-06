########################
CranialWindowPreparation
########################

:Semantic name: https://openminds.om-i.org/types/CranialWindowPreparation

:Display as: Cranial window preparation


------------

------------

Properties
##########

:Required: `constructionType <constructionType_heading_>`_, `input <input_heading_>`_, `isPartOf <isPartOf_heading_>`_, `output <output_heading_>`_, `protocol <protocol_heading_>`_
:Optional: `customPropertySet <customPropertySet_heading_>`_, `description <description_heading_>`_, `dimension <dimension_heading_>`_, `endTime <endTime_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `performedBy <performedBy_heading_>`_, `preparationDesign <preparationDesign_heading_>`_, `reinforcementType <reinforcementType_heading_>`_, `startTime <startTime_heading_>`_, `studyTarget <studyTarget_heading_>`_

------------

.. _constructionType_heading:

****************
constructionType
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/constructionType
   :value type: | linked object of type
                | `CranialWindowConstructionType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/cranialWindowConstructionType.html>`_
   :instructions: Add the construction type of the cranial window.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _customPropertySet_heading:

*****************
customPropertySet
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/customPropertySet
   :value type: | embedded object array \(1-N\) of type
                | `CustomPropertySet <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/customPropertySet.html>`_
   :instructions: Add any user-defined parameters grouped in context-specific sets that are not covered in the standardized properties of this activity.

`BACK TO TOP <CranialWindowPreparation_>`_

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
   :instructions: Enter a description of this activity.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _dimension_heading:

*********
dimension
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/dimension
   :value type: | embedded object of type
                | `CentroidalPyramid <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/centroidalPyramid.html>`_, `Circle <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/circle.html>`_, `CircularSector <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/circularSector.html>`_, `Cube <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/cube.html>`_, `Ellipse <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/ellipse.html>`_, `Ellipsoid <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/ellipsoid.html>`_, `EquilateralTriangle <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/equilateralTriangle.html>`_, `Frustum <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/frustum.html>`_, `IsoscelesTriangle <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/isoscelesTriangle.html>`_, `Kite <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/kite.html>`_, `Parallelogram <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/parallelogram.html>`_, `Rectangle <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/rectangle.html>`_, `RegularPolygon <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/regularPolygon.html>`_, `Rhombus <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/rhombus.html>`_, `RightCone <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/rightCone.html>`_, `RightCylinder <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/rightCylinder.html>`_, `RightPrism <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/rightPrism.html>`_, `RightTriangle <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/rightTriangle.html>`_, `Sphere <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/sphere.html>`_, `Spheroid <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/spheroid.html>`_, `Square <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/square.html>`_, `Trapezoid <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/trapezoid.html>`_ or `Triangle <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/mathematicalShape/triangle.html>`_
   :instructions: Enter the dimension of the cranial window by defining its mathematical shape.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _endTime_heading:

*******
endTime
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/endTime
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date and/or time on when this activity ended, formatted as either '2023-02-07T16:00:00+00:00' (date-time) or '16:00:00+00:00' (time).

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _input_heading:

*****
input
*****

Something or someone that is put into or participates in a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/input
   :value type: | linked object array \(1-N\) of type
                | `SubjectState <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/subjectState.html>`_
   :instructions: Add the state of the subject which received the cranial window before this activity.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _isPartOf_heading:

********
isPartOf
********

Reference to the ensemble of multiple things or beings.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/isPartOf
   :value type: | linked object of type
                | `DatasetVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/datasetVersion.html>`_
   :instructions: Add the dataset version in which this activity was conducted.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this activity that may help you to find this instance more easily.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _output_heading:

******
output
******

Something or someone that comes out of, is delivered or produced by a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/output
   :value type: | linked object array \(1-N\) of type
                | `SubjectState <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/subjectState.html>`_
   :instructions: Add the state of the subject which received the cranial window as a result of this activity.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _performedBy_heading:

***********
performedBy
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/performedBy
   :value type: | linked object array \(1-N\) of type
                | `SoftwareAgent <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/softwareAgent.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html>`_
   :instructions: Add all agents that performed this activity.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _preparationDesign_heading:

*****************
preparationDesign
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/preparationDesign
   :value type: | linked object of type
                | `PreparationType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/preparationType.html>`_
   :instructions: Add the initial preparation type for this activity.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _protocol_heading:

********
protocol
********

Plan that describes the process of a scientific or medical experiment, treatment, or procedure.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/protocol
   :value type: | linked object array \(1-N\) of type
                | `Protocol <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/protocol.html>`_
   :instructions: Add all protocols used during this activity.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _reinforcementType_heading:

*****************
reinforcementType
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/reinforcementType
   :value type: | linked object of type
                | `CranialWindowReinforcementType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/cranialWindowReinforcementType.html>`_
   :instructions: Add the reinforcement type of the cranial window.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _startTime_heading:

*********
startTime
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/startTime
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date and/or time on when this activity started, formatted as either '2023-02-07T16:00:00+00:00' (date-time) or '16:00:00+00:00' (time).

`BACK TO TOP <CranialWindowPreparation_>`_

------------

.. _studyTarget_heading:

***********
studyTarget
***********

Structure or function that was targeted within a study.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/studyTarget
   :value type: | linked object array \(1-N\) of type
                | `AnatomicalCavity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/anatomicalCavity.html>`_, `AuditoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/auditoryStimulusType.html>`_, `BiologicalOrder <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/biologicalOrder.html>`_, `BiologicalSex <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/biologicalSex.html>`_, `BreedingType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/breedingType.html>`_, `CellCultureType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/cellCultureType.html>`_, `CellType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/cellType.html>`_, `DeviceType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/deviceType.html>`_, `Disease <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/disease.html>`_, `DiseaseModel <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/diseaseModel.html>`_, `ElectricalStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/electricalStimulusType.html>`_, `ExternalBodyRegion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/externalBodyRegion.html>`_, `GeneticStrainType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/geneticStrainType.html>`_, `GustatoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/gustatoryStimulusType.html>`_, `Handedness <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/handedness.html>`_, `MolecularEntity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/molecularEntity.html>`_, `MuscularStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/muscularStructure.html>`_, `NervousSystemStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/nervousSystemStructure.html>`_, `OlfactoryStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/olfactoryStimulusType.html>`_, `OpticalStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/opticalStimulusType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organ.html>`_, `OrganSystemStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organSystemStructure.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organismSubstance.html>`_, `OrganismSystem <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organismSystem.html>`_, `SkeletalStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/skeletalStructure.html>`_, `Species <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/species.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/subcellularEntity.html>`_, `TactileStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/tactileStimulusType.html>`_, `TermSuggestion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/termSuggestion.html>`_, `TissueSampleType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/tissueSampleType.html>`_, `TissueStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/tissueStructure.html>`_, `VascularStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/vascularStructure.html>`_, `VisualStimulusType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/visualStimulusType.html>`_, `CustomAnatomicalEntity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/non-atlas/customAnatomicalEntity.html>`_, `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/parcellationEntity.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add all study targets of this activity.

`BACK TO TOP <CranialWindowPreparation_>`_

------------

