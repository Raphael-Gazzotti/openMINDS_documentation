#############
ProductSource
#############

:Semantic name: https://openminds.om-i.org/types/ProductSource

:Display as: Product source

Structured information about the source of a chemical substance or mixture.


------------

------------

Properties
##########

:Required: `productName <productName_heading_>`_, `provider <provider_heading_>`_
:Optional: `digitalIdentifier <digitalIdentifier_heading_>`_, `identifier <identifier_heading_>`_, `purity <purity_heading_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/digitalIdentifier
   :value type: | linked object of type
                | `RRID <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/RRID.html>`_
   :instructions: Add the globally unique and persistent digital identifier of this product.

`BACK TO TOP <ProductSource_>`_

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
   :instructions: Enter the identifier for this product, excluding its RRID (e.g., a catalog number).

`BACK TO TOP <ProductSource_>`_

------------

.. _productName_heading:

***********
productName
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/productName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name of this product as stated by the 'provider'.

`BACK TO TOP <ProductSource_>`_

------------

.. _provider_heading:

********
provider
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/provider
   :value type: | linked object of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add the party (private, commercial or industrial) that provided this product.

`BACK TO TOP <ProductSource_>`_

------------

.. _purity_heading:

******
purity
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/purity
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the purity of the product as stated by the 'provider'.

`BACK TO TOP <ProductSource_>`_

------------

