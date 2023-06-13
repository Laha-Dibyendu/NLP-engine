import spacy
from spacy.tokens import Doc, Span
from spacy.matcher import Matcher

class In22Labs_NLP():
    def __init__(self,param): # initializing class In22Labs_NLP
        self.param = param
        print(type(self.param))    
        self.sentence = self.param["sentence"] # setting the variables
        
        global nlp, all_parameter
        nlp= spacy.load("en_core_web_sm") # Load the spaCy language model
        all_parameter=self.param["parameters"]
        

    def Home(self): # In this we are checking what things we need to check and return as output

        answer={}
        for elem in all_parameter:
            if elem=="index":
                answer["indexes"]=self.__index(self.sentence)    
            
            if elem=="pos":
                answer["pos"]=self.__pos(self.sentence)
            
            if elem=="is_alpha":
                answer["is_alpha"]=self.__alpha(self.sentence) 
            
            if elem=="is_punct":
                answer["punct"]=self.__punct(self.sentence) 
            
            if elem=="like_num":
                answer["num"]=self.__num(self.sentence) 
            
            if elem=="dep":
                answer["dependencies"]=self.__dep(self.sentence) 

            if elem=="ents":
                answer["entities"]=self.__ent(self.sentence)
            
            if elem=="lemma":
                answer["lemma"]=self.__lemma(self.sentence )
            
        if answer:
            return answer
        return {"message":"No parameter provided kindly check the spellings also"} # if no parameters are provided we are returning this.
        

    def __lemma(self,sentence): # lemmatizing the input sentence
        doc=nlp(sentence)
        return [token.lemma_ for token in doc]

    
    def __pos(self,sentence): # giving back parts of speech for each word from the sentence
        doc=nlp(sentence)
        tokens=[(token.text,token.pos_) for token in doc]
        return tokens
    
    def __pos2(self,sentence,posi): # giving back parts of speech for specific word from the sentence
        doc=nlp(sentence)
        tokens=[(token.text,token.pos_) for token in doc if token.pos_==posi]
        if tokens:    
            return tokens
        else:
            return "No text as "+posi+" :( "
    
    def __index(self,sentence, ind=0): # returning token index for each word
        doc=nlp(sentence)
        try:
            tokens=[(token.text,token.i) for token in doc ]
            return tokens
        except:
            return "Sorry Not Possible"

    def __alpha(self,sentence): # returning boolean value on whether the word is alphabet or not
        doc=nlp(sentence)
        tokens=[token.text for token in doc if token.is_alpha==True]
        if tokens:    
            return tokens
        else:
            return "No Alphabets :( "
    
    def __punct(self,sentence): # returning punctuations for each word
        doc=nlp(sentence)
        tokens=[token.text for token in doc if token.is_punct==True]
        if tokens:    
            return tokens
        else:
            return "No Punctuation try learning english more ;) "

    def __num(self,sentence): # returning numerical values for each word
        doc=nlp(sentence)
        tokens=[token.text for token in doc if token.like_num==True]
        if tokens:    
            return tokens
        else:
            return "No number pressent :( "

    def __dep(self,sentence): # returning dependencies for each word
        doc=nlp(sentence)
        tokens=[(token.text, token.dep_) for token in doc ]
        return tokens
     
    def __dep2(self,sentence,depen): # returning token based on queried dependencies
        doc=nlp(sentence)
        tokens=[token.text for token in doc if  token.dep_==depen ]
        if tokens:    
            return tokens
        else:
            return "No dependencies like "+depen

    def __ent(self,sentence): # returning whether a token is an entity or not
        doc=nlp(sentence)
        tokens=[(ent.text,ent.label_) for ent in doc.ents]
        if tokens:            
            return tokens
        else :
            return "Sorry, No entity here. "
    
    def __ent2(self,sentence,label): # returning whether a token is a specific entity or not
        doc=nlp(sentence)
        tokens=[ent.text for ent in doc.ents if ent.label_==label]
        if tokens:            
            return tokens
        else :
            return "Sorry, No entity here as "+label

    def __match(self,sentence,param): ## returning matcher element
        doc=nlp(sentence)
        matcher = Matcher(nlp.vocab)
        matcher.add("pattern",[param])
        matches = matcher(doc)
        tokens=[doc[start:end].text for match_id, start, end in matches]
        if tokens:    
            return tokens
        else:
            return "Nothing Matches :( "
    
    def __spans(self, sentence, start, end): # returning span of a doc
        doc=nlp(sentence)
        if start:
            if end:
                return Span(doc,start,end)
            else:
                return Span(doc,start,)
        else:
            if end:
                return Span(doc,0,end)
            else:
                return "Please Give Start and End."



