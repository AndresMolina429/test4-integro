
class Test4Logic():
    def is_palindrome(self, phrase):
        phrase1 = list(self.delete_accents(phrase).lower())
        phrase2 = phrase1[::-1]
    
        p1 = ''.join(map(str, phrase1))
        p2 = ''.join(map(str, phrase2))
    
        if p1 == p2:
            return {
                'state': True
            }
        else:
            return {
                'state': False
            }

    def delete_accents(self,phrase):
        phrase = phrase.replace('í','i')
        phrase = phrase.replace('á','a')
        phrase = phrase.replace(' ','')
        phrase = phrase.replace(',','')
        return phrase
    
# phrase = "Allí por la tropa portado, traído a ese paraje de maniobras, una tipa como capitán usar boina me dejara, pese a odiar toda tropa por tal ropilla"
# print(is_palindrome(phrase))