# Serviette - A Capstone proposal


### Overview

Q: What is Serviette?
A: Serviette is a tool for easily authoring and rapidly deploying Ethereum smart contracts of basic construction and simple function. These elementary smart contracts, henceforth referred to as 'RoBits', are essentially timer switches that deliver a text 'payload' to a specified e-mail address on a specified date.

Users will select a RoBit type from a menu and then input name, trigger date, payload text, and recipient e-mail address into the appropriate fields. This will generate an instance of a RoBit in the user's account. To launch a RoBit a user will send a specified amount of Ether to the address of the RoBit and

#### Fallback proposal

Create a tool for visualizing aspects of the Ethereum blockchain, e.g. the [number of smart contracts](https://etherscan.io/accounts/c), by means of [Etherscan's API](https://etherscan.io/apis).

Users will be presented with a scene rendered by means of the A-Frame web framework wherein a 3D graph is populated with data streamed from the API. Various data objects may be selectable for viewing.

### Specific Functionality

Spend some time drawing out on paper mockups _every_ page of your MVP site.
Annotate _every_ component of the interface _every_ action the user can take.

If there is any actions your app needs to take in the background describe _each_ of them and how they change the underlying data your app saves.

**Pick the minimum feature set for your product to work.**
Everything else should go in the "further work" section.

You don't have to submit the mockup drawings, but do write out a description of _every_ page and component and action.
I literally mean _every_.

### Data Model

What are the persistent "nouns" you need to save across pages in your project MVP?
What do they represent?

We'll be using a relational database which models things like a spreadsheet.
There are fixed fields and every instance

How do you need to _search_ for specific instances of nouns?

### Technical Components

What are the "moving parts" of your MVP?
What are the things like "modules" you're going to write?
How do they talk to each other?

_Make decisions_ here and now.
Do research and prototyping to figure out what libraries and technologies will help you solve your problems.
Write up which ones you'll use.
It's okay if they end up not working and you have to change your plans.

This is _more specific_ than "Django backend, CSS style, etc."
Please specify what specific technical problems you'll have to solve and a guess at the solution.

### Schedule

Write out the order in which you will tackle your technical components of your MVP.

What are the easy parts?
What are the hard parts?
Can you guess how long you'll take for each?

Work on the tough and crucial parts first.

### Further Work

All of the above parts are _just addressing your MVP_.
Here you should outline other features you'd like to implement if you get "done" early.
Order them by importance towards your high-level goal and what order you'll work on them later.

Don't work on any of these features until **all of MVP is complete**.
