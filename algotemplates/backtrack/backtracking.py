ans = []

def is_valid_state(state):
    # check if it is a valid solution
    return True

def get_candidates(state):
    return []

def search(state):
    if is_valid_state(state):
        ans.append(state.copy())
        # return

    for candidate in get_candidates(state):
        state.append(candidate)
        search(state)
        state.remove(candidate)


state = []
search(state)
