##########
BrainAtlas
##########

:Semantic name: https://openminds.ebrains.eu/sands/BrainAtlas

:Display as: Brain atlas


------------

------------

Properties
##########

:Required: `description <description_heading_>`_, `fullName <fullName_heading_>`_, `hasVersion <hasVersion_heading_>`_, `shortName <shortName_heading_>`_
:Optional: `homepage <homepage_heading_>`_

------------

.. _description_heading:

***********
description
***********

Longer statement or account giving the characteristics of someone or something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a short description for this brain atlas.

`BACK TO TOP <BrainAtlas_>`_

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
   :instructions: Enter a descriptive full name for this brain atlas.

`BACK TO TOP <BrainAtlas_>`_

------------

.. _hasVersion_heading:

**********
hasVersion
**********

Reference to variants of an original.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasVersion
   :value type: | linked object array \(1-N\) of type
                | `BrainAtlasVersion <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/SANDS/brainAtlasVersion.html>`_
   :instructions: Add one or several brain atlas versions that belong to this brain atlas.

`BACK TO TOP <BrainAtlas_>`_

------------

.. _homepage_heading:

********
homepage
********

Main website of something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/homepage
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this brain atlas.

`BACK TO TOP <BrainAtlas_>`_

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
   :instructions: Enter a descriptive short name for this brain atlas.

`BACK TO TOP <BrainAtlas_>`_

------------

