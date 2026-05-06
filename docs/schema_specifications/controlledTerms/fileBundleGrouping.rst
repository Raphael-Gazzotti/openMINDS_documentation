##################
FileBundleGrouping
##################

:Semantic name: https://openminds.om-i.org/types/FileBundleGrouping

:Display as: File bundle grouping

Structured information on the grouping mechanism of a file bundle.


For this schema openMINDS provides a `library of instances <https://openminds-documentation.readthedocs.io/en/latest/instance_libraries/terminologies/fileBundleGrouping.html>`_.

------------

------------

Properties
##########

:Required: `name <name_heading_>`_
:Optional: `definition <definition_heading_>`_, `description <description_heading_>`_, `otherCrossReference <otherCrossReference_heading_>`_, `otherOntologyIdentifier <otherOntologyIdentifier_heading_>`_, `preferredCrossReference <preferredCrossReference_heading_>`_, `preferredOntologyIdentifier <preferredOntologyIdentifier_heading_>`_, `synonym <synonym_heading_>`_

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

`BACK TO TOP <FileBundleGrouping_>`_

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

`BACK TO TOP <FileBundleGrouping_>`_

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

`BACK TO TOP <FileBundleGrouping_>`_

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

`BACK TO TOP <FileBundleGrouping_>`_

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

`BACK TO TOP <FileBundleGrouping_>`_

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

`BACK TO TOP <FileBundleGrouping_>`_

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

`BACK TO TOP <FileBundleGrouping_>`_

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

`BACK TO TOP <FileBundleGrouping_>`_

------------

