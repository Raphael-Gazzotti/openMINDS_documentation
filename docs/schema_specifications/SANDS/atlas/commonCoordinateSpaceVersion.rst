############################
CommonCoordinateSpaceVersion
############################

:Semantic name: https://openminds.om-i.org/types/CommonCoordinateSpaceVersion

:Display as: Common coordinate space version


For this schema openMINDS provides a `library of instances <https://openminds-documentation.readthedocs.io/en/v4.0/instance_libraries/commonCoordinateSpaceVersions.html>`_.

------------

------------

Properties
##########

:Required: `accessibility <accessibility_heading_>`_, `anatomicalAxesOrientation <anatomicalAxesOrientation_heading_>`_, `axesOrigin <axesOrigin_heading_>`_, `fullDocumentation <fullDocumentation_heading_>`_, `nativeUnit <nativeUnit_heading_>`_, `releaseDate <releaseDate_heading_>`_, `shortName <shortName_heading_>`_, `versionIdentifier <versionIdentifier_heading_>`_, `versionInnovation <versionInnovation_heading_>`_
:Optional: `abbreviation <abbreviation_heading_>`_, `author <author_heading_>`_, `copyright <copyright_heading_>`_, `custodian <custodian_heading_>`_, `defaultImage <defaultImage_heading_>`_, `description <description_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `fullName <fullName_heading_>`_, `funding <funding_heading_>`_, `homepage <homepage_heading_>`_, `howToCite <howToCite_heading_>`_, `isAlternativeVersionOf <isAlternativeVersionOf_heading_>`_, `isNewVersionOf <isNewVersionOf_heading_>`_, `keyword <keyword_heading_>`_, `license <license_heading_>`_, `ontologyIdentifier <ontologyIdentifier_heading_>`_, `otherContribution <otherContribution_heading_>`_, `relatedPublication <relatedPublication_heading_>`_, `repository <repository_heading_>`_, `supportChannel <supportChannel_heading_>`_, `usedSpecimen <usedSpecimen_heading_>`_

------------

.. _abbreviation_heading:

************
abbreviation
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/abbreviation
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the official abbreviation of this common coordinate space version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _accessibility_heading:

*************
accessibility
*************

Level to which something is accessible to someone or something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/accessibility
   :value type: | linked object of type
                | `ProductAccessibility <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/productAccessibility.html>`_
   :instructions: Add the accessibility of the data for this research product version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _anatomicalAxesOrientation_heading:

*************************
anatomicalAxesOrientation
*************************

Relation between reference planes used in anatomy and mathematics.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/anatomicalAxesOrientation
   :value type: | linked object of type
                | `AnatomicalAxesOrientation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/anatomicalAxesOrientation.html>`_
   :instructions: Add the axes orientation denoted in standard anatomical terms of direction (stated as XYZ) for this common coordinate space version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _author_heading:

******
author
******

Creator of a literary or creative work, as well as a dataset publication.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/author
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add all parties that contributed to this common coordinate space version as authors. Note that these authors will overwrite the author list provided for the overarching common coordinate space.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _axesOrigin_heading:

**********
axesOrigin
**********

Special point in a coordinate system used as a fixed point of reference for the geometry of the surrounding space.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/axesOrigin
   :value type: | embedded object array \(2-3\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the origin (central point where all axes intersect) of this common coordinate space version for two-dimensional spaces as [x, y] or for three-dimensional space as [x, y, z].

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _copyright_heading:

*********
copyright
*********

Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/copyright
   :value type: | embedded object of type
                | `Copyright <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/copyright.html>`_
   :instructions: Enter the copyright information of this research product version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _custodian_heading:

*********
custodian
*********

The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/custodian
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add all parties that fulfill the role of a custodian for the research product version (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _defaultImage_heading:

************
defaultImage
************

Two or three dimensional image that particluarly represents a specific coordinate space.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/defaultImage
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/file.html>`_
   :instructions: Add all image files used as visual representation of this common coordinate space version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _description_heading:

***********
description
***********

Longer statement or account giving the characteristics of someone or something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/description
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a description (or abstract) of this research product version. Note that this version specific description will overwrite the description for the overarching dataset.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/digitalIdentifier
   :value type: | linked object of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/DOI.html>`_, `ISBN <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/ISBN.html>`_ or `RRID <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/RRID.html>`_
   :instructions: Add the globally unique and persistent digital identifier of this research product version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _fullDocumentation_heading:

*****************
fullDocumentation
*****************

Non-abridged instructions, comments, and information for using a particular product.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/fullDocumentation
   :value type: | linked object of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/DOI.html>`_, `File <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/file.html>`_, `ISBN <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/ISBN.html>`_ or `WebResource <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/webResource.html>`_
   :instructions: Add the publication or file that acts as the full documentation of this research product version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

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
   :instructions: Enter a descriptive full name (or title) for this research product version. Note that this version specific full name will overwrite the full name for the overarching dataset.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _funding_heading:

