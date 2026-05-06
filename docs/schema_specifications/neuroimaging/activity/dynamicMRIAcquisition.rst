#####################
DynamicMRIAcquisition
#####################

:Semantic name: https://openminds.om-i.org/types/DynamicMRIAcquisition

:Display as: Dynamic mriacquisition


------------

------------

Properties
##########

:Required: `behavioralProtocol <behavioralProtocol_heading_>`_, `device <device_heading_>`_, `input <input_heading_>`_, `isPartOf <isPartOf_heading_>`_, `output <output_heading_>`_, `protocol <protocol_heading_>`_, `specimenOrientation <specimenOrientation_heading_>`_, `volumeAcquisitionTime <volumeAcquisitionTime_heading_>`_
:Optional: `contrastAgent <contrastAgent_heading_>`_, `customPropertySet <customPropertySet_heading_>`_, `delayTime <delayTime_heading_>`_, `description <description_heading_>`_, `distortionCorrection <distortionCorrection_heading_>`_, `endTime <endTime_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `motionCorrection <motionCorrection_heading_>`_, `numberOfDiscardedVolumes <numberOfDiscardedVolumes_heading_>`_, `performedBy <performedBy_heading_>`_, `preparationDesign <preparationDesign_heading_>`_, `registrationData <registrationData_heading_>`_, `startTime <startTime_heading_>`_, `studyTarget <studyTarget_heading_>`_, `targetAnatomy <targetAnatomy_heading_>`_, `volumeTiming <volumeTiming_heading_>`_

------------

.. _behavioralProtocol_heading:

******************
behavioralProtocol
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/behavioralProtocol
   :value type: | linked object array \(1-N\) of type
                | `BehavioralProtocol <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/behavioralProtocol.html>`_
   :instructions: Add the behavioral protocol or protocols applied during this acquisition, including all tasks or observed behavioral conditions (for example, resting state).

`BACK TO TOP <DynamicMRIAcquisition_>`_

------------

.. _contrastAgent_heading:

*************
contrastAgent
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/contrastAgent
   :value type: | embedded object array \(1-N\) of type
                | `AmountOfChemical <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/chemicals/amountOfChemical.html>`_
   :instructions: Add the contrast agent(s) administered for this acquisition, including for each the agent identity and administered amount; if no contrast agent was used, leave this field null. Include all agents given prior to or during the scan.

`BACK TO TOP <DynamicMRIAcquisition_>`_

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

`BACK TO TOP <DynamicMRIAcquisition_>`_

------------

.. _delayTime_heading:

*********
delayTime
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/delayTime
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the delay time, defined as the time interval between a protocol-defined reference event (for example, stimulus onset, contrast administration, or physiological trigger) and the start of dynamic image acquisition, expressed in seconds. This value should reflect the actual timing applied during the scan.

`BACK TO TOP <DynamicMRIAcquisition_>`_

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

`BACK TO TOP <DynamicMRIAcquisition_>`_

------------

.. _device_heading:

******
device
******

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/device
   :value type: | linked object of type
                | `MRIScannerUsage <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/neuroimaging/device/MRIScannerUsage.html>`_
   :instructions: Add the magnetic resonance imaging (MRI) scanner used for this acquisition. This reference should identify the specific device configuration under which the scan was performed.

`BACK TO TOP <DynamicMRIAcquisition_>`_

------------

.. _distortionCorrection_heading:

********************
distortionCorrection
********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/distortionCorrection
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/file.html>`_
   :instructions: Add the distortion correction data used for this acquisition, linking to the calibration files applied during image reconstruction or post-processing. If no distortion correction was performed, leave this field null.

`BACK TO TOP <DynamicMRIAcquisition_>`_

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

`BACK TO TOP <DynamicMRIAcquisition_>`_

------------

.. _input_heading:

*****
input
*****

Something or someone that is put into or participates in a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/input
   :value type: | linked object array \(1-N\) of type
                | `SubjectState <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/subjectState.html>`_ or `TissueSampleState <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/tissueSampleState.html>`_
   :instructions: Add the specimen (subject or tissue sample) in the physical and biological state in which it was scanned, referencing the corresponding specimen record at the time of imaging.

`BACK TO TOP <DynamicMRIAcquisition_>`_

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

`BACK TO TOP <DynamicMRIAcquisition_>`_

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

`BACK TO TOP <DynamicMRIAcquisition_>`_

------------

.. _motionCorrection_heading:

