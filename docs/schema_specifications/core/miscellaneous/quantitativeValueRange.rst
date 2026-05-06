######################
QuantitativeValueRange
######################

:Semantic name: https://openminds.ebrains.eu/core/QuantitativeValueRange

:Display as: Quantitative value range

A representation of a range of quantitative values.


------------

------------

Properties
##########

:Required: `maxValue <maxValue_heading_>`_, `minValue <minValue_heading_>`_
:Optional: `unit <unit_heading_>`_

------------

.. _maxValue_heading:

********
maxValue
********

Greatest quantity attained or allowed.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/maxValue
   :value type: number
   :instructions: Add the maximum value measured for this range.

`BACK TO TOP <QuantitativeValueRange_>`_

------------

.. _minValue_heading:

********
minValue
********

Smallest quantity attained or allowed.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/minValue
   :value type: number
   :instructions: Add the minimum value measured for this range.

`BACK TO TOP <QuantitativeValueRange_>`_

------------

.. _unit_heading:

****
unit
****

Determinate quantity adopted as a standard of measurement.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/unit
   :value type: | linked object of type
                | `UnitOfMeasurement <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/unitOfMeasurement.html>`_
   :instructions: Add the unit of measurement of this quantitative value range.

`BACK TO TOP <QuantitativeValueRange_>`_

------------

