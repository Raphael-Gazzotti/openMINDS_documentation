############
SubjectGroup
############

:Semantic name: https://openminds.ebrains.eu/core/SubjectGroup

:Display as: Subject group


------------

------------

Properties
##########

:Required: `species <species_heading_>`_, `studiedState <studiedState_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `biologicalSex <biologicalSex_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `numberOfSubjects <numberOfSubjects_heading_>`_

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
   :instructions: Enter any additional remarks concerning this specimen set.

`BACK TO TOP <SubjectGroup_>`_

------------

.. _biologicalSex_heading:

*************
biologicalSex
*************

Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/biologicalSex
   :value type: | linked object array \(1-N\) of type
                | `BiologicalSex <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/controlledTerms/biologicalSex.html>`_
   :instructions: Add the biological sex of all specimen in this set.

`BACK TO TOP <SubjectGroup_>`_

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
   :instructions: Enter the identifier (or label) of this specimen set that is used within the corresponding data files to identify this specimen set.

`BACK TO TOP <SubjectGroup_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this specimen set that may help you to find this instance more easily.

`BACK TO TOP <SubjectGroup_>`_

------------

.. _numberOfSubjects_heading:

****************
numberOfSubjects
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/numberOfSubjects
   :value type: integer
   :instructions: Enter the number of subjects that belong to this subject group.

`BACK TO TOP <SubjectGroup_>`_

------------

.. _species_heading:

*******
species
*******

Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/species
   :value type: | linked object array \(1-N\) of type
                | `Species <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/controlledTerms/species.html>`_ or `Strain <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/research/strain.html>`_
   :instructions: Add the species and/or strain (a sub-type of a genetic variant of species) of all specimen in this set.

`BACK TO TOP <SubjectGroup_>`_

------------

.. _studiedState_heading:

************
studiedState
************

Reference to a point in time at which something or someone was studied in a particular mode or condition.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/studiedState
   :value type: | linked object array \(1-N\) of type
                | `SubjectGroupState <https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/core/research/subjectGroupState.html>`_
   :instructions: Add all states in which this subject group was studied.

`BACK TO TOP <SubjectGroup_>`_

------------

