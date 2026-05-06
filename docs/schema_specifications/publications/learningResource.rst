################
LearningResource
################

:Semantic name: https://openminds.om-i.org/types/LearningResource

:Display as: Learning resource


------------

------------

Properties
##########

:Required: `about <about_heading_>`_, `name <name_heading_>`_, `publicationDate <publicationDate_heading_>`_
:Optional: `IRI <IRI_heading_>`_, `abstract <abstract_heading_>`_, `citedPublication <citedPublication_heading_>`_, `contribution <contribution_heading_>`_, `contributorAffiliation <contributorAffiliation_heading_>`_, `copyright <copyright_heading_>`_, `creationDate <creationDate_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `educationalLevel <educationalLevel_heading_>`_, `funding <funding_heading_>`_, `keyword <keyword_heading_>`_, `learningOutcome <learningOutcome_heading_>`_, `modificationDate <modificationDate_heading_>`_, `order <order_heading_>`_, `prerequisite <prerequisite_heading_>`_, `requiredTime <requiredTime_heading_>`_, `topic <topic_heading_>`_, `type <type_heading_>`_, `usageCondition <usageCondition_heading_>`_, `versionIdentifier <versionIdentifier_heading_>`_

------------

.. _IRI_heading:

***
IRI
***

Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/IRI
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to this creative work.

`BACK TO TOP <LearningResource_>`_

------------

.. _about_heading:

*****
about
*****

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/about
   :value type: | linked object array \(1-N\) of type
                | `ValidationTest <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/computation/validationTest.html>`_, `ValidationTestVersion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/computation/validationTestVersion.html>`_, `WorkflowRecipe <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/computation/workflowRecipe.html>`_, `WorkflowRecipeVersion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/computation/workflowRecipeVersion.html>`_, `Dataset <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/products/dataset.html>`_, `DatasetVersion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/products/datasetVersion.html>`_, `Interface <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/products/interface.html>`_, `InterfaceVersion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/products/interfaceVersion.html>`_, `MetaDataModel <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/products/metaDataModel.html>`_, `MetaDataModelVersion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/products/metaDataModelVersion.html>`_, `Model <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/products/model.html>`_, `ModelVersion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/products/modelVersion.html>`_, `Software <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/products/software.html>`_, `SoftwareVersion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/products/softwareVersion.html>`_, `LivePaper <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/publications/livePaper.html>`_, `LivePaperVersion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/publications/livePaperVersion.html>`_, `AnatomicalAtlas <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/atlas/anatomicalAtlas.html>`_, `AnatomicalAtlasVersion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/atlas/anatomicalAtlasVersion.html>`_, `CommonCoordinateFramework <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/atlas/commonCoordinateFramework.html>`_ or `CommonCoordinateFrameworkVersion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/atlas/commonCoordinateFrameworkVersion.html>`_
   :instructions: Add all research product (versions) this learning resource are about. Note that the learning resource should supplement the usage of the research product (versions) with e.g., instructions on their usage or additional information.

`BACK TO TOP <LearningResource_>`_

------------

.. _abstract_heading:

********
abstract
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/abstract
   :value type: | string
                | formatting: text/plain; multiline
   :instructions: Enter the abstract or a short description of the creative work.

`BACK TO TOP <LearningResource_>`_

------------

.. _citedPublication_heading:

****************
citedPublication
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/citedPublication
   :value type: | linked object array \(1-N\) of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/digitalIdentifier/DOI.html>`_ or `ISBN <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/digitalIdentifier/ISBN.html>`_
   :instructions: Add all references this creative work cites.

`BACK TO TOP <LearningResource_>`_

------------

.. _contribution_heading:

************
contribution
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/contribution
   :value type: | embedded object array \(1-N\) of type
                | `Contribution <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/actors/contribution.html>`_
   :instructions: Add all individual, organisational, or consortial contributions to this creative work.

`BACK TO TOP <LearningResource_>`_

------------

.. _contributorAffiliation_heading:

**********************
contributorAffiliation
**********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/contributorAffiliation
   :value type: | embedded object array \(1-N\) of type
                | `Affiliation <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/actors/affiliation.html>`_
   :instructions: Add all affiliations for the individual contributors to this research product version.

`BACK TO TOP <LearningResource_>`_

------------

.. _copyright_heading:

*********
copyright
*********

Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/copyright
   :value type: | embedded object of type
                | `Copyright <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/data/copyright.html>`_
   :instructions: Enter the copyright information of this creative work.

`BACK TO TOP <LearningResource_>`_

------------

.. _creationDate_heading:

************
creationDate
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/creationDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date on which this creative work was created, formatted as '2023-02-07'.

`BACK TO TOP <LearningResource_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/digitalIdentifier
   :value type: | linked object of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/digitalIdentifier/DOI.html>`_
   :instructions: Add the globally unique and persistent digital identifier of this creative work.

