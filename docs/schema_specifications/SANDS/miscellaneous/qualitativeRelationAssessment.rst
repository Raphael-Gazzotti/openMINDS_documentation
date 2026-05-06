#############################
QualitativeRelationAssessment
#############################

:Semantic name: https://openminds.om-i.org/types/QualitativeRelationAssessment

:Display as: Qualitative relation assessment


------------

------------

Properties
##########

:Required: `inRelationTo <inRelationTo_heading_>`_, `qualitativeOverlap <qualitativeOverlap_heading_>`_
:Optional: `criteria <criteria_heading_>`_

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
   :instructions: Add the protocol execution defining the criteria that were applied to determine this relation.

`BACK TO TOP <QualitativeRelationAssessment_>`_

------------

.. _inRelationTo_heading:

************
inRelationTo
************

Reference to a related element.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/inRelationTo
   :value type: | linked object of type
                | `CustomAnatomicalEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/non-atlas/customAnatomicalEntity.html>`_, `ParcellationEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntity.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add the anatomical entity to which the relation is described.

`BACK TO TOP <QualitativeRelationAssessment_>`_

------------

.. _qualitativeOverlap_heading:

******************
qualitativeOverlap
******************

Semantic characterization of how much two things occupy the same space.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/qualitativeOverlap
   :value type: | linked object of type
                | `QualitativeOverlap <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/qualitativeOverlap.html>`_
   :instructions: Add the qualitative overlap that best describes the relation between the two anatomical entities.

`BACK TO TOP <QualitativeRelationAssessment_>`_

------------

