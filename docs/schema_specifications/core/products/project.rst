#######
Project
#######

:Semantic name: https://openminds.ebrains.eu/core/Project

:Display as: Project

Structured information on a research project.


------------

------------

Properties
##########

:Required: `description <description_heading_>`_, `fullName <fullName_heading_>`_, `hasResearchProducts <hasResearchProducts_heading_>`_, `shortName <shortName_heading_>`_
:Optional: `coordinator <coordinator_heading_>`_, `homepage <homepage_heading_>`_

------------

.. _coordinator_heading:

***********
coordinator
***********

Legal person who organizes the collaborative work of people or groups.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/coordinator
   :value type: | linked object array \(1-N\) of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add one or several project coordinators (person or organization).

`BACK TO TOP <Project_>`_

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
   :instructions: Enter a description of this project.

`BACK TO TOP <Project_>`_

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
   :instructions: Enter a descriptive full name (title) for this project.

`BACK TO TOP <Project_>`_

------------

.. _hasResearchProducts_heading:

*******************
hasResearchProducts
*******************

Reference to subsidiary research products.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasResearchProducts
   :value type: | linked object array \(2-N\) of type
                | `Dataset <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/products/dataset.html>`_, `DatasetVersion <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/products/datasetVersion.html>`_, `MetaDataModel <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/products/metaDataModel.html>`_, `MetaDataModelVersion <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/products/metaDataModelVersion.html>`_, `Model <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/products/model.html>`_, `ModelVersion <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/products/modelVersion.html>`_, `Software <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/products/software.html>`_ or `SoftwareVersion <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/products/softwareVersion.html>`_
   :instructions: Add all research products or research product versions that are part of this project.

`BACK TO TOP <Project_>`_

------------

.. _homepage_heading:

********
homepage
********

Main website of something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/homepage
   :value type: | linked object of type
                | `URL <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/URL.html>`_
   :instructions: Add the uniform resource locator (URL) to the homepage of this project.

`BACK TO TOP <Project_>`_

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
   :instructions: Enter a short name (alias) for this project.

`BACK TO TOP <Project_>`_

------------

