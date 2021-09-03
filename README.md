## CMPUT 365 Reinforcement Learning I (An Introduction)


## Schedule
[For the current schedule](schedule.md)

## Syllabus

This page!!!

### Term: 
Fall, 2021 

### Lecture Date and Time: 
MWF 13:00 - 13:50 p.m.

### Lecture Location: 
ETLC E1-007

### Instruction Team:
Adam White (amw8@ualberta.ca)<br>
Andrew Patterson<br>
Subhojeet Pramanik<br>
Tian Tian<br>
Yongchang Hao<br>

### Office Hours:
Adam: Wednesday directly after class (in 307 Athabasca Hall)<br>
TAs will hold a 2hr office hour slot every week
Andrew: TBA<br>
Subhojeet: TBA<br>
Tian: TBA<br>
Yongchang: TBA<br>

### TA Email Address:
cmput365@ualberta.ca
(Do not presonally email the TAs. They will only respond via cmput365@ualberta.ca)

### Overview
This course provides an introduction to reinforcement learning intelligence, which focuses on the study and design of agents that interact with a complex, uncertain world to achieve a goal. We will emphasize agents that can make near-optimal decisions in a timely manner with incomplete information and limited computational resources. The course will cover Markov decision processes, reinforcement learning, planning, and function approximation (online supervised learning). The course will take an information-processing approach to the concept of mind and briefly touch on perspectives from psychology, neuroscience, and philosophy.
 
The course will use a recently created MOOC on Reinforcement Learning, created by the Instructors of this course. Much of the lecture material and assignments will come from the MOOC. In-class time will be largely spent on discussion and thinking about the material, with some supplementary lectures.
 
### Objectives
By the end of the course, you will have a solid grasp of the main ideas in reinforcement learning, which is the primary approach to statistical decision-making. Any student who understands the material in this course will understand the foundations of much of modern probabilistic artificial intelligence (AI) and be prepared to take more advanced courses (in particular CMPUT 609: Reinforcement Learning II, and CMPUT 607: Applied Reinforcement Learning), or to apply AI tools and ideas to real-world problems. That person will be able to apply these tools and ideas in novel situations -- eg, to determine whether the methods apply to this situation, and if so, which will work most effectively. They will also be able to assess claims made by others, with respect to both software products and general frameworks, and also be able to appreciate some new research results.
 
### Prerequisites
The course will use Python 3. We will use elementary ideas of probability, calculus, and linear algebra, such as expectations of random variables, conditional expectations, partial derivatives, vectors and matrices. Students should either be familiar with these topics or be ready to pick them up quickly as needed by consulting outside resources.

#### Course Prerequisites
* CMPUT 175 or CMPUT 275<br>
* CMPUT 267 or Stat 265 or CMPUT 466 or consent of the instructor (upper level ML course or non-applied statistics course).
 
### Course Topics
With a focus on AI as the design of agents learning from experience to predict and control their environment, topics will include
* Markov decision processes
* Planning by approximate dynamic programming
* Monte Carlo and Temporal Difference Learning for prediction
* Monte Carlo, Sarsa and Q-learning for control
* Dyna and planning with a learned model
* Prediction and control with function approximation
* Policy gradient methods

### Course Work and Evaluation
The course work will come from the quizzes and assignments through the Coursera Platform. There will be one small programming assignment (notebook) or one multiple choice quiz due each week, through the Coursera Platform. There are also practice quizzes, that will be due before the start of each week for participation marks. Each week, you have to complete the quiz by midnight on Sunday, for the topic that coming week. That means you have to have completed watching the lecture videos on Coursera and readings as well for that week. The course will also have two mini-essays (1/2 page writing assignments), midterm exam, given in class, and a final exam at the end. 

For weekly practice quizzes, each one has a weight of 0.5% . There are a total of 12 weekly pratice quizzes, and you should do all of them. But, due to the fact that issues sometimes arise, we give you a couple of mulligans. You have to complete 10 of the 12 to get the full 5% participation mark. 

There are 11 graded assignments. They are usually python notebooks, but sometimes it is a Graded Quiz or a Peer Review. The Graded Quizzes and Peer Review will be due on Thursday at mignight, and the notebooks (which are longer) are due on Friday at noon (12:00pm). You will get one assignment off, what that means is we will take the top 10 assigments out of your 11 assigment submission. Each graded assignment has equal weight (30/10). 

The mini essays will be writing assignments. You will be given a list of 10 or so discussion topics (no other topics are allowed) and you will need to write 200 to 300 words discussing the topic. Writing is an important skill. You will be marked both on your clarity of thought (and content), as well as your grammar, spelling, sentence & paragraph structure, and overall polish. Each mini-essay will we worth 2.5% of your final grade.

* Assignments (graded on Coursera): 30%
* Project: 6%
* Mini essay (x2): %6
* Participation: 6%
* Midterm Exam: 20%
* Final Exam: 32%
 
### Course Materials
All course reading material will be available online. 
We will be using videos from the RL MOOC.
We will be using the following textbook extensively:
Sutton and Barto, Reinforcement Learning: An Introduction, MIT Press. The book is available from the bookstore or online as a pdf here: http://www.incompleteideas.net/book/the-book-2nd.html
 
### Academic Integrity
All assignments written and programming are to be done individually. No exceptions. Students must write their own answers and code. Students are permitted and encouraged to discuss assignment problems and the contents of the course. However, the discussion should always be about high-level ideas. Students should not discuss with each other (or tutors) while writing answers to written questions our programming. Absolutely no sharing of answers or code sharing with other students or tutors.  All the sources used for problem solution must be acknowledged, e.g. web sites, books, research papers, personal communication with people, etc.
The University of Alberta is committed to the highest standards of academic integrity and honesty. Students are expected to be familiar with these standards regarding academic honesty and to uphold the policies of the University in this respect. Students are particularly urged to familiarize themselves with the provisions of the Code of Student Behaviour and avoid any behaviour which could potentially result in suspicions of cheating, plagiarism, misrepresentation of facts and/or participation in an offence. Academic dishonesty is a serious offence and can result in suspension or expulsion from the University. (GFC 29 SEP 2003)


### FAQ on using Coursera

#### Error with Quiz Submission
If you get have any issues with submitting quizzes, try clearing the internet cache, closing all browser windows, and re-logging again to Coursera.

#### Jupyter Notebook Assignment Grading
Jupyter notebook assignments include local tests (included in the notebook), as well as grader tests that is hidden from the learners. 

Please make sure your assignment passes all the local tests before submitting. Also, the solutions have to be general (i.e. not hard-coded) in order to pass the grader tests. Local test cases are not comprehensive, and even if you pass all the local tests, you may not get full marks.

Try to make your code general to work robustly for various cases. (e.g. using variable `grid_w` instead of value `12`)

#### Error: Submit button is missing
On rare occasion you may face issues submitting jupyter notebook assignments. If the submit button is missing, please make sure you are only working on the notebook on a single device. If the problem still persists, try setting “?forceRefresh=true” in your notebook URL (reference: https://learner.coursera.help/hc/en-us/articles/360004995312-Solve-problems-with-Jupyter-Notebooks)
