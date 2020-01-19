#learn about the probability


aces = 4
hearts = 13
clubs = 13
diamonds = 13
spades = 13

#sample_space

cards = 52


queen_of_hearts = 1
face_cards = 12


#user_defined function for finding the probability

def event_probability(event_outcomes,sample_space):
	probability = (event_outcomes/sample_space) * 100
	return round(probability,1)



#probability of hearts,clubs,spades and diamonds in a deck of card
heart_probability = event_probability(hearts,cards)
clubs_probability = event_probability(clubs,cards)
diamonds_probability = event_probability(diamonds,cards)
spades_probability = event_probability(spades,cards)
queen_of_heart_prob = event_probability(queen_of_hearts,cards)
face_card_prob = event_probability(face_cards,cards)






#printing probability in '%' figure

print(str(heart_probability)+'%')
print(str(clubs_probability)+'%')
print(str(diamonds_probability)+'%')
print(str(spades_probability)+'%')
print(str(queen_of_heart_prob)+'%')
print(str(face_card_prob)+'%')


