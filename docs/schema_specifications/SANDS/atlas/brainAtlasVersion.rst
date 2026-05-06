#################
BrainAtlasVersion
#################

:Semantic name: https://openminds.ebrains.eu/sands/BrainAtlasVersion

:Display as: Brain atlas version


------------

------------

Properties
##########

:Required: `coordinateSpace <coordinateSpace_heading_>`_, `fullName <fullName_heading_>`_, `hasTerminology <hasTerminology_heading_>`_, `releaseDate <releaseDate_heading_>`_, `shortName <shortName_heading_>`_, `versionIdentifier <versionIdentifier_heading_>`_, `versionInnovation <versionInnovation_heading_>`_
:Optional: `digitalIdentifier <digitalIdentifier_heading_>`_, `homepage <homepage_heading_>`_, `howToCite <howToCite_heading_>`_, `isAlternativeVersionOf <isAlternativeVersionOf_heading_>`_, `isNewVersionOf <isNewVersionOf_heading_>`_, `ontologyIdentifier <ontologyIdentifier_heading_>`_

------------

.. _coordinateSpace_heading:

***************
coordinateSpace
***************

Two or three dimensional geometric setting.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/coordinateSpace
   :value type: | linked object of type
                | `CommonCoordinateSpace <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/SANDS/atlas/commonCoordinateSpace.html>`_
   :instructions: Add the common coordinate space in which this brain atlas version exists in.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/core/miscellaneous/DOI.html>`_
   :instructions: Add the globally unique and persistent digital identifier of this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _fullName_heading:

********
fullName
********

Whole, non-abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fullName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive full name for this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _hasTerminology_heading:

**************
hasTerminology
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasTerminology
   :value type: | linked object of type
                | parcellationTerminology \[TYPE_ERROR\]
   :instructions: Add the parcellation terminology for this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _homepage_heading:

********
homepage
********

Main website of something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/homepage
   :value type: | linked object of type
                | `URL <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/core/miscellaneous/URL.html>`_
   :instructions: Add the uniform resource locator (URL) to the homepage of this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _howToCite_heading:

*********
howToCite
*********

Preferred format for citing a particular object or legal person.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/howToCite
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter the preferred citation text for this brain atlas version. Leave blank if citation text can be extracted from the assigned digital identifier.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _isAlternativeVersionOf_heading:

**********************
isAlternativeVersionOf
**********************

Reference to an original form where the essence was preserved, but presented in an alternative form.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isAlternativeVersionOf
   :value type: | linked object array \(1-N\) of type
                | `BrainAtlasVersion <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/SANDS/atlas/brainAtlasVersion.html>`_
   :instructions: Add one or several alternative versions to this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _isNewVersionOf_heading:

**************
isNewVersionOf
**************

Reference to a previous (potentially outdated) particular form of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isNewVersionOf
   :value type: | linked object of type
                | `BrainAtlasVersion <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/SANDS/atlas/brainAtlasVersion.html>`_
   :instructions: Add the earlier version of this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _ontologyIdentifier_heading:

******************
ontologyIdentifier
******************

Term or code used to identify something or someone registered within a particular ontology.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/ontologyIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier (IRI) of the related ontological term matching this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _releaseDate_heading:

***********
releaseDate
***********

Fixed date on which a product is due to become or was made available for the general public to see or buy

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/releaseDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date of first publication of this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _shortName_heading:

*********
shortName
*********

Shortened or fully abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/shortName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive short name for this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _versionIdentifier_heading:

*****************
versionIdentifier
*****************

Term or code used to identify the version of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/versionIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the version identifier of this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _versionInnovation_heading:

*****************
versionInnovation
*****************

Documentation on what changed in comparison to a previously published form of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/versionInnovation
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a short description of the novelties/peculiarities of this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

