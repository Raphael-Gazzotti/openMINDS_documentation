######################
TissueSampleCollection
######################

:Semantic name: https://openminds.ebrains.eu/core/TissueSampleCollection

:Display as: Tissue sample collection


------------

------------

Properties
##########

:Required: `biologicalSex <biologicalSex_heading_>`_, `origin <origin_heading_>`_, `species <species_heading_>`_, `studiedState <studiedState_heading_>`_, `type <type_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `laterality <laterality_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `phenotype <phenotype_heading_>`_, `quantity <quantity_heading_>`_, `strain <strain_heading_>`_

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
   :instructions: Enter additional remarks about the specimen set.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _biologicalSex_heading:

*************
biologicalSex
*************

Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/biologicalSex
   :value type: | linked object array \(1-N\) of type
                | `BiologicalSex <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/biologicalSex.html>`_
   :instructions: Add the biological sex of all specimen in this set.

`BACK TO TOP <TissueSampleCollection_>`_

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
   :instructions: Enter the identifier of this specimen set that is used within the corresponding data.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _laterality_heading:

**********
laterality
**********

Differentiation between a pair of lateral homologous parts of the body.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/laterality
   :value type: | linked object array \(1-2\) of type
                | `Laterality <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/laterality.html>`_
   :instructions: Add one or both hemisphere sides from which the tissue samples in this collection originate from.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this specimen set that may help you to more easily find it again.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _origin_heading:

******
origin
******

Source at which something begins or rises, or from which something derives.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/origin
   :value type: | linked object array \(1-N\) of type
                | `CellType <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/cellType.html>`_ or `Organ <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/organ.html>`_
   :instructions: Add the biogical origin (organ or cell type) of all tissue samples in this collection.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _phenotype_heading:

*********
phenotype
*********

Physical expression of one or more genes of an organism.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/phenotype
   :value type: | linked object array \(1-N\) of type
                | `Phenotype <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/phenotype.html>`_
   :instructions: Add the phenotype of all specimen in this set.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _quantity_heading:

********
quantity
********

Total amount or number of things or beings.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/quantity
   :value type: integer
   :instructions: Enter the number of specimen that belong to this set.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _species_heading:

*******
species
*******

Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/species
   :value type: | linked object array \(1-N\) of type
                | `Species <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/species.html>`_
   :instructions: Add the species of all specimen in this set.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _strain_heading:

******
strain
******

Group of presumed common ancestry with physiological but usually not morphological distinctions.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/strain
   :value type: | linked object array \(1-N\) of type
                | `Strain <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/strain.html>`_
   :instructions: Add the strain of all specimen in this set.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _studiedState_heading:

************
studiedState
************

Reference to a point in time at which something or someone was studied in a particular mode or condition.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/studiedState
   :value type: | linked object array \(1-N\) of type
                | `TissueSampleCollectionState <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/tissueSampleCollectionState.html>`_
   :instructions: Add all states in which this tissue sample collection was studied.

`BACK TO TOP <TissueSampleCollection_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/type
   :value type: | linked object array \(1-N\) of type
                | `TissueSampleType <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/tissueSampleType.html>`_
   :instructions: Add the type of all tissue samples in this collection.

`BACK TO TOP <TissueSampleCollection_>`_

------------

