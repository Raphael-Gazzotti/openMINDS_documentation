#######
Comment
#######

:Semantic name: https://openminds.om-i.org/types/Comment

:Display as: Comment

Structured information about a short text expressing an opinion on, or giving information about some entity.


------------

------------

Properties
##########

:Required: `about <about_heading_>`_, `comment <comment_heading_>`_, `commenter <commenter_heading_>`_, `timestamp <timestamp_heading_>`_
:Optional:

------------

.. _about_heading:

*****
about
*****

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/about
   :value type: | linked object of type
                | `ValidationTest <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/validationTest.html>`_, `ValidationTestVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/validationTestVersion.html>`_, `WorkflowRecipe <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/workflowRecipe.html>`_, `WorkflowRecipeVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/workflowRecipeVersion.html>`_, `Dataset <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/dataset.html>`_, `DatasetVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/datasetVersion.html>`_, `MetaDataModel <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/metaDataModel.html>`_, `MetaDataModelVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/metaDataModelVersion.html>`_, `Model <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/model.html>`_, `ModelVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/modelVersion.html>`_, `Software <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/software.html>`_, `SoftwareVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/softwareVersion.html>`_, `WebService <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/webService.html>`_, `WebServiceVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/webServiceVersion.html>`_, `LivePaper <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/publications/livePaper.html>`_, `LivePaperVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/publications/livePaperVersion.html>`_, `BrainAtlas <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/brainAtlas.html>`_, `BrainAtlasVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/brainAtlasVersion.html>`_, `CommonCoordinateSpace <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/commonCoordinateSpace.html>`_ or `CommonCoordinateSpaceVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/commonCoordinateSpaceVersion.html>`_
   :instructions: Add the research product (version) that this comment is about.

`BACK TO TOP <Comment_>`_

------------

.. _comment_heading:

*******
comment
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/comment
   :value type: | string
                | formatting: text/plain; multiline
   :instructions: Enter the comment about the research product (version) stated under 'about'.

`BACK TO TOP <Comment_>`_

------------

.. _commenter_heading:

*********
commenter
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/commenter
   :value type: | linked object of type
                | `Person <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add the person that created this comment.

`BACK TO TOP <Comment_>`_

------------

.. _timestamp_heading:

*********
timestamp
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/timestamp
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date and time on which this comment was made, formatted as '2023-02-07T16:00:00+00:00'.

`BACK TO TOP <Comment_>`_

------------

