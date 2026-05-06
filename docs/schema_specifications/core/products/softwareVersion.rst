###############
SoftwareVersion
###############

:Semantic name: https://openminds.ebrains.eu/core/SoftwareVersion

:Display as: Software version


------------

------------

Properties
##########

:Required: `accessibility <accessibility_heading_>`_, `applicationCategory <applicationCategory_heading_>`_, `device <device_heading_>`_, `feature <feature_heading_>`_, `fullDocumentation <fullDocumentation_heading_>`_, `language <language_heading_>`_, `license <license_heading_>`_, `operatingSystem <operatingSystem_heading_>`_, `programmingLanguage <programmingLanguage_heading_>`_, `releaseDate <releaseDate_heading_>`_, `shortName <shortName_heading_>`_, `versionIdentifier <versionIdentifier_heading_>`_, `versionInnovation <versionInnovation_heading_>`_
:Optional: `copyright <copyright_heading_>`_, `custodian <custodian_heading_>`_, `description <description_heading_>`_, `developer <developer_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `fullName <fullName_heading_>`_, `funding <funding_heading_>`_, `hasComponent <hasComponent_heading_>`_, `homepage <homepage_heading_>`_, `howToCite <howToCite_heading_>`_, `inputFormat <inputFormat_heading_>`_, `isAlternativeVersionOf <isAlternativeVersionOf_heading_>`_, `isNewVersionOf <isNewVersionOf_heading_>`_, `keyword <keyword_heading_>`_, `otherContribution <otherContribution_heading_>`_, `outputFormat <outputFormat_heading_>`_, `relatedPublication <relatedPublication_heading_>`_, `repository <repository_heading_>`_, `requirement <requirement_heading_>`_, `supportChannel <supportChannel_heading_>`_

------------

.. _accessibility_heading:

*************
accessibility
*************

Level to which something is accessible to someone or something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/accessibility
   :value type: | linked object of type
                | `ProductAccessibility <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/productAccessibility.html>`_
   :instructions: Add the accessibility of the data for this research product version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _applicationCategory_heading:

*******************
applicationCategory
*******************

Distinct class that groups software programs which perform a similar task or set of tasks.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/applicationCategory
   :value type: | linked object array \(1-N\) of type
                | `SoftwareApplicationCategory <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/softwareApplicationCategory.html>`_
   :instructions: Add all categories to which this software version belongs.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _copyright_heading:

*********
copyright
*********

Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/copyright
   :value type: | embedded object of type
                | `Copyright <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/copyright.html>`_
   :instructions: Add the copyright information of this research product version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _custodian_heading:

*********
custodian
*********

The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/custodian
   :value type: | linked object array \(1-N\) of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add one or several custodians (person or organization) that are responsible for this research product version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _description_heading:

***********
description
***********

Longer statement or account giving the characteristics of someone or something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: If necessary, enter a version specific description (abstract) for this research product version (max. 2000 characters, incl. spaces; no references). If left blank, the research product version will inherit the 'description' of it's corresponding research product.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _developer_heading:

*********
developer
*********

Legal person that creates or improves products or services (e.g., software, applications, etc.).

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/developer
   :value type: | linked object array \(1-N\) of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/actors/person.html>`_
   :instructions: If necessary, add one or several developers (person or organization) that contributed to the code implementation of this software version. Note that these developers will overwrite the once provided in the software product this version belongs to.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _device_heading:

******
device
******

Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/device
   :value type: | linked object array \(1-N\) of type
                | `OperatingDevice <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/operatingDevice.html>`_
   :instructions: Add all hardware devices compatible with this software version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/DOI.html>`_ or `SWHID <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/SWHID.html>`_
   :instructions: Add the globally unique and persistent digital identifier of this research product version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _feature_heading:

*******
feature
*******

Structure, form, or appearance that characterizes something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/feature
   :value type: | linked object array \(1-N\) of type
                | `SoftwareFeature <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/softwareFeature.html>`_
   :instructions: Add all distinguishing characteristics of this software version (e.g. performance, portability, or functionality).

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _fullDocumentation_heading:

*****************
fullDocumentation
*****************

Non-abridged instructions, comments, and information for using a particular product.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fullDocumentation
   :value type: | linked object of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/DOI.html>`_, `File <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/file.html>`_ or `URL <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/URL.html>`_
   :instructions: Add the DOI, file or URL that points to a full documentation of this research product version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _fullName_heading:

********
fullName
********

Whole, non-abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fullName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: If necessary, enter a version specific descriptive full name (title) for this research product version. If left blank, the research product version will inherit the 'fullName' of it's corresponding research product.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _funding_heading:

*******
funding
*******

Money provided by a legal person for a particular purpose.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/funding
   :value type: | linked object array \(1-N\) of type
                | `Funding <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/funding.html>`_
   :instructions: Add all funding information of this research product version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _hasComponent_heading:

************
hasComponent
************

Reference to an element of a collection.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasComponent
   :value type: | linked object array \(1-N\) of type
                | `SoftwareVersion <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/products/softwareVersion.html>`_
   :instructions: Add all software versions that supplement this software version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _homepage_heading:

