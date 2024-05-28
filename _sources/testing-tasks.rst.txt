
How do I deploy my AI application: Task List
=====================================================

.. _How do I deploy my AI application? Task List:

:ref:`How do I deploy my AI application?`
-----------------------------------------

.. _Deploying Your Model:

:ref:`Deploying Your Model<How do I deploy my AI application?>`
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Deployment means taking your trained model from an offline environment to a real
world or production system. Exactly what you will need to do for this will
depend a lot on what your application is and what you want to do with it.
However, some things that you should always consider:


**Where you are deploying it (edge, vs centralized).** As with training, an
important part of realizing your deployment will be formulating a way of getting
your data from wherever it is collected, to the deployed model. One of the ways
that you can reduce the cost of getting your data to your models is to deploy
them in a location near the source of the data they will be ingesting. The
advantages of this are:

* Model receives data quickly and can respond quickly, possibly in real time
* Data transfer costs are reduced
* Security burden of transfers is reduced

However, there are some disadvantages:

* Spreading computing power reduces the capacity of each individual unit
* Deploying and maintaining a large number of systems in physically diverse set
  of locations introduces difficulties
* For security purposes, deploying a large number of nodes introduces a larger
  attack surface


The calculus of this decision will vary between projects, however we note that
large projects often find that the cost of transferring large amounts of data
can be very substantial.


**How you are deploying it (internally, externally).** All of the usual caveats
and problems in deploying systems apply. Our product must be prepared for all
cases of misuse we can reasonably prepare for, malicious or otherwise. 


For AI systems there are several additional complications to consider, both when
deploying systems internally or (especially) externally. Unfortunately, a theme
of these issues is that they are all currently difficult to completely
eliminate. This shouldn’t necessarily prevent you from deployment, but might
require you to take some extra care. 


**Out of Sample errors.** For some AI systems, making queries that are
substantially outside the scope of the training data will lead to nonsensical
results. This can be a problem because it is not usually clear to the user what
is in scope and what is out of scope. Knowing how much a result can be trusted
can be problematic. 

An extension from this if the system is exposed externally is that an adversary
may attempt to purposely design an input to the system that produces unexpected
results. As a real world example consider a research project designing stickers
that, when applied to speed signs, cause an onboard computer vision AI to
misread the speed limit. 

This is difficult to fully resolve, and there is no single solution to this
problem currently. If it is of utmost imperative that this behavior is fixed,
some possible solutions are:

* Use techniques that can guarantee behavior (e.g. statistical models can bound
  error rate if their assumptions hold)
* Some techniques (e.g. Bayesian methods) can estimate confidence in solutions. 

The difficulty with both of these approaches is that they place substantial
restrictions on the overall class of available models. Practically in most
cases, the solution needs to be considered at a higher level than the algorithm
itself. Whatever process it is part of should consider the fact that solutions
cannot be guaranteed to be sensible. Rigorous testing should identify and
eliminate as many of these problems as possible.


**Training Data/Model Leakage.** When somebody queries an AI model, they learn
two things. They learn something about how the model understands data, and
something about the data it was trained on itself. This is a problem because
with enough effort, an attacker can steal both of these things.


**Data Leakage.** Consider the statistic that 87% of the US population can be
uniquely identified by gender, ZIP code and full date of birth. It can take a
surprisingly small amount of information to uniquely identify individual points
of data. Large, data driven systems like AI are especially vulnerable to this.
Some AI systems (notably large language models) have also been known to leak
training data when queried directly. 

This is a problem that is difficult to fully prevent. There are some techniques
that can substantially reduce the threat:

* Removal of identifying variables
* Differential privacy mechanisms
* Private model training techniques
* Use of synthetic data

Again, a problem with these techniques is that they introduce limitations and
complexity on the final result. Whether this is worth it depends on the
application. 

**Model Leakage.** Querying a model gives information about how it sees the
relationship between input and output variables. With enough examples of this,
it is possible for an adversary to effectively recover the model. Examples don
not necessarily even need to be related to the original training set, though it
is beneficial.

There are several approaches that can reduce the impact of this:

* Restricting the number of queries to the model
* Watermarking the model, to identify stolen models
* Adding noise, and Differential Privacy approaches


What you are deploying it on (hardware)
This section strongly corresponds to the training pipeline set out in the
training section, and will be expanded in future.

To complete this step:

* Deploy your model

.. _Testing, Validation & Biases in Deployment:

:ref:`Testing, Validation & Biases in Deployment<How do I deploy my AI application?>`
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This section strongly corresponds to the testing and validation set out in the
training section, and will be expanded in future. 