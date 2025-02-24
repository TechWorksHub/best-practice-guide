.. _Should I use AI/ML Task List:

Should I use AI/ML: Task List
==============================


:ref:`Should I Use AI/ML?`
---------------------------

.. _Evaluate Engineering Case:

:ref:`Evaluate Engineering Case<Should I Use AI/ML?>`
+++++++++++++++++++++++++++++++++++++++++++++++++++++

As we discussed previously, developing an AI and Machine learning approach to a
project comes with a range of challenges over and above a typical software
engineering project. AI and Machine Learning are also not suitable for solving
some classes of problems compared to other approaches. The goal of this task is
to provide a first pass at a high level to establish whether or not the AI and
Machine Learning approach is right for your project. To do this, it will cover
several key considerations, and guidance on completing a cost-benefit analysis.  

The first key point to enumerate is around data. Despite the
anthropomorphization that terms like "AI" and "Machine learning" imply, current
approaches are (fairly simple) algorithms with free parameters that are tuned in
response to **data** ("learning") to affect their behavior. As an example,
three key learning paradigms are: 

* Supervised Learning: The algorithms is tuned from a set of examples to create 
  a mapping from an input to an output. For example, mapping an image as an
  input to a label (e.g. "cat" or "dog") as output.
* Unsupervised Learning: The algorithm is tuned on input data to understand
  qualities of that data. For example, a clustering algorithm tuned on a set of
  healthcare data to identify patterns of similar behaviour ("men are more prone
  to heart disease").  
* Reinforcement Learning. The algorithm itself selects input/output pairs to
  learn from, to solve a specific task. For example, an algorithm learning to
  drive a buggy will itself select which actions (direction, speed) it wishes to
  learn from to drive without crashing. 

Across all cases, the unifying factor is the presence of **data** driving
the solution to the given problem. The data contains the key solution
to each of the project in question, and the AI and Machine Learning approach
simply leverages it. *A key criteria* for applying AI and Machine Learning to
your project is that it can be driven by data in this way.

The second key point is that even with an abundance of data, alternative
solutions are often better approaches than AI and Machine Learning ones. The
collection, maintenence, and usage of data is a significant burden. For some
types of problems, this burden is a worthwhile cost for the benefits gained. For
many others it is not. 

AI often struggles to make it's case in problem domains that are already well
understood, and/or in which standard algorithmic solutions are strong. Problems
like sorting, for example, are very well understood, and are poor targets for AI
and Machine Learning. Areas in which AI excels versus standard algorithimic
solutions are those in which the data (or the relationships between data) being
dealt with are abstract or difficult for another reason to capture with a
standard algorithmic approach. For example, explicitly programing an algorithm
to determine whether a picture contains a cat is difficult, but learning a
solution from many examples of cats is feasible. Size can be a motivation as
well.

With these key points in mind, to complete the goal of this first step, and
determine at a very high level whether AI and Machine Learning are likely to be
appropriate for your project you should:

Propose answers to each of the following questions:

* What data will drive your project?
* How it will leveraged by an AI and Machine Learning approach?
* An enumeration of alternative approaches to the project
* The expected cost/benefits of the AI and Machine Learning approach versus
  these alternatives



Examples
###########

In this example, we work through the engineering case for a phishing email
detector.

Our use case is a filter to reduce the success rate of phishing emails. As an
example of how we might think about this, we consider three alternative internal
solutions:

* A non data driven (or minimally data driven) approach. All emails that are
  from external email addresses automatically have a header attached warning
  employees that the sender may not be trustworthy, and to apply caution in
  respect of the contents.
* A data driven approach that uses engineer designed heuristics instead of a
  learning approach. For example, emails are filtered if they:

  * Are from a list of known “bad” addresses
  * Contain too many known “bad” words, e.g. “low interest rate loans”
  * Has “.exe” attachments

* An AI approach that learns from a corpus of previous emails to read an emails
  content, and classifies it as phishing, or not phishing. 

The respective advantages of each approach are:

* The non data driven approach is simple to implement, requires few resources to
  execute, and is simple and cheap to maintain. It will never incorrectly filter
  out legitimate emails as it passes the burden of decision making to employees
  (with extra information).
* The heuristic approach is also fairly simple to implement, and requires few
  resources to execute. It is also very easy to tune for specific requirements
  (e.g. never do this, always do this).
* The AI approach will likely have the best performance at identifying spam
  emails, if trained on sufficient data. It is also likely to adapt fairly well
  to changes in phishing approaches over time, if continually fed with data.  

The disadvantages of each are:

* The non-data driven approach provides extra information, but the decision
  making ultimately places responsibility on the end user.
* The heuristic approach requires each rule to be created manually, scaling
  poorly to large scale problems. Creating effective heuristic rules that do not
  result in any real emails being filtered out is also likely to be challenging.
  Adapting to new phishing approaches is also likely to be a significant burden,
  requiring new rules to be written or old rules to be rewritten.
* The AI approach will need a large corpus of data to learn from which will
  have to be prepared appropriately. It will flag real emails incorrectly some
  of the time (no matter how well trained), and this may not be easy to fix.
  Adoption will require more data preparation and training.

Picking the best approach (or approaches) to use depends on our context. In this
particular example, our non-AI examples are significantly simpler to implement,
and are likely to do better for small scale problems. Other conditions may also
influence the decision. An organization of phishing-aware staff that largely
communicates internally may hugely benefit from the first approach. 


.. _Unacceptable AI Risk:

:ref:`Unacceptable AI Risk<Should I Use AI/ML?>`
+++++++++++++++++++++++++++++++++++++++++++++++++++++
In the Using This Guide section, we defined AI risk in several categories:
Unacceptable, High, Limited, and Minimal. Before continuing any further in this
guide, it is important to consider the risk that your project may fall into the
Unacceptable category. These are applications that are a clear threat to the
safety, livelihoods or rights of people, and are not suitable to be solved with
AI. Examples include:

* AI systems using subliminal techniques, or manipulative or deceptive
  techniques to distort behavior
* AI systems exploiting vulnerabilities of individuals or specific groups
* Biometric categorization systems based on sensitive attributes or
  characteristics
* AI systems used for social scoring or evaluating trustworthiness
* AI systems used for risk assessments predicting criminal or administrative
  offenses
* AI systems creating or expanding facial recognition databases through
  untargeted scraping
* AI systems inferring emotions in law enforcement, border management, the
  workplace, and education

At this stage, you may not have fully fleshed out the scope of your application.
Nonetheless, this initial assessment is important to pre-empt this risk. If you
believe your application may fall into this category, discontinue further work
on it until you have resolved this issue.

To complete this step, complete a risk assessment on the harms your AI project
may pose to the safety, livelihoods or rights of people.

 
Examples
###########

.. _Problematic Data Risk:

:ref:`Problematic Data Risk<Should I Use AI/ML?>`
+++++++++++++++++++++++++++++++++++++++++++++++++++++
Some types of data are subject to extra difficulties that will either require
extra licensing, oversight, or may be effectively impracticable to collect. This
section is about evaluating the risk that the data you are likely to wish to
collect is available within the constraints of your business. Note that this
section *is not* a dive into data collection requirements under GDPR, but a higher
level feasibility check. Some examples of types of data that will be
problematic:

* Criminal Conviction Data, only processable: 

  * under the control of official authority; or
  * authorized by domestic law.

* Data collected by experimenting on humans or animals

  * requiring extra licensing and oversight

* Data surrounding experimentation with infectious diseases

The specifics of problematic data will depend on the domain the data is being
collected in. At this stage, you may not have fully fleshed out the scope of
your application. Nonetheless, you should, before proceeding further, assess the
risk that this applies to you. If you believe your application may fall into
this category, you should once again discontinue further work on it until you
have resolved this issue.

To complete this step, complete a risk assessment on potential problems
surrounding the collection of the type of data you are likely to require. 

Examples
###########
