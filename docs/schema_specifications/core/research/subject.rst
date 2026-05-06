#######
Subject
#######

:Semantic name: https://openminds.ebrains.eu/core/Subject

:Display as: Subject

Structured information on a subject.


------------

------------

Properties
##########

:Required: `biologicalSex <biologicalSex_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `species <species_heading_>`_, `studiedState <studiedState_heading_>`_
:Optional: `isPartOf <isPartOf_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `phenotype <phenotype_heading_>`_, `strain <strain_heading_>`_

------------

.. _biologicalSex_heading:

*************
biologicalSex
*************

Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/biologicalSex
   :value type: | linked object of type
                | `BiologicalSex <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/biologicalSex.html>`_
   :instructions: Add the biological sex of this specimen.

`BACK TO TOP <Subject_>`_

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
   :instructions: Enter the identifier of this specimen that is used within the corresponding data.

`BACK TO TOP <Subject_>`_

------------

.. _isPartOf_heading:

********
isPartOf
********

Reference to the ensemble of multiple things or beings.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object array \(1-N\) of type
                | `SubjectGroup <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/subjectGroup.html>`_
   :instructions: Add all subject groups of which this subject is a member.

`BACK TO TOP <Subject_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this specimen that may help you to more easily find it again.

`BACK TO TOP <Subject_>`_

------------

.. _phenotype_heading:

*********
phenotype
*********

Physical expression of one or more genes of an organism.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/phenotype
   :value type: | linked object of type
                | `Phenotype <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/phenotype.html>`_
   :instructions: Add the phenotype of this specimen.

`BACK TO TOP <Subject_>`_

------------

.. _species_heading:

*******
species
*******

Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/species
   :value type: | linked object of type
                | `Species <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/species.html>`_
   :instructions: Add the species of this specimen.

`BACK TO TOP <Subject_>`_

------------

.. _strain_heading:

******
strain
******

Group of presumed common ancestry with physiological but usually not morphological distinctions.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/strain
   :value type: | linked object of type
                | `Strain <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/strain.html>`_
   :instructions: Add the strain of this specimen.

`BACK TO TOP <Subject_>`_

------------

.. _studiedState_heading:

************
studiedState
************

Reference to a point in time at which something or someone was studied in a particular mode or condition.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/studiedState
   :value type: | linked object array \(1-N\) of type
                | `SubjectState <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/subjectState.html>`_
   :instructions: Add all states in which this subject was studied.

`BACK TO TOP <Subject_>`_

------------