*******
funding
*******

Money provided by a legal person for a particular purpose.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/funding
   :value type: | linked object array \(1-N\) of type
                | `Funding <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/funding.html>`_
   :instructions: Add all funding information of this research product version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

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
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this research product version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _howToCite_heading:

*********
howToCite
*********

Preferred format for citing a particular object or legal person.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/howToCite
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter the preferred citation text for this research product version. Leave blank if citation text can be extracted from the assigned digital identifier.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _isAlternativeVersionOf_heading:

**********************
isAlternativeVersionOf
**********************

Reference to an original form where the essence was preserved, but presented in an alternative form.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/isAlternativeVersionOf
   :value type: | linked object array \(1-N\) of type
                | `CommonCoordinateSpaceVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/commonCoordinateSpaceVersion.html>`_
   :instructions: Add all common coordinate space versions that can be used alternatively to this common coordinate space version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _isNewVersionOf_heading:

**************
isNewVersionOf
**************

Reference to a previous (potentially outdated) particular form of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/isNewVersionOf
   :value type: | linked object of type
                | `CommonCoordinateSpaceVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/atlas/commonCoordinateSpaceVersion.html>`_
   :instructions: Add the common coordinate space version preceding this common coordinate space version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _keyword_heading:

*******
keyword
*******

Significant word or concept that are representative of something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/keyword
   :value type: | linked object array \(1-N\) of type
                | `ActionStatusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/actionStatusType.html>`_, `AgeCategory <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/ageCategory.html>`_, `AnalysisTechnique <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/analysisTechnique.html>`_, `AnatomicalAxesOrientation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/anatomicalAxesOrientation.html>`_, `AnatomicalIdentificationType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/anatomicalIdentificationType.html>`_, `AnatomicalPlane <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/anatomicalPlane.html>`_, `AnnotationCriteriaType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/annotationCriteriaType.html>`_, `AnnotationType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/annotationType.html>`_, `AtlasType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/atlasType.html>`_, `AuditoryStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/auditoryStimulusType.html>`_, `BiologicalOrder <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/biologicalOrder.html>`_, `BiologicalProcess <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/biologicalProcess.html>`_, `BiologicalSex <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/biologicalSex.html>`_, `BreedingType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/breedingType.html>`_, `CellCultureType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/cellCultureType.html>`_, `CellType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/cellType.html>`_, `ChemicalMixtureType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/chemicalMixtureType.html>`_, `Colormap <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/colormap.html>`_, `ContributionType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/contributionType.html>`_, `CranialWindowConstructionType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/cranialWindowConstructionType.html>`_, `CranialWindowReinforcementType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/cranialWindowReinforcementType.html>`_, `CriteriaQualityType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/criteriaQualityType.html>`_, `DataType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/dataType.html>`_, `DeviceType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/deviceType.html>`_, `DifferenceMeasure <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/differenceMeasure.html>`_, `Disease <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/disease.html>`_, `DiseaseModel <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/diseaseModel.html>`_, `EducationalLevel <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/educationalLevel.html>`_, `ElectricalStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/electricalStimulusType.html>`_, `EthicsAssessment <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/ethicsAssessment.html>`_, `ExperimentalApproach <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/experimentalApproach.html>`_, `FileBundleGrouping <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/fileBundleGrouping.html>`_, `FileRepositoryType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/fileRepositoryType.html>`_, `FileUsageRole <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/fileUsageRole.html>`_, `GeneticStrainType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/geneticStrainType.html>`_, `GustatoryStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/gustatoryStimulusType.html>`_, `Handedness <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/handedness.html>`_, `Language <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/language.html>`_, `Laterality <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/laterality.html>`_, `LearningResourceType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/learningResourceType.html>`_, `MRIPulseSequence <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/MRIPulseSequence.html>`_, `MRIWeighting <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/MRIWeighting.html>`_, `MeasuredQuantity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/measuredQuantity.html>`_, `MeasuredSignalType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/measuredSignalType.html>`_, `MetaDataModelType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/metaDataModelType.html>`_, `ModelAbstractionLevel <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/modelAbstractionLevel.html>`_, `ModelScope <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/modelScope.html>`_, `MolecularEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/molecularEntity.html>`_, `OlfactoryStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/olfactoryStimulusType.html>`_, `OperatingDevice <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/operatingDevice.html>`_, `OperatingSystem <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/operatingSystem.html>`_, `OpticalStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/opticalStimulusType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/organ.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/organismSubstance.html>`_, `OrganismSystem <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/organismSystem.html>`_, `PatchClampVariation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/patchClampVariation.html>`_, `PreparationType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/preparationType.html>`_, `ProductAccessibility <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/productAccessibility.html>`_, `ProgrammingLanguage <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/programmingLanguage.html>`_, `QualitativeOverlap <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/qualitativeOverlap.html>`_, `SemanticDataType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/semanticDataType.html>`_, `Service <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/service.html>`_, `SetupType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/setupType.html>`_, `SoftwareApplicationCategory <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/softwareApplicationCategory.html>`_, `SoftwareFeature <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/softwareFeature.html>`_, `Species <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/species.html>`_, `StimulationApproach <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/stimulationApproach.html>`_, `StimulationTechnique <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/stimulationTechnique.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/subcellularEntity.html>`_, `SubjectAttribute <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/subjectAttribute.html>`_, `TactileStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/tactileStimulusType.html>`_, `Technique <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/technique.html>`_, `TermSuggestion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/termSuggestion.html>`_, `Terminology <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/terminology.html>`_, `TissueSampleAttribute <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/tissueSampleAttribute.html>`_, `TissueSampleType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/tissueSampleType.html>`_, `TypeOfUncertainty <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/typeOfUncertainty.html>`_, `UBERONParcellation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/UBERONParcellation.html>`_, `UnitOfMeasurement <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/unitOfMeasurement.html>`_ or `VisualStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/visualStimulusType.html>`_
   :instructions: Add all relevant keywords to this research product version either by adding controlled terms or by suggesting new terms.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _license_heading:

