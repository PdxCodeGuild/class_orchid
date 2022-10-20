# Professional Development Practices

When you are working in your own repositories, you are writing your code portfolio. Employers will read your code and look at your history to get a sense of your development style and your adherence to best practices. Follow this advice to keep your code looking tidy and professional.

## Clean, readable history

### Commit often
Commit every time it works! Commit and push every day no matter what.

### Descriptive commit messages

Don't use names like "done for now" or "it's working", describe what you accomplished with this commit. Be consistent with your comment style, choose a convention and stick with it.

Common style patterns are:
- no trailing punctuation
- all lowercase, or only first character uppercase
- start with an imperative verb rather than past tense
- examples:
  - create models for authentication app
  - add input fields to file upload template
  - update results view to include timestamps
  - style results page
  - refactor user profile view

### Use feature branches

Split your tasks into cohesive, coherent chunks of work. For each chunk: 
- Make a feature branch named after that chunk of work. (ex: `user-uploads`, `keyword-search`) 
- When that work is done and you're ready to move onto a new task, create a pull request for the feature branch. 
- Give the PR a descriptive name, and put any relevant details about the development in the PR description. This is a great place to document the resources you referenced as well. 
- This is also a great time to ask for code review from me or from your peers
- When the PR is ready, perform a "Squash and Merge" to merge it into your main branch
  - click the dropdown menu on the merge button to find the different types of merge options

## Clean, readable code


### Comment your code

Add a comment to anything that you're not totally sure is self-explanatory. (Good variable names will help simple things be self-explanatory!)

Functions that are complex should have a docstring that lists 
- each parameter, it's type, and what it represents
- the action of the function
- the return type

If you copy code from somewhere, comment a link to the source. It's good to give credit, and this will also help you when you're trying to debug code you didn't write yourself.


### Use sensible variable names

Naming things is one of the two hard problems of computer programming (along with cache invalidation and off-by-one errors) but it's incredibly important for readable, understandable code. 

When you're not sure what to name something, try to think about what the variable *actually represents*. Give names that reflect what the variable actually is. However, do *not* include the type in your variable names.

Also, always follow the casing conventions of the language for the type. 

some examples of good variable names: 
- `quote`: a single quote
- `quotes`: a collection of quotes
- `options`: a configuration object, such as the headers and params for an axios call
- `quote_options`: a config object specific to the quotes (in python)
- `quoteOptions`: same, but in JavaScript
- `OptionView`: a class-based Django view
- `option_view`: a function-based Django view

some examples of bad variable names: 
- `quote`: for a list of quotes (use singular and plural carefully!)
- `quoteDict`: just call this `quotes`, don't include the data type in the variable
- `quote_Options`: stick to the common casing strategy for your context
- `x`: single character variables are only appropriate in callbacks, list and dict comprehensions, lambdas, etc. Never give a single character name to a variable you will need to reuse in another code block


### Use an autoformatter

Code styling (white space, capitalization) should be consistent within and between documents. The easiest way to achieve this is to set up autoformatters. I like to have mine format on save, but you can format manually as well. If you need help setting up `autopep8` for python or VSCode's built-in JavaScript formatter, let me know and I'm happy to help.
