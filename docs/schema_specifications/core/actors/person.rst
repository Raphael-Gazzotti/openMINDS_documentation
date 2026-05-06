######
Person
######

:Semantic name: https://openminds.ebrains.eu/core/Person

:Display as: Person

Structured information on a person.


------------

------------

Properties
##########

:Required: `givenName <givenName_heading_>`_
:Optional: `affiliation <affiliation_heading_>`_, `contactInformation <contactInformation_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `familyName <familyName_heading_>`_

------------

.. _affiliation_heading:

***********
affiliation
***********

Declaration of a person being closely associated to an organization.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/affiliation
   :value type: | embedded object array \(1-N\) of type
                | `Affiliation <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/core/actors/affiliation.html>`_
   :instructions: Add the current and, if necessary, past affiliations of this person

`BACK TO TOP <Person_>`_

------------

.. _contactInformation_heading:

******************
contactInformation
******************

Any available way used to contact a person or business (e.g., address, phone number, email address, etc.).

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contactInformation
   :value type: | linked object of type
                | `ContactInformation <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/core/actors/contactInformation.html>`_
   :instructions: Add the contact information of this person.

`BACK TO TOP <Person_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object array \(1-N\) of type
                | `ORCID <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/core/miscellaneous/ORCID.html>`_
   :instructions: Add one or several globally unique and persistent digital identifier for this person.

`BACK TO TOP <Person_>`_

------------

.. _familyName_heading:

**********
familyName
**********

Name borne in common by members of a family.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/familyName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the family name of this person.

`BACK TO TOP <Person_>`_

------------

.. _givenName_heading:

*********
givenName
*********

Name given to a person, including all potential middle names, but excluding the family name.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/givenName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the given name of this person.

`BACK TO TOP <Person_>`_

------------

