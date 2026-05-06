###########
SpecimenAge
###########

:Semantic name: https://openminds.om-i.org/types/SpecimenAge

:Display as: Specimen age


------------

------------

Properties
##########

:Required: `age <age_heading_>`_, `reference <reference_heading_>`_
:Optional:

------------

.. _age_heading:

***
age
***

Time of life or existence at which some particular qualification, capacity or event arises.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/age
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the age value.

`BACK TO TOP <SpecimenAge_>`_

------------

.. _reference_heading:

*********
reference
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/reference
   :value type: | linked object of type
                | `AgeReference <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/ageReference.html>`_
   :instructions: Enter the age reference for the specified age value.

`BACK TO TOP <SpecimenAge_>`_

------------

