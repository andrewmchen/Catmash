from catmash.models import pictures

# adjusts according to elo formula
def adjust(winner, loser): #parameters are the urls
    # get objects and extract ratings
    winner_object = pictures.objects.filter(url=winner)[0]
    winner_rating = winner_object.rating
    loser_object = pictures.objects.filter(url=loser)[0]
    loser_rating = loser_object.rating

    # calculate expected score
    winner_expected = 1.0 / (1. + 10.**((loser_rating - winner_rating)/400.))

    # update values and save
    delta = 32*(1 - winner_expected)
    winner_new = winner_rating + delta
    #print("old score: %s, expected: %s, new score: %s" %(winner_object.rating, winner_expected, winner_new))
    winner_object.rating = winner_new

    loser_new = loser_rating - delta
    #print("old score: %s, expected: %s, new score: %s" %(loser_object.rating, loser_expected, loser_new))
    loser_object.rating = loser_new

    winner_object.save()
    loser_object.save()
    return winner_rating, loser_rating, delta

###determines how many people agree with you
def agree(winner,loser): #parameters are urls
    winner_object = pictures.objects.filter(url=winner)[0]
    winner_rating = winner_object.rating
    loser_object = pictures.objects.filter(url=loser)[0]
    loser_rating = loser_object.rating

    #calculate expected score
    winner_expected = 1.0 / (1 + 10**((loser_rating - winner_rating)/400.))
    winner_clicks = winner_expected*winner_object.clicks
    #return how many people agree with you
    winner_clicks = (int)(winner_clicks+0.5)
    return (winner_clicks)
