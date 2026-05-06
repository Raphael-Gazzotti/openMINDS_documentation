############
SubjectState
############

:Semantic name: https://openminds.om-i.org/types/SubjectState

:Display as: Subject state

Structured information on a temporary state of a subject.


------------

------------

Properties
##########

:Required: `ageCategory <ageCategory_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `age <age_heading_>`_, `attribute <attribute_heading_>`_, `descendedFrom <descendedFrom_heading_>`_, `handedness <handedness_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `pathology <pathology_heading_>`_, `relativeTimeIndication <relativeTimeIndication_heading_>`_, `weight <weight_heading_>`_

------------

.. _additionalRemarks_heading:

*****************
additionalRemarks
*****************

Mention of what deserves additional attention or notice.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/additionalRemarks
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter any additional remarks concerning the specimen (set) in this state.

`BACK TO TOP <SubjectState_>`_

------------

.. _age_heading:

***
age
***

Time of life or existence at which some particular qualification, capacity or event arises.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/age
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the age of the specimen (set) in this state.

`BACK TO TOP <SubjectState_>`_

------------

.. _ageCategory_heading:

***********
ageCategory
***********

Distinct life cycle class that is defined by a similar age or age range (developmental stage) within a group of individual beings.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/ageCategory
   :value type: | linked object of type
                | `AgeCategory <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/ageCategory.html>`_
   :instructions: Add the age category of the subject in this state.

`BACK TO TOP <SubjectState_>`_

------------

.. _attribute_heading:

*********
attribute
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/attribute
   :value type: | linked object array \(1-N\) of type
                | `SubjectAttribute <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/subjectAttribute.html>`_
   :instructions: Add all attributes that can be ascribed to this subject state.

`BACK TO TOP <SubjectState_>`_

------------

.. _descendedFrom_heading:

*************
descendedFrom
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/descendedFrom
   :value type: | linked object of type
                | `SubjectState <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/subjectState.html>`_
   :instructions: Add the previous subject state.

`BACK TO TOP <SubjectState_>`_

------------

.. _handedness_heading:

**********
handedness
**********

Degree to which an organism prefers one hand or foot over the other hand or foot during the performance of a task.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/handedness
   :value type: | linked object of type
                | `Handedness <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/handedness.html>`_
   :instructions: Add the preferred handedness of the subject in this state.

`BACK TO TOP <SubjectState_>`_

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
   :instructions: Enter the identifier (or label) of this specimen (set) state that is used within the corresponding data files to identify this specimen (set) state.

`BACK TO TOP <SubjectState_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this specimen (set) state that may help you to find this instance more easily.

`BACK TO TOP <SubjectState_>`_

------------

.. _pathology_heading:

*********
pathology
*********

Structural and functional deviation from the normal that constitutes a disease or characterizes a particular disease.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/pathology
   :value type: | linked object array \(1-N\) of type
                | `Disease <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/disease.html>`_ or `DiseaseModel <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/diseaseModel.html>`_
   :instructions: Add all (human) diseases and/or conditions that the specimen (set) in this state has and/or is a model for.

`BACK TO TOP <SubjectState_>`_

------------

.. _relativeTimeIndication_heading:

**********************
relativeTimeIndication
**********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/relativeTimeIndication
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: If there is a temporal relation between the states of a specimen (set), enter the relative time that has passed between this and the preceding specimen (set) state referenced under 'descendedFrom'.

`BACK TO TOP <SubjectState_>`_

------------

.. _weight_heading:

******
weight
******

Amount that a thing or being weighs.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/weight
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the weight of the specimen (set) in this state.

`BACK TO TOP <SubjectState_>`_

------------

