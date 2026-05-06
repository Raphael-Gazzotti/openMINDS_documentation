#######
Project
#######

:Semantic name: https://openminds.om-i.org/types/Project

:Display as: Project

Structured information on a research project.


------------

------------

Properties
##########

:Required: `description <description_heading_>`_, `fullName <fullName_heading_>`_, `hasPart <hasPart_heading_>`_, `shortName <shortName_heading_>`_
:Optional: `coordinator <coordinator_heading_>`_, `homepage <homepage_heading_>`_

------------

.. _coordinator_heading:

***********
coordinator
***********

Legal person who organizes the collaborative work of people or groups.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/coordinator
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add all parties that coordinate this project.

`BACK TO TOP <Project_>`_

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
   :instructions: Enter a description of this project.

`BACK TO TOP <Project_>`_

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
   :instructions: Enter a descriptive full name (or title) for this project.

`BACK TO TOP <Project_>`_

------------

.. _hasPart_heading:

*******
hasPart
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/hasPart
   :value type: | linked object array \(2-N\) of type
                | `ValidationTest <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/validationTest.html>`_, `ValidationTestVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/validationTestVersion.html>`_, `WorkflowRecipe <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/workflowRecipe.html>`_, `WorkflowRecipeVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/workflowRecipeVersion.html>`_, `Dataset <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/dataset.html>`_, `DatasetVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/datasetVersion.html>`_, `MetaDataModel <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/metaDataModel.html>`_, `MetaDataModelVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/metaDataModelVersion.html>`_, `Model <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/model.html>`_, `ModelVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/modelVersion.html>`_, `Software <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/software.html>`_, `SoftwareVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/softwareVersion.html>`_, `WebService <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/webService.html>`_, `WebServiceVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/webServiceVersion.html>`_, `LivePaper <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/publications/livePaper.html>`_, `LivePaperVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/publications/livePaperVersion.html>`_, `BrainAtlas <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/brainAtlas.html>`_, `BrainAtlasVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/brainAtlasVersion.html>`_, `CommonCoordinateSpace <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/commonCoordinateSpace.html>`_ or `CommonCoordinateSpaceVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/commonCoordinateSpaceVersion.html>`_
   :instructions: Add all research product (versions) that are part of this project.

`BACK TO TOP <Project_>`_

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
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this project.

`BACK TO TOP <Project_>`_

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
   :instructions: Enter a short name (or alias) for this project that could be used as a shortened display title (e.g., for web services with too little space to display the full name).

`BACK TO TOP <Project_>`_

------------

