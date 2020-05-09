"""Screening test questions for the Facebook Production Engineering Apprenticeship
role."""

# My Code:

# Complete the stickers_for function below.
def stickers_for(phrase):
    """returns number of 'instagram' stickers needed to make a phrase"""

    stic_dict = {}
    for ltr in 'instagram':
        if ltr not in stic_dict:
            stic_dict[ltr] = 1
        else:
            stic_dict[ltr] += 1
        print(ltr)

    phr_dict = {}
    for ltr in phrase:
        if ltr not in phr_dict:
            phr_dict[ltr] = 1
        else:
            phr_dict[ltr] += 1
        print(ltr)

    ratios = []
    for ltr in stic_dict:
        if ltr in phr_dict:
            ratio = phr_dict[ltr] / stic_dict[ltr]
            ratios.append(ratio)

    if len(ratios) > 0:
        num_sticks = max(ratios)
        num_sticks = int(round(num_sticks, 0))
        return stic_dict, phr_dict, ratios, num_sticks

    else: 
        return 0


if __name__ == '__main__':

    # TEST 1
    test_1 = 'artisan martians'
    print(test_1)
    print(stickers_for(test_1))

    test_2 = 'taming giant gnats'
    print(test_2)
    print(stickers_for(test_2))

    """All test cases pass in hacker rank"""