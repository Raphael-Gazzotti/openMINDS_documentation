######################
QuantitativeValueRange
######################

:Semantic name: https://openminds.om-i.org/types/QuantitativeValueRange

:Display as: Quantitative value range

A representation of a range of quantitative values.


------------

------------

Properties
##########

:Required: `maxValue <maxValue_heading_>`_, `minValue <minValue_heading_>`_
:Optional: `maxValueUnit <maxValueUnit_heading_>`_, `minValueUnit <minValueUnit_heading_>`_

------------

.. _maxValue_heading:

********
maxValue
********

Greatest quantity attained or allowed.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/maxValue
   :value type: number
   :instructions: Enter the maximum value.

`BACK TO TOP <QuantitativeValueRange_>`_

------------

.. _maxValueUnit_heading:

************
maxValueUnit
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/maxValueUnit
   :value type: | linked object of type
                | `UnitOfMeasurement <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/unitOfMeasurement.html>`_
   :instructions: Add the unit of measurement for the maximum value.

`BACK TO TOP <QuantitativeValueRange_>`_

------------

.. _minValue_heading:

********
minValue
********

Smallest quantity attained or allowed.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/minValue
   :value type: number
   :instructions: Enter the minimum value.

`BACK TO TOP <QuantitativeValueRange_>`_

------------

.. _minValueUnit_heading:

************
minValueUnit
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/minValueUnit
   :value type: | linked object of type
                | `UnitOfMeasurement <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/unitOfMeasurement.html>`_
   :instructions: Add the unit of measurement for the minimum value.

`BACK TO TOP <QuantitativeValueRange_>`_

------------

