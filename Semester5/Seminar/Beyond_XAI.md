https://link.springer.com/chapter/10.1007/978-3-031-04083-2_2?utm_medium=referral&utm_source=slink&utm_content=RM&utm_term=null&utm_campaign=HSCR_BOOKS_AWA1_GL_MPAS_005KU_LNCS50-AA

**local:** individual model decisions 
**global:** characterize whole components (eg neuron, layer, entire network)

**post-hoc:** explains NN after its been trained with standard training procedures
**ante-hoc:** produces novel network architecture that produces an explination as part of its decision
[Page 6]

Focusing on explaining AI preditions: [Seite 6]
 - Feature attribution -> which parts of the NN are responsible for the decision
   - *heatmaps*: computer visualization 
   - *feature visualization*: global explanations


# XAI Methods

## LIME (Local Interpretable Model Agnostic Explanations)

https://github.com/marcotcr/lime

Model agnostic explananations have typically only access to the output. (Black box)
They don't require any information about the innner workings -> widely applicable and flexible

Tries to explain a complex model my fitting an surrogate model around it, which decisions are easy to explain.
=> surrogate-based explanation technique.
LIME does not explain the models decision, but instead the prediction of the surrogate model, which locally approximates the target model.

Quality of explanation largely reliant on the quality of the surrogate fit. 
May have high compuational costs. Also has an uncertainty, which can lead to non-deterministic behaviour.

# GraphLIME

takes the basic idea of LIME but non-linear. Applies to Graph Neural Networks (GNN)



## LRP (Layer-wise Relevance Propagation)

Propagation based explanation method -> requires access to the models internals (topology, weights, activations, ...)
This allows LRP to simplify and thus solve the explanation problem mor efficiently.
Other than agnostic methods LRP does not explain the decision process in one step but instead explains the process layer by layer. 
Each explanation


## Anchors

https://github.com/marcotcr/anchor

Explains by finding decision rules, that "anchor" the predictions. They are in form of *IF-THEN* Statements which define regions in the feature space.
In these Regions the predictions are fixed. -> They stay the same no matter, what other features may change.
Good anchors should have high *precision* and high *coverage* (high coverage means a more general rule)

Anchors is a model-agnostic explanation methods and thus needs no knowledge of the internals of the model.

The rules are searched and constructed by reinforcement learning (RL)

anchor steps: 
- produce candidate anchors
- select candidate
- use beam search to extend anchor search

to find the best method it is necessary to cycle through these steps many times (exploration; multi-armed badit problem)

Anchors only support tabular and text data
scope is clearer than LIME because of the clear boundary of the anchors.
Decision rules are easy to understand
Widht of the beam and precision threshold need to be tuned individually
computationally intense
danger of trivial rules







