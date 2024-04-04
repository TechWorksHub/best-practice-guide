.. header:: TechNES AI Best Practices Group: Definitions

.. _Application Specific Requirements:

Application Specific Requirements
==================================

.. _AI Risk:

AI Risk
--------

Direct regulation of AI in the EU is tending to a risk based approach based on
the harm than an AI application poses to people. Applications are classified
into risk categories, and those that pose a high risk are to be subject to more
stringent requirements. These categories are currently:

* Unacceptable risk. Applications that are a clear threat to the safety,
  livelihoods or rights of people.
* High risk. Applications that are critical to the safety or wellbeing of
  people, that require special mitigations to adequately cover the risks they
  pose 
* Limited risk. Applications with lower impacts to safety or wellbeing, but
  which still require some level of mitigation 
* Minimal or no risk. Applications with minimal to zero risk. 

Providing guidance on any upcoming or current legislation is out of the scope of
this guide. However, this categorization of the risk that AI applications pose
is a useful tool for discussing best engineering practices. These risk levels
will recur in this guide, and we will refer to them as AI Risk. 

.. _Data Protection:

Data Protection
----------------

AI models are data driven. This leaves them significantly subject to data
protection regulation, especially GDPR. According to GDPR, if you process data,
you have to do so according to seven protection and accountability principles:

* Lawfulness, fairness and transparency — Processing must be lawful, fair, and
  transparent to the data subject.
* Purpose limitation — You must process data for the legitimate purposes
  specified explicitly to the data subject when you collected it.
* Data minimization — You should collect and process only as much data as
  absolutely necessary for the purposes specified.
* Accuracy — You must keep personal data accurate and up to date.
* Storage limitation — You may only store personally identifying data for as
  long as necessary for the specified purpose.
* Integrity and confidentiality — Processing must be done in such a way as to
  ensure appropriate security, integrity, and confidentiality (e.g. by using
  encryption).
* Accountability — The data controller is responsible for being able to
  demonstrate GDPR compliance with all of these principles.

There are also certain categories of data that must be given special
consideration. Providing guidance on legislation remains out of the scope of
this guide. However, once again, the ideas put forward in GDPR are important in
framing the discussion of best engineering practices, and will recur in this
guide.

.. _Safety, Security and Robustness:

Safety, Security and Robustness
----------------------------------

A core requirement of any system is that it functions correctly, both in
conditions of normal use, as well as conditions of misuse (intentional or
otherwise), or other adverse conditions. An AI system should be:

* Safe: either functioning correctly or failing safely in all conditions
* Secure: resilient against misuse or abuse (intentionally or otherwise), and
* Robust: ensuring functionality in as wide a range of conditions as possible

While the need to meet these challenges is not unique to AI systems, AI systems
bring several unique problems to each of these areas. For example:

* Safety is a continual challenge in AI systems that are fundamentally
  statistical. Guaranteeing safe behavior in the wide range of situations an
  automotive AI may encounter, for example, remains a continuous challenge. 
* AI models present unique attack surfaces that must be secured. For example,
  in many situations, models will leak information about the data that they were
  trained on.
* Similarly, AI models struggle to robustly deal with novel data outside of
  their training set. This can both cause problems in normal use, and be
  exploited by attackers.

Safety, security and robustness will be important ideas throughout this document.

.. _Transparency and Explainability:

Transparency and Explainability
----------------------------------

It is important in many cases that we can understand how our systems function.
This imperative should be familiar to any electronic systems engineer, through
the value of clear code and documentation. We use two terms to describe these
requirements:

* Transparency: the communication of appropriate information about an AI system
  to relevant people (for example, information on how, when, and for which
  purposes an AI system is being used), and
* Explainability: the extent to which it is possible for relevant parties to
  access, interpret and understand the decision-making processes of an AI system

Many AI systems are uniquely troublesome in these respects. Many common methods,
such as Neural Networks are effectively “black boxes”. These methods provide a
solution, but through a means that is ultimately not human interpretable. 

.. _Fairness:

Fairness
---------
Fairness is another core requirement of any system, especially in light of the
above ideas of transparency and explainability. By fairness, we mean a system
that:

* Does not undermine the legal rights of individuals or organizations,
  discriminate unfairly against individuals or create unfair market outcomes. 

Fairness is a challenge in AI systems that learn from data. The decisions these
systems make are a reflection of the patterns in the data they are trained on.
If the data is biased, the systems trained on them will also be biased. This has
been proven expensively and at length in the real world, for example through
attempts at creating `criminal justice AI <https://www.technologyreview.com/2019
/01/21/137783/algorithms-criminal-justice-ai/>`_ or 
`hiring AI <https://www.reuters.com/article/us-amazon-com-jobs-automation-
insight-idUSKCN1MK08G>`_.

.. _Accountability and Governance:

Accountability and Governance
------------------------------
Any system that has the potential to cause harm requires oversight. Any AI
system will therefore require systems of:

* Governance, a framework for managing the development, deployment and operation
  of AI
* Accountability, clear lines of responsibility for all aspects of the AI
  applications

The full scope of requirements is unlikely to be fully addressed by engineering.
Nonetheless, these principles are important in the greater context of the AI
application, and will be an important part of development. 

.. _Contestability and Redress:

Contestability and Redress
-----------------------------
Any system that has the potential to cause harm to people also requires ways for
this harm to be recognised and reversed. Any such AI system will therefore
require systems of:

* Contestability, those who may be adversely affected must have a route to
  contest decisions or outcomes
* Redress, there must be a system in place to assess these concerns, and redress
  the affected party when necessary

The full scope of requirements is unlikely to be fully addressed by engineering.
Nonetheless, these principles are important in the greater context of the AI
application, and will be an important part of development.
