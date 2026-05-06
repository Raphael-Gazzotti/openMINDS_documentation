###########
StockNumber
###########

:Semantic name: https://openminds.om-i.org/types/StockNumber

:Display as: Stock number


------------

------------

Properties
##########

:Required: `identifier <identifier_heading_>`_, `vendor <vendor_heading_>`_
:Optional:

------------

.. _identifier_heading:

**********
identifier
**********

Term or code used to identify something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/identifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the stock number of an item provided by a store or company.

`BACK TO TOP <StockNumber_>`_

------------

.. _vendor_heading:

******
vendor
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/vendor
   :value type: | linked object of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/organization.html>`_
   :instructions: Add the vendor that has the item with this identifier in stock.

`BACK TO TOP <StockNumber_>`_

------------

