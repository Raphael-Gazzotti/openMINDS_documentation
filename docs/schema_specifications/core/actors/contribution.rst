############
Contribution
############

:Semantic name: https://openminds.om-i.org/types/Contribution

:Display as: Contribution

Structured information on the contribution made to a research product.


------------

------------

Properties
##########

:Required: `contributor <contributor_heading_>`_, `type <type_heading_>`_
:Optional:

------------

.. _contributor_heading:

***********
contributor
***********

Legal person that gave or supplied something as a part or share.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/contributor
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html>`_
   :instructions: Add all contributors who made this contribution, in the desired display order.

`BACK TO TOP <Contribution_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/type
   :value type: | linked object of type
                | `ContributionType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/contributionType.html>`_
   :instructions: Add the type of contribution.

`BACK TO TOP <Contribution_>`_

------------

