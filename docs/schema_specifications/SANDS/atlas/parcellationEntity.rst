##################
ParcellationEntity
##################

:Semantic name: https://openminds.om-i.org/types/ParcellationEntity

:Display as: Parcellation entity


For this schema openMINDS provides a `library of instances <https://openminds-documentation.readthedocs.io/en/v5.0/instance_libraries/parcellationEntities.html>`_.

------------

------------

Properties
##########

:Required: `lookupLabel <lookupLabel_heading_>`_, `name <name_heading_>`_
:Optional: `abbreviation <abbreviation_heading_>`_, `alternateName <alternateName_heading_>`_, `definition <definition_heading_>`_, `hasParent <hasParent_heading_>`_, `ontologyIdentifier <ontologyIdentifier_heading_>`_, `relatedInterspeciesAnatomy <relatedInterspeciesAnatomy_heading_>`_

------------

.. _abbreviation_heading:

************
abbreviation
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/abbreviation
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the official abbreviation of this parcellation entity.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _alternateName_heading:

*************
alternateName
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/alternateName
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter any alternate names, including any alternative abbreviations, for this parcellation entity.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _definition_heading:

**********
definition
**********

Short, but precise statement of the meaning of a word, word group, sign or a symbol.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/definition
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter the definition for this parcellation entity.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _hasParent_heading:

*********
hasParent
*********

Reference to a parent object or legal person.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/hasParent
   :value type: | linked object array \(1-N\) of type
                | `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/atlas/parcellationEntity.html>`_
   :instructions: Add all anatomical parent structures for this parcellation entity as defined within the corresponding brain atlas.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this parcellation entity that may help you to find this instance more easily.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _name_heading:

****
name
****

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name of this parcellation entity.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _ontologyIdentifier_heading:

******************
ontologyIdentifier
******************

Term or code used to identify something or someone registered within a particular ontology.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/ontologyIdentifier
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this parcellation entity.

`BACK TO TOP <ParcellationEntity_>`_

------------

.. _relatedInterspeciesAnatomy_heading:

**************************
relatedInterspeciesAnatomy
**************************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/relatedInterspeciesAnatomy
   :value type: | linked object of type
                | `AnatomicalCavity <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/anatomicalCavity.html>`_, `ExternalBodyRegion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/externalBodyRegion.html>`_, `MuscularStructure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/muscularStructure.html>`_, `NervousSystemStructure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/nervousSystemStructure.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/organ.html>`_, `OrganSystemStructure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/organSystemStructure.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/organismSubstance.html>`_, `OrganismSystem <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/organismSystem.html>`_, `SkeletalStructure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/skeletalStructure.html>`_, `TissueStructure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/tissueStructure.html>`_ or `VascularStructure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/vascularStructure.html>`_
   :instructions: Add the corresponding cross-species anatomical entity from the UBERON-derived terminologies that represents the generic anatomical concept underlying the atlas parcellation entity.

`BACK TO TOP <ParcellationEntity_>`_

------------