`BACK TO TOP <LearningResource_>`_

------------

.. _educationalLevel_heading:

****************
educationalLevel
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/educationalLevel
   :value type: | linked object of type
                | `EducationalLevel <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/educationalLevel.html>`_
   :instructions: Add the educational level that best summarizes the prerequisite of this learning resource.

`BACK TO TOP <LearningResource_>`_

------------

.. _funding_heading:

*******
funding
*******

Money provided by a legal person for a particular purpose.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/funding
   :value type: | linked object array \(1-N\) of type
                | `Funding <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/miscellaneous/funding.html>`_
   :instructions: Add all funding information of this creative work.

`BACK TO TOP <LearningResource_>`_

------------

.. _keyword_heading:

*******
keyword
*******

Significant word or concept that are representative of something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/keyword
   :value type: | linked object array \(1-N\) of type
                | `AccessChannel <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/accessChannel.html>`_, `AccessEligibilityType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/accessEligibilityType.html>`_, `AccessForm <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/accessForm.html>`_, `AccessProcessType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/accessProcessType.html>`_, `ActionStatusType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/actionStatusType.html>`_, `AgeCategory <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/ageCategory.html>`_, `AgeReference <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/ageReference.html>`_, `AnalysisTechnique <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/analysisTechnique.html>`_, `AnatomicalAxesOrientation <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/anatomicalAxesOrientation.html>`_, `AnatomicalCavity <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/anatomicalCavity.html>`_, `AnatomicalIdentificationType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/anatomicalIdentificationType.html>`_, `AnatomicalPlane <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/anatomicalPlane.html>`_, `AnnotationCriteriaType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/annotationCriteriaType.html>`_, `AnnotationType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/annotationType.html>`_, `AtlasType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/atlasType.html>`_, `AuditoryStimulusType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/auditoryStimulusType.html>`_, `BiologicalOrder <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/biologicalOrder.html>`_, `BiologicalProcess <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/biologicalProcess.html>`_, `BiologicalSex <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/biologicalSex.html>`_, `BreedingType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/breedingType.html>`_, `CellCultureType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/cellCultureType.html>`_, `CellType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/cellType.html>`_, `ChemicalMixtureType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/chemicalMixtureType.html>`_, `Colormap <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/colormap.html>`_, `CommunicationInterfaceType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/communicationInterfaceType.html>`_, `CommunicationProtocol <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/communicationProtocol.html>`_, `ContributionType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/contributionType.html>`_, `CranialWindowConstructionType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/cranialWindowConstructionType.html>`_, `CranialWindowReinforcementType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/cranialWindowReinforcementType.html>`_, `CriteriaQualityType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/criteriaQualityType.html>`_, `DataType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/dataType.html>`_, `DependencyImpact <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/dependencyImpact.html>`_, `DeploymentEnvironmentType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/deploymentEnvironmentType.html>`_, `DeviceMountingType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/deviceMountingType.html>`_, `DeviceType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/deviceType.html>`_, `DifferenceMeasure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/differenceMeasure.html>`_, `Disease <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/disease.html>`_, `DiseaseModel <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/diseaseModel.html>`_, `EducationalLevel <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/educationalLevel.html>`_, `ElectricalStimulusType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/electricalStimulusType.html>`_, `ExperimentalApproach <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/experimentalApproach.html>`_, `ExternalBodyRegion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/externalBodyRegion.html>`_, `FileBundleGrouping <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/fileBundleGrouping.html>`_, `FileRepositoryType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/fileRepositoryType.html>`_, `FileUsageRole <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/fileUsageRole.html>`_, `GeneticStrainType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/geneticStrainType.html>`_, `GustatoryStimulusType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/gustatoryStimulusType.html>`_, `Handedness <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/handedness.html>`_, `Language <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/language.html>`_, `Laterality <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/laterality.html>`_, `LearningResourceType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/learningResourceType.html>`_, `MRIFatSuppressionTechnique <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/MRIFatSuppressionTechnique.html>`_, `MRIParallelAcquisitionTechnique <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/MRIParallelAcquisitionTechnique.html>`_, `MRIPulseSequence <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/MRIPulseSequence.html>`_, `MRISpoilingTechnique <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/MRISpoilingTechnique.html>`_, `MRIWeighting <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/MRIWeighting.html>`_, `MeasuredQuantity <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/measuredQuantity.html>`_, `MeasuredSignalType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/measuredSignalType.html>`_, `MetaDataModelType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/metaDataModelType.html>`_, `ModelAbstractionLevel <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/modelAbstractionLevel.html>`_, `ModelScope <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/modelScope.html>`_, `ModificationConsentRequirement <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/modificationConsentRequirement.html>`_, `ModificationConstraint <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/modificationConstraint.html>`_, `ModificationForm <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/modificationForm.html>`_, `ModificationScope <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/modificationScope.html>`_, `MolecularEntity <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/molecularEntity.html>`_, `MuscularStructure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/muscularStructure.html>`_, `NervousSystemStructure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/nervousSystemStructure.html>`_, `OlfactoryStimulusType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/olfactoryStimulusType.html>`_, `OperatingDevice <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/operatingDevice.html>`_, `OperatingSystem <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/operatingSystem.html>`_, `OperationalApproach <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/operationalApproach.html>`_, `OpticalStimulusType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/opticalStimulusType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/organ.html>`_, `OrganSystemStructure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/organSystemStructure.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/organismSubstance.html>`_, `OrganismSystem <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/organismSystem.html>`_, `OrganizationType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/organizationType.html>`_, `PatchClampVariation <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/patchClampVariation.html>`_, `PaymentModelType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/paymentModelType.html>`_, `PreparationType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/preparationType.html>`_, `ProgrammingLanguage <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/programmingLanguage.html>`_, `ProjectType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/projectType.html>`_, `PublicationStatus <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/publicationStatus.html>`_, `PulseShape <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/pulseShape.html>`_, `QualitativeOverlap <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/qualitativeOverlap.html>`_, `SemanticDataType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/semanticDataType.html>`_, `SetupType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/setupType.html>`_, `SignalDirectionality <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/signalDirectionality.html>`_, `SkeletalStructure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/skeletalStructure.html>`_, `SoftwareApplicationCategory <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/softwareApplicationCategory.html>`_, `SoftwareFeature <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/softwareFeature.html>`_, `SovereignState <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/sovereignState.html>`_, `SpatialEncoding <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/spatialEncoding.html>`_, `Species <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/species.html>`_, `StimulationApproach <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/stimulationApproach.html>`_, `StimulationTechnique <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/stimulationTechnique.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/subcellularEntity.html>`_, `SubjectAttribute <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/subjectAttribute.html>`_, `SupranationalBody <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/supranationalBody.html>`_, `TactileStimulusType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/tactileStimulusType.html>`_, `Technique <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/technique.html>`_, `TermSuggestion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/termSuggestion.html>`_, `Terminology <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/terminology.html>`_, `TissueSampleAttribute <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/tissueSampleAttribute.html>`_, `TissueSampleType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/tissueSampleType.html>`_, `TissueStructure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/tissueStructure.html>`_, `TypeOfUncertainty <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/typeOfUncertainty.html>`_, `UnitOfMeasurement <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/unitOfMeasurement.html>`_, `VascularStructure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/vascularStructure.html>`_, `VisualStimulusType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/visualStimulusType.html>`_ or `WeightType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/weightType.html>`_
   :instructions: Add all relevant keywords to this creative work either by adding controlled terms or by suggesting new terms.

