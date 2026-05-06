##############
TermSuggestion
##############

:Semantic name: https://openminds.om-i.org/types/TermSuggestion

:Display as: Term suggestion


------------

------------

Properties
##########

:Required: `name <name_heading_>`_
:Optional: `addExistingTerminology <addExistingTerminology_heading_>`_, `definition <definition_heading_>`_, `description <description_heading_>`_, `otherCrossReference <otherCrossReference_heading_>`_, `otherOntologyIdentifier <otherOntologyIdentifier_heading_>`_, `preferredCrossReference <preferredCrossReference_heading_>`_, `preferredOntologyIdentifier <preferredOntologyIdentifier_heading_>`_, `suggestNewTerminology <suggestNewTerminology_heading_>`_, `synonym <synonym_heading_>`_

------------

.. _addExistingTerminology_heading:

**********************
addExistingTerminology
**********************

Reference to an existing terminology (distinct class to group related terms).

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/addExistingTerminology
   :value type: | linked object of type
                | `Terminology <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/terminology.html>`_
   :instructions: Add an existing terminology in which the suggested term should be integrated in.

`BACK TO TOP <TermSuggestion_>`_

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
   :instructions: Enter one sentence for defining this term.

`BACK TO TOP <TermSuggestion_>`_

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
   :instructions: Enter a short text describing this term.

`BACK TO TOP <TermSuggestion_>`_

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
   :instructions: Controlled term originating from a defined terminology.

`BACK TO TOP <TermSuggestion_>`_

------------

.. _otherCrossReference_heading:

*******************
otherCrossReference
*******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/otherCrossReference
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter all internationalized resource identifiers (IRIs) pointing to cross-references to external databases or registries that are equivalent to this term (e.g., Wikidata). Do not repeat the preferred cross-reference.

`BACK TO TOP <TermSuggestion_>`_

------------

.. _otherOntologyIdentifier_heading:

***********************
otherOntologyIdentifier
***********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/otherOntologyIdentifier
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter all internationalized resource identifiers (IRIs) pointing to ontology entries that are equivalent to this term (e.g., UBERON). Do not repeat the preferred ontology identifier.

`BACK TO TOP <TermSuggestion_>`_

------------

.. _preferredCrossReference_heading:

***********************
preferredCrossReference
***********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/preferredCrossReference
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) pointing to the preferred cross-reference to an external database or registry (e.g., KnowledgeSpace).

`BACK TO TOP <TermSuggestion_>`_

------------

.. _preferredOntologyIdentifier_heading:

***************************
preferredOntologyIdentifier
***************************

Persistent identifier of a preferred ontological term.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/preferredOntologyIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) pointing to the preferred ontological term (e.g., InterLex).

`BACK TO TOP <TermSuggestion_>`_

------------

.. _suggestNewTerminology_heading:

*********************
suggestNewTerminology
*********************

Proposal of a new distinct class to group related terms.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/suggestNewTerminology
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Propose a name for a new terminology in which the suggested term should be integrated in.

`BACK TO TOP <TermSuggestion_>`_

------------

.. _synonym_heading:

*******
synonym
*******

Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/synonym
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter one or several synonyms (including abbreviations) for this controlled term.

`BACK TO TOP <TermSuggestion_>`_

------------

