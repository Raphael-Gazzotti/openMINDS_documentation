###############
AtlasAnnotation
###############

:Semantic name: https://openminds.om-i.org/types/AtlasAnnotation

:Display as: Atlas annotation


------------

------------

Properties
##########

:Required: `criteriaQualityType <criteriaQualityType_heading_>`_, `criteriaType <criteriaType_heading_>`_, `type <type_heading_>`_
:Optional: `anchorPoint <anchorPoint_heading_>`_, `criteria <criteria_heading_>`_, `inspiredBy <inspiredBy_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `laterality <laterality_heading_>`_, `preferredVisualization <preferredVisualization_heading_>`_, `specification <specification_heading_>`_

------------

.. _anchorPoint_heading:

***********
anchorPoint
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/anchorPoint
   :value type: | embedded object array \(2-3\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the coordinates of the anchor point for this annotation (e.g., its centroid in two dimensional space as [x, y] or in three dimensional space as [x, y, z]).

`BACK TO TOP <AtlasAnnotation_>`_

------------

.. _criteria_heading:

********
criteria
********

Aspects or standards on which a judgement or decision is based.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/criteria
   :value type: | linked object of type
                | `ProtocolExecution <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/protocolExecution.html>`_
   :instructions: Add the protocol execution defining the criteria that were applied to produce this annotation.

`BACK TO TOP <AtlasAnnotation_>`_

------------

.. _criteriaQualityType_heading:

*******************
criteriaQualityType
*******************

Distinct class that defines how the judgement or decision was made for a particular criteria.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/criteriaQualityType
   :value type: | linked object of type
                | `CriteriaQualityType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/criteriaQualityType.html>`_
   :instructions: Add the quality type of the stated criteria used to define this annotation.

`BACK TO TOP <AtlasAnnotation_>`_

------------

.. _criteriaType_heading:

************
criteriaType
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/criteriaType
   :value type: | linked object of type
                | `AnnotationCriteriaType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/annotationCriteriaType.html>`_
   :instructions: Add the criteria type for this annotation.

`BACK TO TOP <AtlasAnnotation_>`_

------------

.. _inspiredBy_heading:

**********
inspiredBy
**********

Reference to an inspiring element.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/inspiredBy
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/file.html>`_
   :instructions: Add all (source) files that inspired the definition of this annotation.

`BACK TO TOP <AtlasAnnotation_>`_

------------

.. _internalIdentifier_heading:

******************
internalIdentifier
******************

Term or code that identifies someone or something within a particular product.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/internalIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier (or label) of this annotation that is used within the corresponding data files to identify this annotation.

`BACK TO TOP <AtlasAnnotation_>`_

------------

.. _laterality_heading:

**********
laterality
**********

Differentiation between a pair of lateral homologous parts of the body.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/laterality
   :value type: | linked object array \(1-2\) of type
                | `Laterality <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/laterality.html>`_
   :instructions: Add one or both sides of the body, bilateral organ or bilateral organ part that this annotation is defined in.

`BACK TO TOP <AtlasAnnotation_>`_

------------

.. _preferredVisualization_heading:

**********************
preferredVisualization
**********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/preferredVisualization
   :value type: | embedded object of type
                | `ViewerSpecification <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/miscellaneous/viewerSpecification.html>`_
   :instructions: Add the preferred viewer specification to visualize this annotation.

`BACK TO TOP <AtlasAnnotation_>`_

------------

.. _specification_heading:

*************
specification
*************

Detailed and precise presentation of, or proposal for something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/specification
   :value type: | linked object of type
                | `File <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/file.html>`_
   :instructions: Add the non-parametric specification of this annotation.

`BACK TO TOP <AtlasAnnotation_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/type
   :value type: | linked object of type
                | `AnnotationType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/annotationType.html>`_
   :instructions: Add the geometry type of this annotation.

`BACK TO TOP <AtlasAnnotation_>`_

------------