`BACK TO TOP <LearningResource_>`_

------------

.. _learningOutcome_heading:

***************
learningOutcome
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/learningOutcome
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a description for the expected learning outcomes of this learning resource.

`BACK TO TOP <LearningResource_>`_

------------

.. _modificationDate_heading:

****************
modificationDate
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/modificationDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date on which this creative work was last modified, formatted as '2023-02-07'.

`BACK TO TOP <LearningResource_>`_

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
   :instructions: Enter the name (or title) of this creative work.

`BACK TO TOP <LearningResource_>`_

------------

.. _order_heading:

*****
order
*****

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/order
   :value type: integer
   :instructions: Enter the order in which this resource should appear, relative to other resources with the same topic.

`BACK TO TOP <LearningResource_>`_

------------

.. _prerequisite_heading:

************
prerequisite
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/prerequisite
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter any knowledge, skills, or abilities that are required to be able to use this learning resource.

`BACK TO TOP <LearningResource_>`_

------------

.. _publicationDate_heading:

***************
publicationDate
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/publicationDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date on which this creative work was published, formatted as '2023-02-07'.

`BACK TO TOP <LearningResource_>`_

------------

.. _requiredTime_heading:

************
requiredTime
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/requiredTime
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the time that is required to complete this learning resource.

`BACK TO TOP <LearningResource_>`_

------------

.. _topic_heading:

*****
topic
*****

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/topic
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name or a short description of the aspect of the research product that is covered by this tutorial

`BACK TO TOP <LearningResource_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/type
   :value type: | linked object of type
                | `LearningResourceType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/learningResourceType.html>`_
   :instructions: Add the type of this learning resource.

`BACK TO TOP <LearningResource_>`_

------------

.. _usageCondition_heading:

**************
usageCondition
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/usageCondition
   :value type: | linked object array \(1-N\) of type
                | `License <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/data/license.html>`_ or `UsageAgreement <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/data/usageAgreement.html>`_
   :instructions: Add all licenses and available data usage agreements applicable to this creative work.

`BACK TO TOP <LearningResource_>`_

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
   :instructions: Enter the version identifier of this creative work.

`BACK TO TOP <LearningResource_>`_

------------

