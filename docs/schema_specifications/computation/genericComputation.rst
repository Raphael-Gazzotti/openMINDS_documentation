##################
GenericComputation
##################

:Semantic name: https://openminds.om-i.org/types/GenericComputation

:Display as: Generic computation

Structured information about a computation whose type is unknown or unspecified.


------------

------------

Properties
##########

:Required: `environment <environment_heading_>`_, `input <input_heading_>`_, `output <output_heading_>`_, `startTime <startTime_heading_>`_
:Optional: `customPropertySet <customPropertySet_heading_>`_, `description <description_heading_>`_, `endTime <endTime_heading_>`_, `launchConfiguration <launchConfiguration_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `performedBy <performedBy_heading_>`_, `recipe <recipe_heading_>`_, `resourceUsage <resourceUsage_heading_>`_, `startedBy <startedBy_heading_>`_, `status <status_heading_>`_, `studyTarget <studyTarget_heading_>`_, `tag <tag_heading_>`_, `technique <technique_heading_>`_, `wasInformedBy <wasInformedBy_heading_>`_

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

`BACK TO TOP <GenericComputation_>`_

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

`BACK TO TOP <GenericComputation_>`_

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

`BACK TO TOP <GenericComputation_>`_

------------

.. _environment_heading:

***********
environment
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/environment
   :value type: | linked object of type
                | `Environment <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/environment.html>`_ or `WebServiceVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/webServiceVersion.html>`_
   :instructions: Add the computational environment in which this computation was executed.

`BACK TO TOP <GenericComputation_>`_

------------

.. _input_heading:

*****
input
*****

Something or someone that is put into or participates in a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/input
   :value type: | linked object array \(1-N\) of type
                | `LocalFile <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/localFile.html>`_, `File <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/file.html>`_, `FileBundle <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/fileBundle.html>`_ or `SoftwareVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/softwareVersion.html>`_
   :instructions: Add all inputs used by this activity.

`BACK TO TOP <GenericComputation_>`_

------------

.. _launchConfiguration_heading:

*******************
launchConfiguration
*******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/launchConfiguration
   :value type: | linked object of type
                | `LaunchConfiguration <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/launchConfiguration.html>`_
   :instructions: Add the launch configuration of this computation (e.g., command-line arguments).

`BACK TO TOP <GenericComputation_>`_

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

`BACK TO TOP <GenericComputation_>`_

------------

.. _output_heading:

******
output
******

Something or someone that comes out of, is delivered or produced by a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/output
   :value type: | linked object array \(1-N\) of type
                | `LocalFile <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/localFile.html>`_, `File <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/file.html>`_, `FileArchive <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/fileArchive.html>`_ or `FileBundle <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/fileBundle.html>`_
   :instructions: Add all outputs generated by this activity.

`BACK TO TOP <GenericComputation_>`_

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

`BACK TO TOP <GenericComputation_>`_

------------

.. _recipe_heading:

******
recipe
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/recipe
   :value type: | linked object of type
                | `WorkflowRecipeVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/workflowRecipeVersion.html>`_
   :instructions: Add the workflow recipe version used for this computation.

`BACK TO TOP <GenericComputation_>`_

------------

.. _resourceUsage_heading:

*************
resourceUsage
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/resourceUsage
   :value type: | embedded object array \(1-N\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter all resources used during this computation (e.g., core-hours or energy).

`BACK TO TOP <GenericComputation_>`_

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

`BACK TO TOP <GenericComputation_>`_

------------

.. _startedBy_heading:

*********
startedBy
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/startedBy
   :value type: | linked object of type
                | `SoftwareAgent <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/softwareAgent.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add the agent that started this computation.

`BACK TO TOP <GenericComputation_>`_

------------

.. _status_heading:

******
status
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/status
   :value type: | linked object of type
                | `ActionStatusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/actionStatusType.html>`_
   :instructions: Enter the current status of this computation.

`BACK TO TOP <GenericComputation_>`_

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

`BACK TO TOP <GenericComputation_>`_

------------

.. _tag_heading:

***
tag
***

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/tag
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter any custom tags for this computation.

`BACK TO TOP <GenericComputation_>`_

------------

.. _technique_heading:

*********
technique
*********

Method of accomplishing a desired aim.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/technique
   :value type: | linked object array \(1-N\) of type
                | `AnalysisTechnique <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/analysisTechnique.html>`_
   :instructions: Add all analysis techniques that were used in this computation.

`BACK TO TOP <GenericComputation_>`_

------------

.. _wasInformedBy_heading:

*************
wasInformedBy
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/wasInformedBy
   :value type: | linked object of type
                | `DataAnalysis <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/dataAnalysis.html>`_, `DataCopy <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/dataCopy.html>`_, `GenericComputation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/genericComputation.html>`_, `ModelValidation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/modelValidation.html>`_, `Optimization <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/optimization.html>`_, `Simulation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/simulation.html>`_ or `Visualization <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/visualization.html>`_
   :instructions: Add another computation that sent data to this one during runtime.

`BACK TO TOP <GenericComputation_>`_

------------

