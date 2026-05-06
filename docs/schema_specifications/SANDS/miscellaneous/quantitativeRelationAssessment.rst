##############################
QuantitativeRelationAssessment
##############################

:Semantic name: https://openminds.om-i.org/types/QuantitativeRelationAssessment

:Display as: Quantitative relation assessment


------------

------------

Properties
##########

:Required: `inRelationTo <inRelationTo_heading_>`_, `quantitativeOverlap <quantitativeOverlap_heading_>`_
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

`BACK TO TOP <QuantitativeRelationAssessment_>`_

------------

.. _inRelationTo_heading:

************
inRelationTo
************

Reference to a related element.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/inRelationTo
   :value type: | linked object of type
                | `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add the parcellation entity version to which the relation is described.

`BACK TO TOP <QuantitativeRelationAssessment_>`_

------------

.. _quantitativeOverlap_heading:

*******************
quantitativeOverlap
*******************

Numerical characterization of how much two things occupy the same space.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/quantitativeOverlap
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the quantitative overlap between the two anatomical entities, preferably expressed in percentage.

`BACK TO TOP <QuantitativeRelationAssessment_>`_

------------

