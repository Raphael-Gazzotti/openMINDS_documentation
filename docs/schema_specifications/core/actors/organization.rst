############
Organization
############

:Semantic name: https://openminds.om-i.org/types/Organization

:Display as: Organization

An entity comprised of one or more natural persons with a particular purpose. [adapted from Wikipedia](https://en.wikipedia.org/wiki/Organization)


------------

------------

Properties
##########

:Required: `countryOfFormation <countryOfFormation_heading_>`_, `name <name_heading_>`_, `type <type_heading_>`_
:Optional: `acronym <acronym_heading_>`_, `alternateName <alternateName_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `hasParent <hasParent_heading_>`_, `homepage <homepage_heading_>`_, `jurisdiction <jurisdiction_heading_>`_, `location <location_heading_>`_, `membership <membership_heading_>`_

------------

.. _acronym_heading:

*******
acronym
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/acronym
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the acronym of this organization.

`BACK TO TOP <Organization_>`_

------------

.. _alternateName_heading:

*************
alternateName
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/alternateName
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter any other known name or acronym of this organization.

`BACK TO TOP <Organization_>`_

------------

.. _countryOfFormation_heading:

******************
countryOfFormation
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/countryOfFormation
   :value type: | linked object of type
                | `SovereignState <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/sovereignState.html>`_
   :instructions: Add the country where the organization was formed.

`BACK TO TOP <Organization_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/digitalIdentifier
   :value type: | linked object array \(1-N\) of type
                | `GenericIdentifier <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/digitalIdentifier/genericIdentifier.html>`_, `ISNI <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/digitalIdentifier/ISNI.html>`_, `LEI <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/digitalIdentifier/LEI.html>`_, `RORID <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/digitalIdentifier/RORID.html>`_ or `RRID <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/digitalIdentifier/RRID.html>`_
   :instructions: Add all globally unique and persistent digital identifier of this organization.

`BACK TO TOP <Organization_>`_

------------

.. _hasParent_heading:

*********
hasParent
*********

Reference to a parent object or legal person.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/hasParent
   :value type: | linked object array \(1-N\) of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/actors/organization.html>`_
   :instructions: Add all parent organizations of this organization.

`BACK TO TOP <Organization_>`_

------------

.. _homepage_heading:

********
homepage
********

Main website of something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/homepage
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this organization.

`BACK TO TOP <Organization_>`_

------------

.. _jurisdiction_heading:

************
jurisdiction
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/jurisdiction
   :value type: | linked object of type
                | `SovereignState <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/sovereignState.html>`_ or `SupranationalBody <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/supranationalBody.html>`_
   :instructions: Add the jurisdiction under which the organization operates.

`BACK TO TOP <Organization_>`_

------------

.. _location_heading:

********
location
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/location
   :value type: | embedded object of type
                | `Location <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/miscellaneous/location.html>`_
   :instructions: Add the headquarters location of this organization.

`BACK TO TOP <Organization_>`_

------------

.. _membership_heading:

**********
membership
**********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/membership
   :value type: | embedded object array \(1-N\) of type
                | `Membership <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/miscellaneous/membership.html>`_
   :instructions: Add all membership records (one per member) for this organization. Who is considered a qualified member is typically defined in the organization’s membership agreements.

`BACK TO TOP <Organization_>`_

------------

.. _name_heading:

****
name
****

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the organization’s preferred name for use in international contexts.

`BACK TO TOP <Organization_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/type
   :value type: | linked object of type
                | `OrganizationType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/organizationType.html>`_
   :instructions: Add the type of this organization (legal entity or organizational unit).

`BACK TO TOP <Organization_>`_

------------

