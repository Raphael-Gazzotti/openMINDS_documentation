###########################################
Terminologies: MRISpoilingTechnique library
###########################################

Related schema specification: `MRISpoilingTechnique <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/MRISpoilingTechnique.html>`_

------------

------------

combinedSpoiling
----------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/MRISpoilingTechnique/combinedSpoiling
   :@type: https://openminds.om-i.org/types/MRISpoilingTechnique
   :definition: A spoiling technique that suppresses residual transverse magnetization by combining radiofrequency phase cycling with gradient-induced spatial dephasing.
   :description: Combined spoiling applies radiofrequency (RF) phase cycling together with spoiler gradients within the same pulse sequence. This dual approach disrupts transverse coherence both temporally and spatially. RF spoiling controls phase evolution across repetitions. Gradient spoiling further enforces dephasing within each repetition. The combination provides robust suppression of steady-state transverse magnetization in modern gradient-echo imaging.
   :name: combined spoiling

`BACK TO TOP <Terminologies: MRISpoilingTechnique library_>`_

------------

gradientSpoiling
----------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/MRISpoilingTechnique/gradientSpoiling
   :@type: https://openminds.om-i.org/types/MRISpoilingTechnique
   :definition: A spoiling technique that suppresses residual transverse magnetization by applying additional gradient moments to induce spatial dephasing.
   :description: Gradient spoiling applies crusher or spoiler gradients after signal acquisition. These gradients introduce position-dependent phase shifts in transverse magnetization. The resulting spatial dephasing reduces coherent signal contributions in subsequent repetitions. The effectiveness depends on gradient strength and duration. Gradient spoiling is widely used in gradient-echo and spin-echo sequences to control unwanted coherence pathways.
   :name: gradient spoiling

`BACK TO TOP <Terminologies: MRISpoilingTechnique library_>`_

------------

radiofrequencySpoiling
----------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/MRISpoilingTechnique/radiofrequencySpoiling
   :@type: https://openminds.om-i.org/types/MRISpoilingTechnique
   :definition: A spoiling technique that suppresses residual transverse magnetization by applying controlled phase cycling to successive radiofrequency excitation pulses.
   :description: Radiofrequency (RF) spoiling introduces systematic phase increments between consecutive RF pulses to disrupt coherent transverse magnetization. This phase cycling prevents the formation of stable transverse steady states. The method enforces incoherence of residual magnetization across repetitions. Reconstruction relies on predictable phase behavior imposed by the RF scheme. RF spoiling is commonly used in spoiled gradient-echo sequences for T1-weighted imaging.
   :name: radiofrequency spoiling

`BACK TO TOP <Terminologies: MRISpoilingTechnique library_>`_

------------

