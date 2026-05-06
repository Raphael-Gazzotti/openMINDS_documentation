########
CellType
########

:Semantic name: https://openminds.om-i.org/types/CellType

:Display as: Cell type


For this schema openMINDS provides a `library of instances <https://openminds-documentation.readthedocs.io/en/v4.0/instance_libraries/terminologies/cellType.html>`_.

------------

------------

Properties
##########

:Required: `name <name_heading_>`_
:Optional: `definition <definition_heading_>`_, `description <description_heading_>`_, `interlexIdentifier <interlexIdentifier_heading_>`_, `knowledgeSpaceLink <knowledgeSpaceLink_heading_>`_, `preferredOntologyIdentifier <preferredOntologyIdentifier_heading_>`_, `synonym <synonym_heading_>`_

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

`BACK TO TOP <CellType_>`_

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

`BACK TO TOP <CellType_>`_

------------

.. _interlexIdentifier_heading:

******************
interlexIdentifier
******************

Persistent identifier for a term registered in the InterLex project.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/interlexIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) pointing to the integrated ontology entry in the InterLex project.

`BACK TO TOP <CellType_>`_

------------

.. _knowledgeSpaceLink_heading:

******************
knowledgeSpaceLink
******************

Persistent link to an encyclopedia entry in the Knowledge Space project.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/knowledgeSpaceLink
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) pointing to the wiki page of the corresponding term in the KnowledgeSpace.

`BACK TO TOP <CellType_>`_

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

`BACK TO TOP <CellType_>`_

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
   :instructions: Enter the internationalized resource identifier (IRI) pointing to the preferred ontological term.

`BACK TO TOP <CellType_>`_

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

`BACK TO TOP <CellType_>`_

------------