********
homepage
********

Main website of something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/homepage
   :value type: | linked object of type
                | `URL <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/URL.html>`_
   :instructions: Add the uniform resource locator (URL) to the homepage of this research product version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _howToCite_heading:

*********
howToCite
*********

Preferred format for citing a particular object or legal person.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/howToCite
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter the preferred citation text for this research product version. Leave blank if citation text can be extracted from the assigned digital identifier.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _inputFormat_heading:

***********
inputFormat
***********

Format of data that is put into a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/inputFormat
   :value type: | linked object array \(1-N\) of type
                | `ContentType <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/contentType.html>`_
   :instructions: Add the content types of all possible input formats for this software version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _isAlternativeVersionOf_heading:

**********************
isAlternativeVersionOf
**********************

Reference to an original form where the essence was preserved, but presented in an alternative form.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isAlternativeVersionOf
   :value type: | linked object array \(1-N\) of type
                | `SoftwareVersion <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/products/softwareVersion.html>`_
   :instructions: Add all software versions that can be used alternatively to this software version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _isNewVersionOf_heading:

**************
isNewVersionOf
**************

Reference to a previous (potentially outdated) particular form of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isNewVersionOf
   :value type: | linked object of type
                | `SoftwareVersion <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/products/softwareVersion.html>`_
   :instructions: Add the software version preceding this software version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _keyword_heading:

*******
keyword
*******

Significant word or concept that are representative of something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/keyword
   :value type: | string array \(1-5\)
                | formatting: text/plain; singleline
   :instructions: Enter custom keywords to this research product version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _language_heading:

********
language
********

System of communication (words, their pronunciation, and the methods of combining them) used and understood by a particular community.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/language
   :value type: | linked object array \(1-N\) of type
                | `Language <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/language.html>`_
   :instructions: Add all languages supported by this software version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _license_heading:

*******
license
*******

Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/license
   :value type: | linked object array \(1-N\) of type
                | `License <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/license.html>`_
   :instructions: Add at least one license for this software version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _operatingSystem_heading:

***************
operatingSystem
***************

Software that controls the operation of a computer and directs the processing of programs.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/operatingSystem
   :value type: | linked object array \(1-N\) of type
                | `OperatingSystem <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/operatingSystem.html>`_
   :instructions: Add all operating systems supported by this software version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _otherContribution_heading:

*****************
otherContribution
*****************

Giving or supplying of something (such as money or time) as a part or share other than what is covered elsewhere.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/otherContribution
   :value type: | embedded object array \(1-N\) of type
                | `Contribution <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/actors/contribution.html>`_
   :instructions: Add the contributions for each involved person or organization going beyond being an author, custodian or developer of this research product version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _outputFormat_heading:

************
outputFormat
************

Format of data that comes out of, is delivered or produced by a process or machine.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/outputFormat
   :value type: | linked object array \(1-N\) of type
                | `ContentType <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/contentType.html>`_
   :instructions: Add the content types of all possible input formats for this software version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _programmingLanguage_heading:

*******************
programmingLanguage
*******************

Distinct set of instructions for computer programs in order to produce various kinds of output.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/programmingLanguage
   :value type: | linked object array \(1-N\) of type
                | `ProgrammingLanguage <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/programmingLanguage.html>`_
   :instructions: Add all programming languages used for this software version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _relatedPublication_heading:

******************
relatedPublication
******************

Reference to something that was made available for the general public to see or buy.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relatedPublication
   :value type: | linked object array \(1-N\) of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/DOI.html>`_ or `ISBN <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/ISBN.html>`_
   :instructions: Add further publications besides the documentation (e.g. an original research article) providing the original context for the production of this research product version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _releaseDate_heading:

***********
releaseDate
***********

Fixed date on which a product is due to become or was made available for the general public to see or buy

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/releaseDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date (actual or intended) of the first broadcast/publication of this research product version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _repository_heading:

**********
repository
**********

Place, room, or container where something is deposited or stored.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/repository
   :value type: | linked object of type
                | `FileRepository <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/fileRepository.html>`_
   :instructions: Add the file repository of this research product version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _requirement_heading:

***********
requirement
***********

Something essential to the existence, occurrence or function of something else.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/requirement
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter all requirements of this software version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _shortName_heading:

*********
shortName
*********

Shortened or fully abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/shortName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short name (alias) for this research product version (max. 30 characters, no space).

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _supportChannel_heading:

**************
supportChannel
**************

Way of communication used to interact with users or customers.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/supportChannel
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter all channels through which a user can receive support for handling this research product.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _versionIdentifier_heading:

*****************
versionIdentifier
*****************

Term or code used to identify the version of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/versionIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the version identifier of this research product version.

`BACK TO TOP <SoftwareVersion_>`_

------------

.. _versionInnovation_heading:

*****************
versionInnovation
*****************

Documentation on what changed in comparison to a previously published form of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/versionInnovation
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a summary/description of the novelties/peculiarities of this research product version in comparison to other versions of it's research product. If this research product version is the first released version, you can enter the following disclaimer 'This is the first version of this research product.'

`BACK TO TOP <SoftwareVersion_>`_

------------

