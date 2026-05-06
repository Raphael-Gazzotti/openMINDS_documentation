##################
NumericalParameter
##################

:Semantic name: https://openminds.ebrains.eu/core/NumericalParameter

:Display as: Numerical parameter


------------

------------

Properties
##########

:Required: `name <name_heading_>`_, `value <value_heading_>`_
:Optional:

------------

.. _name_heading:

****
name
****

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive name for this numerical parameter.

`BACK TO TOP <NumericalParameter_>`_

------------

.. _value_heading:

*****
value
*****

Entry for a property.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/value
   :value type: | embedded object array \(1-N\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Add at least one quantitative value for this parameter.

`BACK TO TOP <NumericalParameter_>`_

------------

