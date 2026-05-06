#################
QuantitativeValue
#################

:Semantic name: https://openminds.om-i.org/types/QuantitativeValue

:Display as: Quantitative value

Structured information on a quantitative value.


------------

------------

Properties
##########

:Required: `value <value_heading_>`_
:Optional: `typeOfUncertainty <typeOfUncertainty_heading_>`_, `uncertainty <uncertainty_heading_>`_, `unit <unit_heading_>`_

------------

.. _typeOfUncertainty_heading:

*****************
typeOfUncertainty
*****************

Distinct technique used to quantify the uncertainty of a measurement.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/typeOfUncertainty
   :value type: | linked object of type
                | `TypeOfUncertainty <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/typeOfUncertainty.html>`_
   :instructions: Add the type of uncertainty used to determine the uncertainty for this quantitative value.

`BACK TO TOP <QuantitativeValue_>`_

------------

.. _uncertainty_heading:

***********
uncertainty
***********

Quantitative value range defining the uncertainty of a measurement.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/uncertainty
   :value type: number array \(2-2\)
   :instructions: Enter the uncertainty of this quantitative value.

`BACK TO TOP <QuantitativeValue_>`_

------------

.. _unit_heading:

****
unit
****

Determinate quantity adopted as a standard of measurement.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/unit
   :value type: | linked object of type
                | `UnitOfMeasurement <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/unitOfMeasurement.html>`_
   :instructions: Add the unit of measurement of this quantitative value and its uncertainty.

`BACK TO TOP <QuantitativeValue_>`_

------------

.. _value_heading:

*****
value
*****

Entry for a property.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/value
   :value type: number
   :instructions: Enter the value of this quantitative value.

`BACK TO TOP <QuantitativeValue_>`_

------------

