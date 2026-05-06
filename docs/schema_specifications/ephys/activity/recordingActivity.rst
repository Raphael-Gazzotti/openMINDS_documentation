#################
RecordingActivity
#################

:Semantic name: https://openminds.om-i.org/types/RecordingActivity

:Display as: Recording activity


------------

------------

Properties
##########

:Required: `input <input_heading_>`_, `isPartOf <isPartOf_heading_>`_, `output <output_heading_>`_, `protocol <protocol_heading_>`_
:Optional: `customPropertySet <customPropertySet_heading_>`_, `description <description_heading_>`_, `device <device_heading_>`_, `endTime <endTime_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `performedBy <performedBy_heading_>`_, `preparationDesign <preparationDesign_heading_>`_, `startTime <startTime_heading_>`_, `studyTarget <studyTarget_heading_>`_

------------

.. _customPropertySet_heading:

*****************
customPropertySet
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/customPropertySet
   :value type: | embedded object array \(1-N\) of type
                | `CustomPropertySet <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/customPropertySet.html>`_
   :instructions: Add any user-defined parameters grouped in context-specific sets that are not covered in the standardized properties of this activity.

`BACK TO TOP <RecordingActivity_>`_

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

`BACK TO TOP <RecordingActivity_>`_

------------

.. _device_heading:

******
device
******

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/device
   :value type: | linked object array \(1-N\) of type
                | `ElectrodeArrayUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/electrodeArrayUsage.html>`_, `ElectrodeUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/electrodeUsage.html>`_ or `PipetteUsage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/ephys/device/pipetteUsage.html>`_
   :instructions: Add all devices used during this recording activity.

`BACK TO TOP <RecordingActivity_>`_

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

`BACK TO TOP <RecordingActivity_>`_

------------

.. _input_heading:

*****
input
*****

Something or someone that is put into or participates in a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/input
   :value type: | linked object array \(1-N\) of type
                | `SubjectGroupState <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/subjectGroupState.html>`_, `SubjectState <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/subjectState.html>`_, `TissueSampleCollectionState <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/tissueSampleCollectionState.html>`_ or `TissueSampleState <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/tissueSampleState.html>`_
   :instructions: Add all inputs used by this activity.

`BACK TO TOP <RecordingActivity_>`_

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
   :instructions: Enter the identifier (or label) of this recording activity that is used within the corresponding data files to identify this recording activity.

`BACK TO TOP <RecordingActivity_>`_

------------

.. _isPartOf_heading:

********
isPartOf
********

Reference to the ensemble of multiple things or beings.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/isPartOf
   :value type: | linked object of type
                | `DatasetVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/datasetVersion.html>`_
   :instructions: Add the dataset version in which this activity was conducted.

`BACK TO TOP <RecordingActivity_>`_

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

`BACK TO TOP <RecordingActivity_>`_

------------

.. _output_heading:

******
output
******

Something or someone that comes out of, is delivered or produced by a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/output
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/file.html>`_ or `FileBundle <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/fileBundle.html>`_
   :instructions: Add all outputs generated by this activity.

`BACK TO TOP <RecordingActivity_>`_

------------

.. _performedBy_heading:

***********
performedBy
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/performedBy
   :value type: | linked object array \(1-N\) of type
                | `SoftwareAgent <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/softwareAgent.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add all agents that performed this activity.

`BACK TO TOP <RecordingActivity_>`_

------------

.. _preparationDesign_heading:

*****************
preparationDesign
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/preparationDesign
   :value type: | linked object of type
                | `PreparationType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/preparationType.html>`_
   :instructions: Add the initial preparation type for this activity.

`BACK TO TOP <RecordingActivity_>`_

------------

.. _protocol_heading:

********
protocol
********

Plan that describes the process of a scientific or medical experiment, treatment, or procedure.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/protocol
   :value type: | linked object array \(1-N\) of type
                | `Protocol <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/protocol.html>`_
   :instructions: Add all protocols used during this activity.

`BACK TO TOP <RecordingActivity_>`_

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

`BACK TO TOP <RecordingActivity_>`_

------------

.. _studyTarget_heading:

***********
studyTarget
***********

Structure or function that was targeted within a study.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/studyTarget
   :value type: | linked object array \(1-N\) of type
                | `AuditoryStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/auditoryStimulusType.html>`_, `BiologicalOrder <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/biologicalOrder.html>`_, `BiologicalSex <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/biologicalSex.html>`_, `BreedingType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/breedingType.html>`_, `CellCultureType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/cellCultureType.html>`_, `CellType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/cellType.html>`_, `Disease <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/disease.html>`_, `DiseaseModel <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/diseaseModel.html>`_, `ElectricalStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/electricalStimulusType.html>`_, `GeneticStrainType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/geneticStrainType.html>`_, `GustatoryStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/gustatoryStimulusType.html>`_, `Handedness <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/handedness.html>`_, `MolecularEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/molecularEntity.html>`_, `OlfactoryStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/olfactoryStimulusType.html>`_, `OpticalStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/opticalStimulusType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/organ.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/organismSubstance.html>`_, `OrganismSystem <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/organismSystem.html>`_, `Species <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/species.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/subcellularEntity.html>`_, `TactileStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/tactileStimulusType.html>`_, `TermSuggestion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/termSuggestion.html>`_, `TissueSampleType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/tissueSampleType.html>`_, `UBERONParcellation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/UBERONParcellation.html>`_, `VisualStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/visualStimulusType.html>`_, `CustomAnatomicalEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/non-atlas/customAnatomicalEntity.html>`_, `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntity.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add all study targets of this activity.

`BACK TO TOP <RecordingActivity_>`_

------------

