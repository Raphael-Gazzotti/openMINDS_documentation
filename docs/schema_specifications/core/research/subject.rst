#######
Subject
#######

:Semantic name: https://openminds.om-i.org/types/Subject

:Display as: Subject

Structured information on a subject.


------------

------------

Properties
##########

:Required: `species <species_heading_>`_, `studiedState <studiedState_heading_>`_
:Optional: `biologicalSex <biologicalSex_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `isPartOf <isPartOf_heading_>`_, `lookupLabel <lookupLabel_heading_>`_

------------

.. _biologicalSex_heading:

*************
biologicalSex
*************

Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/biologicalSex
   :value type: | linked object of type
                | `BiologicalSex <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/biologicalSex.html>`_
   :instructions: Add the biological sex of this specimen.

`BACK TO TOP <Subject_>`_

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
   :instructions: Enter the identifier (or label) of this specimen that is used within the corresponding data files to identify this specimen.

`BACK TO TOP <Subject_>`_

------------

.. _isPartOf_heading:

********
isPartOf
********

Reference to the ensemble of multiple things or beings.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/isPartOf
   :value type: | linked object array \(1-N\) of type
                | `SubjectGroup <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/subjectGroup.html>`_
   :instructions: Add all subject groups of which this subject is a member.

`BACK TO TOP <Subject_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this specimen that may help you to find this instance more easily.

`BACK TO TOP <Subject_>`_

------------

.. _species_heading:

*******
species
*******

Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/species
   :value type: | linked object of type
                | `Species <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/species.html>`_ or `Strain <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/strain.html>`_
   :instructions: Add the species or strain (a sub-type of a genetic variant of species) of this specimen.

`BACK TO TOP <Subject_>`_

------------

.. _studiedState_heading:

************
studiedState
************

Reference to a point in time at which something or someone was studied in a particular mode or condition.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/studiedState
   :value type: | linked object array \(1-N\) of type
                | `SubjectState <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/subjectState.html>`_
   :instructions: Add all states in which this subject was studied.

`BACK TO TOP <Subject_>`_

------------

