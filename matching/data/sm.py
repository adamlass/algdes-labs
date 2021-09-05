import random

n = 3

proposer_names = ["Ross", "Chandler", "Joey"]
rejecter_names = ["Monica", "Phoebe", "Rachel"]

indexies = [x for x in range(3)]
nones = [None for x in indexies]

proposers_rank = [[2, 1, 0], [0, 2, 1], [2, 1, 0]]
rejecters_rank = [[1, 2, 0], [2, 0, 1], [0, 2, 1]]

proposers = [list(x) for x in list(zip(indexies, proposer_names, proposers_rank, nones))]

rejecters = [list(x) for x in list(zip(indexies, rejecter_names, rejecters_rank, nones))]

engagements = 0

while engagements < n:
    proposer = random.choice(proposers)
    if(proposer[3] is not None):
        continue

    proposer_index = proposer[0]

    rejecter_index = proposer[2].pop(0)
    rejecter = rejecters[rejecter_index]
    rejecter_engagement = rejecter[3]

    proposer_rank = rejecter[2].index(proposer_index)
    rejecter_engagement_rank = None

    if(rejecter_engagement is not None):
        rejecter_engagement_rank = rejecter[2].index(rejecter_engagement)

    # If no marriage is found on rejecter
    if(rejecter_engagement is None):
        # Engage couple
        proposer[3] = rejecter[0]
        rejecter[3] = proposer_index
        engagements += 1
    elif(proposer_rank < rejecter_engagement_rank):
        proposers[rejecter_engagement][3] = None

        rejecter[3] = proposer_index
        proposer[3] = rejecter_index
    else:
        continue

for proposer in proposers:
    name = proposer[1]
    fiance = rejecters[proposer[3]][1]
    print(f'{name} -- {fiance}')