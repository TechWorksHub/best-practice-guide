.. _How do I define my AI project Task List:

How do I define my AI project: Task List
========================================


:ref:`How do I define my AI project?`
--------------------------------------

.. _Establish Goals and KPIs:

:ref:`Establish Goals and KPIs<How do I define my AI project?>`
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
In the previous section we established, at a high level, the viability of the
project we intend to undertake. In this section we refine the proposed project
into a set of concrete engineering goals. To do this, we open this section by
setting out a little bit more about how AI approaches can be used to solve
problems. We then move through a standard goal setting approach (making sure
goals are Specific, Measurable, etc.), and discuss some of the challenges that
AI approaches can bring for this. 

As we discussed, the scope of this guide is such that one can expect to revisit
earlier steps while evaluating later ones. This step in particular, setting a
concrete definition for the project is one that is likely to cause us to
re-evaluate the checks we made in the previous steps. This is fine, and a
natural part of using the guide. Our previous effort is not wasted, but informs
our current and future decisions. 

We can break AI approaches into 3 categories. We provide a more detailed
explanation of these terms in the [appendix]. However, briefly:

* In supervised learning approaches we are learning by example. We have a set of
  input data points with corresponding known output data points (labels) for
  each. We’re trying to learn what this relationship is so that we can predict
  the outputs that correspond to the inputs for unknown data points. For
  example:

  * Learning to predict stock prices from economic indicators
  * Learning to translate one language into another
  * Learning the relationship between images chest x-rays and the presence of
    cancer
    
* In unsupervised learning we are learning patterns. We have a set of input data
  points without any corresponding output data points. Our goal isn’t to learn
  an input-output relationship (because there isn’t one), but to learn things
  about the input data points that will generalize to all possible input data
  points. For example:

  * Learning to identify clusters of like behavior
  * Learning to identify outliers
  * Dimensionality reduction

* In reinforcement learning approaches, we are learning by example with an
  algorithm that interacts with its environment to select the data points it wants
  to learn from. Our goal is to create a policy from which tells the algorithm the
  best action to take at any point. For example:

  * Learning to play chess
  * Learning to play atari video games
  * Autonomous vehicles

Previously, we assumed that you entered this guide with a broad project goal in
mind. With the above in mind, the goal of this section is to convert that idea
into:

* A set of project goals, defining:

  * What will define when the project will be complete
  * What, specifically it needs to achieve
  * When this should be completed by

* A set of KPIs, defining:

  * How well the project is currently performing on some important benchmarks

We will not cover again the work of general goal setting here, which we assume
should be familiar to any competent engineer. However, over other engineering
projects AI and Machine learning projects have several uncommon considerations.

The first is that AI and Machine Learning algorithms are often stochastic in
nature, behaving in a non-deterministic and statistical way. All goals and KPIs
must be aware of this. For example, for a face detection software it is
appropriate to set goals such as “95% of this set of faces can be recognised”
rather than “the software must recognise all these specific people”.

The second is that human interpretability is a difficult topic in AI and Machine
Learning, and it may be difficult to define why the software is doing the things
or making the decisions that it makes. We will cover this topic (and its
mitigations in more detail) in later sections, but it is important to be aware
that metrics that rely on a deep understanding of functionality may be difficult
to resolve at later stages. 

To complete this step:

* Define a set of Goals and KPIs

.. _Risk Assessment:

:ref:`Risk Assessment<How do I define my AI project?>`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

In the last section, we did a preliminary assessment of some high level project
sinking risks to establish that our project was viable. In this section we do a
more detailed analysis of the risks of our proposed project.

Risk assessment is a basic engineering skill and we will not cover the basics of
performing a risk assessment here. There are a multitude of resources available
on how to do this. In future versions of this document, this section we discuss
some common risks in more detail.