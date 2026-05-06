###########################
TissueSampleCollectionState
###########################

:Semantic name: https://openminds.ebrains.eu/core/TissueSampleCollectionState

:Display as: Tissue sample collection state


------------

------------

Properties
##########

:Required:
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `age <age_heading_>`_, `attribute <attribute_heading_>`_, `descendedFrom <descendedFrom_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `pathology <pathology_heading_>`_, `relativeTimeIndication <relativeTimeIndication_heading_>`_, `weight <weight_heading_>`_

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
   :instructions: Enter any additional remarks concerning the specimen (set) in this state.

`BACK TO TOP <TissueSampleCollectionState_>`_

------------

.. _age_heading:

***
age
***

Time of life or existence at which some particular qualification, capacity or event arises.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/age
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the age of the specimen (set) in this state.

`BACK TO TOP <TissueSampleCollectionState_>`_

------------

.. _attribute_heading:

*********
attribute
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/attribute
   :value type: | linked object array \(1-N\) of type
                | `TissueSampleAttribute <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/controlledTerms/tissueSampleAttribute.html>`_
   :instructions: Add all attributes that can be ascribed to this tissue sample collection state.

`BACK TO TOP <TissueSampleCollectionState_>`_

------------

.. _descendedFrom_heading:

*************
descendedFrom
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/descendedFrom
   :value type: | linked object array \(1-N\) of type
                | `SubjectGroupState <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/research/subjectGroupState.html>`_, `SubjectState <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/research/subjectState.html>`_, `TissueSampleCollectionState <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/research/tissueSampleCollectionState.html>`_ or `TissueSampleState <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/research/tissueSampleState.html>`_
   :instructions: Add all specimen states used to produce or obtain this tissue sample collection state.

`BACK TO TOP <TissueSampleCollectionState_>`_

------------

.. _internalIdentifier_heading:

******************
internalIdentifier
******************

Term or code that identifies someone or something within a particular product.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/internalIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier (or label) of this specimen (set) state that is used within the corresponding data files to identify this specimen (set) state.

`BACK TO TOP <TissueSampleCollectionState_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this specimen (set) state that may help you to find this instance more easily.

`BACK TO TOP <TissueSampleCollectionState_>`_

------------

.. _pathology_heading:

*********
pathology
*********

Structural and functional deviation from the normal that constitutes a disease or characterizes a particular disease.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/pathology
   :value type: | linked object array \(1-N\) of type
                | `Disease <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/controlledTerms/disease.html>`_ or `DiseaseModel <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/controlledTerms/diseaseModel.html>`_
   :instructions: Add all (human) diseases and/or conditions that the specimen (set) in this state has and/or is a model for.

`BACK TO TOP <TissueSampleCollectionState_>`_

------------

.. _relativeTimeIndication_heading:

**********************
relativeTimeIndication
**********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relativeTimeIndication
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: If there is a temporal relation between the states of a specimen (set), enter the relative time that has passed between this and the preceding specimen (set) state referenced under 'descendedFrom'.

`BACK TO TOP <TissueSampleCollectionState_>`_

------------

.. _weight_heading:

******
weight
******

Amount that a thing or being weighs.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/weight
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the weight of the specimen (set) in this state.

`BACK TO TOP <TissueSampleCollectionState_>`_

------------

