##############
SpecimenWeight
##############

:Semantic name: https://openminds.om-i.org/types/SpecimenWeight

:Display as: Specimen weight


------------

------------

Properties
##########

:Required: `type <type_heading_>`_, `weight <weight_heading_>`_
:Optional:

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/type
   :value type: | linked object of type
                | `WeightType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/weightType.html>`_
   :instructions: Enter the weight type for the specified weight value.

`BACK TO TOP <SpecimenWeight_>`_

------------

.. _weight_heading:

******
weight
******

Amount that a thing or being weighs.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/weight
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the weight value.

`BACK TO TOP <SpecimenWeight_>`_

------------

