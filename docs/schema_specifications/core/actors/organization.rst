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

:Required: `fullName <fullName_heading_>`_
:Optional: `affiliation <affiliation_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `hasParent <hasParent_heading_>`_, `homepage <homepage_heading_>`_, `shortName <shortName_heading_>`_

------------

.. _affiliation_heading:

***********
affiliation
***********

Declaration of a person being closely associated to an organization.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/affiliation
   :value type: | embedded object array \(1-N\) of type
                | `Affiliation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/affiliation.html>`_
   :instructions: Enter all current and, if necessary, past affiliations of this organization.

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
                | `GRIDID <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/GRIDID.html>`_, `RORID <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/RORID.html>`_ or `RRID <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/RRID.html>`_
   :instructions: Add all globally unique and persistent digital identifier of this organization.

`BACK TO TOP <Organization_>`_

------------

.. _fullName_heading:

********
fullName
********

Whole, non-abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/fullName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the full name of this organization.

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
                | `Organization <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/organization.html>`_
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

.. _shortName_heading:

*********
shortName
*********

Shortened or fully abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/shortName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short name (or alias) for this organization that could be used as a shortened display title (e.g., for web services with too little space to display the full name).

`BACK TO TOP <Organization_>`_

------------

