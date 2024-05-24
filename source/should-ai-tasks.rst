.. _Should I use AI/ML Task List:

Should I use AI/ML: Task List
==============================


:ref:`Should I Use AI/ML?`
---------------------------

.. _Evaluate Engineering Case:

:ref:`Evaluate Engineering Case<Should I Use AI/ML?>`
+++++++++++++++++++++++++++++++++++++++++++++++++++++

In this guide, we assume you have a broad end goal in mind to achieve with AI
and Machine Learning. Through this guide, we will take you through the process
of converting this broad goal to a concrete plan. 

As we discussed previously, while AI is a powerful tool in many applications it
may not be immediately appropriate for the problem you are trying to solve. This
step requires you to enumerate and assess what available alternative approaches
to solving the problem, and how they compare to an AI solution. This isn’t
intended as a deep dive into the details and risks of your prospective systems,
but a high level check that this engineering approach is right for you.

At this stage, you may not have a complete and full understanding of the scope
and limitations of an AI and Machine Learning approach. However, the design of
this guide is such that you should expect to revisit earlier steps (like this
one) from later steps as your understanding improves. You should therefore fill
this out to the best of your ability, then return to this later as the project
and your understanding evolve. 

This step is fairly short, and to complete it, you simply need to list the
viable approaches to solving your problem (including the AI approach), and
compare them. This should include solutions that might not take a data driven
approach, as well as data driven approaches that don’t use learning, for
example, heuristic based approaches. The choice of how to compare these will be
dictated by your use case, but you’re likely to want to consider the following:

* What are the financial burdens of each case?
* What are the engineering burdens of each case?
* What are the legal burdens?

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
