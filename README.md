# Popol Vuh: Nixtla's operating system

## Nixtla's Creed - 

We put culture first. [We will never stop learning](#i-will-never-stop-learning). [We will build our business through maximizing value for our users, customers and colleagues](#i-will-build-our-business-through-creating-the-most-value-for-our-community-of-users-customers-and-collegues). We believe that Open Source is an extremely powerful idea. [We am motivated by the impact of my work.](#i-am-motivated-by-impact) [We will communicate a lot and effectively](#i-will-communicate-as-much-as-possible-because-its-the-oxygen-of-a-distributed-company). We value the bond that connects us as a team. We support inclusion and diversity. We believe in treating each other, and the world, with compassion, kindness and respect. [We do a freaking good job.](#i-do-a-freaking-good-job)

## Notes:

You are expected to contribute. This system is expected to crash. Raise issues and push fixes.

Thesis: a great culture is a culture that is constantly being improved and is in constand flux.

Corollary: the activity of this repos reflects the engagement of the community and the health of the company.



## Mission
[Nixtla's Mission](Mission.md)

## Blurbs
[Blurbs](Blurbs.md)

## Origin Story
[Origin Story](OriginStory.md)

## Investors
[Investors](Investors.md)


## Expansions of Creed - Culture comes first

### [We will never stop learning](#i-will-never-stop-learning)
The first and most important line of the creed means that you’re never finished. There is always more to learn. The enemy of this is thinking you’re right, putting too much weight on your experience, or passing up an opportunity to understand someone’s point of view.

### [We will build our business  through creating the most value for our community of users, customers and collegues.](#i-will-build-our-business-through-creating-the-most-value-for-our-community-of-users-customers-and-colleagues)

There are three groups of people that we care most about: users, customers, collegues and investors. We want to create the most possible value for them. We understand this as a max-min  Rawlsian  welfare function. We believe that by optimizing that wellnes function we will ultimately reach financial success and personal satisfaction. 


We define success as maximazing the wellfare of the groups that consitute Nixtla. We want to create the most possible welfare for our community of customers, users, collegues and investors. We understand this as a max-min Rawlsian social welfare function.  

Wellness is: 

$$
\max_{x\in X}\min_{i\in I}u_{i}(x)
$$

Where $X$ be a set of possible 'states of the world' or 'alternatives states of our company'. Nixtla wishes to choose a single state from $X$ that maximizes the wellness function.

Let $I$ be a finite set, representing a collection of individuals.  For each $i \in I$, let $u_i:X\longrightarrow\mathbb{R}$ be a utility function, describing the amount of happiness or welness an individual $i$ derives from each possible state.

A social choice theory|social choice rule is a mechanism which uses the data $(u_i)_{i \in I}$ to select some element(s) from $X$ which are `best' for society. The question of what 'best' means is the basic question of social choice theory. The 'egalitarian rule' selects an element $x \in X$ which maximizes the 'minimum utility', that is, it solves the optimization problem above. 


### [I will never pass up an opportunity to help out a colleague](#i-will-never-pass-up-an-opportunity-to-help-out-a-colleague)
It doesn’t matter who you report to or what division you’re in. If you’re an Nixtlican, every other Nixtlican is your colleague. A culture where we always try to help one another is the one we all want to work in.

Taken more broadly, `colleague` is all those in the same role in the world. Can you write a blog post or give a talk that will help everyone who is exposed to it?

Part of helping someone is communicating clearly. This doesn’t mean saying “yes” to every request. The distance between saying you’ll help someone and actually helping them is a gap often created with the best intentions. But when we don’t bridge that gap, accountability suffers throughout the organization. Our desire to help might make it tempting to tell someone we’ll do something, but we should always be impeccable with our word. 


### [We will communicate as much as possible, because it’s the oxygen of a distributed company](#i-will-communicate-as-much-as-possible-because-its-the-oxygen-of-a-distributed-company)

This is true in all relationships, and especially in the long distance ones we’re in during most of the year at Nixtla. 

Poor communication (and understanding) is at the root of every disagreement, conflict, and poorly managed project. When people understand each other, difficulties melt away. (Most true conflict in a work environment is imagined.)

The reference to oxygen is not accidental: too much oxygen can be fatal as well. As a group scales past the level where it’s most efficient for everyone to keep up with everything, it’s important to invest time from an editorial mindset making sure that the right information isn’t just published, but it’s heard and understood by those who need to.


### [We am motivated by impact](#i-am-motivated-by-impact)

`We don’t make software to make money, we make money to make more software.`

However, we also like nice things and money is totally fine, and it’s completely necessary in our current socioeconomic system for everything we want to accomplish as a company — and for many things individually. 
No one should feel embarrassed about discussing compensation with HR. But we work for more than just a paycheck.

### [We do a freaking good job.](#i-do-a-freaking-good-job)

Doing a freaking good job means neccesarly embracing failure in your work and other's work. Feel free to experiment and fail. Break stuff... but not the same stuff. And also, please fix it, or at least raise an issue.

We understand quality of our work with the following criteria:
* Ownership
* Delivery focused
* Tested
* Documented

If you are not embarrassed by your old code, you’re not learning enough. If you’re not embarrassed when you ship your first version, you waited too long. =

Good workd is anchored in first principles thinking.

We ship good code fast.

Be aware that you are always writing code for others, not only yourself. Please be mindful. In other words: be kind and take the necessary time to write good code. Its better and faster in the long term.

Given our definition of sucess (Maximizing value for users, customers and collegues) a good proxy of our perfomance is the sum of the satisfaction metric of each of those groups in relation to the individauls in the company and the company itself. 

Food for thought:
This three metrics should be your guiding light:
* User satisfaction: how are the internal or external users of your code perceive the value you create for them?
* Customer satisfaction: how satisfied are the customers? 
* Collegue satisfaction: how satisfied are your collegues with you?
