#################
ProtocolExecution
#################

:Semantic name: https://openminds.ebrains.eu/core/ProtocolExecution

:Display as: Protocol execution

Structured information on a protocol execution.


------------

------------

Properties
##########

:Required: `input <input_heading_>`_, `isPartOf <isPartOf_heading_>`_, `output <output_heading_>`_, `protocol <protocol_heading_>`_
:Optional: `behavioralTask <behavioralTask_heading_>`_, `description <description_heading_>`_, `endedAtTime <endedAtTime_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `parameterSet <parameterSet_heading_>`_, `preparationType <preparationType_heading_>`_, `startedAtTime <startedAtTime_heading_>`_, `studyTarget <studyTarget_heading_>`_

------------

.. _behavioralTask_heading:

**************
behavioralTask
**************

Specific set of defined activities (or their absence) that should be performed (or avoided) by a subject.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/behavioralTask
   :value type: | linked object array \(1-N\) of type
                | `BehavioralTask <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/behavioralTask.html>`_
   :instructions: Add all behavioral tasks that were performed during this protocol execution.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _description_heading:

***********
description
***********

Longer statement or account giving the characteristics of someone or something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a description of this activity.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _endedAtTime_heading:

***********
endedAtTime
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/endedAtTime
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the time (e.g., '20:20:39+00:00') or datetime (e.g., '2018-11-13T20:20:39+00:00') of when the activity ended.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _input_heading:

*****
input
*****

Something or someone that is put into or participates in a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/input
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/file.html>`_, `FileBundle <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/fileBundle.html>`_, `SubjectGroupState <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/subjectGroupState.html>`_, `SubjectState <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/subjectState.html>`_, `TissueSampleCollectionState <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/tissueSampleCollectionState.html>`_ or `TissueSampleState <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/tissueSampleState.html>`_
   :instructions: Add all inputs used by this activity.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _isPartOf_heading:

********
isPartOf
********

Reference to the ensemble of multiple things or beings.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object of type
                | `DatasetVersion <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/products/datasetVersion.html>`_
   :instructions: Add the dataset version in which this protocol execution was conducted.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this activity that may help you to more easily find it again.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _output_heading:

******
output
******

Something or someone that comes out of, is delivered or produced by a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/output
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/file.html>`_, `FileBundle <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/fileBundle.html>`_, `SubjectGroupState <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/subjectGroupState.html>`_, `SubjectState <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/subjectState.html>`_, `TissueSampleCollectionState <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/tissueSampleCollectionState.html>`_ or `TissueSampleState <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/tissueSampleState.html>`_
   :instructions: Add all outputs generated by this activity.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _parameterSet_heading:

************
parameterSet
************

Manner, position, or direction in which digital or physical properties are set to determine a particular function, characteristics or behavior of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/parameterSet
   :value type: | embedded object array \(1-N\) of type
                | `ParameterSet <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/parameterSet.html>`_
   :instructions: Add all important parameters grouped in context-specific sets that were used in this activity.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _preparationType_heading:

***************
preparationType
***************

Distinct class of actions or processes that make something ready for use or service.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/preparationType
   :value type: | linked object of type
                | `PreparationType <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/preparationType.html>`_
   :instructions: Add the initial preparation type for this protocol execution.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _protocol_heading:

********
protocol
********

Plan that describes the process of a scientific or medical experiment, treatment, or procedure.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/protocol
   :value type: | linked object array \(1-N\) of type
                | `Protocol <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/protocol.html>`_
   :instructions: Add all protocols that were used in this protocol execution.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _startedAtTime_heading:

*************
startedAtTime
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/startedAtTime
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the time (e.g., '20:20:39+00:00') or datetime (e.g., '2018-11-13T20:20:39+00:00') of when the activity started.

`BACK TO TOP <ProtocolExecution_>`_

------------

.. _studyTarget_heading:

***********
studyTarget
***********

Structure or function that was targeted within a study.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/studyTarget
   :value type: | linked object array \(1-N\) of type
                | undefined
   :instructions: Add all study targets of this activity.

`BACK TO TOP <ProtocolExecution_>`_

------------

