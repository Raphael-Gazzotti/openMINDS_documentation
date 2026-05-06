#################################
Terminologies: PulseShape library
#################################

Related schema specification: `PulseShape <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/pulseShape.html>`_

------------

------------

FermiPulse
----------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/pulseShape/FermiPulse
   :@type: https://openminds.om-i.org/types/PulseShape
   :definition: A pulse whose amplitude envelope follows a Fermi (logistic) function.
   :description: A Fermi pulse exhibits a smooth transition between low and high amplitude regions. Its shape is defined by a logistic function with adjustable slope parameters. The envelope allows controlled edge steepness. The pulse provides reduced spectral ringing compared to abrupt transitions. It is used in applications requiring smooth but bounded excitation profiles.
   :name: Fermi pulse

`BACK TO TOP <Terminologies: PulseShape library_>`_

------------

Gaussian-HanningPulse
---------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/pulseShape/Gaussian-HanningPulse
   :@type: https://openminds.om-i.org/types/PulseShape
   :definition: A composite pulse formed by applying a Hanning window to a Gaussian pulse envelope.
   :description: A Gaussian-Hanning pulse combines a Gaussian envelope with a Hanning apodization window. The additional windowing further smooths temporal boundaries. This reduces spectral leakage beyond that of a simple Gaussian pulse. The pulse maintains symmetry about its center. It is used in applications requiring controlled spectral characteristics.
   :name: Gaussian-Hanning pulse

`BACK TO TOP <Terminologies: PulseShape library_>`_

------------

GaussianPulse
-------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/pulseShape/GaussianPulse
   :@type: https://openminds.om-i.org/types/PulseShape
   :definition: A pulse whose amplitude envelope follows a Gaussian function over time.
   :description: A Gaussian pulse exhibits a smooth, symmetric amplitude profile. Its spectral distribution is also Gaussian. The smooth temporal transitions reduce spectral sidelobes. It is commonly used in RF excitation and optical systems. The pulse shape is fully defined by its standard deviation or width parameter.
   :name: Gaussian pulse

`BACK TO TOP <Terminologies: PulseShape library_>`_

------------

rectangularPulse
----------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/pulseShape/rectangularPulse
   :@type: https://openminds.om-i.org/types/PulseShape
   :definition: A pulse with constant amplitude over its duration and abrupt onset and offset transitions.
   :description: A rectangular pulse maintains a uniform amplitude for a defined time interval. The rise and fall times are ideally instantaneous. Its frequency spectrum follows a sinc distribution. This shape is widely used in stimulation and RF excitation as a hard pulse. It represents the simplest temporal pulse form.
   :name: rectangular pulse

`BACK TO TOP <Terminologies: PulseShape library_>`_

------------

sinc-GaussianPulse
------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/pulseShape/sinc-GaussianPulse
   :@type: https://openminds.om-i.org/types/PulseShape
   :definition: A composite pulse formed by modulating a sinc pulse with a Gaussian envelope.
   :description: A sinc-Gaussian pulse multiplies a sinc waveform by a Gaussian window. The Gaussian envelope reduces sidelobes in the frequency domain. This modification improves spectral selectivity compared to a truncated sinc pulse. The resulting waveform retains the central lobe characteristics of the sinc function. It is commonly used where reduced spectral leakage is required.
   :name: sinc-Gaussian pulse

`BACK TO TOP <Terminologies: PulseShape library_>`_

------------

sinc-HanningPulse
-----------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/pulseShape/sinc-HanningPulse
   :@type: https://openminds.om-i.org/types/PulseShape
   :definition: A composite pulse formed by modulating a sinc pulse with a Hanning window.
   :description: A sinc-Hanning pulse applies a Hanning window to a sinc waveform. The window smooths the pulse edges and suppresses spectral sidelobes. This reduces ringing artifacts compared to a simple truncated sinc. The central excitation profile remains governed by the sinc component. The pulse is used in applications requiring improved spectral control.
   :name: sinc-Hanning pulse

`BACK TO TOP <Terminologies: PulseShape library_>`_

------------

sincPulse
---------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/pulseShape/sincPulse
   :@type: https://openminds.om-i.org/types/PulseShape
   :definition: A pulse whose amplitude envelope follows a sinc function in time.
   :description: A sinc pulse is defined by the mathematical sinc function. It produces a rectangular frequency-domain profile under ideal conditions. The pulse typically includes truncation in practical implementations. It is widely used in selective excitation applications. Its bandwidth is determined by the temporal scaling of the function.
   :name: sinc pulse

`BACK TO TOP <Terminologies: PulseShape library_>`_

------------

