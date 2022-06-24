# pienex user's manual:

An agent that has learned to identify some concepts/objects in its environment, if equipped with pienex, then it can almost instantly start to look for complex logical patterns between these initial concepts in that environment, for either their verification or falsation. All of this without the need of a previous explicit training consisting in the systematic exposure to several concrete and real examples of the patterns in question*.

The programme works on the basis of a finite number of pre-trained networks, labeled each by an integer number (not necessarily sorted, nor in any particular order or form in general) and each stored as “n.h5” files, with n its integer label. The training and test data (all of the same shape for all the networks; the test data can have much less examples, though) are stored as “X_train_n.csv” (capital x), “y_train_n.csv” (lowercase y), “X_test_n.csv”, and “y_test_n.csv”. Furthermore, since it deals with propositional logic only, y_train/test... can only take values of 1 or 0. The networks must have one inner deep layer, called “dense_1”, for a total of three layers then (for more deep layers, be sure to call “dense_1” to the final deep layer, then).

The logical operations are denoted as _and_=1, _or_=2, _implies_=3, and _iff_=4. They are taken as binary operators only, and the result of their application is denoted as a 3-tuple of the form (a, b, c), where a and c are positive or negative integers (the negation operator is denoted by a minus sign _neg_=-) and correspond (before negation, in case it applies) to the original pre-trained networks, while b from the set {1, 2, 3, 4} corresponds to the logical connective. Negations are incorporated only at the component-proposition level and not at the 3-tuple, since the standard rules of logic, like, e.g., _neg_ (p _and_ q)=(_neg_ p) _or_ (_neg_ q), offer a way of translation between these two ways. A general propositional reasoning is formed by the iterative application of the binary logical operations. Here, thus, takes the form of nested 3-tuples, like, e.g., (5, 4, (((2, 3, 1), 1, 4), 2, 3)). Recall that the implication is order-sensitive (i.e., it makes a difference if the rest of the 3-tuple is applied to the right or to the left).

With all this preparation, what pienex does, with its “.programme()” method, is to build (via fibering/meta-networks and recursion) new networks, on top of the ones provided initially, and trains them so that the whole system learns the propositional reasoning (the nested 3-tuple) that was introduced as attribute of the class “reasoning”.

That is, based -only- on the training data of the -initial- propositions/networks, pienex programmes the desired reasoning.

This reasoning, since it's programmed in an ad hoc way into the system, may turn out to be empirically true or false. Thus, given new data, stored as “new_data_name.csv” (this name is left to the user, the programme will go along with whatever name is assigned to it), the “.ndpredict(“new_data_name”)” method gives the probability for the reasoning being true or false for this new data.

*Thing which may be, anyway, inconclusive, since an empirically true implication cannot cover, as training data, all of the truth table of a generic implication; during the training phase, pienex uses the training data of the initial networks to create “chimeras” that can produce those missing outputs in the truth tables, even when they would be impossible for data coming from the consistent empirical reality.
