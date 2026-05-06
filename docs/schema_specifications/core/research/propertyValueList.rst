#################
PropertyValueList
#################

:Semantic name: https://openminds.om-i.org/types/PropertyValueList

:Display as: Property value list

An identifiable list of property-value pairs.


------------

------------

Properties
##########

:Required: `propertyValuePair <propertyValuePair_heading_>`_
:Optional: `lookupLabel <lookupLabel_heading_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this property-value list that may help you to find this instance more easily.

`BACK TO TOP <PropertyValueList_>`_

------------

.. _propertyValuePair_heading:

*****************
propertyValuePair
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/propertyValuePair
   :value type: | embedded object array \(1-N\) of type
                | `NumericalProperty <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/numericalProperty.html>`_ or `StringProperty <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/stringProperty.html>`_
   :instructions: Enter all numerical and string property-value pairs that belong to this property-value list.

`BACK TO TOP <PropertyValueList_>`_

------------