*******
license
*******

Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/license
   :value type: | linked object of type
                | `License <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/license.html>`_
   :instructions: Add the license of this common coordinate space version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _nativeUnit_heading:

**********
nativeUnit
**********

Determinate quantity used in the original measurement.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/nativeUnit
   :value type: | linked object of type
                | `UnitOfMeasurement <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/unitOfMeasurement.html>`_
   :instructions: Add the native unit that is used for this common coordinate space version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _ontologyIdentifier_heading:

******************
ontologyIdentifier
******************

Term or code used to identify something or someone registered within a particular ontology.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/ontologyIdentifier
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this common coordinate space version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _otherContribution_heading:

*****************
otherContribution
*****************

Giving or supplying of something (such as money or time) as a part or share other than what is covered elsewhere.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/otherContribution
   :value type: | embedded object array \(1-N\) of type
                | `Contribution <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/contribution.html>`_
   :instructions: Add any other contributions to this research product version that are not covered under 'author'/'developer' or 'custodian'.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _relatedPublication_heading:

******************
relatedPublication
******************

Reference to something that was made available for the general public to see or buy.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/relatedPublication
   :value type: | linked object array \(1-N\) of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/DOI.html>`_, `HANDLE <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/HANDLE.html>`_, `ISBN <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/ISBN.html>`_, `ISSN <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/ISSN.html>`_, `Book <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/publications/book.html>`_, `Chapter <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/publications/chapter.html>`_ or `ScholarlyArticle <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/publications/scholarlyArticle.html>`_
   :instructions: Add all further publications besides the full documentation that provide the original context for the production of this research product version (e.g., an original research article that used or produced the data of this research product version).

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _releaseDate_heading:

***********
releaseDate
***********

Fixed date on which a product is due to become or was made available for the general public to see or buy

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/releaseDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date (actual or intended) on which this research product version was first release, formatted as 'YYYY-MM-DD'.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _repository_heading:

**********
repository
**********

Place, room, or container where something is deposited or stored.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/repository
   :value type: | linked object of type
                | `FileRepository <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/fileRepository.html>`_
   :instructions: Add the file repository of this research product version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

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
   :instructions: Enter a short name (or alias) for this research product version that could be used as a shortened display title (e.g., for web services with too little space to display the full name).

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _supportChannel_heading:

**************
supportChannel
**************

Way of communication used to interact with users or customers.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/supportChannel
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter all channels through which a user can receive support for handling this research product version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _usedSpecimen_heading:

************
usedSpecimen
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/usedSpecimen
   :value type: | linked object array \(1-N\) of type
                | `Subject <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/subject.html>`_, `SubjectGroup <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/subjectGroup.html>`_, `TissueSample <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/tissueSample.html>`_ or `TissueSampleCollection <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/tissueSampleCollection.html>`_
   :instructions: Add the specimen that was used for the creation of this common coordinate space version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _versionIdentifier_heading:

*****************
versionIdentifier
*****************

Term or code used to identify the version of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/versionIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the version identifier of this research product version.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

.. _versionInnovation_heading:

*****************
versionInnovation
*****************

Documentation on what changed in comparison to a previously published form of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/versionInnovation
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a short description (or summary) of the novelties/peculiarities of this research product version in comparison to its preceding versions. If this research product version is the first version, you can enter the following disclaimer 'This is the first version of this research product'.

`BACK TO TOP <CommonCoordinateSpaceVersion_>`_

------------

