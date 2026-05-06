##########
BrainAtlas
##########

:Semantic name: https://openminds.om-i.org/types/BrainAtlas

:Display as: Brain atlas


For this schema openMINDS provides a `library of instances <https://openminds-documentation.readthedocs.io/en/v4.0/instance_libraries/brainAtlases.html>`_.

------------

------------

Properties
##########

:Required: `author <author_heading_>`_, `description <description_heading_>`_, `fullName <fullName_heading_>`_, `hasTerminology <hasTerminology_heading_>`_, `hasVersion <hasVersion_heading_>`_, `shortName <shortName_heading_>`_
:Optional: `abbreviation <abbreviation_heading_>`_, `custodian <custodian_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `homepage <homepage_heading_>`_, `howToCite <howToCite_heading_>`_, `ontologyIdentifier <ontologyIdentifier_heading_>`_, `usedSpecies <usedSpecies_heading_>`_

------------

.. _abbreviation_heading:

************
abbreviation
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/abbreviation
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the official abbreviation of this brain atlas.

`BACK TO TOP <BrainAtlas_>`_

------------

.. _author_heading:

******
author
******

Creator of a literary or creative work, as well as a dataset publication.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/author
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add all parties that contributed to this brain atlas as authors.

`BACK TO TOP <BrainAtlas_>`_

------------

.. _custodian_heading:

*********
custodian
*********

The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/custodian
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add all parties that fulfill the role of a custodian for this research product (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product. Unless specified differently, this custodian will be responsible for all attached research product versions.

`BACK TO TOP <BrainAtlas_>`_

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
   :instructions: Enter a description (or abstract) of this research product. Note that this should be a suitable description for all attached research product versions.

`BACK TO TOP <BrainAtlas_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/digitalIdentifier
   :value type: | linked object of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/DOI.html>`_, `ISBN <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/ISBN.html>`_ or `RRID <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/RRID.html>`_
   :instructions: Add the globally unique and persistent digital identifier of this research product. Note that this digital identifier will be used to reference all attached research product versions.

`BACK TO TOP <BrainAtlas_>`_

------------

.. _fullName_heading:

********
fullName
********

Whole, non-abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/fullName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive full name (or title) for this research product. Note that this should be a suitable full name for all attached research product versions.

`BACK TO TOP <BrainAtlas_>`_

------------

.. _hasTerminology_heading:

**************
hasTerminology
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/hasTerminology
   :value type: | embedded object of type
                | `ParcellationTerminology <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationTerminology.html>`_
   :instructions: Enter the parcellation terminology of this brain atlas.

`BACK TO TOP <BrainAtlas_>`_

------------

.. _hasVersion_heading:

**********
hasVersion
**********

Reference to variants of an original.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/hasVersion
   :value type: | linked object array \(1-N\) of type
                | `BrainAtlasVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/brainAtlasVersion.html>`_
   :instructions: Add versions of this brain atlas.

`BACK TO TOP <BrainAtlas_>`_

------------

.. _homepage_heading:

********
homepage
********

Main website of something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/homepage
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this research product.

`BACK TO TOP <BrainAtlas_>`_

------------

.. _howToCite_heading:

*********
howToCite
*********

Preferred format for citing a particular object or legal person.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/howToCite
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter the preferred citation text for this research product. Leave blank if citation text can be extracted from the assigned digital identifier.

`BACK TO TOP <BrainAtlas_>`_

------------

.. _ontologyIdentifier_heading:

******************
ontologyIdentifier
******************

Term or code used to identify something or someone registered within a particular ontology.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/ontologyIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to the related ontological term matching this brain atlas.

`BACK TO TOP <BrainAtlas_>`_

------------

.. _shortName_heading:

*********
shortName
*********

Shortened or fully abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/shortName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short name (or alias) for this research product that could be used as a shortened display title (e.g., for web services with too little space to display the full name).

`BACK TO TOP <BrainAtlas_>`_

------------

.. _usedSpecies_heading:

***********
usedSpecies
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/usedSpecies
   :value type: | linked object of type
                | `Species <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/species.html>`_
   :instructions: Add the species that was used for the creation of this brain atlas.

`BACK TO TOP <BrainAtlas_>`_

------------

