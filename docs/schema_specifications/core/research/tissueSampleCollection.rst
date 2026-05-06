######################
TissueSampleCollection
######################

:Semantic name: https://openminds.om-i.org/types/TissueSampleCollection

:Display as: Tissue sample collection


------------

------------

Properties
##########

:Required: `origin <origin_heading_>`_, `species <species_heading_>`_, `studiedState <studiedState_heading_>`_, `type <type_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `anatomicalLocation <anatomicalLocation_heading_>`_, `biologicalSex <biologicalSex_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `laterality <laterality_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `numberOfTissueSamples <numberOfTissueSamples_heading_>`_

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
   :instructions: Enter any additional remarks concerning this specimen set.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _anatomicalLocation_heading:

******************
anatomicalLocation
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/anatomicalLocation
   :value type: | linked object array \(1-N\) of type
                | `CellType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/cellType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/organ.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/organismSubstance.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/subcellularEntity.html>`_, `UBERONParcellation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/UBERONParcellation.html>`_, `CustomAnatomicalEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/non-atlas/customAnatomicalEntity.html>`_, `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntity.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add all anatomical entities that describe the anatomical location of this tissue sample collection.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _biologicalSex_heading:

*************
biologicalSex
*************

Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/biologicalSex
   :value type: | linked object array \(1-N\) of type
                | `BiologicalSex <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/biologicalSex.html>`_
   :instructions: Add the biological sex of all specimen in this set.

`BACK TO TOP <TissueSampleCollection_>`_

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
   :instructions: Enter the identifier (or label) of this specimen set that is used within the corresponding data files to identify this specimen set.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _laterality_heading:

**********
laterality
**********

Differentiation between a pair of lateral homologous parts of the body.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/laterality
   :value type: | linked object array \(1-2\) of type
                | `Laterality <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/laterality.html>`_
   :instructions: Add one or both sides of the body, bilateral organ or bilateral organ part that this tissue sample collection originates from.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this specimen set that may help you to find this instance more easily.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _numberOfTissueSamples_heading:

*********************
numberOfTissueSamples
*********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/numberOfTissueSamples
   :value type: integer
   :instructions: Enter the number of tissue samples that belong to this tissue sample collection.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _origin_heading:

******
origin
******

Source at which something begins or rises, or from which something derives.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/origin
   :value type: | linked object array \(1-N\) of type
                | `CellType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/cellType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/organ.html>`_ or `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/organismSubstance.html>`_
   :instructions: Add the biogical origin of all tissue samples in this collection.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _species_heading:

*******
species
*******

Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/species
   :value type: | linked object array \(1-N\) of type
                | `Species <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/species.html>`_ or `Strain <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/strain.html>`_
   :instructions: Add the species and/or strain (a sub-type of a genetic variant of species) of all specimen in this set.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _studiedState_heading:

************
studiedState
************

Reference to a point in time at which something or someone was studied in a particular mode or condition.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/studiedState
   :value type: | linked object array \(1-N\) of type
                | `TissueSampleCollectionState <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/tissueSampleCollectionState.html>`_
   :instructions: Add all states in which this tissue sample collection was studied.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/type
   :value type: | linked object array \(1-N\) of type
                | `TissueSampleType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/tissueSampleType.html>`_
   :instructions: Add the type of all tissue samples in this collection.

`BACK TO TOP <TissueSampleCollection_>`_

------------