****************
motionCorrection
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/motionCorrection
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/file.html>`_
   :instructions: Add the motion correction data used for this acquisition, linking to the calibration files or reference images applied during image reconstruction or post-processing. If no motion correction was performed, leave this field null.

`BACK TO TOP <DynamicMRIAcquisition_>`_

------------

.. _numberOfDiscardedVolumes_heading:

************************
numberOfDiscardedVolumes
************************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/numberOfDiscardedVolumes
   :value type: integer
   :instructions: Enter the number of image volumes discarded by the operator or analyst prior to post-processing, including initial equilibration volumes and any later volumes removed due to artifacts or instability. This value should reflect the total user-defined exclusion applied after acquisition.

`BACK TO TOP <DynamicMRIAcquisition_>`_

------------

.. _output_heading:

******
output
******

Something or someone that comes out of, is delivered or produced by a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/output
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/file.html>`_
   :instructions: Add the output data generated by this acquisition by linking to one or more files containing the primary imaging outputs and/or, if applicable, any secondary reconstructed or corrected outputs produced during post-processing.

`BACK TO TOP <DynamicMRIAcquisition_>`_

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

`BACK TO TOP <DynamicMRIAcquisition_>`_

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

`BACK TO TOP <DynamicMRIAcquisition_>`_

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

`BACK TO TOP <DynamicMRIAcquisition_>`_

------------

.. _registrationData_heading:

****************
registrationData
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/registrationData
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/file.html>`_
   :instructions: Add the registration data used for this acquisition, linking to the transformation and/or reference files applied during image alignment in post-processing. If no registration was performed, leave this field null.

`BACK TO TOP <DynamicMRIAcquisition_>`_

------------

.. _specimenOrientation_heading:

*******************
specimenOrientation
*******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/specimenOrientation
   :value type: | linked object of type
                | `AnatomicalAxesOrientation <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/anatomicalAxesOrientation.html>`_
   :instructions: Add the specimen orientation as the anatomical directions corresponding to the scanner X, Y, and Z axes, describing the alignment of the specimen's anatomy with the scanner coordinate system. Note that this orientation may differ from the prescribed slice orientation, especially in nonstandard specimen positioning.

`BACK TO TOP <DynamicMRIAcquisition_>`_

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

`BACK TO TOP <DynamicMRIAcquisition_>`_

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

`BACK TO TOP <DynamicMRIAcquisition_>`_

------------

.. _targetAnatomy_heading:

*************
targetAnatomy
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/targetAnatomy
   :value type: | linked object of type
                | `AnatomicalCavity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/anatomicalCavity.html>`_, `CellType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/cellType.html>`_, `ExternalBodyRegion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/externalBodyRegion.html>`_, `MuscularStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/muscularStructure.html>`_, `NervousSystemStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/nervousSystemStructure.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organ.html>`_, `OrganSystemStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organSystemStructure.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organismSubstance.html>`_, `OrganismSystem <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/organismSystem.html>`_, `SkeletalStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/skeletalStructure.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/subcellularEntity.html>`_, `TissueStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/tissueStructure.html>`_, `VascularStructure <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/vascularStructure.html>`_, `CustomAnatomicalEntity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/non-atlas/customAnatomicalEntity.html>`_, `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/parcellationEntity.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add the target anatomy, indicating the primary anatomical structure or region intended to be imaged in this acquisition. This field describes the imaging objective (for example, organ, tissue, or structure) and may be derived from the acquisition protocol description.

`BACK TO TOP <DynamicMRIAcquisition_>`_

------------

.. _volumeAcquisitionTime_heading:

*********************
volumeAcquisitionTime
*********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/volumeAcquisitionTime
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the volume acquisition time, defined as the time required to acquire a single image volume, expressed in seconds. This value is typically equivalent to the repetition time for volume-based acquisitions and can be retrieved from the sequence timing information in the DICOM header.

`BACK TO TOP <DynamicMRIAcquisition_>`_

------------

.. _volumeTiming_heading:

************
volumeTiming
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/volumeTiming
   :value type: | embedded object of type
                | `QuantitativeValueArray <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValueArray.html>`_
   :instructions: Enter the volume timing as an array specifying the acquisition time of each volume relative to the start of the dynamic scan, expressed in seconds, with one entry per acquired volume. These values may be derived from the repetition time or extracted from the acquisition metadata.

`BACK TO TOP <DynamicMRIAcquisition_>`_

------------

